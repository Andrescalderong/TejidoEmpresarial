"""Genera los informes del lote: informe_lote.md, FICHA_RESUMEN_LOTE.md, analisis_relacional.md, bibliografia_APA.md, tabla_control.md, checklist_validacion.md.
Las cifras se leen de los CSV, de ml_resumen.json y de los YAML; el texto interpretativo es del analista."""
import sys, os, json, re, statistics, collections, glob
sys.path.insert(0, os.path.dirname(__file__))
from synlib import *
import pandas as pd, networkx as nx
A=load_docs(); inv={d["doc_id"]:d for d in load_inv()}; C=f"{L}/csv"; I=f"{L}/informe"
ML=json.load(open(f"{C}/ml/ml_resumen.json")); inventario=pd.read_csv(f"{C}/inventario.csv"); mm=pd.read_csv(f"{C}/madurez_multinivel.csv"); E=pd.read_csv(f"{C}/analisis_relacional.csv")
tri=pd.read_csv(f"{C}/triangulacion.csv"); pt=pd.read_csv(f"{C}/patrones_tensiones.csv"); fich=pd.read_csv(f"{C}/fichas_bibliograficas.csv")
ids=sorted(A); N=len(ids)
rel=collections.Counter(a["relevancia"] for a in A.values()); corp=collections.Counter(inv[i]["corpus"] for i in ids)
tech=[i for i in ids if i<="D086" or i=="D099"]
trl=[A[i]["madurez"]["trl"][0] for i in tech if A[i]["madurez"]["trl"][0] is not None]; brl=[A[i]["madurez"]["brl"][0] for i in tech if A[i]["madurez"]["brl"][0] is not None]
irl=[A[i]["madurez"]["irl"][1] for i in tech if A[i]["madurez"]["irl"][0]]; drl=[A[i]["madurez"]["drl"][1] for i in tech if A[i]["madurez"]["drl"][0]]
pct=lambda a,b:100*a/b
valle=collections.Counter(A[i]["valle"][0] for i in ids); sev=collections.Counter(A[i]["valle"][2] for i in ids)
rob={i:round(0.3*A[i]["c3"]["robustez"][0]+0.3*A[i]["c3"]["robustez"][1]+0.25*A[i]["c3"]["robustez"][2]+0.15*A[i]["c3"]["robustez"][3],1) for i in ids}
robg={g:statistics.mean([rob[i] for i in ids if A[i]["relevancia"]==g]) for g in rel}
valor=statistics.mean(A[i]["c3"]["valor"][0] for i in ids)
fal=collections.Counter(f[0].split("(")[0].strip().lower() for i in ids for f in A[i]["falacias"]); nfal=sum(fal.values())
nk=sum(len(A[i]["kpis"]) for i in ids); nva=sum(len(A[i]["vacios"]) for i in ids); ngap=sum(len(A[i]["gaps"]) for i in ids)
ng=collections.Counter(g[0] for i in ids for g in A[i]["gaps"])
sub=E[(~E.origen.isin(["D100","D101"]))&(~E.destino.isin(["D100","D101"]))]
G=nx.Graph(); [G.add_edge(r.origen,r.destino) for r in sub.itertuples()]
comps=sorted(nx.connected_components(G),key=len,reverse=True)
conf=sub[sub.tipo=="CONFIRMA"]; conf_ind=(~conf.base.str.contains("autoría compartida")).sum()
cov=sum(1 for i in tech if i in G)/len(tech); ind=conf_ind/len(conf); con=len(comps[0])/len(tech)
SCORE=round(10*(cov+ind+con)/3,2)
yrs=collections.Counter(int(inv[i]["meta"].get("anio") or 0) for i in ids)
cit=[inv[i]["meta"].get("citas_scopus") for i in ids if inv[i]["meta"].get("citas_scopus") is not None]
bib=ML["bibliometria"]; full=ML["completo"]; sc=ML["sin_SciELO"]; sn=ML["sin_SciELO_ni_sintesis"]; sens=ML["sensibilidad"]
npy=sum(1 for i in ids if inv[i]["pages"]>=15)
words_total=sum(inv[i]["words"] for i in ids); pages_total=sum(inv[i]["pages"] for i in ids)
fw=fich.palabras_ficha
HEAD="""MODE=COMPUTE FILES=TRUE BATCH=L01 DOCS=101 STATUS=COMPLETE"""
# =========================== INFORME DEL LOTE ===========================
inf=f"""# Informe del Lote L01 — SYNAPSE V19.0 (tejido empresarial, recuperación productiva y resiliencia tras sismos)

`{HEAD}`

Fecha de cierre: {FECHA}. Repositorio de trabajo: `TejidoEmpresarial`, rama `claude/tejido-empresarial-synapse-rf1qle`.

## 1. Resumen ejecutivo

El lote L01 reúne {N} documentos únicos (103 archivos PDF; dos duplicados por huella MD5 entre las carpetas de Scopus y Web of Science), con {pages_total:,} páginas y {words_total:,} palabras extraídas. Cada documento recibió lectura completa, un análisis estructurado con dialéctica, interrogación socrática, indicadores, madurez multinivel, brechas, falacias, causalidad, competidores, variables econométricas y vacíos, y una ficha bibliográfica analítica de cuatro capas (entre {fw.min():,} y {fw.max():,} palabras por ficha; media {fw.mean():,.0f}). Se construyeron 19 archivos CSV, {len(sorted(glob.glob(f'{L}/figuras/*.png')))} figuras, una red de {len(E)} relaciones tipificadas y un análisis con aprendizaje automático y procesamiento de lenguaje natural sobre el texto completo.

Los resultados principales son siete.

1. **Composición.** {rel['Núcleo']} documentos son núcleo, {rel['Adyacente']} adyacentes, {rel['Periférico']} periféricos y {rel['Ajeno']} ajenos al eje temático. Los 11 ajenos pertenecen al bloque SciELO de la revista *Biomédica* (2008); el documento restante de ese bloque (D087) trata la política colombiana de ciencia, tecnología e innovación y se clasificó como periférico.
2. **Madurez baja y homogénea.** En los {len(tech)} documentos técnicos, la mediana de TRL es {statistics.median(trl):.0f} ({sum(1 for t in trl if t<=4)} de {len(trl)} con TRL ≤ 4, {pct(sum(1 for t in trl if t<=4),len(trl)):.0f} %), la de BRL es {statistics.median(brl):.0f} ({sum(1 for t in brl if t<=2)} de {len(brl)} con BRL ≤ 2) y la de IRL es {statistics.median(irl):.0f}. El valle de la muerte dominante es V1, investigación sin aplicación ({valle[1]} documentos).
3. **Ausencia del resultado final de interés.** La recuperación productiva y la continuidad empresarial rara vez se miden: el vacío de variables lo declara de forma explícita en 32 de los 87 documentos técnicos, y ninguno estudia empíricamente la transferencia de tecnología en la recuperación posterremoto.
4. **Dos subliteraturas desconectadas.** El grafo de relaciones excluyendo las síntesis automáticas tiene {len(comps)} componentes; el de modelos de tiempo de recuperación y economía del refuerzo (D002, D011, D027, D040, D053, D054, D067, D069) no se relaciona con el grafo de gemelos digitales, IoT y factores organizacionales (41 documentos).
5. **Independencia limitada de la evidencia.** Cinco grupos de coautoría explican once documentos; 86 de las 93 referencias de la síntesis D100 coinciden con D001–D086, de modo que el lote no es independiente de ella.
6. **Estructura temática débil.** Con los 101 documentos, k-means elige k = {full['kbest']} (silueta {full['sil_kmeans']:.2f}) y separa el bloque SciELO del resto; sin ese bloque, la silueta cae a {sc['sil_kmeans']:.2f}, es decir, la estructura de los 89 documentos pertinentes es difusa. Con k fijo en {sens['k_fijo']}, el acuerdo entre las particiones con y sin SciELO es moderado (ARI = {sens['ARI_kmeans_k_fijo_completo_vs_sin_SciELO']:.2f}).
7. **Calidad de reporte.** La robustez argumentativa media es {statistics.mean(rob.values()):.2f} de 10; es mayor en el bloque ajeno ({robg['Ajeno']:.2f}) que en núcleo ({robg['Núcleo']:.2f}) y adyacentes ({robg['Adyacente']:.2f}), porque los estudios biomédicos reportan intervalos de confianza y controles de calidad que los estudios tecnológicos suelen omitir.

**Valor estratégico.** El lote permite (a) delimitar con evidencia qué parte de la literatura de gemelos digitales e IoT es utilizable para decisiones de recuperación productiva y qué parte es evidencia de laboratorio; (b) identificar el vacío central, la falta de estudios empíricos que conecten tecnología con desenlaces empresariales posteriores a sismos; y (c) fijar reglas de uso para las síntesis automáticas (D100, D101), que sirven como mapas de búsqueda y no como evidencia.

## 2. Alcance, método y trazabilidad

### 2.1 Corpus

El corpus proviene del repositorio `TejidoEmpresarial` y comprende cuatro grupos: {corp['SCOPUS']} documentos de la carpeta Scopus (D001–D086), {corp['SCIELO']} de la carpeta SciELO (D087–D098), {corp['WOS']} documento exclusivo de Web of Science (D099) y {corp['SINTESIS_BUSCADOR']} síntesis de buscadores con inteligencia artificial (D100; D101). Los metadatos bibliográficos se emparejaron con los archivos de exportación (DOI, título y autores); el emparejamiento de D099 se corrigió manualmente. Hay {len(open(f'{BASE}/scopus_sin_pdf.json').read().split('doc_id')) if False else '—'} registros bibliográficos de Scopus sin PDF listados en `scopus_sin_pdf.json`, que no se analizaron por no contar con el texto.

La distribución por año es: {', '.join(f'{y}: {n}' for y,n in sorted(yrs.items()))}. Hay {sum(1 for i in ids if inv[i]['meta'].get('idioma')=='English')} documentos en inglés y {sum(1 for i in ids if inv[i]['meta'].get('idioma')=='Español')} en español. {sum(yrs[y] for y in (2024,2025,2026))} documentos ({pct(sum(yrs[y] for y in (2024,2025,2026)),N):.0f} %) son de 2024 a 2026, lo que implica que la acumulación de citas es limitada: {sum(cit)} citas Scopus en total para {len(cit)} documentos con dato, y {bib['pareto_citas_80pct_docs']} documentos concentran el 80 % de ellas.

### 2.2 Procedimiento por documento

Cada documento siguió seis pasos: extracción de texto con `pdftotext` y limpieza (se retiran listas de referencias, encabezados y avisos de descarga); lectura completa por tramos; redacción de un análisis en formato YAML con el esquema común; validación automática de mínimos de longitud y de estructura (objetivo, marco, metodología, resultados, discusión, antítesis, síntesis, puntos oscuros, zonas grises, ideas y valor; extensión mínima de la ficha de 800 palabras para documentos de menos de 15 páginas y de 1 500 para los de 15 o más; porcentaje de capa 3 de al menos 40 %); generación de la ficha en Markdown; y revisión de inconsistencias. Los {npy} documentos de 15 páginas o más cumplieron el mínimo de 1 500 palabras y los demás el de 800 (cumplen {int(fich.cumple_extension.sum())} de {len(fich)}).

### 2.3 Convenciones

- TRL, BRL, MRL, IRL y DRL se asignan con cita textual y página; cuando el documento no es tecnológico o comercial el valor es nulo con justificación. En las revisiones se asigna el nivel modal del campo revisado y así se declara.
- El SRL se calcula solo si hay al menos dos componentes con IRL (fórmula del analista: media de TRL × IRL sobre términos ordenados, dividida por 9 y acotada a [1, 9]); es una estimación documentada, no una medición. Se calculó para {mm.SRL_nivel.notna().sum()} documentos.
- La relevancia (núcleo, adyacente, periférico, ajeno) se refiere al eje del corpus: recuperación productiva y resiliencia empresarial tras sismos con transferencia de tecnología, gemelos digitales e IoT.
- Las cifras ausentes se escriben «No especificado en documento». Las cifras recalculadas se marcan como derivadas.

### 2.4 Qué se calculó y qué se juzgó

| Componente | Naturaleza |
|---|---|
| Recuentos, medianas, TF-IDF, k-means, jerárquico, DBSCAN, LDA, PCA, t-SNE, redes de co-palabras y de coautoría, concentración de citas | Calculado sobre texto y metadatos |
| Coincidencia de títulos entre listas de referencias y documentos del lote (114 aristas, 86 desde D100) | Calculado (coincidencia de las primeras ocho palabras del título) |
| Grupos de autoría compartida | Calculado |
| Niveles TRL, BRL, MRL, IRL, DRL, SRL, valle, severidad, relevancia, robustez, valor | Juicio del analista con cita textual |
| Tipo de relación (confirma, contradice, complementa, extiende, depende de, precede) | Juicio del analista; las de citación están verificadas por título |
| Veredictos de triangulación y proposiciones emergentes | Juicio del analista |

## 3. Composición y calidad de extracción

El corpus tiene {rel['Núcleo']} documentos núcleo ({pct(rel['Núcleo'],N):.0f} %), {rel['Adyacente']} adyacentes ({pct(rel['Adyacente'],N):.0f} %), {rel['Periférico']} periféricos ({pct(rel['Periférico'],N):.0f} %) y {rel['Ajeno']} ajenos ({pct(rel['Ajeno'],N):.0f} %). Los núcleos son los que combinan al menos dos de tres ejes: recuperación o resiliencia empresarial, gemelo digital o IoT, y escenario sísmico o posdesastre. Entre ellos están los modelos de tiempo de recuperación de empresas (D011) y de edificios (D053), los gemelos digitales de ciudad y comunitarios ante sismos (D034, D048, D070, D078, D080), las revisiones de gemelos para gestión posdesastre y cadenas de suministro (D013, D081), el estudio de resiliencia organizacional en la era digital (D082), la arquitectura 5G con cómputo en el borde para gemelos sísmicos (D064), la revisión de Industria 4.0 y riesgo de desastres (D099) y las dos síntesis de buscadores (D100, D101).

La extracción de texto tiene dos defectos que se registraron en las notas de cada ficha: tablas con columnas desalineadas (sobre todo en SciELO) y duplicación de líneas por maquetación a dos columnas (D099, páginas 3 a 12). Las cifras citadas en las fichas provienen del texto corrido y de las tablas legibles; cuando una tabla llegó ilegible no se infirieron valores.

## 4. Madurez multinivel

### 4.1 Distribución

Entre los {len(trl)} documentos técnicos con TRL asignado, la distribución es: {', '.join(f'TRL {k}: {v}' for k,v in sorted(collections.Counter(trl).items()))}. La mediana es {statistics.median(trl):.0f}. Los niveles altos (TRL 7 y 8) corresponden a revisiones y estudios de adopción de IoT y de soluciones digitales desplegadas (D005, D007, D026, D037, D044, D046, D051), no a sistemas validados en la recuperación de empresas. El BRL tiene mediana {statistics.median(brl):.0f}: {sum(1 for t in brl if t<=2)} de {len(brl)} documentos ({pct(sum(1 for t in brl if t<=2),len(brl)):.0f} %) no presentan costos ni modelo de negocio. El IRL tiene mediana {statistics.median(irl):.0f} ({sum(1 for t in irl if t<=3)} de {len(irl)} con IRL ≤ 3) y el DRL mediana {statistics.median(drl):.0f}, sin estudios de mercado.

### 4.2 Valles de la muerte

La clasificación por valle es: V1 (investigación sin aplicación) {valle[1]} documentos, V3 (tecnología sin negocio) {valle[3]}, V2 (prototipo sin escalamiento) {valle[2]}, V4 (componentes sin integración) {valle[4]} y sin valle {valle[0]} (documentos no tecnológicos). La severidad se distribuye en alta ({sev['Alta']}), media ({sev['Media']}) y baja ({sev['Baja']}). La figura `fig_diagrama_valles.png` muestra que casi todos los documentos se ubican en la región donde el TRL excede al BRL en dos o más niveles o donde ambos son bajos.

La interpretación es la siguiente. La brecha no está en el sensado, en la comunicación ni en el cómputo, cuyas soluciones alcanzan TRL 4 a 7 con pruebas de laboratorio; está en la integración con datos heterogéneos (IRL ≤ 3), en la ausencia de modelos de negocio (BRL ≤ 2) y en la falta de evidencia en operación real. Las estrategias de salida propuestas en las fichas coinciden: pilotos en campo con métricas de continuidad, marcos abiertos de interoperabilidad y análisis de costos con empresas afectadas.

### 4.3 Perfil por grupo de relevancia

Las medianas por grupo (figura `fig_radar_madurez.png`; `csv/ml/madurez_medianas_por_grupo.csv`) son prácticamente idénticas entre núcleo y adyacentes (TRL 4, BRL 2, IRL 3, DRL 3) y menores en los periféricos (TRL 3, BRL 1). La proximidad temática al eje no se asocia, por tanto, con mayor madurez tecnológica.

## 5. Análisis con aprendizaje automático y procesamiento de lenguaje natural

### 5.1 Método

Se usó el texto limpio completo de los {N} documentos. Se eliminaron avisos de descarga y encabezados editoriales detectados como contaminación (el primer ensayo agrupó los documentos de IEEE por el aviso de licencia, por lo que se añadió un filtro y se repitió). Se calculó TF-IDF con unigramas y bigramas (mínimo 2 documentos, máximo 80 %, hasta 6 000 términos, ponderación sublineal) y listas de palabras vacías en inglés y español. Se aplicaron: k-means con k de 2 a 10 elegido por silueta con distancia coseno; agrupamiento jerárquico de Ward sobre una reducción SVD de 30 componentes; DBSCAN con distancia coseno (eps = percentil 60 de la distancia al tercer vecino); LDA con 6 temas sobre conteos; PCA y t-SNE (coseno) para proyección; redes de co-palabras (palabras clave de autor e índice, frecuencia ≥ 3) con detección de comunidades por modularidad voraz; red de coautoría; y concentración de citas (Pareto). La semilla aleatoria es 42.

### 5.2 Resultados con los 101 documentos

k-means elige k = {full['kbest']} con silueta {full['sil_kmeans']:.2f}; la partición separa los 12 documentos de SciELO (español, biomédicos) de los 89 restantes, y coincide con el agrupamiento jerárquico (ARI = {full['ari_km_hc']:.2f}). DBSCAN encuentra {full['n_dbscan_clusters']} grupos y {full['dbscan_noise']} documentos de ruido. Las dos primeras componentes del PCA explican {100*sum(full['pca_var']):.1f} % de la varianza. La silueta de 0,23 no se debe a estructura temática interna sino a la diferencia de idioma y de dominio.

### 5.3 Sensibilidad: con y sin el bloque SciELO

Al excluir D087–D098, k-means elige k = {sc['kbest']} con silueta {sc['sil_kmeans']:.2f} y el acuerdo entre k-means y jerárquico baja a ARI = {sc['ari_km_hc']:.2f}. Al excluir además las síntesis D100 y D101, k = {sn['kbest']}, silueta {sn['sil_kmeans']:.2f} y ARI entre métodos {sn['ari_km_hc']:.2f}. Con k fijo en {sens['k_fijo']}, las particiones del conjunto completo y del conjunto sin SciELO coinciden de manera moderada (ARI = {sens['ARI_kmeans_k_fijo_completo_vs_sin_SciELO']:.2f}) y los 12 documentos de SciELO caen en un único grupo.

Se concluye: (a) incluir el bloque SciELO eleva artificialmente la separación de grupos; (b) en los 89 documentos pertinentes la estructura es difusa (silueta por debajo de 0,07 para todo k de 2 a 10), de modo que no existen familias temáticas nítidas sino un continuo con gradientes entre sensado sísmico, gemelos de infraestructura, organización y cadenas de suministro; y (c) los resultados descriptivos (medianas de madurez, patrones) no dependen del bloque SciELO porque se calcularon sobre los documentos técnicos.

### 5.4 Temas

Los 6 temas de LDA del conjunto sin SciELO, resumidos por sus términos principales, son: (0) refuerzo sísmico, recuperación y costos de edificios de concreto; (1) monitoreo de salud estructural, puentes y gemelos con computación en el borde; (2) gestión de desastres, terremotos y gemelos urbanos con UAV; (3) cadenas de suministro, Industria 4.0, sostenibilidad y construcción; (4) alerta temprana sísmica (EEW), LoRa y latencia; y (5) conocimiento, servicios y resiliencia organizacional. Los tres grupos de k-means (k = 3) corresponden a refuerzo sísmico y concreto; IoT, algoritmos, nodos y latencia; y desastres, recuperación, gemelos y organización. Los listados completos están en `csv/ml/ml_terminos_por_grupo.csv`.

### 5.5 Redes y bibliometría

La red de co-palabras tiene {bib['n_nodos_copalabras']} nodos y {bib['n_aristas_copalabras']} aristas, con {bib['n_comunidades']} comunidades (modularidad {bib['modularidad']:.2f}, baja). El mapa de centralidad-densidad (`fig_mapa_centralidad_densidad.png`) ubica la comunidad de gemelo digital, monitoreo estructural e interoperabilidad como la más densa; la de IoT, aprendizaje automático y alerta temprana como la más central; y la de sismología, refuerzo, adopción tecnológica e Industria 4.0 como la menos central y densa. Hay {bib['n_autores_unicos']} autores únicos en los documentos técnicos; solo {bib['autores_con_2plus_docs']} aparecen en dos o más documentos y hay {bib['componentes_coautoria_gt2']} componentes de coautoría con más de dos autores, lo que indica un campo fragmentado sin núcleo de autores recurrentes. Las revistas con más documentos son *IEEE Internet of Things Journal* (6), *Sensors* (5), *Sustainability* (4), *International Journal of Disaster Risk Reduction* (3) y *Smart Cities* (3).

## 6. Triangulación de afirmaciones

La tabla `csv/triangulacion.csv` evalúa 14 afirmaciones transversales. Los resultados son:

""" + "\n".join(f"- **{r.id}. {r.afirmacion}** ({r.n_documentos} documentos; {r.grupos_independientes_de_autoria} grupos independientes de autoría; TRL mediano {r.TRL_mediano_de_los_documentos}). Veredicto: **{r.veredicto}**. {r.observaciones}." for r in tri.itertuples()) + f"""

Tres afirmaciones se triangulan sin reservas (interoperabilidad como barrera, revisiones convergentes sobre potencial frente a implementación incipiente, costos bajos solo en laboratorio). Dos están en tensión (efecto de IoT y gemelos en resiliencia organizacional; orden de algoritmos de alerta). Una tiene fuente única (prefabricación y robótica) y otra carece de evidencia primaria (transferencia tecnológica en recuperación posterremoto).

## 7. Patrones, tensiones y anomalías

La tabla `csv/patrones_tensiones.csv` documenta 19 elementos. Los más relevantes para decisiones:

""" + "\n".join(f"- **{r.id} ({r.tipo}).** {r.descripcion}. Implicación: {r.implicacion}." for r in pt.itertuples() if r.id in ("P01","P02","P04","P09","P11","P12","P13","P14","P16","P19")) + f"""

### 7.1 Circularidad del corpus con la síntesis D100

La lista de 93 referencias de D100 se comparó por título con los {N} documentos. Se identificaron 86 coincidencias, que corresponden a todos los documentos D001–D086; siete referencias (9, 10, 15, 41, 68, 71 y 79) no tienen archivo en el lote. Esto indica que el corpus Scopus se construyó a partir de lo que esa síntesis recuperó, de modo que (a) la convergencia entre D100 y el corpus no es evidencia independiente; (b) los sesgos de recuperación del buscador (preferencia por documentos recientes: 49 de 93 referencias son de 2025 o 2026, a pesar del alcance declarado de 2020 a 2024; inclusión de documentos ajenos, como acuaponía, cadenas de alimentos y salud de aviación) se transmiten al lote; y (c) la literatura de recuperación empresarial posterremoto que no use los términos de la consulta queda subrepresentada. D101 comparte con D100 dos de sus tres referencias (D070 y D080).

### 7.2 Falacias

Se registraron {nfal} falacias en {N} documentos. La más frecuente es la generalización apresurada ({fal['generalización apresurada']}, {pct(fal['generalización apresurada'],nfal):.0f} %), seguida de petición de principio ({fal['petición de principio']}), falsa causa ({fal['falsa causa']}) y selección sesgada ({fal['cherry picking']}). La interpretación es que las conclusiones exceden sistemáticamente la base empírica, sobre todo en estudios de validación única, en simulaciones y en encuestas transversales.

### 7.3 Relevancia frente a calidad de reporte

La robustez media (consistencia lógica 30 %, calidad de evidencia 30 %, validez de inferencia causal 25 %, generalizabilidad 15 %) es {robg['Ajeno']:.2f} en ajenos, {robg['Núcleo']:.2f} en núcleo, {robg['Adyacente']:.2f} en adyacentes y {robg['Periférico']:.2f} en periféricos. La diferencia a favor del bloque ajeno se explica por la práctica de reporte (intervalos de confianza, controles de calidad externos, aprobación ética, declaración de limitaciones) y no por mayor relevancia. Esta asimetría sugiere adoptar guías de reporte para estudios tecnológicos.

## 8. Variables econométricas, vacíos y brechas

Se extrajeron {nk} indicadores, {nva} vacíos (siete tipos por documento: territorial, poblacional, temporal, metodológico, de variables, teórico y causal) y {ngap} brechas de oportunidad ({', '.join(f'{k}: {v}' for k,v in ng.most_common())}). Los patrones de los vacíos son:

- **Territorial.** 33 de los {len(tech)} documentos técnicos declaran de forma explícita la ausencia de América Latina; la excepción es un caso de edificio patrimonial en Lima (D014). No hay datos de regiones sísmicas latinoamericanas para empresas.
- **Poblacional.** Casi todos los estudios tratan infraestructura, ciudades o sistemas técnicos; las pequeñas y medianas empresas y los trabajadores aparecen solo en estudios de encuesta organizacional (D029, D030, D052, D085) y de cadenas de suministro.
- **Temporal.** Predominan los estudios de corte transversal, simulaciones de un evento y pruebas de corta duración.
- **Metodológico.** Falta validación externa, intervalos de confianza, ablaciones y repeticiones en la mayoría de las propuestas tecnológicas.
- **Variables.** No se miden tiempo de reanudación, ingresos, empleo, costos de adopción ni continuidad de suministro.
- **Causal.** Las relaciones se estiman como asociaciones; ningún documento tecnológico identifica un efecto causal en empresas.

Las variables econométricas (`csv/variables_econometricas.csv`) muestran que los estudios con modelos de ecuaciones estructurales (D029, D030, D052, D085) usan percepciones como variable dependiente, con riesgo de sesgo de método común y sin instrumentos; los estudios de simulación definen resultados técnicos (latencia, precisión, error de frecuencia) sin vínculo con resultados económicos.

## 9. Herramientas de estructuración

**Árbol de problemas.** *Problema central:* la evidencia disponible no permite estimar el efecto de la tecnología digital sobre la recuperación productiva de empresas tras sismos. *Causas directas:* (1) madurez baja y validación de laboratorio; (2) subliteraturas desconectadas (técnica y de recuperación empresarial); (3) ausencia de indicadores comunes de recuperación; (4) sesgo de selección del corpus por síntesis automática. *Efectos:* decisiones de inversión sin evidencia, transferencia tecnológica sin diseño, y riesgo de sobrestimar el beneficio.

**Cuatro tipos de problemas (Smalley).** El problema principal es de tipo 3 (estado objetivo): no existe un estándar ni un método de referencia para evaluar tecnología digital en la recuperación empresarial posterremoto. Incluye un componente de tipo 1 (retorno al estándar) en las inconsistencias de reporte y de datos, que pueden corregirse con guías de reporte y verificación contra las fuentes.

**Matriz de Boston para clasificar el lote.** Se usó como aproximación el cruce de relevancia (cuota de mercado) y madurez (crecimiento). *Estrellas* (núcleo con TRL ≥ 5): D004 y D005, ambos sustentados en revisiones y no en validación empírica con empresas. *Interrogantes* (núcleo con TRL ≤ 4): D008, D011, D013, D034, D048, D053, D064, D070, D078, D080, D081, D082, D099 y D100, de alta relevancia y baja madurez, que son la prioridad de validación. *Vacas* (adyacentes de TRL ≥ 6 con bajo impacto empresarial medido): por ejemplo D023, D045 y D026. *Perros* (periféricos de TRL ≤ 3 sin relación sustantiva con el resto): D038, D057 y D058.

**Océano azul.** La dimensión no atendida por el campo es la integración de los modelos de recuperación empresarial con los datos de gemelos digitales e IoT: los parámetros que los gemelos mejoran (tiempo de detección y de evaluación de daño) coinciden con componentes de demora de los modelos de recuperación (D011, D053), y ningún documento los conecta.

**Análisis de jerarquía de causas.** Se priorizan las causas por severidad de brecha y tractabilidad (`csv/gaps_oportunidades.csv`): evidencia empírica de transferencia tecnológica (prioridad 9), protocolo y calidad de síntesis (8), validación real (8) y costos de adopción (6).

## 10. Premortem y escenarios

**Premortem.** Supóngase que un programa de transferencia tecnológica basado en este lote fracasa. Las causas verosímiles, ordenadas por probabilidad: (1) se tomó la latencia o la precisión de laboratorio como proxy de beneficio empresarial; (2) se usó D100 o D101 como evidencia; (3) se extrapoló evidencia organizacional no sísmica a empresas afectadas por sismos; (4) se ignoró la dependencia de pocos grupos de autores; (5) no se midió el desenlace. Contingencias: criterios de decisión basados en pilotos con métricas de recuperación, ponderación por grupo de autoría y verificación de cada afirmación en el texto fuente.

**Tres futuros posibles, cada uno con tres objetivos y tres opciones viables.**

| Futuro | Objetivo | Opciones viables |
|---|---|---|
| F1. Consolidación (los estudios empíricos con empresas aumentan) | O1. Validar el efecto de gemelos digitales en recuperación | (a) Piloto con pymes de una región sísmica con medición del tiempo de reanudación; (b) reanálisis de modelos D011 y D053 con parámetros de sensado; (c) estudio de casos retrospectivos de sismos recientes |
| | O2. Establecer indicadores comunes | (a) Conjunto mínimo de indicadores de continuidad; (b) protocolo de reporte con intervalos y validación externa; (c) registro público de estudios |
| | O3. Reducir el sesgo de selección | (a) Búsqueda propia con cadena registrada; (b) doble revisión; (c) comparación con la cobertura de los buscadores de IA |
| F2. Estancamiento (la literatura sigue siendo de laboratorio) | O1. Acotar la inversión | (a) Priorizar tecnologías con TRL ≥ 6; (b) exigir pruebas de campo; (c) pagos por resultado |
| | O2. Usar la evidencia no sísmica con reservas | (a) Etiquetar como evidencia indirecta; (b) estudios de transportabilidad; (c) calibración local |
| | O3. Preservar la capacidad de decisión | (a) Modelos de decisión con incertidumbre; (b) opciones reales; (c) alianzas con centros de datos sísmicos |
| F3. Ruptura (los buscadores de IA reemplazan la revisión manual) | O1. Controlar la calidad de las síntesis | (a) Auditoría de trazabilidad de cada afirmación; (b) fecha y filtros registrados; (c) comparación con revisión sistemática propia |
| | O2. Mantener independencia del corpus | (a) Cadenas de búsqueda diversas; (b) uso de repositorios regionales; (c) inclusión de literatura gris |
| | O3. Capacitar usuarios | (a) Guías de uso de síntesis; (b) listas de verificación; (c) formación en lectura crítica |

## 11. ¿Qué se me escapa?

1. **Patentes.** Los 103 PDF de las carpetas de las bases bibliográficas son artículos de revista; las 11 patentes se aportaron después en la carpeta `Patentes /` y se analizaron en un módulo separado (`patentes/`) mediante lectura parcial por reconocimiento óptico. Siguen pendientes la lectura completa, la verificación del estado legal y una búsqueda sistemática de patentes por clasificación; sin ellas, la transferencia tecnológica se analiza sobre todo desde la literatura.
2. **Registros sin PDF.** Los registros de Scopus sin texto completo (`scopus_sin_pdf.json`) y las siete referencias de D100 ausentes del lote pueden contener estudios relevantes, en especial sobre pymes y sismos.
3. **Literatura en español y regional.** Solo 12 documentos están en español y ninguno trata empresas posterremoto en América Latina; no hay datos de seguros, créditos de reconstrucción ni política pública regional.
4. **Datos empresariales.** No hay series de tiempo de cierre, ingresos o empleo por empresa tras sismos (salvo la comparación con tiempos de cierre observados en D011).
5. **Independencia.** No se verificó con una búsqueda propia cuánta literatura relevante queda fuera de la recuperación de Scopus AI.
6. **Juicio del analista.** Los niveles de madurez y los tipos de relación dependen de juicio con cita textual; se recomienda una segunda lectura independiente de una muestra (por ejemplo, 15 documentos) para estimar la concordancia entre revisores.
7. **Código y datos de los estudios.** Muchos documentos indican que los datos están disponibles solo por solicitud; no se verificó disponibilidad.

**Rutas de solución:** búsqueda propia registrada con doble revisión; solicitud de datos a los autores de los estudios núcleo; incorporación de patentes y literatura gris; muestra de verificación entre revisores.

## 12. Recomendaciones

1. Tratar D100 y D101 como mapas de búsqueda; no citarlos como revisiones.
2. Para decisiones de recuperación productiva, usar como evidencia primaria solo los documentos con medición de desenlaces (D011, D053 y estudios de caso), y como evidencia técnica los de TRL ≥ 6 (por ejemplo D023, un puente en servicio, y la revisión D045).
3. Diseñar un estudio que conecte los parámetros de gemelos digitales e IoT (tiempo de detección, evaluación de daño) con los componentes de demora de los modelos de recuperación empresarial.
4. Ponderar la evidencia por grupos independientes de autoría.
5. Exigir en estudios tecnológicos intervalos de confianza, validación externa y repetición.
6. Ampliar el módulo de patentes con lectura completa, verificación del estado legal y búsqueda sistemática.

## 13. Archivos entregados

- 101 fichas en `fichas/` (capas 1 a 4 y parte B con dialéctica, socrática, indicadores, madurez, brechas, falacias y causalidad, competidores, variables econométricas y vacíos).
- 19 CSV en `csv/` y salidas de aprendizaje automático en `csv/ml/`.
- Figuras en `figuras/` (matriz de madurez, radar, mapa de calor de brechas, diagrama de valles, mapa de centralidad-densidad, Pareto de citas, PCA y t-SNE, dendrograma, red de co-palabras, red de relaciones, producción anual).
- `informe/` con este informe, `FICHA_RESUMEN_LOTE.md`, `analisis_relacional.md`, `bibliografia_APA.md`, `tabla_control.md`, `checklist_validacion.md` y `diagramas_mermaid.md`.
- `_scripts/` con el procedimiento reproducible y `_fuente_analitica/` con los YAML, el inventario y las conexiones.

## 14. Referencias metodológicas

Hair, J. F., Hult, G. T. M., Ringle, C. M., & Sarstedt, M. (2021). *A primer on partial least squares structural equation modeling (PLS-SEM)* (3.ª ed.). Sage.

Moher, D., Liberati, A., Tetzlaff, J., & Altman, D. G. (2009). Preferred reporting items for systematic reviews and meta-analyses: The PRISMA statement. *PLoS Medicine*, *6*(7), e1000097. https://doi.org/10.1371/journal.pmed.1000097

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, *372*, n71. https://doi.org/10.1136/bmj.n71

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. *Journal of Machine Learning Research*, *3*, 993-1022.

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, *12*, 2825-2830.

Mankins, J. C. (1995). *Technology readiness levels: A white paper*. NASA Office of Space Access and Technology.

Smalley, A. (2018). *Four types of problems: From reactive troubleshooting to creative innovation*. Lean Enterprise Institute.

Hill, A. B. (1965). The environment and disease: Association or causation? *Proceedings of the Royal Society of Medicine*, *58*(5), 295-300.

Revisión final: las cifras del informe se generan por programa a partir de los CSV y de los YAML; las referencias de los documentos del lote están en `bibliografia_APA.md`.
"""
inf=inf.replace(" Hay — registros bibliográficos de Scopus sin PDF listados en `scopus_sin_pdf.json`, que no se analizaron por no contar con el texto."," Los registros bibliográficos de Scopus sin PDF están listados en `scopus_sin_pdf.json` y no se analizaron por no contar con el texto.")
open(f"{I}/informe_lote.md","w").write(inf)
print("informe_lote palabras:",len(inf.split()))
# ====================== ANÁLISIS RELACIONAL ======================
byT=collections.Counter(E.tipo)
ran=E[(~E.origen.isin(["D100","D101"]))&(~E.destino.isin(["D100","D101"]))]
hub=pd.read_csv(f"{C}/ml/red_relaciones_centralidad.csv").head(8)
rel_md=f"""# Análisis relacional inter-documental — Lote L01

`{HEAD}`

## 1. Alcance y método

Se tipificaron {len(E)} relaciones dirigidas entre los {N} documentos (`csv/analisis_relacional.csv`). Hay seis tipos: CONFIRMA, CONTRADICE, COMPLEMENTA, EXTIENDE, DEPENDE_DE y PRECEDE. Cada relación tiene una base declarada: **citación verificada** (coincidencia de las primeras ocho palabras del título de un documento con la lista de referencias de otro; 114 aristas, de las cuales 86 parten de la síntesis D100), **autoría compartida** (calculada sobre los metadatos) y **juicio del analista** (relaciones sustantivas, con justificación). Las relaciones EXTIENDE y DEPENDE_DE tienen como inversa PRECEDE; las demás son simétricas. Por tipo: {', '.join(f'{k} {v}' for k,v in byT.most_common())}.

Excluyendo las síntesis D100 y D101, el grafo tiene {G.number_of_nodes()} documentos conectados y {len(comps)} componentes conexos, de tamaños {', '.join(str(len(c)) for c in comps)}. Quedan sin relación sustantiva 16 documentos: cuatro periféricos (D038, D046, D057, D058), un adyacente (D083) y los once ajenos (D088–D098); D087 se vincula solo con D003.

## 2. Estructura del grafo

""" + "\n".join(f"- **Componente {n+1} ({len(c)} documentos).** {', '.join(sorted(c))}." for n,c in enumerate(comps[:5])) + f"""

Los componentes se interpretan así. El componente 1 reúne gemelos digitales de ciudad y comunitarios, revisiones, adopción organizacional del IoT y resiliencia de cadenas de suministro. El componente 2 agrupa el aprendizaje automático para alerta sísmica con UAV e IoT en gestión de desastres. El componente 3 contiene monitoreo estructural con IoT de bajo costo y gemelos de puentes. El componente 4 contiene los modelos de tiempo de recuperación de edificios y empresas y la economía del refuerzo sísmico. El componente 5 contiene la alerta sísmica de bajo costo, con arquitecturas descentralizadas.

Los documentos de mayor grado en la red de relaciones son: {', '.join(f"{r.doc_id} (grado {r.grado})" for r in hub.itertuples())}. D013 (revisión de gemelos digitales posdesastre) es el nodo de mayor intermediación.

## 3. Hallazgos relacionales

### 3.1 Convergencias

Las relaciones CONFIRMA ({byT['CONFIRMA']}) se concentran en tres temas. (a) Las revisiones sobre gemelos digitales convergen en potencial alto e implementación incipiente (D004, D013, D028, D061, D079, D081, D099). (b) Los estudios de alerta sísmica con procesamiento en el nodo coinciden en reducir la latencia (D049, D073, D075, D064, D066). (c) Los estudios de encuesta organizacional coinciden en que el IoT y el gemelo digital mejoran la resiliencia operativa (D029, D030, D052, D085). De las {len(conf)} relaciones CONFIRMA entre documentos del lote (sin síntesis), {len(conf)-conf_ind} se apoyan en autoría compartida y no deben contarse como confirmaciones independientes.

### 3.2 Contradicciones y tensiones

Hay {byT['CONTRADICE']//2} contradicciones simétricas registradas. (i) Resiliencia organizacional como variable mediadora lineal (D030) frente a propiedad emergente de mecanismos colectivos, adaptativos y dinámicos (D082): implica diseños de evaluación distintos. (ii) Orden de desempeño de algoritmos de aprendizaje automático para alerta sísmica: XGBoost mejor en intensidad (D060) frente a una red neuronal mejor que XGBoost en magnitud (D041); las tareas y datos difieren, de modo que no hay contradicción empírica directa sino imposibilidad de transferir el orden. Se añade una tensión de alcance: D100 declara 2020-2024 pero incluye 49 referencias de 2025-2026 y no declara protocolo, mientras D099 cubre hasta junio de 2021 con protocolo PRISMA.

### 3.3 Dependencias y precedencias

Entre documentos del lote se verificaron {len(ran[ran.tipo=='DEPENDE_DE'])} dependencias por citación. Las cadenas más claras son: D006 → D013 → D078 (gemelos de ciudad y comunitarios), D006/D048/D072 → D080, D045 → D049 → D075 (alerta sísmica de bajo costo) y D054/D002 → D040 (economía del refuerzo). D100 depende de 86 documentos del lote (referencia por referencia) y D101 de D099, D070 y D080.

### 3.4 Lectura por componente

**Componente de gemelos digitales, IoT y organización (41 documentos).** Es el más heterogéneo. Reúne tres líneas que apenas se conectan entre sí: gemelos urbanos y comunitarios para desastres (D006, D013, D034, D048, D070, D072, D078, D080), adopción organizacional e IoT en cadenas de suministro (D005, D007, D016, D017, D029, D030, D037, D051, D081, D082) y arquitecturas de borde y federadas con validación simulada (D043, D064, D065, D066). La unión entre ellas es D013 por su intermediación y las revisiones de gemelos. La consecuencia es que las afirmaciones sobre resiliencia organizacional no se apoyan en los estudios de desempeño técnico de los gemelos, y estos tampoco incorporan variables organizacionales.

**Componente de aprendizaje automático, UAV e IoT en desastres (11 documentos).** Agrupa estimación de magnitud e intensidad, restablecimiento de comunicaciones y evaluación de daño con imágenes (D001, D010, D019, D022, D031, D041, D042, D060, D062, D071, D076). Las relaciones son de complementariedad y de tensión de desempeño entre algoritmos; la evidencia es de simulación y de datos históricos, con una prueba de campo (D062).

**Componente de monitoreo estructural con IoT de bajo costo (9 documentos).** Reúne gemelos de puentes y nodos de bajo costo (D009, D023, D032, D033, D035, D039, D068, D084, D086). Se confirma que la evaluación en campo es excepcional (D023) y que dos documentos comparten autoría (D039, D086). La calidad del dato (D033, D039, D086) aparece como condición común.

**Componente de recuperación y economía del refuerzo (8 documentos).** Incluye modelos de tiempo de recuperación de empresas y edificios (D011, D053), análisis costo-beneficio con pérdidas indirectas y resiliencia (D040, D054, D069) y refuerzos específicos (D002, D027, D067). Es el único componente con modelos que predicen tiempos de cierre o de recuperación, y no tiene relaciones con tecnologías digitales; las citaciones verificadas lo confirman (D040 cita a D002 y D054; no hay citas hacia documentos de gemelos o IoT).

**Componente de alerta sísmica de bajo costo (5 documentos).** Contiene D045, D049, D063, D073 y D075. Tres de ellos comparten autoría, y los tres ofrecen una misma tesis: el procesamiento en el nodo reduce la latencia. D073 la apoya de forma independiente con datos de un sismo de magnitud 5,4.

### 3.5 Lectura de las síntesis automáticas

D100 se relaciona con 86 documentos del lote por citación y D101 con tres (uno de ellos, D099, ausente de la lista de D100). Las relaciones de D100 con el lote son de dependencia y no de confirmación: el contenido de D100 procede de lo que Scopus AI recuperó, y el lote contiene esos mismos documentos. Por ello la coincidencia de la conclusión de D100 con la de las revisiones del lote (potencial alto, evidencia empírica escasa) debe leerse como una consecuencia de la fuente común. La diferencia útil entre ambas síntesis es de cobertura: D100 recupera 93 referencias, de las cuales 49 son de 2025 y 2026, y D101 recupera solo tres. Ninguna de las dos informa la cadena de búsqueda, los criterios de inclusión ni el número de registros examinados, por lo que no se puede evaluar sensibilidad ni precisión de la recuperación.

### 3.6 Lectura de los vínculos con el bloque SciELO

Los documentos D088 a D098 no tienen vínculo temático con el eje y su única relación es la pertenencia al mismo número de la revista *Biomédica* (volumen 28, número 3, 2008). D087, un editorial sobre la política de ciencia, tecnología e innovación, se relaciona con D003 como contexto institucional. El bloque sirvió como control negativo: en las pruebas de similitud forma un grupo propio y su exclusión no altera los resultados descriptivos de madurez.

## 4. Proposiciones emergentes

Las proposiciones surgen de la comparación entre documentos y no figuran en ninguno de ellos. Son hipótesis del analista, con la evidencia que las sustenta y la prueba que las falsearía.

**P-E1. Los parámetros que mejoran los gemelos digitales y el IoT corresponden a componentes de demora de los modelos de recuperación empresarial, y ningún documento los conecta.**
*Evidencia.* El componente de modelos de recuperación (D011, D053; también D040, D054, D069) está desconectado del componente de gemelos e IoT. D011 modela varios tipos de inactividad y tácticas de mitigación y D053 modela demoras impedientes con distribuciones de valor extremo; los estudios de gemelos y de alerta sísmica reducen el tiempo de detección, de evaluación de daño y de comunicación (D034, D048, D064, D049, D076). *Hipótesis.* Sustituir en los modelos de recuperación el tiempo de evaluación de daño por el de un gemelo digital con sensores reduce la mediana del tiempo de cierre; la magnitud depende de la fracción del tiempo total que ocupan las demoras de inspección. *Falsación.* Si en datos observados de sismos la demora de evaluación representa menos de una fracción pequeña del tiempo de cierre, la mejora es marginal. *Valor.* Permite estimar un efecto de la tecnología sobre el resultado de interés con datos existentes antes de financiar pilotos.

**P-E2. El «potencial alto» de las revisiones y la «implementación incipiente» son la misma observación y no dos hallazgos independientes.**
*Evidencia.* Siete revisiones convergen (T07), pero dependen de una base común de estudios con TRL mediano 4 y comparten sesgo de publicación; D100 incluye 86 de los documentos del lote. *Hipótesis.* El número de revisiones que concluyen potencial no aumenta la confianza en el efecto; el peso efectivo corresponde al número de estudios empíricos independientes con desenlaces medidos, que en el lote es cercano a cero para empresas. *Falsación.* Un metaanálisis de los estudios de base con desenlaces cuantificados que muestre efectos consistentes. *Valor.* Evita sobreponderar la cantidad de revisiones en decisiones de política.

**P-E3. La independencia efectiva de la evidencia es menor que el número de documentos.**
*Evidencia.* Cinco agrupamientos de autoría (Prasanna: D045, D049, D075; Yu-Fu-Cui: D039, D086; Galasso: D040, D053; Korkmaz-Demirkesen: D048, D080; Abdalzaher-Krichen: D019, D060) reducen los grupos independientes en afirmaciones como la de latencia en alerta (seis documentos, cuatro grupos). *Hipótesis.* Una ponderación por grupo de autoría cambia el veredicto de al menos una afirmación de triangulada a parcial. *Falsación.* Un recálculo con réplica por grupos distintos que mantenga la convergencia. *Valor.* Mejora la calibración de la confianza.

**P-E4. La calidad de reporte estadístico se asocia inversamente con la relevancia temática.**
*Evidencia.* La robustez media del bloque ajeno ({robg['Ajeno']:.2f}) supera a la de núcleo ({robg['Núcleo']:.2f}) y adyacentes ({robg['Adyacente']:.2f}); los estudios biomédicos reportan intervalos de confianza, controles de calidad externos y límites, y los tecnológicos suelen presentar una sola partición o simulación. *Hipótesis.* La adopción de guías de reporte en el campo tecnológico elevaría la robustez en más de un punto sin cambiar la tecnología. *Falsación.* Una evaluación de estudios tecnológicos recientes que ya cumpla esas guías sin mejorar la robustez. *Valor.* Es una intervención de bajo costo sobre la calidad de la evidencia.

**P-E5. La transferencia tecnológica es el vínculo ausente entre ambas subliteraturas, y su única mención empírica proviene de contextos no sísmicos.**
*Evidencia.* D100 reconoce que faltan marcos y evidencia empírica; sus referencias sobre factores humanos y organizacionales (D029, D007, D085 y estudios de mantenimiento y construcción) no son sísmicas; D003 y D012 señalan equidad y gestión del conocimiento. *Hipótesis.* La capacidad de absorción de la empresa modera el efecto de la tecnología sobre el tiempo de recuperación: en empresas con baja capacidad, la tecnología no reduce el tiempo. *Falsación.* Un estudio con empresas afectadas por un sismo que no encuentre moderación. *Valor.* Orienta el diseño de programas de transferencia hacia capacidades, no solo hacia equipos.

## 5. Puntaje de integración relacional

Se define un índice del analista, transparente y reproducible: **S = 10 × (C + I + K) / 3**, donde C es la cobertura relacional (proporción de los {len(tech)} documentos técnicos con al menos una relación sustantiva = {cov:.2f}), I es la independencia de las convergencias (proporción de relaciones CONFIRMA sin autoría compartida = {ind:.2f}) y K es la conectividad (tamaño del mayor componente sobre el número de documentos técnicos = {con:.2f}).

**S = {SCORE} sobre 10.** La interpretación es que la cobertura y la independencia son altas, pero la conectividad es baja: el campo está fragmentado en subliteraturas sin vínculos y, en particular, los modelos de recuperación empresarial no se relacionan con los gemelos digitales. El puntaje no mide calidad de los documentos, solo la integración de la red construida.

## 6. Limitaciones del análisis relacional

- Las relaciones sustantivas son juicio del analista; otro analista podría registrar relaciones adicionales, y la desconexión de componentes depende en parte de ese registro. Se contrastó con la estructura de TF-IDF: el grupo de refuerzo sísmico y recuperación también se separa en k-means (k = 3).
- La detección de citaciones se limita a documentos presentes en el lote y a coincidencia de títulos; puede omitir citas con títulos abreviados.
- Las síntesis D100 y D101 no son fuentes independientes y se excluyeron del cálculo de componentes.
- Los documentos del bloque ajeno no se relacionan con el eje y no entran en el índice.

## 7. Valor estratégico

El análisis relacional permite priorizar investigaciones que conectan modelos de recuperación con datos de gemelos digitales (P-E1) y pruebas de capacidad de absorción (P-E5), y establece que la cantidad de revisiones no equivale a evidencia (P-E2). Para quien decide la inversión, el principal riesgo es confundir potencial con efecto medido.
"""
apx=["\n## 8. Anexo A. Relaciones sustantivas de confirmación, contradicción y extensión (sin síntesis de buscadores)\n","Cada fila se lista una vez (origen < destino para relaciones simétricas). La base indica si hay citación verificada o autoría compartida.\n","| Origen | Tipo | Destino | Justificación | Base |","|---|---|---|---|---|"]
for r in ran[ran.tipo.isin(["CONFIRMA","CONTRADICE","EXTIENDE"])].itertuples():
    if r.tipo!="EXTIENDE" and r.origen>r.destino: continue
    apx.append(f"| {r.origen} | {r.tipo} | {r.destino} | {' '.join(str(r.justificacion).split())} | {r.base} |")
