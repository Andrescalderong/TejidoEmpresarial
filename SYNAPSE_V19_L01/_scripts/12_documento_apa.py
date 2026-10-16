"""Compone el documento completo en formato APA 7 (JSON de bloques para el generador DOCX).
Convierte las claves D### del análisis en citas autor-año y construye la lista de referencias."""
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(__file__))
from synlib import *
import pandas as pd
inv={d["doc_id"]:d for d in load_inv()}; A=load_docs(); C=f"{L}/csv"; I=f"{L}/informe"; OUT=f"{L}/documento"; os.makedirs(OUT,exist_ok=True)
ids=sorted(inv)
# ---------- citas autor-año ----------
def surnames(i):
    m=inv[i]["meta"]; c=inv[i]["corpus"]
    if c=="SINTESIS_BUSCADOR": return ["Elsevier" if "Scopus" in m["fuente"] else "Clarivate"]
    return [n.split(",")[0].strip() for n in __import__("synlib")._apa_names(m,c)] or ["Autor no identificado"]
def base_key(i):
    s=surnames(i); y=inv[i]["meta"].get("anio","s. f.")
    if len(s)==1: a=s[0]
    elif len(s)==2: a=f"{s[0]} y {s[1]}"
    else: a=f"{s[0]} et al."
    return a,y
grp=collections.defaultdict(list)
for i in ids: grp[base_key(i)].append(i)
suffix={}
for k,v in grp.items():
    if len(v)>1:
        for n,i in enumerate(sorted(v,key=lambda x:inv[x]["meta"].get("titulo","").lower())): suffix[i]="abcdefghij"[n]
def cite(i,narr=False):
    a,y=base_key(i); y=f"{y}{suffix.get(i,'')}"
    if narr and i=="D100": return f"Scopus AI ({a}, {y})"
    if narr and i=="D101": return f"Web of Science Research Assistant ({a}, {y})"
    return f"{a} ({y})" if narr else f"{a}, {y}"
PLUR={"propuso":"propusieron","desarrolló":"desarrollaron","mostró":"mostraron","halló":"hallaron","reportó":"reportaron","describió":"describieron","sostuvo":"sostuvieron","usó":"usaron","implementó":"implementaron","aplicó":"aplicaron","llevó":"llevaron","diseñó":"diseñaron","reconstruyó":"reconstruyeron","actualizó":"actualizaron","operó":"operaron","corrigió":"corrigieron","clasificó":"clasificaron","estimó":"estimaron","analizó":"analizaron","caracterizó":"caracterizaron","revisó":"revisaron","identificó":"identificaron","vinculó":"vincularon","situó":"situaron","incorporó":"incorporaron","concibió":"concibieron","trató":"trataron","recupera":"recuperan","modela":"modelan","incluye":"incluyen","declara":"declaran","trata":"tratan","reconoce":"reconocen","procede":"proceden","es":"son","depende":"dependen","cubre":"cubren","cita":"citan","comparte":"comparten","antecede":"anteceden","aporta":"aportan","muestra":"muestran","propone":"proponen","señala":"señalan","coincide":"coinciden","tiene":"tienen","ofrece":"ofrecen","concluye":"concluyen","atribuye":"atribuyen","reporta":"reportan","halla":"hallan","describe":"describen","sostiene":"sostienen","usa":"usan","aplica":"aplican","opera":"operan","sustenta":"sustentan","evalúa":"evalúan","presenta":"presentan","estudia":"estudian","extiende":"extienden","resuelve":"resuelven","aborda":"abordan"}
NOUN=("revisión","estudio","síntesis","documento","editorial","marco","artículo","análisis","trabajo")
# ---------- referencias ----------
def ref_apa(i):
    r=apa_ref(inv[i])
    if i=="D087": r=r.replace("*28*(3), 5-6.","*28*(3), 315-316.")
    r=r.replace(", & ",", y ")
    mt=re.search(r"\) ([A-Z0-9 ,:\-–'’]{25,})\. \*",r)
    if mt and mt.group(1)==mt.group(1).upper(): r=r.replace(mt.group(1),mt.group(1).capitalize())
    a,y=base_key(i)
    if i in suffix: r=re.sub(r"\((\d{4})\)",lambda m:f"({m.group(1)}{suffix[i]})",r,count=1)
    return r
# ---------- conversión de texto ----------
RANGE=re.compile(r"D(\d{3})\s*[–-]\s*D(\d{3})")
def conv(text):
    ph={}
    def hold(m):
        k=f"§R{len(ph)}§"; ph[k]=f"las claves D{m.group(1)}–D{m.group(2)} del Apéndice A"; return k
    text=RANGE.sub(hold,text)
    def inparen(m):
        inner=m.group(1)
        if not re.search(r"D\d{3}",inner): return m.group(0)
        inner=re.sub(r"(D\d{3})\s*(?:,|;|\sy)\s*(?=D\d{3})",r"\1; ",inner)
        inner=re.sub(r"D\d{3}",lambda t:cite(t.group(0)) if t.group(0) in inv else t.group(0),inner)
        return "("+inner+")"
    text=re.sub(r"\(([^()]*)\)",inparen,text)
    def narr(m):
        code=m.group(2); 
        if code not in inv: return m.group(0)
        pre=m.group(1) or ""; c=cite(code,True); nxt=m.group(3) or ""
        if pre.strip() in NOUN and not c.startswith(("Scopus AI","Web of Science")): pre=pre+"de "
        elif pre.strip() in NOUN: pre=pre+"de "
        plural=("et al." in c) or (" y " in c.split("(")[0])
        if plural and nxt.strip() in PLUR: nxt=nxt.replace(nxt.strip(),PLUR[nxt.strip()])
        return pre+c+nxt
    text=re.sub(r"((?:\b(?:%s) )?)\b(D\d{3})\b(\s+[a-záéíóú]+)?"%"|".join(NOUN),narr,text)
    for k,v in ph.items(): text=text.replace(k,v)
    return text
