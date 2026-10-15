# Lista de verificación — Lote L01

| # | Requisito | Estado | Evidencia |
|---|---|---|---|
| 1 | 101 documentos únicos analizados | Cumplido | `fichas/` contiene 101 fichas; `docs/` contiene 101 YAML |
| 2 | Ficha de cuatro capas por documento, extensión mínima (800 / 1 500 palabras) | Cumplido | 101 de 101 fichas cumplen (`csv/fichas_bibliograficas.csv`) |
| 3 | Capa 3 ≥ 40 %, ≥ 3 zonas grises y ≥ 2 ideas propositivas por ficha | Cumplido | validación automática `validate_doc.py` sobre los 101 YAML |
| 4 | Dialéctica, socrática, KPIs, madurez multinivel con cita, brechas y valles, falacias y causalidad, competidores, variables econométricas, vacíos | Cumplido | secciones B.1 a B.8 de cada ficha |
| 5 | 19 archivos CSV | Cumplido | 19 CSV en `csv/` (inventario, kpis, madurez_multinivel, brechas_madurez, valles_muerte, dialectica, falacias, gaps_oportunidades, competidores, figuras, sintesis_interpretativa, triangulacion, variables_econometricas, vacios_detectados, protopreguntas, patrones_tensiones, bibliografia, fichas_bibliograficas, analisis_relacional) |
| 6 | Informe del lote > 5 000 palabras | Cumplido | `informe/informe_lote.md` (5,420 palabras) |
| 7 | FICHA_RESUMEN_LOTE con 16 secciones | Cumplido | `informe/FICHA_RESUMEN_LOTE.md` |
| 8 | Análisis relacional > 2 000 palabras, ≥ 3 proposiciones emergentes y puntaje | Cumplido | `informe/analisis_relacional.md` (4,974 palabras; 5 proposiciones; S = 7.8) |
| 9 | Aprendizaje automático y PLN reales, con sensibilidad con y sin bloque SciELO | Cumplido | `_scripts/05_ml_nlp.py`, `csv/ml/`, `ml_resumen.json` |
| 10 | Visualizaciones (matriz de madurez, radar, mapa de calor de brechas, diagrama de valles, centralidad-densidad, Pareto, Mermaid) | Cumplido | 11 PNG en `figuras/` y `informe/diagramas_mermaid.md` |
| 11 | Bibliografía APA 7 | Cumplido | `informe/bibliografia_APA.md` (101 entradas) |
| 12 | Tabla de control | Cumplido | `informe/tabla_control.md` |
| 13 | Distinción entre cálculo y juicio | Cumplido | sección 2.4 del informe |
| 14 | Patentes | **Pendiente** | El repositorio no contiene patentes; requiere archivos o autorización de búsqueda externa |
| 15 | Anomalías de datos registradas | Cumplido | `csv/patrones_tensiones.csv` (P06, P13, P14) y notas de cada ficha |