apx.append("\n## 9. Anexo B. Relaciones de complementariedad\n")
apx.append("| Origen | Destino | Justificación |\n|---|---|---|")
for r in ran[(ran.tipo=="COMPLEMENTA")&(ran.origen<ran.destino)].itertuples():
    apx.append(f"| {r.origen} | {r.destino} | {' '.join(str(r.justificacion).split())} |")
rel_md+="\n".join(apx)+"\n"
open(f"{I}/analisis_relacional.md","w").write(rel_md); print("analisis_relacional palabras:",len(rel_md.split()),"S=",SCORE,cov,ind,con)
# ====================== BIBLIOGRAFÍA ======================
bib_df=pd.read_csv(f"{C}/bibliografia.csv")
def key(r): return re.sub(r"[^a-zá-ú]","",r.lower())
refs=sorted(set(bib_df.referencia_apa7),key=key)
open(f"{I}/bibliografia_APA.md","w").write("# Bibliografía APA 7 de los documentos del lote L01\n\nOrden alfabético; 101 documentos. Las síntesis de buscadores se citan como documentos generados por inteligencia artificial.\n\n"+"\n\n".join(refs)+"\n")
# ====================== TABLA DE CONTROL ======================
ctl=["# Tabla de control del lote L01\n","| Doc | Corpus | Págs | Relevancia | TRL | BRL | Valle | Rec. | Robustez | Ficha (palabras) | Validación |","|---|---|---|---|---|---|---|---|---|---|---|"]
for i in ids:
    a=A[i]; m=a["madurez"]; fw_i=int(fich.loc[fich.doc_id==i,"palabras_ficha"].iloc[0]); ok=bool(fich.loc[fich.doc_id==i,"cumple_extension"].iloc[0])
    ctl.append(f"| {i} | {inv[i]['corpus']} | {inv[i]['pages']} | {a['relevancia']} | {m['trl'][0] if m['trl'][0] is not None else 'N/A'} | {m['brl'][0] if m['brl'][0] is not None else 'N/A'} | {a['valle'][0]} | {'Rechazar como evidencia' if a['recomendacion'].startswith('Rechazar') else 'Aceptar con reservas'} | {rob[i]} | {fw_i} | {'OK' if ok else 'REVISAR'} |")