# ---------- lectura de markdown ----------
def lines_of(path): return open(path).read().split("\n")
INF=lines_of(f"{I}/informe_lote.md"); REL=lines_of(f"{I}/analisis_relacional.md")
def section(lines,start,level="##"):
    """líneas de la sección cuyo encabezado empieza por `start`, sin el encabezado, hasta el siguiente encabezado del mismo nivel o superior."""
    out=[];on=False
    for ln in lines:
        if ln.startswith(start) and not on: on=True; continue
        if on:
            if re.match(r"^#{1,%d} "%len(level),ln): break
            out.append(ln)
    return out
def sec(lines,num,level="##"): return section(lines,f"{level} {num}",level)
blocks=[]
def H(level,text): blocks.append(dict(t=f"h{level}",x=conv(text)))
def P(text):
    text=text.strip()
    if text: blocks.append(dict(t="p",x=conv(text)))
tab_caps=[]
fig_n=[0]
def FIG(name,title,desc,nota):
    fig_n[0]+=1
    P(f"La Figura {fig_n[0]} presenta {desc}.")
    blocks.append(dict(t="fig",f=name,x=title,n=nota.replace("`",""),num=fig_n[0]))
def emit(lines,shift=0):
    """convierte markdown a bloques; ### -> h2+shift, #### -> h3+shift"""
    i=0; para=[]
    def flush():
        nonlocal para
        if para: P(" ".join(para)); para=[]
    while i<len(lines):
        ln=lines[i].rstrip()
        if not ln.strip(): flush(); i+=1; continue
        m=re.match(r"^(#{3,4}) (.*)",ln)
        if m:
            flush(); lvl=2+(len(m.group(1))-3)+shift; H(min(lvl,3),re.sub(r"^\d+(\.\d+)*\.?\s+","",m.group(2))); i+=1; continue
        if ln.startswith("|"):
            flush(); rows=[]
            while i<len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| :]+\|$",lines[i]): rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i+=1
            blocks.append(dict(t="table",rows=[[conv(c) for c in r] for r in rows])); continue
        m=re.match(r"^(\d+)\. (.*)",ln)
        if m:
            flush(); items=[]
            while i<len(lines) and re.match(r"^\d+\. ",lines[i]): items.append(re.sub(r"^\d+\. ","",lines[i])); i+=1
            blocks.append(dict(t="ol",items=[conv(x) for x in items])); continue
        if ln.startswith("- "):
            flush(); items=[]
            while i<len(lines) and lines[i].startswith("- "): items.append(lines[i][2:]); i+=1
            blocks.append(dict(t="ul",items=[conv(x) for x in items])); continue
        if ln.startswith("`") and ln.endswith("`"): i+=1; continue
        para.append(ln.replace("`","")); i+=1
    flush()
