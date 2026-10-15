"""FICHA_RESUMEN_LOTE.md (16 secciones) y README del lote; cifras desde CSV/YAML."""
import sys, os, json, collections, statistics, glob
sys.path.insert(0, os.path.dirname(__file__))
from synlib import *
import pandas as pd
A=load_docs(); inv={d["doc_id"]:d for d in load_inv()}; C=f"{L}/csv"; I=f"{L}/informe"; ids=sorted(A)
ML=json.load(open(f"{C}/ml/ml_resumen.json")); tri=pd.read_csv(f"{C}/triangulacion.csv"); pt=pd.read_csv(f"{C}/patrones_tensiones.csv"); gp=pd.read_csv(f"{C}/gaps_oportunidades.csv")
E=pd.read_csv(f"{C}/analisis_relacional.csv"); kp=pd.read_csv(f"{C}/kpis.csv"); fich=pd.read_csv(f"{C}/fichas_bibliograficas.csv")
rel=collections.Counter(a["relevancia"] for a in A.values()); corp=collections.Counter(inv[i]["corpus"] for i in ids)
tech=[i for i in ids if i<="D086" or i=="D099"]
trl=[A[i]["madurez"]["trl"][0] for i in tech if A[i]["madurez"]["trl"][0] is not None]; brl=[A[i]["madurez"]["brl"][0] for i in tech if A[i]["madurez"]["brl"][0] is not None]
irl=[A[i]["madurez"]["irl"][1] for i in tech if A[i]["madurez"]["irl"][0]]; drl=[A[i]["madurez"]["drl"][1] for i in tech if A[i]["madurez"]["drl"][0]]
valle=collections.Counter(A[i]["valle"][0] for i in ids)
rob={i:0.3*A[i]["c3"]["robustez"][0]+0.3*A[i]["c3"]["robustez"][1]+0.25*A[i]["c3"]["robustez"][2]+0.15*A[i]["c3"]["robustez"][3] for i in ids}
top=sorted([i for i in ids if A[i]["relevancia"]=="Núcleo"],key=lambda i:-A[i]["c3"]["valor"][0])
g8=gp.sort_values("prioridad_1_10",ascending=False).head(8)
sc=ML["sin_SciELO"]; fu=ML["completo"]; se=ML["sensibilidad"]
HEAD="MODE=COMPUTE FILES=TRUE BATCH=L01 DOCS=101 STATUS=COMPLETE"
t=lambda i:inv[i]["meta"].get("titulo","")[:80]
md=f"""# FICHA_RESUMEN_LOTE — L01

`{HEAD}`

## 1. Identificación del lote
Lote L01 de SYNAPSE V19.0; repositorio `TejidoEmpresarial`; rama `claude/tejido-empresarial-synapse-rf1qle`; fecha de cierre {FECHA}. Tema: tecnología, transferencia, gemelos digitales e IoT para la recuperación productiva y la resiliencia empresarial tras sismos.

## 2. Alcance y criterios de inclusión
Se incluyeron todos los documentos del repositorio: 103 archivos PDF, de los cuales 101 son únicos (dos duplicados por MD5). Sin filtro por relevancia; la relevancia se asigna después (núcleo, adyacente, periférico, ajeno).

## 3. Inventario y composición
Scopus {corp['SCOPUS']} (D001–D086), SciELO {corp['SCIELO']} (D087–D098), Web of Science {corp['WOS']} (D099), síntesis de buscadores {corp['SINTESIS_BUSCADOR']} (D100–D101). Idioma: 87 en inglés y 12 en español (dos sin dato). Años: 66 documentos de 2024 a 2026 y 12 de 2008.

## 4. Calidad de extracción
Texto completo de todos los documentos. Defectos documentados: tablas desalineadas (SciELO y otros), líneas duplicadas por dos columnas (D099), y recorte de listas de referencias en el texto limpio. Ninguna cifra se infirió de tablas ilegibles.

## 5. Distribución de relevancia
Núcleo {rel['Núcleo']}; adyacente {rel['Adyacente']}; periférico {rel['Periférico']}; ajeno {rel['Ajeno']}. Recomendación: aceptar con reservas {sum(1 for a in A.values() if a['recomendacion'].startswith('Aceptar'))}; rechazar como evidencia (usar solo como hipótesis) {sum(1 for a in A.values() if a['recomendacion'].startswith('Rechazar'))}.

## 6. Madurez multinivel
Mediana TRL {statistics.median(trl):.0f} (n = {len(trl)}; {sum(1 for t_ in trl if t_<=4)} con TRL ≤ 4); BRL {statistics.median(brl):.0f} (n = {len(brl)}); IRL {statistics.median(irl):.0f} (n = {len(irl)}); DRL {statistics.median(drl):.0f} (n = {len(drl)}). MRL no aplica en prácticamente todo el lote (sin manufactura). SRL estimado en {int(pd.read_csv(f'{C}/madurez_multinivel.csv').SRL_nivel.notna().sum())} documentos con la fórmula del analista.

## 7. Brechas y valles de la muerte
V1 {valle[1]}; V3 {valle[3]}; V2 {valle[2]}; V4 {valle[4]}; sin valle {valle[0]}. Brecha dominante: tecnología e integración por delante del negocio y de la evidencia en operación real.

## 8. Síntesis dialéctica del lote
*Tesis.* Los gemelos digitales, el IoT y la inteligencia en el borde pueden acelerar la detección, la evaluación de daño y la coordinación tras un sismo, y mejorar la resiliencia organizacional. *Antítesis.* La evidencia es de laboratorio, simulación, encuesta transversal o caso único; no mide tiempo de reanudación, ingresos ni empleo de empresas; y la evidencia de recuperación empresarial está desconectada de la tecnológica. *Síntesis.* La tecnología es una condición necesaria para reducir las demoras de detección y evaluación, pero su efecto sobre la recuperación productiva es una hipótesis cuya prueba exige integrar los modelos de recuperación con los datos de los gemelos y evaluar la transferencia con empresas.

## 9. KPIs agregados
Se extrajeron {len(kp)} indicadores. Cifras de referencia del lote: 101 documentos; {len(E)} relaciones tipificadas; {int(fich.palabras_ficha.sum()):,} palabras en fichas; k-means con 101 documentos k = {fu['kbest']} (silueta {fu['sil_kmeans']:.2f}) y sin SciELO k = {sc['kbest']} (silueta {sc['sil_kmeans']:.2f}); {ML['bibliometria']['citas_total']} citas Scopus en {ML['bibliometria']['n_docs_con_citas']} documentos con dato.

## 10. Triangulación
""" + "\n".join(f"- {r.id}: {r.afirmacion} — **{r.veredicto}** ({r.n_documentos} documentos, {r.grupos_independientes_de_autoria} grupos independientes)." for r in tri.itertuples()) + f"""

## 11. Patrones y tensiones
""" + "\n".join(f"- {r.id} ({r.tipo}): {r.descripcion}." for r in pt.itertuples() if r.id in ("P01","P02","P09","P10","P13","P14","P16","P19")) + f"""

## 12. Competidores y actores
Los competidores registrados (`csv/competidores.csv`) son enfoques alternativos y grupos de investigación citados en los documentos: sistemas centralizados frente a descentralizados de alerta, métodos clásicos frente a aprendizaje automático, ecuaciones de refuerzo y herramientas comerciales, y los dos asistentes de IA (Scopus AI y Web of Science Research Assistant). No hay competidores de mercado empresarial documentados con cuota o precio.

## 13. Variables econométricas y vacíos
Los estudios con modelos estructurales (D029, D030, D052, D085) usan percepciones como variable dependiente; los demás reportan resultados técnicos. Vacíos más frecuentes: territorial (sin América Latina en 33 de 87 documentos técnicos), de variables (sin métricas de recuperación en al menos 32) y causal (sin identificación). Total de vacíos registrados: {sum(len(A[i]['vacios']) for i in ids)}.

## 14. ML/NLP y sensibilidad
TF-IDF (unigramas y bigramas), k-means, Ward, DBSCAN, LDA (6 temas), PCA, t-SNE, redes de co-palabras y de coautoría. Con SciELO la estructura se reduce a dos bloques (idioma y dominio); sin SciELO, la silueta es {sc['sil_kmeans']:.2f} (difusa). ARI entre particiones con y sin SciELO a k = {se['k_fijo']}: {se['ARI_kmeans_k_fijo_completo_vs_sin_SciELO']:.2f}. Los resultados descriptivos de madurez no dependen del bloque SciELO.

## 15. Riesgos y premortem
Riesgos principales: usar proxies técnicos como beneficio empresarial; usar D100 o D101 como evidencia; extrapolar evidencia organizacional no sísmica; sobreponderar la cantidad de revisiones; ignorar la dependencia de pocos grupos de autores. Contingencia: pilotos con métricas de recuperación, ponderación por grupo de autoría y verificación contra las fuentes.

## 16. Recomendaciones, valor estratégico y próximos pasos
1. Conectar los parámetros de los gemelos digitales con los componentes de demora de los modelos de recuperación (proposición P-E1).
2. Diseñar un estudio empírico de transferencia tecnológica con empresas afectadas por sismos, con capacidad de absorción como moderador (P-E5).
3. Usar D100 y D101 solo como mapas de búsqueda y registrar una búsqueda propia con doble revisión.
4. Ponderar la evidencia por grupo de autoría y exigir intervalos de confianza y validación externa.
5. Ampliar el módulo de patentes: 11 patentes analizadas con OCR de sus 4.048 páginas (`patentes/`); faltan estado legal, lectura frase por frase de los pasajes críticos y búsqueda sistemática.

**Valor estratégico.** Fija qué evidencia puede sustentar decisiones de inversión y cuál es una hipótesis, y señala el vacío central del corpus.

**¿Qué se me escapa?** Estado legal y lectura frase por frase de las 11 patentes, búsqueda sistemática de patentes, registros de Scopus sin PDF y siete referencias de D100 fuera del lote, literatura regional en español, datos empresariales de cierre e ingresos, y una verificación entre revisores de los juicios de madurez.

**Documentos núcleo de mayor valor estratégico:** """ + "; ".join(f"{i} ({A[i]['c3']['valor'][0]}/10)" for i in top[:8]) + """.

**Prioridades de brecha:** """ + "; ".join(f"{r.doc_id}: {r.descripcion[:90]} (prioridad {r.prioridad_1_10})" for r in g8.itertuples()) + f"""

---
Archivos: `informe/informe_lote.md`, `informe/analisis_relacional.md`, `informe/bibliografia_APA.md`, `informe/tabla_control.md`, `informe/checklist_validacion.md`, `informe/diagramas_mermaid.md`, `csv/`, `figuras/`, `fichas/`.
"""
open(f"{I}/FICHA_RESUMEN_LOTE.md","w").write(md)
readme=f"""# SYNAPSE V19.0 — Lote L01

`{HEAD}`

Estructura: `fichas/` (101), `csv/` (19 + `csv/ml/`), `figuras/`, `informe/`, `_scripts/` (01–11, ejecutar en orden), `_fuente_analitica/` (YAML, inventario, conexiones).

Reproducción: `01_match_metadata.py`, `02_master_inventory.py`, `03_clean_texts.py`, YAML + `validate_doc.py`, `04_render_fichas.py`, `05_ml_nlp.py`, `06_conexiones.py`, `07_csvs.py`, `08_triangulacion_patrones.py`, `09_figuras.py`, `10_informes.py`, `11_ficha_resumen.py`. Los scripts 05 y 06 leen texto limpio y listas de referencias desde la carpeta de trabajo de la sesión; los resultados de citación verificada están guardados en `_fuente_analitica/aristas_citacion_verificadas.json` y `d100_referencia_a_documento.json`.

Módulo de patentes: `patentes/` (11 patentes de la carpeta `Patentes /`; informe, fichas P001-P011 y CSV); scripts `14_patentes_ocr.py`, `14b_patentes_terminos.py`, `15_patentes.py`, `15b_informe_patentes.py`.
"""
open(f"{L}/README.md","w").write(readme)
print("ficha resumen palabras:",len(md.split()))