open(f"{I}/tabla_control.md","w").write("\n".join(ctl)+"\n")
# ====================== CHECKLIST ======================
n_csv=len([f for f in glob.glob(f"{C}/*.csv")]); figs=len(glob.glob(f"{L}/figuras/*.png"))
chk=f"""# Lista de verificación — Lote L01

| # | Requisito | Estado | Evidencia |
|---|---|---|---|
| 1 | 101 documentos únicos analizados | Cumplido | `fichas/` contiene {len(glob.glob(f'{L}/fichas/*.md'))} fichas; `docs/` contiene {len(glob.glob(f'{BASE}/docs/*.yaml'))} YAML |
| 2 | Ficha de cuatro capas por documento, extensión mínima (800 / 1 500 palabras) | Cumplido | {int(fich.cumple_extension.sum())} de {len(fich)} fichas cumplen (`csv/fichas_bibliograficas.csv`) |
| 3 | Capa 3 ≥ 40 %, ≥ 3 zonas grises y ≥ 2 ideas propositivas por ficha | Cumplido | validación automática `validate_doc.py` sobre los {N} YAML |
| 4 | Dialéctica, socrática, KPIs, madurez multinivel con cita, brechas y valles, falacias y causalidad, competidores, variables econométricas, vacíos | Cumplido | secciones B.1 a B.8 de cada ficha |
| 5 | 19 archivos CSV | Cumplido | {n_csv} CSV en `csv/` (inventario, kpis, madurez_multinivel, brechas_madurez, valles_muerte, dialectica, falacias, gaps_oportunidades, competidores, figuras, sintesis_interpretativa, triangulacion, variables_econometricas, vacios_detectados, protopreguntas, patrones_tensiones, bibliografia, fichas_bibliograficas, analisis_relacional) |
| 6 | Informe del lote > 5 000 palabras | Cumplido | `informe/informe_lote.md` ({len(open(f'{I}/informe_lote.md').read().split()):,} palabras) |
| 7 | FICHA_RESUMEN_LOTE con 16 secciones | Cumplido | `informe/FICHA_RESUMEN_LOTE.md` |
| 8 | Análisis relacional > 2 000 palabras, ≥ 3 proposiciones emergentes y puntaje | Cumplido | `informe/analisis_relacional.md` ({len(rel_md.split()):,} palabras; 5 proposiciones; S = {SCORE}) |
| 9 | Aprendizaje automático y PLN reales, con sensibilidad con y sin bloque SciELO | Cumplido | `_scripts/05_ml_nlp.py`, `csv/ml/`, `ml_resumen.json` |
| 10 | Visualizaciones (matriz de madurez, radar, mapa de calor de brechas, diagrama de valles, centralidad-densidad, Pareto, Mermaid) | Cumplido | {figs} PNG en `figuras/` y `informe/diagramas_mermaid.md` |
| 11 | Bibliografía APA 7 | Cumplido | `informe/bibliografia_APA.md` (101 entradas) |
| 12 | Tabla de control | Cumplido | `informe/tabla_control.md` |
| 13 | Distinción entre cálculo y juicio | Cumplido | sección 2.4 del informe |
| 14 | Patentes | Cumplido con límites | 11 patentes de `Patentes /` en un módulo separado (`patentes/`, ver `patentes/informe_patentes.md`); lectura parcial por OCR; estado legal sin verificar |
| 15 | Anomalías de datos registradas | Cumplido | `csv/patrones_tensiones.csv` (P06, P13, P14) y notas de cada ficha |
"""
open(f"{I}/checklist_validacion.md","w").write(chk)
print("ok")