# ---------- cifras ----------
fich=pd.read_csv(f"{C}/fichas_bibliograficas.csv")
# ---------- texto nuevo ----------
RESUMEN=("Este informe sintetiza el análisis de 101 documentos únicos (2008-2026) sobre tecnologías digitales, transferencia tecnológica y recuperación productiva y resiliencia empresarial tras sismos, aplicando el protocolo SYNAPSE V19.0. "
"Cada documento se leyó completo y se evaluó en dialéctica, madurez (TRL, BRL, IRL, DRL y SRL), brechas, falacias, causalidad y vacíos; los resultados se integraron con aprendizaje automático (TF-IDF, k-means, agrupamiento jerárquico, DBSCAN y LDA), redes bibliométricas, triangulación y relaciones tipificadas entre documentos. "
"En los 87 documentos técnicos, la mediana de TRL fue 4, la de BRL fue 2 y la de IRL fue 3; 55 de 84 documentos con TRL asignado tuvieron TRL de 4 o menos. Ningún documento estudia de forma empírica la transferencia tecnológica en la recuperación empresarial posterremoto, y los modelos de tiempo de recuperación (8 documentos) no se relacionan con la literatura de gemelos digitales e IoT (41 documentos). "
"Cinco grupos de coautoría concentran 11 documentos, y 86 de las 93 referencias de una síntesis automática coinciden con el corpus, lo que limita la independencia de la evidencia. Sin el bloque biomédico, la estructura temática es difusa (silueta de 0,06). "
"Se formulan cinco proposiciones emergentes y se concluye que la literatura documenta potencial y desempeño técnico, no efectos medidos sobre la continuidad de empresas.")
KW="gemelo digital; Internet de las cosas; transferencia tecnológica; resiliencia empresarial; recuperación posterremoto; madurez tecnológica; revisión sistemática"
INTRO=[
"La recuperación productiva tras un sismo depende de cuánto tiempo permanecen inactivos los edificios, los servicios y las comunidades de los que dependen las empresas. D011 mostró que modelar varios tipos de inactividad y tácticas de mitigación reproduce los tiempos de cierre observados mejor que usar el tiempo de reparación del edificio como sustituto, y D053 incorporó demoras impedientes y funciones de fragilidad de tiempo de inactividad mediante simulaciones de alta fidelidad. En paralelo, una literatura amplia propone gemelos digitales, Internet de las cosas (IoT), computación en el borde e inteligencia artificial para detectar, evaluar y coordinar la respuesta (D006, D013, D034, D048).",
"Las síntesis generadas por buscadores con inteligencia artificial describen el potencial de integrar estas tecnologías con la transferencia tecnológica para la resiliencia empresarial (D100, D101). No es claro, sin embargo, qué parte de esa afirmación descansa en evidencia primaria con desenlaces empresariales y qué parte en pruebas técnicas de laboratorio o simulación. Este informe aborda esa pregunta mediante un análisis sistemático de todo el corpus disponible en el repositorio del proyecto.",
"El objetivo es evaluar la madurez, la calidad y la independencia de la evidencia sobre tecnologías digitales para la recuperación productiva y la resiliencia empresarial tras sismos, y determinar vacíos y rutas de investigación. Las preguntas son: (a) ¿qué nivel de madurez tecnológica, comercial y de integración muestra la literatura?; (b) ¿qué afirmaciones transversales se sostienen por triangulación entre estudios independientes?; (c) ¿cómo se relacionan entre sí las subliteraturas técnicas y las de recuperación y organización?; y (d) ¿qué vacíos impiden estimar el efecto de la tecnología sobre la continuidad de las empresas?",
"El informe se organiza así: método e integración de datos; revisión de la literatura por líneas temáticas; resultados (composición, madurez, aprendizaje automático, triangulación, patrones y relaciones); discusión de controversias; discusión; limitaciones; conclusión y áreas futuras.",
]
REVISION=[
("Gemelos digitales para la gestión de desastres y la recuperación",
["D006 propuso un gemelo digital de ciudad en desastre con cuatro componentes (sensado multidato, integración analítica, decisión multiactor y análisis dinámico), y D013 desarrolló un marco integral para la gestión posdesastre con inteligencia artificial explicable y dinámica social; ambos son propuestas conceptuales. Las aplicaciones sísmicas incluyen un gemelo urbano que estima respuesta y daño por edificio con sensores de actualización (D034), un gemelo como imagen operativa común para estimar daños y necesidades de rescate en un escenario de Kocaeli (D048), un gemelo comunitario con datos públicos (D078) y un distrito industrial con red IoT y arquitectura híbrida (D080); D048 y D080 comparten autoría. D070 analizó los beneficios de sostenibilidad de los gemelos en ciudades inteligentes ante terremotos fuertes.",
"Las revisiones sobre gemelos de servicios esenciales (D004), de infraestructura civil (D028), de ciudades inteligentes con IoT e IA (D079) y de inundaciones urbanas (D061) coinciden en que el potencial es alto y la implementación todavía incipiente, con interoperabilidad, calidad de datos y escalabilidad como barreras. Esas barreras se abordan en propuestas concretas: una ficha de identidad de modelos de simulación para sincronizar simulaciones estructurales y de evacuación (D008), un repositorio híbrido con estándares BIM y web semántica (D021) y identificadores persistentes alineados con IFC 4.3 (D025)."]),
("Alerta sísmica, sensado y aprendizaje automático",
["La alerta sísmica de bajo costo con sensores MEMS se revisó en D045, y D049 implementó detección y alerta en el nodo con una variante del principio PLUM; D063 aplicó el mismo principio a ferrocarriles de alta velocidad. D073 llevó el picado de la onda P al dispositivo IoT y D075 propuso una difusión LoRa multisalto que alcanza todos los nodos de un área de 30 km de radio en 2,4 s o menos. D064 diseñó una arquitectura con 5G y cómputo en el borde para actualizar gemelos con un retardo medio de aplicación de 2,1 ms. En aprendizaje automático, D060 reportó una exactitud de 99,05 % para la intensidad sísmica en sitio con XGBoost, D041 halló que una red neuronal supera a XGBoost en la estimación de magnitud con datos de California y D010 usó datos sintéticos para mejorar la estimación de eventos grandes escasos. D031 y D071 aportaron enfoques de IoT semántico para amenazas geológicas.",
"Los UAV complementan el sensado con restablecimiento de comunicaciones (D022, D062), recolección de datos (D001), evaluación de daño con imágenes (D076) e integración con IoT (D042)."]),
("Monitoreo estructural con IoT y calidad del dato",
["En el monitoreo de puentes, D009 reconstruyó cargas y respuestas con errores de 1 % a 5 %, D035 actualizó un modelo de elementos finitos de un puente ferroviario de acero con errores de frecuencia menores de 5 %, y D023 operó un gemelo con red LoRaWAN en un puente ferroviario en servicio. Las propuestas de bajo costo se validaron en laboratorio: un gemelo de una viga con sensores de 84 dólares y 15 dólares (D068) y una red de cinco nodos sincronizados por GPS con error de temporización de 50 microsegundos (D084). La calidad del dato es una condición común: D033 sostuvo que pesa más que la arquitectura, D039 corrigió retardos temporales no enteros con aprendizaje profundo y D086 clasificó anomalías a bordo de un nodo de bajo costo con 96,36 % de precisión; D039 y D086 comparten autoría."]),
("Tiempo de recuperación y economía del refuerzo",
["D011 desarrolló un marco analítico de recuperación empresarial con varios tipos de inactividad, y D053 estimó modelos de consecuencia de tiempo de recuperación con distribuciones beta y de valor extremo generalizado. En la economía del refuerzo, D054 mostró que la mitigación de edificios antiguos de concreto es atractiva solo si se valora la reducción del riesgo de víctimas, D040 incorporó pérdidas indirectas y carbono del ciclo de vida, y D069 propuso medir el beneficio por el aumento de resiliencia. Las propuestas de refuerzo específicas incluyen camisas de acero optimizadas con algoritmo genético (D002), confinamiento con fibras (D027) y concreto reforzado con fibras de acero (D067). D040 y D053 comparten autoría."]),
("Adopción organizacional, resiliencia y cadenas de suministro",
["D005 describió el IoT como un ciclo dual entre tecnología y organización, y D007 situó el potencial transformador del IoT en la aceptación de las partes interesadas. Las encuestas transversales con modelos estructurales asocian IoT y gemelo digital con mayor resiliencia y eficiencia operativa (D029, D030, D052, D085), mientras D082 concibió la resiliencia organizacional como propiedad emergente de mecanismos colectivos, adaptativos y dinámicos. En cadenas de suministro, D037 halló una asociación moderada entre tecnologías digitales y resiliencia (r = 0,331), mayor en preparación y respuesta que en recuperación, y D081 describió efectos por etapa de la disrupción; D016, D017 y D051 documentaron el crecimiento de la literatura y las barreras de adopción del IoT."]),
("Gestión de desastres, conocimiento e Industria 4.0",
["D050, D056 y D044 describen beneficios del IoT en la gestión de desastres, y D019 y D042 integran IoT, UAV y comunicaciones en el ciclo del terremoto. D026 caracterizó las soluciones digitales tras el sismo de 2023 en Türkiye y D047 revisó los sistemas de información geográfica en la gestión del transporte posterremoto. D003 y D012 señalan que la tecnología domina la literatura con integración limitada de conocimiento, equidad y factores humanos. D099 identificó seis familias de tecnologías de la Industria 4.0 en la gestión del riesgo de desastres y las vinculó con el marco de Sendai."]),
]
ESCENA_CONTROV=[
"Las controversias del lote son de cuatro tipos. La primera es conceptual: D030 trata la resiliencia organizacional como una variable mediadora lineal entre tecnología y desempeño, y D082 la concibe como propiedad emergente; el diseño de evaluación de empresas posterremoto depende de esa elección. La segunda es de desempeño comparado: D060 reporta que XGBoost supera a otros algoritmos en intensidad sísmica y D041 que una red neuronal supera a XGBoost en magnitud, con tareas, datos y métricas distintos. La tercera es de independencia de la evidencia: la síntesis D100 incluye como referencias a los documentos del lote y cinco grupos de coautoría reducen el número de confirmaciones independientes. La cuarta es de alcance de las síntesis automáticas: D100 declara un periodo de 2020 a 2024 con 49 referencias de 2025 y 2026, sin protocolo declarado."]
FUTURAS=[
"Las áreas futuras se derivan de los vacíos, y cada una se asocia con una proposición del análisis relacional:",
]
FUT_LIST=[
"**Integración de modelos de recuperación con datos de gemelos digitales.** Estimar con datos observados cuánto del tiempo de cierre corresponde a demoras de detección y evaluación de daño, y simular el efecto de reducirlas con sensado y gemelos (proposición P-E1).",
"**Estudios empíricos de transferencia tecnológica en recuperación posterremoto.** Diseños con empresas afectadas, medición de tiempo de reanudación, ingresos y empleo, y capacidad de absorción como moderador (proposición P-E5).",
"**Síntesis con protocolo.** Búsqueda propia con cadena registrada, doble revisión y evaluación de calidad, que incluya literatura sin etiqueta de Industria 4.0 y fuentes regionales en español (proposiciones P-E2 y P-E3).",
"**Ponderación de la evidencia por grupo de autoría y réplica independiente** de los estudios de alerta sísmica de bajo costo y de monitoreo estructural con IoT.",
"**Guías de reporte para estudios tecnológicos:** intervalos de confianza, validación externa, repetición y datos disponibles (proposición P-E4).",
"**Módulo de patentes.** Verificar el estado legal de las 11 patentes aportadas, revisar frase por frase sus pasajes críticos y realizar una búsqueda sistemática de patentes de gemelos digitales, IoT y alerta sísmica con clasificación y doble revisión (Apéndice K).",
"**Cobertura regional.** Estudios y datos de regiones sísmicas de América Latina, incluidos seguros, créditos de reconstrucción y política pública.",
]
# ---------- composición ----------
def sub(lines,num): return section(lines,f"### {num}","###")
H(1,"Introducción")
for p in INTRO: P(p)
H(1,"Método e integración de datos")
H(2,"Corpus"); emit(sub(INF,"2.1"))
H(2,"Procedimiento por documento"); emit(sub(INF,"2.2"))
H(2,"Convenciones de análisis"); emit(sub(INF,"2.3"))
H(2,"Cálculo y juicio del analista"); emit(sub(INF,"2.4"))
H(2,"Aprendizaje automático y procesamiento de lenguaje natural"); emit(sub(INF,"5.1"))
H(2,"Relaciones tipificadas entre documentos"); emit(sec(REL,"1."))
H(1,"Revisión de la literatura")
for t,ps in REVISION:
    H(2,t)
    for p in ps: P(p)
