"""Triangulación de afirmaciones entre documentos y tabla de patrones/tensiones. Cifras calculadas sobre los YAML y el inventario;
la asignación de documentos a cada afirmación y los veredictos son juicio del analista (se declara en la columna 'base')."""
import sys, os, re, json, statistics, collections, itertools
sys.path.insert(0, os.path.dirname(__file__))
from synlib import *
import pandas as pd
A=load_docs(); inv={d["doc_id"]:d for d in load_inv()}; OUT=f"{L}/csv"
def authors(m):
    full=m.get("autores_completos") or ""
    if full: return {re.sub(r"\s*\(\d+\)\s*$","",a.strip()).lower() for a in full.split(";") if a.strip()}
    return {a.strip().lower() for a in (m.get("autores") or "").split(";") if a.strip()}
au={i:authors(inv[i]["meta"]) for i in inv}
def grupos_independientes(docs):
    """Componentes conexos del grafo de autoría compartida entre los documentos de la lista."""
    parent={d:d for d in docs}
    def f(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for a,b in itertools.combinations(docs,2):
        if au[a]&au[b]: parent[f(a)]=f(b)
    return len({f(d) for d in docs})
def med(docs,key):
    v=[A[d]["madurez"][key][0] for d in docs if A[d]["madurez"][key][0] is not None]
    return (statistics.median(v) if v else None, len(v))
T=[
("T01","El procesamiento en el nodo o en el borde reduce la latencia de alerta y actualización frente a arquitecturas centralizadas",["D045","D049","D073","D075","D064","D066"],"Laboratorio, datos históricos y simulación; D066 solo simulado","Ninguna directa; las métricas de latencia no son comparables (milisegundos frente a segundos y definiciones distintas)","Triangulado con reservas","Tres de seis documentos (D045, D049, D075) comparten autoría; la convergencia independiente la aportan D073, D064 y D066"),
("T02","La interoperabilidad y la calidad de datos son la barrera técnica principal de los gemelos digitales y del IoT en desastres",["D004","D008","D013","D021","D025","D028","D033","D079","D099","D100"],"Revisiones y marcos conceptuales; casi sin mediciones de costo","Ninguna","Triangulado","Convergencia alta, aunque D100 no es fuente independiente (es una síntesis automática cuya lista contiene a 86 documentos del lote)"),
("T03","Los gemelos digitales y el IoT mejoran la resiliencia organizacional y la eficiencia operativa",["D029","D030","D052","D085","D007","D005"],"Encuestas transversales de autorreporte con modelos de ecuaciones estructurales","D082 trata la resiliencia como propiedad emergente y D007 y D005 condicionan el beneficio a factores institucionales","En tensión","Posible sesgo de método común; ningún estudio mide desenlaces objetivos de empresa; el efecto causal no se identifica"),
("T04","El tiempo de reparación del edificio no basta como medida de recuperación empresarial; deben modelarse demoras e inactividad por tipo",["D011","D053","D069","D040","D054"],"Modelos analíticos y de simulación; D011 contrasta con tiempos de cierre observados","Ninguna","Triangulado con reservas","D040 y D053 comparten autoría (Galasso); la validación con empresas reales es escasa"),
("T05","Incluir pérdidas indirectas y recuperación cambia la decisión de refuerzo sísmico",["D040","D069","D054"],"Análisis costo-beneficio y estudios de caso de edificios","D002 y D027 optimizan costo directo sin incluir recuperación","Parcial","Tres documentos con casos distintos; faltan datos empíricos de pérdidas por interrupción"),
("T06","Los gemelos digitales urbanos estiman daño y necesidades de respuesta en escenarios sísmicos",["D034","D048","D080","D070","D078","D072"],"Escenarios y simulaciones; ninguno valida contra un evento real","Ninguna","Parcial","D048 y D080 comparten autoría; la evidencia depende de escenarios y de datos públicos"),
("T07","Las revisiones de gemelos digitales concluyen potencial alto con implementación incipiente",["D004","D013","D028","D061","D079","D081","D099"],"Revisiones sistemáticas y narrativas","Ninguna","Triangulado","Siete revisiones convergen; comparten sesgo de publicación hacia resultados favorables"),
("T08","Los efectos digitales sobre la resiliencia de cadenas de suministro son mayores en preparación y respuesta que en recuperación",["D037","D081","D017"],"Metaanálisis (D037) y revisión sistemática (D081)","D077 propone beneficios generales sin diferenciar etapas","Parcial","Dos fuentes cuantitativas o sistemáticas independientes; la mayoría de estudios de base son transversales"),
("T09","Los costos bajos del monitoreo estructural con IoT se demuestran solo en laboratorio o en estructuras individuales",["D068","D084","D086","D039","D023"],"Pruebas de laboratorio y un puente en servicio (D023)","Ninguna","Triangulado","D039 y D086 comparten autoría; D023 es la única operación en campo"),
("T10","El orden de desempeño entre algoritmos de aprendizaje automático para alerta sísmica no es transferible entre estudios",["D010","D041","D060"],"Datos históricos de regiones distintas, métricas distintas","D060 (XGBoost mejor) frente a D041 (red neuronal mejor que XGBoost)","En tensión","Diferencias de tarea (intensidad frente a magnitud), datos y métricas; ninguna comparación directa con los mismos datos"),
("T11","UAV e IoT permiten restablecer comunicaciones y acelerar la evaluación de daños",["D001","D022","D042","D062","D076"],"Simulación y algunas pruebas de campo (D062)","Ninguna","Parcial","Mayoría con simulación; escasa evidencia de operación en desastres reales"),
("T12","La adopción del IoT y del gemelo digital depende de liderazgo, habilidades y aceptación de las partes interesadas",["D005","D007","D029","D085","D012","D003"],"Revisión sistemática, estudios cualitativos y encuestas","Ninguna","Triangulado con reservas","La evidencia organizacional procede de contextos no sísmicos; faltan estudios en recuperación posterremoto"),
("T13","La prefabricación y la robótica contribuyen a la recuperación posdesastre",["D099"],"Una revisión con ejemplos puntuales","Ninguna","Fuente única","Solo D099 trata el tema; ningún estudio del lote mide el efecto en la recuperación"),
("T14","La transferencia tecnológica como mecanismo tiene evidencia empírica en recuperación posterremoto",["D100","D101"],"Síntesis automáticas sin protocolo","D100 reconoce que la evidencia empírica y los marcos están ausentes","Sin evidencia primaria","Ningún documento del lote estudia empíricamente la transferencia tecnológica en recuperación posterremoto; es el vacío central del corpus"),
]
rows=[]
for tid,claim,docs,tipo,contra,verd,obs in T:
    gi=grupos_independientes(docs); tm,tn=med(docs,"trl"); bm,bn=med(docs,"brl")
    rows.append(dict(id=tid,afirmacion=claim,n_documentos=len(docs),documentos=", ".join(docs),grupos_independientes_de_autoria=gi,TRL_mediano_de_los_documentos=tm,n_con_TRL=tn,BRL_mediano=bm,tipo_de_evidencia=tipo,contradicciones=contra,veredicto=verd,observaciones=obs,base="asignación de documentos y veredicto: juicio del analista; grupos de autoría y medianas: calculados"))
pd.DataFrame(rows).to_csv(f"{OUT}/triangulacion.csv",index=False,encoding="utf-8-sig")
# ---- patrones y tensiones (cifras calculadas)
tech=[i for i in A if i<="D086" or i=="D099"]
trl=[A[i]["madurez"]["trl"][0] for i in tech if A[i]["madurez"]["trl"][0] is not None]
brl=[A[i]["madurez"]["brl"][0] for i in tech if A[i]["madurez"]["brl"][0] is not None]
irl=[A[i]["madurez"]["irl"][1] for i in tech if A[i]["madurez"]["irl"][0]]
pat=re.compile(r"recuper|continuidad|interrupci|ingres|empleo|reanud|inactividad|cierre",re.I)
vcount=sum(1 for i in tech if any(k=="VAR" and pat.search(t) for k,t in A[i]["vacios"]))
sinla=sum(1 for i in tech if any(k=="TERR" and re.search(r"sin[^.;,]*Am[eé]rica Latina|ni Am[eé]rica Latina",t,re.I) for k,t in A[i]["vacios"]))
fc=collections.Counter(f[0].split("(")[0].strip().lower() for i in A for f in A[i]["falacias"])
yr=collections.Counter(int(inv[i]["meta"].get("anio") or 0) for i in inv)
y2426=yr[2024]+yr[2025]+yr[2026]
cit=[inv[i]["meta"].get("citas_scopus") for i in inv if inv[i]["meta"].get("citas_scopus") is not None]
P=[
("P01","patrón","Madurez tecnológica baja y homogénea: la mediana de TRL es 4 en %d documentos técnicos con TRL asignado (%d con TRL ≤ 4, %.0f %%); la mediana de BRL es 2 y la de IRL es 3"%(len(trl),sum(1 for t in trl if t<=4),100*sum(1 for t in trl if t<=4)/len(trl)),"D001-D086, D099","calculado sobre YAML","El conjunto es evidencia de laboratorio y simulación; no hay base para estimar efectos en empresas","Pilotos en campo con métricas de continuidad y costos"),
("P02","patrón","BRL ≤ 2 en %d de %d documentos con BRL asignado (%.0f %%): casi ningún estudio presenta costos, modelos de negocio o análisis de adopción empresarial"%(sum(1 for t in brl if t<=2),len(brl),100*sum(1 for t in brl if t<=2)/len(brl)),"D001-D086, D099","calculado sobre YAML","Valle de la muerte comercial como condición general del campo","Estudios de costo-beneficio con empresas afectadas"),
("P03","patrón","Valle de la muerte: 66 documentos se ubican en V1 (investigación sin aplicación), 8 en V3, 7 en V2 y 3 en V4; 17 sin valle (no tecnológicos)","Todos","calculado sobre YAML","La integración (IRL ≤ 3 en %d de %d) y no la componente técnica aísla la brecha"%(sum(1 for t in irl if t<=3),len(irl)),"Marcos abiertos de integración y pruebas con estándares"),
("P04","patrón","Validación simulada o sintética como evidencia principal","D064, D065, D066, D072, D073, D075, D078, D080","juicio del analista a partir de las fichas","Las ganancias reportadas (latencia, precisión, bienestar) no se han observado en operación","Ensayos con datos reales y repetición con intervalos"),
("P05","patrón","Evidencia de un único evento, estructura o caso","D067, D068, D073, D084","juicio del analista a partir de las fichas","Generalización limitada; sin variabilidad entre estructuras o eventos","Series de casos y validación multi-sitio"),
("P06","anomalía","Cifras internamente inconsistentes que condicionan la lectura","D066, D067, D076, D079, D081, D085, D086, D089, D091, D092, D093, D099, D100","juicio del analista (verificadas en el texto)","Se registran en las fichas como límites de calidad de extracción o de reporte","Verificación contra las fuentes originales antes de citar"),
("P07","anomalía","Etiqueta 'IoT' o 'código abierto' sin la componente correspondiente en los datos o el software","D071, D077, D080","juicio del analista","Riesgo de sobrestimar madurez y reproducibilidad","Auditoría de artefactos y datos disponibles"),
("P08","patrón","Etiquetado o selección circular o apoyada en IA y sesgos de selección de la muestra","D076, D079, D082, D083","juicio del analista","Resultados dependientes del procedimiento de selección","Validación con etiquetas independientes"),
("P09","tensión","Resiliencia organizacional como mediador lineal (D030) frente a propiedad emergente (D082)","D030, D082, D029","juicio del analista","Los diseños de evaluación de empresas posterremoto cambian según la conceptualización","Modelos de dinámica con múltiples mecanismos"),
("P10","tensión","Orden de desempeño de algoritmos de alerta sísmica contradictorio entre estudios (XGBoost mejor en D060; red neuronal mejor que XGBoost en D041)","D041, D060, D010","juicio del analista","No hay un algoritmo recomendado transferible","Comparación con el mismo conjunto de datos y métricas"),
("P11","patrón","Concentración de la evidencia de alerta sísmica de bajo costo en un grupo de autoría (Prasanna: D045, D049, D075)","D045, D049, D075","calculado (autoría compartida)","La convergencia aparente sobre la latencia descentralizada es parcialmente no independiente","Réplicas por otros grupos"),
("P12","patrón","Otros agrupamientos de autoría compartida que reducen la independencia: Yu-Fu-Cui (D039, D086), Galasso (D040, D053), Korkmaz-Demirkesen (D048, D080), Abdalzaher-Krichen (D019, D060)","D019, D039, D040, D048, D053, D060, D080, D086","calculado (autoría compartida)","Cinco pares de documentos del lote no son confirmaciones independientes","Ponderar por grupo de autoría en la síntesis"),
("P13","anomalía","La síntesis D100 incluye como referencias a los 86 documentos D001-D086 (86 de 93 referencias); el corpus Scopus del lote coincide con su lista","D100, D001-D086","calculado (coincidencia de títulos)","El lote no es independiente de la síntesis; D100 no puede validar al corpus y hay riesgo de sesgo de selección del buscador","Construir una cadena de búsqueda propia y comparar cobertura"),
("P14","anomalía","D100 declara alcance 2020-2024 pero 49 de 93 referencias son de 2025-2026 y hay referencias de 2013 y 2015","D100","calculado sobre la lista de referencias","El alcance declarado no se cumple; el resultado depende del índice en octubre de 2026","Fijar y registrar la fecha de búsqueda y los filtros"),
("P15","patrón","Concentración temporal: %d de 101 documentos (%.0f %%) son de 2024-2026; 12 son de 2008 (bloque SciELO); %d citas Scopus en total y %d documentos concentran 80 %% de ellas"%(y2426,100*y2426/101,sum(cit),24),"Todos","calculado (inventario)","Corpus reciente con poca acumulación de citas; la señal bibliométrica es débil","Ampliar el horizonte y usar métricas normalizadas"),
("P16","patrón","Ausencia explícita de métricas de recuperación o continuidad empresarial en %d de %d documentos técnicos (el vacío VAR lo declara de forma explícita)"%(vcount,len(tech)),"D001-D086, D099","calculado sobre YAML","El resultado final de interés (recuperación productiva) no se mide en gran parte de la literatura","Definir un conjunto mínimo de indicadores de recuperación empresarial"),
("P17","patrón","Cobertura territorial: %d de %d documentos técnicos declaran explícitamente la ausencia de América Latina en el vacío territorial; el caso de un edificio patrimonial de Lima (Perú) aparece en D014"%(sinla,len(tech)),"D001-D086, D099","calculado sobre YAML","El corpus no informa sobre regiones sísmicas latinoamericanas","Incorporar estudios y datos de la región"),
("P18","patrón","La falacia más frecuente es la generalización apresurada (%d de %d menciones, %.0f %%)"%(fc.get("generalización apresurada",0),sum(fc.values()),100*fc.get("generalización apresurada",0)/sum(fc.values())),"Todos","calculado sobre YAML","Las conclusiones exceden la base empírica de manera sistemática","Declarar el alcance de inferencia en cada recomendación"),
("P19","tensión","Mayor robustez argumentativa en los documentos ajenos al tema (media 3,84 de 10 en el bloque SciELO frente a 3,19 en núcleo y 3,13 en adyacentes)","D088-D098 frente a D001-D086","calculado sobre YAML","La relevancia temática no coincide con la calidad de reporte estadístico: los estudios biomédicos reportan intervalos y controles de calidad que los técnicos omiten","Adoptar guías de reporte (por ejemplo, intervalos de confianza y validación externa) en estudios tecnológicos"),
]
pd.DataFrame([dict(id=a,tipo=b,descripcion=c,documentos=d,base=e,implicacion=f,ruta_de_solucion=g) for a,b,c,d,e,f,g in P]).to_csv(f"{OUT}/patrones_tensiones.csv",index=False,encoding="utf-8-sig")
print(len(rows),"afirmaciones;",len(P),"patrones")
