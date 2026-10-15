"""Genera conexiones.json (relaciones inter-documentales tipificadas) y csv/analisis_relacional.csv.
Fuentes: (1) citación verificada por título contra listas de referencias; (2) autoría compartida; (3) juicio del analista (relaciones HAND)."""
import sys, os, re, json, itertools, collections
sys.path.insert(0, os.path.dirname(__file__))
from synlib import *
import pandas as pd
inv={d["doc_id"]:d for d in load_inv()}; A=load_docs()
cites=set(tuple(x) for x in json.load(open(f"{BASE}/aristas_citacion_verificadas.json")))
refmap={int(k):v for k,v in json.load(open(f"{BASE}/d100_referencia_a_documento.json")).items()}
refmap.setdefault(1,["D070"])  # la referencia 1 queda fuera del patrón de división del texto extraído; verificada por título (Habib et al., 2025)
assert sum(1 for v in refmap.values() for _ in v)==86, "se esperaban 86 documentos del lote citados por D100"
def authors(m):
    full=m.get("autores_completos") or ""
    if full: return {re.sub(r"\s*\(\d+\)\s*$","",a.strip()).lower() for a in full.split(";") if a.strip()}
    return {a.strip().lower() for a in (m.get("autores") or "").split(";") if a.strip()}
au={i:authors(inv[i]["meta"]) for i in inv}
def short(i): return A[i]["cluster_tema"][:70]
INV={"CONFIRMA":"CONFIRMA","CONTRADICE":"CONTRADICE","COMPLEMENTA":"COMPLEMENTA","EXTIENDE":"PRECEDE","DEPENDE_DE":"PRECEDE","PRECEDE":"EXTIENDE"}
H=[]  # (a, tipo, b, texto)
def h(a,t,b,x): H.append((a,t,b,x))
# --- Gemelos digitales para desastres y recuperación
h("D013","EXTIENDE","D006","propone un marco integral de gemelo digital posdesastre (IA explicable, dinámica social, sistemas interconectados) que desarrolla la visión de ciudad-gemelo en desastre de D006; ambos son propuestas conceptuales sin validación operativa")
h("D048","EXTIENDE","D072","usa el gemelo digital como imagen operativa común para estimar daños y necesidades de rescate, apoyado en el antecedente de modelado híbrido físico-datos de D072")
h("D080","EXTIENDE","D048","replica la lógica de imagen operativa común en un distrito industrial con sensores IoT y arquitectura híbrida; comparte autoría (Korkmaz, Demirkesen) con D048, por lo que no es una confirmación independiente")
h("D080","DEPENDE_DE","D006","retoma la propuesta de gemelo digital de ciudad en desastre como referencia conceptual")
h("D078","EXTIENDE","D013","construye un gemelo comunitario con datos públicos reales que operacionaliza parte del marco posdesastre de D013, con validación todavía simulada")
h("D070","COMPLEMENTA","D079","D079 revisa gemelos urbanos con IoT e IA en ciudades inteligentes y D070 los aplica al caso de terremotos fuertes y a los ODS; ambos concluyen potencial con evidencia empírica escasa")
h("D070","DEPENDE_DE","D006","adopta el concepto de gemelo para gestión de desastres como base del análisis de beneficios de sostenibilidad")
h("D034","CONFIRMA","D048","ambos estiman daño por edificio y necesidades de respuesta con gemelos urbanos y escenarios sísmicos; proceden de contextos y grupos distintos (Ningxia, China, y Kocaeli, Türkiye)")
h("D034","COMPLEMENTA","D064","D034 modela intensidad y daño por edificio con actualización por sensores; D064 aporta la arquitectura 5G y de borde para actualizar gemelos con baja latencia")
h("D008","COMPLEMENTA","D064","D008 resuelve la interoperabilidad entre simulaciones (ficha BSIC) y D064 la latencia de actualización; los dos desafíos coinciden con los identificados por D100 como barreras centrales")
h("D021","COMPLEMENTA","D025","D021 integra datos heterogéneos con repositorio BIM y web semántica para gestión de activos; D025 sincroniza BIM, inspecciones y sensores con identificadores persistentes alineados con IFC 4.3")
h("D004","CONFIRMA","D028","ambas revisiones concluyen que los gemelos digitales tienen potencial pero la implementación real es incipiente y depende de integración de datos, escalabilidad e inversión")
h("D028","CONFIRMA","D079","ambas revisiones señalan interoperabilidad, calidad de datos y escalabilidad como barreras y escasa validación en operación real")
h("D013","CONFIRMA","D004","coinciden en que la literatura de gemelos digitales es fragmentada e incipiente y en que faltan marcos integrados")
h("D061","CONFIRMA","D013","la revisión PRISMA de gemelos para inundaciones urbanas (85 estudios) reporta mejoras de pronóstico y respuesta y coincide en la necesidad de integrar datos de teledetección, IoT y modelos; D061 cita a D013 y D006")
h("D081","COMPLEMENTA","D013","D081 estudia el efecto del gemelo sobre la resiliencia de cadenas de suministro por etapas y D013 sobre la gestión posdesastre; ambas mezclan evidencia conceptual y de simulación")
h("D081","CONFIRMA","D037","ambos hallan efectos por etapa de la disrupción, mayores en preparación y respuesta que en recuperación (D037 r=0,331 global y r=0,273 en recuperación)")
h("D037","COMPLEMENTA","D017","D037 mide asociación entre tecnologías digitales y resiliencia de cadena de suministro con metaanálisis y D017 describe la evolución y barreras del IoT en esas cadenas")
h("D017","CONFIRMA","D016","ambos describen crecimiento de la literatura de IoT en cadenas de suministro desde 2017-2018 y concentración en blockchain, aprendizaje automático y Industria 4.0")
h("D051","COMPLEMENTA","D017","D051 clasifica 92 desafíos en 16 categorías y D017 sintetiza barreras (seguridad, interoperabilidad) para IoT en cadenas de suministro")
h("D024","COMPLEMENTA","D016","D024 trata cadenas de alimentos y D016 logística general; ambos son revisiones bibliométricas de periferia temática con IoT")
h("D077","COMPLEMENTA","D037","D077 propone un marco conceptual ilustrado con datos abiertos de compras en línea durante la pandemia en Australia, sin medir resiliencia; D037 cuantifica una asociación moderada y distinta por etapa, lo que matiza las afirmaciones generales de D077")
# --- Organización, adopción y resiliencia organizacional
h("D007","EXTIENDE","D005","D007 refina la tesis de D005 (los beneficios del IoT dependen de condiciones institucionales) con aceptación de partes interesadas, liderazgo digital y opacidad parcial; D007 cita a D005")
h("D007","CONFIRMA","D005","ambos concluyen que la adopción del IoT es un proceso organizacional y no solo técnico, con consecuencias estructurales")
h("D030","DEPENDE_DE","D017","D030 cita a D017 como respaldo del vínculo entre IoT y resiliencia; su evidencia es una encuesta transversal")
h("D030","CONFIRMA","D029","ambos muestran con encuestas que IoT y gemelo digital mejoran la resiliencia organizacional operativa mediante capacidades; ambos son transversales y de autorreporte")
h("D082","CONTRADICE","D030","D082 concibe la resiliencia organizacional como propiedad emergente de mecanismos colectivos, adaptativos y dinámicos, mientras D030 la trata como variable mediadora lineal entre tecnología y desempeño; tensión conceptual no resuelta")
h("D082","COMPLEMENTA","D029","D082 ofrece el marco de mecanismos y D029 aporta evidencia sobre capacidad de absorción y turbulencia tecnológica como moderador")
h("D052","COMPLEMENTA","D085","D052 identifica la transparencia de la información como mediador del efecto del gemelo en la eficiencia (0,749); D085 identifica factores de oficina, obra e interfaz; ambos usan encuestas de percepción en construcción")
h("D085","CONFIRMA","D052","coinciden en que el valor del gemelo digital en construcción pasa por el intercambio de información y la decisión colaborativa, no por la tecnología por sí sola")
h("D029","CONFIRMA","D005","la capacidad de absorción de conocimiento como condición de beneficio refuerza la tesis de D005 sobre condiciones institucionales de la adopción")
h("D012","CONFIRMA","D003","ambos señalan que las soluciones tecnológicas dominan la literatura de desastres con integración débil de conocimiento, equidad y factores humanos")
h("D099","CONFIRMA","D003","coinciden en que la evidencia es fragmentada y en que faltan estudios sobre las condiciones de adopción tecnológica en desastres (barreras y factores críticos en D099; acceso, equidad y gobernanza en D003)")
h("D099","COMPLEMENTA","D013","D099 mapea seis familias de Industria 4.0 en gestión de riesgo de desastres y D013 se centra en gemelos posdesastre; ambos reconocen un campo incipiente")
h("D099","CONFIRMA","D050","ambos identifican el IoT como núcleo de la gestión de desastres con beneficios de monitoreo y comunicación y con desafíos de confiabilidad")
h("D087","COMPLEMENTA","D003","ambos son editoriales de política sin datos propios: D087 sobre el sistema de ciencia, tecnología e innovación de Colombia (2008) y D003 sobre tecnología y gestión de desastres (2026); D087 aporta el contexto institucional nacional")
# --- Reforzamiento y economía sísmica
h("D040","EXTIENDE","D054","D040 incorpora pérdidas indirectas y carbono del ciclo de vida al análisis costo-beneficio de refuerzo que D054 desarrolla con víctimas y reparaciones; D040 cita a D054")
h("D040","DEPENDE_DE","D002","D040 cita a D002 al comparar estrategias de refuerzo con camisas de acero")
h("D040","CONFIRMA","D069","ambos muestran que incluir recuperación, tiempo de inhabilitación y pérdidas indirectas cambia la medida preferida de refuerzo frente a considerar solo pérdidas directas")
h("D069","COMPLEMENTA","D054","D054 valora la reducción de víctimas y D069 la ganancia de funcionalidad; ambos contribuyen a justificar el refuerzo más allá de las reparaciones")
h("D053","CONFIRMA","D011","ambos muestran que el tiempo de reparación del edificio no basta como medida de recuperación y que las demoras y la inactividad deben modelarse; D011 antecede a D053")
h("D053","COMPLEMENTA","D040","comparten autoría (Galasso): D053 aporta modelos de consecuencia de tiempo de recuperación y D040 los usa en decisiones de refuerzo; no son confirmaciones independientes")
h("D002","COMPLEMENTA","D067","D002 optimiza camisas de acero con algoritmo genético (costo 40 % menor) y D067 evalúa camisas de concreto con fibras de acero (capacidad cortante hasta 39 % mayor); ambos son estudios de caso en estructuras específicas")
h("D027","COMPLEMENTA","D002","D027 compara fibras de vidrio y carbono por rentabilidad del confinamiento y D002 el costo de camisas de acero; ambos priorizan costo con evidencia de laboratorio o modelo")
h("D011","PRECEDE","D053","el marco analítico de D011 (varios tipos de inactividad y tácticas de mitigación) antecede a los modelos de simulación de alta fidelidad de D053")
# --- Alerta temprana y sensado sísmico
h("D075","EXTIENDE","D045","D075 lleva la alerta sísmica de bajo costo a una red LoRa multisalto descentralizada; D045 revisa sensores MEMS de bajo costo y cita a D049; D075 cita a D045; comparten autoría (Prasanna)")
h("D049","CONFIRMA","D073","ambos muestran que detectar y generar la alerta en el nodo reduce la latencia frente a arquitecturas centralizadas (D049 1,24 a 2,88 s; D073 localización más temprana en sismo de magnitud 5,4), con evidencia de simulación o datos históricos")
h("D075","CONFIRMA","D049","comparten autoría (Prasanna, Holden): la arquitectura descentralizada reduce la latencia; la concordancia procede del mismo grupo")
h("D063","COMPLEMENTA","D049","ambos aplican el principio PLUM: D063 a ferrocarriles de alta velocidad con arquitectura jerárquica y D049 de forma modificada en sensores MEMS de bajo costo con procesamiento en el nodo")
h("D060","CONTRADICE","D041","D060 reporta que XGBoost supera a otros algoritmos en intensidad sísmica (99,05 %) y D041 que una red neuronal supera a XGBoost en magnitud; las tareas, datos y métricas difieren, por lo que el orden de modelos no es transferible")
h("D010","COMPLEMENTA","D041","ambos estiman magnitud con aprendizaje automático; D010 corrige el desbalance de eventos grandes con datos sintéticos (CTGAN) y D041 compara modelos con datos históricos de California")
h("D019","CONFIRMA","D042","ambas revisiones integran IoT, UAV, comunicaciones y aprendizaje automático en el ciclo del terremoto y concluyen que la integración mejora la conciencia situacional con validación real escasa")
h("D019","DEPENDE_DE","D031","D019 cita a D031 como antecedente de IoT semántico para amenazas geológicas")
h("D019","COMPLEMENTA","D060","comparten autoría (Abdalzaher, Krichen): D019 revisa tecnologías emergentes y D060 aplica aprendizaje automático a intensidad sísmica en sitio")
h("D071","EXTIENDE","D031","D071 desarrolla la semántica de IoT para detección sísmica (ontología SSN/SOSA y clasificador profundo) que D031 planteaba como arquitectura de alerta temprana")
h("D064","CONFIRMA","D066","ambos sostienen que el cómputo en el borde reduce la latencia (D064 retardo medio de 2,1 ms; D066 mejora en simulación); D066 no tiene despliegue real")
h("D066","CONFIRMA","D065","ambos son propuestas de asignación descentralizada de recursos en el borde validadas solo por simulación")
h("D043","CONFIRMA","D065","validación únicamente simulada de marcos descentralizados con tecnologías de borde y aprendizaje federado")
h("D036","DEPENDE_DE","D074","D036 cita a D074 como marco de referencia de IoT con gemelo digital y requisitos de sostenibilidad y resiliencia")
h("D018","COMPLEMENTA","D055","D018 integra agentes de IA y gemelos digitales (demostración por simulación de una red eléctrica genérica) y D055 modela gemelos como agentes BDI; ambos son propuestas de baja madurez")
h("D059","COMPLEMENTA","D018","D059 redefine el gemelo como motor de datos con modelo grande como motor de inteligencia y D018 usa el gemelo como entorno de simulación de agentes; ambos de baja madurez")
# --- SHM, IoT de bajo costo y calidad de datos
h("D086","CONFIRMA","D039","comparten autoría (Yu, Fu, Cui): resuelven calidad de datos y sincronización en redes inalámbricas de monitoreo estructural; no son confirmaciones independientes")
h("D086","DEPENDE_DE","D033","D086 clasifica anomalías de datos a bordo, lo que atiende el hallazgo de D033 de que la calidad del dato pesa más que la arquitectura")
h("D084","COMPLEMENTA","D039","D084 sincroniza nodos por hardware (error de 50 microsegundos) y D039 corrige retardos por aprendizaje profundo; son soluciones alternativas al mismo problema")
h("D084","CONFIRMA","D068","ambos demuestran monitoreo estructural con IoT de bajo costo solo en laboratorio (modelo a escala o viga), con TRL 4 y sin pruebas de campo")
h("D084","COMPLEMENTA","D023","D084 valida nodos en laboratorio y D023 opera un gemelo con LoRaWAN en un puente ferroviario en servicio, lo que muestra la brecha entre prototipo y campo")
h("D009","CONFIRMA","D035","ambos reconstruyen el comportamiento dinámico de puentes con modelos actualizados por datos con errores de hasta 5 % (D009: 1 % a 5 %; D035: menos de 5 % en frecuencias)")
h("D023","COMPLEMENTA","D035","D023 mantiene medición continua con LoRaWAN y D035 actualiza el modelo por algoritmo genético en el puente de acero; ambos aportan a gemelos de puentes")
h("D014","COMPLEMENTA","D020","D014 define dónde instalar sensores en un edificio patrimonial y D020 asocia componentes de IoT con resiliencia sísmica; ambos de ingeniería de edificios con IoT")
h("D015","EXTIENDE","D020","D015 modela de forma conjunta la incertidumbre del sensado y el cumplimiento normativo con un modelo bayesiano ordinal y cita a D020, que asocia componentes de IoT con la resiliencia sísmica mediante una encuesta")
h("D015","DEPENDE_DE","D056","D015 cita a D056 como antecedente de IoT en gestión de desastres")
h("D032","COMPLEMENTA","D009","D032 mapea la literatura de gemelos con IA para SHM y D009 es un ejemplo de gemelo con monitoreo híbrido de modelo y datos")
# --- IoT/UAV y respuesta
h("D062","COMPLEMENTA","D022","D062 planifica trayectorias de AAV con LoRa por aprendizaje por refuerzo y D022 revisa UAV como estaciones base aéreas para restablecer comunicaciones; D062 se valida con simulaciones y pruebas de campo con una plataforma dron-LoRa y D022 sintetiza estudios con evidencia empírica a nivel de sistema")
h("D001","COMPLEMENTA","D062","D001 optimiza la ruta y la energía de un UAV para recolectar datos y D062 la trayectoria y la conectividad; ambos con simulación")
h("D076","COMPLEMENTA","D042","D076 clasifica daño posterremoto en imágenes de UAV con aprendizaje profundo ligero y D042 revisa IoT y UAV en la gestión del terremoto")
h("D044","CONFIRMA","D050","ambos informan beneficios del IoT en respuesta a emergencias y gestión de desastres, con ejemplos descriptivos")
h("D056","CONFIRMA","D050","ambos describen mejoras del IoT en alerta temprana, monitoreo y comunicación para desastres naturales con evidencia mayormente descriptiva")
h("D026","COMPLEMENTA","D048","D026 caracteriza las soluciones digitales tras el terremoto de 2023 en Türkiye (plataformas web de proveedores privados) y D048 modela un gemelo para una respuesta en Kocaeli; ambos con Türkiye como referencia territorial")
h("D047","COMPLEMENTA","D026","D047 revisa SIG en la gestión del transporte posterremoto y D026 las soluciones digitales de respuesta y recuperación; ambos con evidencia mayormente descriptiva")
h("D100","PRECEDE","D101","ambas son síntesis automáticas del mismo tema generadas en 2026 por buscadores distintos; D101 comparte al menos dos documentos de referencia con la lista de D100")
h("D101","CONFIRMA","D100","coinciden en la conclusión de que gemelo digital, IoT e Industria 4.0 son centrales para la recuperación posdesastre, pero no son fuentes independientes (la lista de D100 incluye los documentos D070 y D080 citados por D101)")
h("D101","DEPENDE_DE","D099","la primera referencia de D101 es la revisión de Habibi Rad et al. (D099)")
h("D101","DEPENDE_DE","D070","la segunda referencia de D101 es el estudio de Habib et al. (D070)")
h("D101","DEPENDE_DE","D080","la tercera referencia de D101 es el estudio de caso de Cayirova (D080)")
h("D100","COMPLEMENTA","D099","D100 declara un alcance de 2020-2024 pero su lista incluye 49 referencias de 2025-2026 y no declara protocolo; D099 cubre el tema hasta junio de 2021 con protocolo PRISMA declarado, lo que contrasta el rigor y el periodo")
# registro
EDGES=[]  # dict(src,tipo,dst,base,texto)
seen=set()
def add(a,t,b,x,base):
    k=(a,t,b)
    if k in seen: return
    seen.add(k); EDGES.append(dict(origen=a,tipo=t,destino=b,base=base,justificacion=x))
