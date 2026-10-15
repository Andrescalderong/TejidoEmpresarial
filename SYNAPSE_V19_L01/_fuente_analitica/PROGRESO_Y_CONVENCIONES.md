# Control de proceso — Lote L01 (SYNAPSE V19.0)

## Corpus (101 documentos únicos; 103 PDF; 2 duplicados MD5 entre Scopus y WOS)
D001–D086 Scopus (orden alfabético de archivo) · D087–D098 SciELO (Biomédica 28(3), 2008) · D099 WOS exclusivo (Habibi Rad et al., 2021) · D100 Scopus AI (síntesis) · D101 WoS Research Assistant (síntesis).
Registros Scopus sin PDF: ver `scopus_sin_pdf.json`.

## Flujo por documento
1. Texto limpio en el scratchpad de sesión: `.../scratchpad/clean/D###.txt` (regenerable con `_scripts/03_clean_texts.py <dir>`).
2. Lectura completa (Read, por tramos si > 25k tokens).
3. Escritura de `docs/D###.yaml` (esquema = D001..D005). Cada campo de texto en español.
4. `python3 _scripts/validate_doc.py docs/D###.yaml` (mínimos de la especificación: objetivo≥80, marco≥100, metodología≥150, resultados≥200, discusión≥100, antítesis≥100, síntesis≥100, puntos oscuros≥150, áreas grises≥3 y ≥150 palabras, ideas≥2 y ≥200, valor≥50, ficha≥800 (<15 pp) o ≥1500 (≥15 pp), Capa 3 ≥40 %).
5. Ajustes con `_scripts/patch.py D###.yaml` (ancla tolerante a saltos de línea; recibe JSON [[ancla, reemplazo],...]).
6. `python3 _scripts/04_render_fichas.py` → `fichas/D###_slug.md`.

## Convenciones analíticas
- TRL/BRL = `null` cuando el documento no es tecnológico/comercial (editorial, biomédico, síntesis de buscador), con justificación. Para revisiones se asigna el TRL/BRL modal del campo revisado y se declara así.
- SRL: se calcula solo si hay ≥2 componentes con IRL (`madurez.srl`); fórmula del analista = media de TRLi×IRLij sobre términos ordenados, ÷9, acotada a [1,9]. Es una estimación documentada, no una medición.
- KPIs: se marca como "Derivado/cálculo del analista" cualquier cifra recalculada. Nunca se completan datos ausentes: se escribe "No especificado en documento".
- Relevancia respecto del eje del corpus (recuperación productiva y resiliencia empresarial tras sismos con transferencia de tecnología, gemelos digitales e IoT): Núcleo | Adyacente | Periférico | Ajeno.
- Citas textuales de evidencia: ≤25 palabras, con página PDF.

## Pasos finales (después de D101)
A. `01–03` ya ejecutados. B. Pipeline ML/NLP real (TF-IDF, k-means, jerárquico, DBSCAN, LDA, PCA/t-SNE, redes de co-palabras/co-autoría) sobre texto limpio + metadatos → `csv/` y `figuras/`.
C. `conexiones.json` (relaciones inter-documentales por DOC_ID) → re-render de fichas.
D. CSV por lote (19), informe del lote (>5 000 palabras), FICHA_RESUMEN_LOTE (16 secciones), análisis relacional (>2 000 palabras), bibliografía APA, tabla de control, visualizaciones, checklist.

## Pendiente: patentes (solicitado por el usuario durante la ejecución)
- Verificado: el repo no contiene patentes (103 PDF, 2 RIS, 3 CSV; todo TY - JOUR). Solo hay 2 referencias bibliográficas a estudios sobre patentes dentro de scopus.csv.
- Plan: (1) completar D044-D101; (2) al cierre, módulo de patentes: si el usuario aporta archivos o autoriza búsqueda externa (Google Patents/Espacenet), se analizarán con el mismo esquema; si no, se documenta como vacío del corpus y se incluyen en el informe las dos referencias de paisaje de patentes como pistas.