H(1,"Resultados")
H(2,"Composición y calidad de extracción"); emit(sec(INF,"3."))
FIG("fig_produccion_anual.png","Distribución de los documentos del lote por año de publicación","la distribución por año de publicación de los 101 documentos","*Nota.* n = 101. Elaboración propia a partir del inventario del lote (`csv/inventario.csv`).")
H(2,"Madurez multinivel"); emit(sec(INF,"4."),shift=1)
FIG("fig_matriz_madurez.png","Matriz de madurez multinivel por documento","los niveles TRL, MRL, BRL, IRL, DRL y SRL de cada documento","*Nota.* n = 84 documentos con TRL o BRL asignado. N = núcleo, A = adyacente, P = periférico; las celdas grises indican que la dimensión no aplica o no es evaluable. El SRL se calculó con la fórmula del analista. Elaboración propia (`csv/madurez_multinivel.csv`).")
FIG("fig_radar_madurez.png","Perfil de madurez: mediana por grupo de relevancia","las medianas de madurez por grupo de relevancia","*Nota.* Núcleo n = 15, adyacente n = 48, periférico n = 21; escala de 1 a 9. Elaboración propia (`csv/ml/madurez_medianas_por_grupo.csv`).")
FIG("fig_diagrama_valles.png","Valle de la muerte comercial y documentos por valle y severidad","la relación entre TRL y BRL y la distribución de los documentos por valle de la muerte","*Nota.* Panel izquierdo: TRL modal frente a BRL; el tamaño del círculo indica el número de documentos y el área sombreada, una brecha TRL − BRL ≥ 2. Panel derecho: n = 101. Elaboración propia (`csv/valles_muerte.csv`).")
FIG("fig_mapa_calor_brechas.png","Brechas de madurez por documento","las brechas de madurez TRL − BRL, TRL − IRL y BRL − DRL de cada documento","*Nota.* Los tonos rojos indican tecnología por delante del negocio o de la integración. Elaboración propia (`csv/brechas_madurez.csv`).")
H(2,"Resultados del aprendizaje automático y sensibilidad")
FIG("fig_ml_pca_tsne.png","Mapa de los documentos según su contenido","la proyección de los documentos por contenido con PCA y t-SNE","*Nota.* TF-IDF de unigramas y bigramas; k-means con k = 2. Los círculos rojos señalan el bloque SciELO (D087-D098). Elaboración propia (`csv/ml/`).")
FIG("fig_ml_dendrograma.png","Dendrograma jerárquico de Ward de los 101 documentos","el agrupamiento jerárquico de los documentos","*Nota.* Método de Ward sobre la reducción SVD del TF-IDF. Elaboración propia (`csv/ml/`).")
FIG("fig_red_copalabras.png","Red de co-palabras clave","la red de co-ocurrencia de palabras clave con frecuencia mayor o igual a 3","*Nota.* El color indica la comunidad detectada por modularidad (modularidad baja). Elaboración propia a partir de las palabras clave de los registros.")
FIG("fig_mapa_centralidad_densidad.png","Mapa estratégico de centralidad y densidad de las comunidades de palabras clave","el mapa estratégico de las comunidades de palabras clave","*Nota.* Centralidad: enlaces externos ponderados; densidad: enlaces internos por palabra. Elaboración propia.")
FIG("fig_pareto_citas.png","Concentración de citas de los documentos (diagrama de Pareto)","la concentración de las citas de Scopus en pocos documentos","*Nota.* Documentos con dato de citas de Scopus. Veinticuatro documentos concentran 80 % de las citas. Elaboración propia.")
for n in ("5.2","5.3","5.4","5.5"):
    emit(section(INF,f"### {n}","###") and [f"### {n} "+re.sub(r'^\d+\.\d+ ','',[l for l in INF if l.startswith(f'### {n} ')][0][4:].split(' ',1)[1])]+section(INF,f"### {n}","###"),shift=1)