for a,t,b,x in H:
    base=["juicio del analista"]
    if (a,b) in cites: base.append("citación verificada de %s a %s"%(a,b))
    if (b,a) in cites: base.append("citación verificada de %s a %s"%(b,a))
    if au[a]&au[b]: base.append("autoría compartida")
    add(a,t,b,x,"; ".join(base))
    add(b,INV[t],a,"relación inversa de %s %s %s: %s"%(a,t,b,x[:150]),"; ".join(base))
# citas verificadas no cubiertas: DEPENDE_DE y su inverso
for a,b in sorted(cites):
    if a=="D100": continue
    pair=any((x==a and y==b) or (x==b and y==a) for x,_,y,_ in H)
    if not pair:
        add(a,"DEPENDE_DE",b,"cita a %s en su lista de referencias (verificado por coincidencia de título); %s: %s"%(b,b,short(b)),"citación verificada")
        add(b,"PRECEDE",a,"es citado por %s (verificado por coincidencia de título)"%a,"citación verificada")
# D100 -> corpus
for n,docs in refmap.items():
    for b in docs:
        add("D100","DEPENDE_DE",b,"referencia %d de la lista de la síntesis"%n,"citación verificada (lista de referencias de D100)")
        add(b,"PRECEDE","D100","es la referencia %d de la síntesis de Scopus AI"%n,"citación verificada (lista de referencias de D100)")
