# SYNAPSE V19.0 — Lote L01

`MODE=COMPUTE FILES=TRUE BATCH=L01 DOCS=101 STATUS=COMPLETE`

Estructura: `fichas/` (101), `csv/` (19 + `csv/ml/`), `figuras/`, `informe/`, `_scripts/` (01–11, ejecutar en orden), `_fuente_analitica/` (YAML, inventario, conexiones).

Reproducción: `01_match_metadata.py`, `02_master_inventory.py`, `03_clean_texts.py`, YAML + `validate_doc.py`, `04_render_fichas.py`, `05_ml_nlp.py`, `06_conexiones.py`, `07_csvs.py`, `08_triangulacion_patrones.py`, `09_figuras.py`, `10_informes.py`, `11_ficha_resumen.py`. Los scripts 05 y 06 leen texto limpio y listas de referencias desde la carpeta de trabajo de la sesión; los resultados de citación verificada están guardados en `_fuente_analitica/aristas_citacion_verificadas.json` y `d100_referencia_a_documento.json`.

Módulo de patentes: `patentes/` (11 patentes de la carpeta `Patentes /`; informe, fichas P001-P011 y CSV); scripts `14_patentes_ocr.py`, `14b_patentes_terminos.py`, `15_patentes.py`, `15b_informe_patentes.py`.