H(2,"Triangulación de afirmaciones"); emit(sec(INF,"6."))
H(2,"Variables econométricas, vacíos y brechas"); emit(sec(INF,"8."))
H(2,"Análisis relacional"); emit(sec(REL,"2.")); emit(sub(REL,"3.1")); emit(sub(REL,"3.3")); emit(sub(REL,"3.4")); emit(sub(REL,"3.5")); emit(sub(REL,"3.6"))
FIG("fig_red_relaciones.png","Red de relaciones tipificadas entre documentos","la red de relaciones tipificadas entre documentos","*Nota.* El color del nodo indica la relevancia (rojo, núcleo; azul, adyacente; verde, periférico); el color de la arista indica el tipo de relación. Se excluye la síntesis D100. Elaboración propia (`csv/analisis_relacional.csv`).")
H(3,"Puntaje de integración relacional"); emit(sec(REL,"5."))
PIF=f"{L}/patentes/informe_patentes.md"; PI=open(PIF).read().split("\n") if os.path.exists(PIF) else []
if PI:
    H(2,"Módulo de patentes")
    P("Se analizó un módulo separado de 11 patentes (10 de Strong Force VCN Portfolio 2019 y 1 de International Business Machines) aportadas en la carpeta Patentes del repositorio, con reconocimiento óptico de sus 4.048 páginas. El método, las 11 fichas y el informe completo figuran en el Apéndice K; aquí se resumen la relevancia y la madurez.")
    emit(sub(PI,"3.3")); emit(sub(PI,"3.4"))
    FIG("fig_patentes_terminos.png","Frecuencia de términos del eje del corpus en las patentes","la frecuencia de términos del eje del corpus en el texto completo de cada patente","*Nota.* Apariciones por 1.000 palabras en el texto completo reconocido por OCR (4.048 páginas; frecuencias como límites inferiores). Los diez documentos de Strong Force comparten una descripción de plataforma. Elaboración propia (`patentes/csv/patentes_terminos.csv`).")
    FIG("fig_patentes_relaciones.png","Relaciones entre las patentes y los documentos del corpus","las relaciones tipificadas entre las patentes y los documentos del corpus","*Nota.* El color de la línea indica el tipo de relación; los arcos de la izquierda unen patentes de una misma familia o con funciones afines. Elaboración propia (`patentes/csv/patentes_relaciones.csv`).")