df=pd.DataFrame(EDGES); df.to_csv(f"{L}/csv/analisis_relacional.csv",index=False,encoding="utf-8-sig")
# conexiones.json para fichas
conns=collections.defaultdict(list)
for e in EDGES:
    if e["origen"]=="D100" and e["justificacion"].startswith("referencia"): continue
    if e["destino"]=="D100" and e["justificacion"].startswith("es la referencia") : continue
    conns[e["origen"]].append(f"**{e['tipo']}** {e['destino']} ({short(e['destino'])}): {e['justificacion']} [{e['base']}]")
conns["D100"].insert(0,"**DEPENDE_DE** D001-D086 (86 documentos del lote): 86 de las 93 referencias de la síntesis coinciden con documentos D001-D086 (verificado por título); las 7 restantes no figuran en el lote [citación verificada]. El corpus Scopus del lote y la síntesis D100 no son, por tanto, fuentes independientes")
for b,docs in list(collections.defaultdict(list).items()): pass
for n,docs in refmap.items():
    for b in docs:
        conns[b].append(f"**PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia {n} de la síntesis [citación verificada]")
for i in inv:
    if "D088"<=i<="D098": conns[i].append("Sin relación temática con el eje del corpus; comparte número de revista (Biomédica 28(3), 2008) con D087-D098; actúa como control negativo en las pruebas de similitud y sensibilidad [juicio del analista]")
json.dump(conns,open(f"{BASE}/conexiones.json","w"),ensure_ascii=False,indent=1)
print(len(EDGES),"aristas;",sum(1 for i in inv if conns.get(i)),"documentos con conexiones; tipos:",collections.Counter(e["tipo"] for e in EDGES))