H(1,"Discusión de controversias")
for p in ESCENA_CONTROV: P(p)
H(2,"Contradicciones y tensiones entre documentos"); emit(sub(REL,"3.2"))
H(2,"Patrones, tensiones y anomalías"); emit(sec(INF,"7.")[:sec(INF,"7.").index("### 7.1 Circularidad del corpus con la síntesis D100")])
H(2,"Circularidad del corpus con la síntesis de Scopus AI"); emit(sub(INF,"7.1"))
H(2,"Falacias"); emit(sub(INF,"7.2"))
H(2,"Relevancia frente a calidad de reporte"); emit(sub(INF,"7.3"))
H(1,"Discusión")
H(2,"Herramientas de estructuración"); emit(sec(INF,"9."))
H(2,"Proposiciones emergentes"); emit(sec(REL,"4."))
H(2,"Premortem y escenarios"); emit(sec(INF,"10."))
H(2,"Limitaciones del análisis relacional"); emit(sec(REL,"6."))
H(1,"Limitaciones y vacíos (¿qué se me escapa?)"); emit(sec(INF,"11."))
H(1,"Conclusión")
emit(sec(INF,"1."))
H(2,"Recomendaciones"); emit(sec(INF,"12."))
emit(sec(REL,"7."))
H(1,"Áreas futuras")
for p in FUTURAS: P(p)
blocks.append(dict(t="ol",items=[conv(x) for x in FUT_LIST]))
# ---------- referencias ----------
refs=[ref_apa(i) for i in ids]
meto=[l for l in sec(INF,"14.") if l.strip() and not l.startswith("Revisión final")]
refs+= [l.strip() for l in meto]
def keyf(r): return re.sub(r"[^a-záéíóúñ0-9]","",r.lower())
_pb=f"{L}/patentes/csv/patentes_bibliografia.csv"
if os.path.exists(_pb): refs+= [r for r in pd.read_csv(_pb).referencia_apa7]
refs=sorted(set(refs),key=keyf)
blocks.append(dict(t="pb")); blocks.append(dict(t="h1",x="Referencias"))
for r in refs: blocks.append(dict(t="ref",x=r))
# ---------- apéndices ----------
tri=pd.read_csv(f"{C}/triangulacion.csv"); pt=pd.read_csv(f"{C}/patrones_tensiones.csv"); mm=pd.read_csv(f"{C}/madurez_multinivel.csv").set_index("doc_id"); E=pd.read_csv(f"{C}/analisis_relacional.csv")
def apx(letter,title):
    blocks.append(dict(t="pb")); blocks.append(dict(t="h1",x=f"Apéndice {letter}")); blocks.append(dict(t="h1",x=title))
apx("A","Clave de documentos")
P("Cada clave del análisis (D001 a D101) corresponde a la cita autor-año y al título indicados. Las referencias completas figuran en la lista de referencias.")
rowsA=[["Clave","Cita","Título"]]
for i in ids: rowsA.append([i,cite(i),inv[i]["meta"].get("titulo","")[:150]])
blocks.append(dict(t="table",rows=rowsA,w=[8,22,70],small=True,cap=("Clave de los documentos del lote","Correspondencia entre clave, cita y título")))
apx("B","Triangulación de afirmaciones transversales")
rowsB=[["ID","Afirmación","Docs.","Grupos","Veredicto"]]
for r in tri.itertuples(): rowsB.append([r.id,conv(r.afirmacion),str(r.n_documentos),str(r.grupos_independientes_de_autoria),r.veredicto])
blocks.append(dict(t="table",rows=rowsB,w=[6,60,8,8,18],small=True,cap=("Triangulación de afirmaciones","Documentos y grupos independientes de autoría por afirmación")))
apx("C","Patrones, tensiones y anomalías")
rowsC=[["ID","Tipo","Descripción","Implicación"]]
for r in pt.itertuples(): rowsC.append([r.id,r.tipo,conv(r.descripcion),conv(r.implicacion)])
blocks.append(dict(t="table",rows=rowsC,w=[6,10,50,34],small=True,cap=("Patrones, tensiones y anomalías","Resumen de los 19 elementos identificados")))
apx("D","Tabla de control del lote")
rowsD=[["Clave","Relevancia","TRL","BRL","Valle","Recomendación","Robustez"]]
for i in ids:
    a=A[i]; m=a["madurez"]; rb=round(0.3*a["c3"]["robustez"][0]+0.3*a["c3"]["robustez"][1]+0.25*a["c3"]["robustez"][2]+0.15*a["c3"]["robustez"][3],1)
    rowsD.append([i,a["relevancia"],str(m["trl"][0]) if m["trl"][0] is not None else "N/A",str(m["brl"][0]) if m["brl"][0] is not None else "N/A",str(a["valle"][0]),"Rechazar como evidencia" if a["recomendacion"].startswith("Rechazar") else "Aceptar con reservas",str(rb)])
blocks.append(dict(t="table",rows=rowsD,w=[10,16,8,8,8,38,12],small=True,cap=("Tabla de control","Relevancia, madurez, valle de la muerte, recomendación y robustez por documento")))
apx("E","Relaciones tipificadas de confirmación, contradicción y extensión")
sub_=E[(~E.origen.isin(["D100","D101"]))&(~E.destino.isin(["D100","D101"]))&(E.tipo.isin(["CONFIRMA","CONTRADICE","EXTIENDE"]))]
rowsE=[["Origen","Tipo","Destino","Justificación"]]
for r in sub_.itertuples():
    if r.tipo!="EXTIENDE" and r.origen>r.destino: continue
    rowsE.append([r.origen,r.tipo,r.destino," ".join(str(r.justificacion).split())])
blocks.append(dict(t="table",rows=rowsE,w=[8,12,8,72],small=True,cap=("Relaciones sustantivas entre documentos","Confirmación, contradicción y extensión; excluye las síntesis de buscadores")))
# ---------- fichas (apéndice F) y patentes (apéndice G) en formato compacto ----------
def ficha_blocks(path):
    ls=open(path).read().split("\n"); i=0; para=[]
    def fl():
        nonlocal para
        if para: blocks.append(dict(t="p",x=" ".join(para),c=1)); para=[]
    first=True
    while i<len(ls):
        ln=ls[i].rstrip()
        if not ln.strip(): fl(); i+=1; continue
        m=re.match(r"^(#{1,4}) (.*)",ln)
        if m:
            fl(); n=len(m.group(1)); blocks.append(dict(t="fh%d"%min(n,4),x=m.group(2),pb=(n==1))); i+=1; continue
        if ln.startswith("> "): fl(); blocks.append(dict(t="p",x=ln[2:].replace("`",""),c=1)); i+=1; continue
        if ln.startswith("|"):
            fl(); rows=[]
            while i<len(ls) and ls[i].startswith("|"):
                if not re.match(r"^\|[-| :]+\|$",ls[i]): rows.append([c.strip() for c in ls[i].strip().strip("|").split("|")])
                i+=1
            blocks.append(dict(t="table",rows=rows,small=True,c=1,cap=("",""))); continue
        if re.match(r"^\d+\. ",ln):
            fl(); items=[]
            while i<len(ls) and re.match(r"^\d+\. ",ls[i]): items.append(re.sub(r"^\d+\. ","",ls[i]).replace("`","")); i+=1
            blocks.append(dict(t="ol",items=items,c=1)); continue
        if ln.startswith("- "):
            fl(); items=[]
            while i<len(ls) and ls[i].startswith("- "): items.append(ls[i][2:].replace("`","")); i+=1
            blocks.append(dict(t="ul",items=items,c=1)); continue
        if ln.strip()=="---": fl(); i+=1; continue
        para.append(ln.replace("`","")); i+=1
    fl()
# ---------- apéndices F a I: ficha resumen, verificación, diagramas e índice de datos ----------
def md_sections(lines):
    out=[]
    for ln in lines:
        if ln.startswith("# ") or (ln.startswith("`") and ln.endswith("`")) or ln.strip()=="---": continue
        out.append("### "+ln[3:] if ln.startswith("## ") else ln)
    return out
apx("F","Ficha resumen del lote (16 secciones)")
P("Se reproduce la ficha resumen del lote con sus 16 secciones: identificación, alcance, inventario, calidad de extracción, relevancia, madurez, brechas, síntesis dialéctica, indicadores, triangulación, patrones, competidores, variables, aprendizaje automático, riesgos y recomendaciones.")
emit(md_sections(open(f"{I}/FICHA_RESUMEN_LOTE.md").read().split("\n")))
apx("G","Lista de verificación del protocolo")
P("La lista siguiente contrasta cada requisito del protocolo SYNAPSE V19.0 con el producto que lo cumple y con su estado, incluidos los límites declarados.")
emit(md_sections(open(f"{I}/checklist_validacion.md").read().split("\n")))
apx("H","Diagramas de proceso y de relaciones")
P("Los diagramas se generaron con Mermaid a partir de los datos del lote y se incluyen en formato vectorial (SVG) con texto editable.")
FIG("fig_mermaid_flujo_proceso.png","Flujo de proceso del análisis del lote L01","el flujo de proceso desde los documentos hasta el informe del lote","*Nota.* Elaboración propia (`informe/diagramas_mermaid.md`).")
FIG("fig_mermaid_relaciones_nucleo.png","Relaciones tipificadas entre documentos núcleo","las relaciones tipificadas entre los documentos núcleo que tienen al menos un vínculo","*Nota.* Solo se muestran los documentos núcleo con vínculos; los demás carecen de relaciones con otro núcleo. Elaboración propia (`informe/diagramas_mermaid.md`).")
FIG("fig_mermaid_valle_muerte.png","Estructura del valle de la muerte dominante","la estructura del valle de la muerte dominante (V1) y su salida propuesta","*Nota.* Medianas del lote de 87 documentos técnicos. Elaboración propia (`informe/diagramas_mermaid.md`).")
apx("I","Índice de los archivos de datos y su ubicación en el documento")
P("Los archivos de datos del repositorio (carpeta csv) contienen la información tabular completa del análisis. La tabla indica el contenido de cada archivo, su número de filas y el lugar del documento en que se reproduce. Los datos por documento se reproducen dentro de cada ficha (Apéndice J), de modo que no se duplican como tablas independientes.")
DESC=[("inventario","Metadatos de los 101 documentos (autores, año, fuente, tipo, relevancia)","Apéndice A; Capa 1 de cada ficha"),("kpis","Indicadores extraídos de cada documento","Sección B.3 de cada ficha"),
("madurez_multinivel","TRL, MRL, BRL, IRL, DRL y SRL con evidencia y justificación","Apéndice D; sección B.4 de cada ficha; Figuras 2 y 3"),("brechas_madurez","Brechas TRL−BRL, TRL−IRL y BRL−DRL","Sección B.4; Figura 5"),
("valles_muerte","Valle de la muerte, severidad y estrategia de salida","Sección B.4; Figura 4"),("dialectica","Tesis, antítesis, síntesis y robustez","Capa 3 y sección B.1 de cada ficha"),
("falacias","Falacias detectadas con evidencia e impacto","Sección B.5 de cada ficha"),("gaps_oportunidades","Brechas de conocimiento y oportunidades con prioridad","Sección B.6 de cada ficha"),
("competidores","Competidores, actores y alternativas tecnológicas","Sección B.8 de cada ficha"),("figuras","Figuras y tablas clave de cada documento","Sección B.7 de cada ficha"),
("sintesis_interpretativa","Síntesis, zonas grises, ideas propositivas y relaciones poco exploradas","Capa 3 de cada ficha"),("variables_econometricas","Variables dependientes, explicativas, controles, datos y método","Sección B.9 de cada ficha"),
("vacios_detectados","Vacíos por tipo (TERR, POBL, TEMP, MET, VAR, TEOR, CAUS)","Sección B.9 de cada ficha"),("protopreguntas","Preguntas del documento, hipótesis rivales y contraejemplos","Sección B.2 y Capa 3 de cada ficha"),
("bibliografia","Referencias APA 7 de los 101 documentos","Referencias"),("fichas_bibliograficas","Control de extensión y completitud de las fichas","Solo archivo de datos"),
("analisis_relacional","Relaciones tipificadas entre documentos con justificación","Apéndice E; Resultados (análisis relacional); Figura 11"),("triangulacion","Triangulación de afirmaciones transversales","Apéndice B"),("patrones_tensiones","Patrones, tensiones y anomalías","Apéndice C")]
rowsI=[["Archivo","Contenido","Filas","Dónde se reproduce"]]
import glob as _gg
for n,d_,w_ in DESC:
    f_=f"{C}/{n}.csv"; rowsI.append([n+".csv",d_,str(len(pd.read_csv(f_))) if os.path.exists(f_) else "—",w_])
mlf=sorted(_gg.glob(f"{C}/ml/*.csv")); rowsI.append(["ml/ (%d archivos)"%len(mlf),"Resultados de aprendizaje automático: grupos, temas LDA, redes, bibliometría y sensibilidad","—","Resultados (aprendizaje automático); Figuras 6 a 10"])
for f_ in sorted(_gg.glob(f"{L}/patentes/csv/patentes_*.csv")):
    rowsI.append(["patentes/"+os.path.basename(f_),"Módulo de patentes: "+os.path.basename(f_)[9:-4].replace("_"," "),str(len(pd.read_csv(f_))),"Apéndice K"])
blocks.append(dict(t="table",rows=rowsI,w=[26,40,7,27],small=True,cap=("Archivos de datos del repositorio","Contenido, filas y ubicación en el documento")))
import glob as _g
apx("J","Fichas bibliográficas analíticas de los 101 documentos")
P("Se reproducen las 101 fichas de cuatro capas con el análisis SYNAPSE de cada documento, en el orden de las claves D001 a D101. Las fichas conservan su formato de trabajo (interlineado sencillo y tablas de indicadores) y su referencia APA 7 en la Capa 1.")
for f in sorted(_g.glob(f"{L}/fichas/D*.md")): ficha_blocks(f)
PAT=sorted(_g.glob(f"{L}/patentes/fichas/P*.md"))
if PAT:
    apx("K","Módulo de patentes: informe y fichas")
    if PI:
        lines=[]; skip=False
        for ln in PI[1:]:
            if ln.startswith("## 10."): skip=True
            elif ln.startswith("## "): skip=False
            if skip: continue
            lines.append("### "+ln[3:] if ln.startswith("## ") else ln)
        emit(lines,shift=0)
    for f in PAT: ficha_blocks(f)
# captions para tablas del cuerpo
caps=[("Naturaleza de los componentes del análisis","Qué se calculó y qué se juzgó"),("Triangulación y escenarios","Futuros posibles, objetivos y opciones viables")]
k=0
for b in blocks:
    if b["t"]=="table" and "cap" not in b:
        b["cap"]=caps[k] if k<len(caps) else ("Tabla","Resumen"); k+=1
meta=dict(titulo="Tecnología, transferencia y resiliencia empresarial tras sismos: análisis sistemático del lote L01 con SYNAPSE V19.0",resumen=RESUMEN,kw=KW)
json.dump(dict(meta=meta,blocks=blocks),open(f"{OUT}/bloques.json","w"),ensure_ascii=False)
words=sum(len(re.sub(r"\*","",(b.get("x") or "")).split())+sum(len(x.split()) for x in b.get("items",[])) for b in blocks)
print("bloques:",len(blocks),"palabras aprox. (cuerpo+refs):",words,"tablas:",sum(1 for b in blocks if b["t"]=="table"),"refs:",len(refs))
