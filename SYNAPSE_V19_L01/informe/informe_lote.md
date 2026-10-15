# Informe del Lote L01 — SYNAPSE V19.0 (tejido empresarial, recuperación productiva y resiliencia tras sismos)

`MODE=COMPUTE FILES=TRUE BATCH=L01 DOCS=101 STATUS=COMPLETE`

Fecha de cierre: 2026-10-15. Repositorio de trabajo: `TejidoEmpresarial`, rama `claude/tejido-empresarial-synapse-rf1qle`.

## 1. Resumen ejecutivo

El lote L01 reúne 101 documentos únicos (103 archivos PDF; dos duplicados por huella MD5 entre las carpetas de Scopus y Web of Science), con 1,898 páginas y 1,136,120 palabras extraídas. Cada documento recibió lectura completa, un análisis estructurado con dialéctica, interrogación socrática, indicadores, madurez multinivel, brechas, falacias, causalidad, competidores, variables econométricas y vacíos, y una ficha bibliográfica analítica de cuatro capas (entre 3,763 y 5,529 palabras por ficha; media 4,679). Se construyeron 19 archivos CSV, 13 figuras, una red de 362 relaciones tipificadas y un análisis con aprendizaje automático y procesamiento de lenguaje natural sobre el texto completo.

Los resultados principales son siete.

1. **Composición.** 17 documentos son núcleo, 50 adyacentes, 23 periféricos y 11 ajenos al eje temático. Los 11 ajenos pertenecen al bloque SciELO de la revista *Biomédica* (2008); el documento restante de ese bloque (D087) trata la política colombiana de ciencia, tecnología e innovación y se clasificó como periférico.
2. **Madurez baja y homogénea.** En los 87 documentos técnicos, la mediana de TRL es 4 (55 de 84 con TRL ≤ 4, 65 %), la de BRL es 2 (62 de 83 con BRL ≤ 2) y la de IRL es 3. El valle de la muerte dominante es V1, investigación sin aplicación (66 documentos).
3. **Ausencia del resultado final de interés.** La recuperación productiva y la continuidad empresarial rara vez se miden: el vacío de variables lo declara de forma explícita en 32 de los 87 documentos técnicos, y ninguno estudia empíricamente la transferencia de tecnología en la recuperación posterremoto.
4. **Dos subliteraturas desconectadas.** El grafo de relaciones excluyendo las síntesis automáticas tiene 9 componentes; el de modelos de tiempo de recuperación y economía del refuerzo (D002, D011, D027, D040, D053, D054, D067, D069) no se relaciona con el grafo de gemelos digitales, IoT y factores organizacionales (41 documentos).
5. **Independencia limitada de la evidencia.** Cinco grupos de coautoría explican once documentos; 86 de las 93 referencias de la síntesis D100 coinciden con D001–D086, de modo que el lote no es independiente de ella.
6. **Estructura temática débil.** Con los 101 documentos, k-means elige k = 2 (silueta 0.23) y separa el bloque SciELO del resto; sin ese bloque, la silueta cae a 0.06, es decir, la estructura de los 89 documentos pertinentes es difusa. Con k fijo en 3, el acuerdo entre las particiones con y sin SciELO es moderado (ARI = 0.58).
7. **Calidad de reporte.** La robustez argumentativa media es 3.01 de 10; es mayor en el bloque ajeno (3.84) que en núcleo (3.19) y adyacentes (3.13), porque los estudios biomédicos reportan intervalos de confianza y controles de calidad que los estudios tecnológicos suelen omitir.

**Valor estratégico.** El lote permite (a) delimitar con evidencia qué parte de la literatura de gemelos digitales e IoT es utilizable para decisiones de recuperación productiva y qué parte es evidencia de laboratorio; (b) identificar el vacío central, la falta de estudios empíricos que conecten tecnología con desenlaces empresariales posteriores a sismos; y (c) fijar reglas de uso para las síntesis automáticas (D100, D101), que sirven como mapas de búsqueda y no como evidencia.

## 2. Alcance, método y trazabilidad

### 2.1 Corpus

El corpus proviene del repositorio `TejidoEmpresarial` y comprende cuatro grupos: 86 documentos de la carpeta Scopus (D001–D086), 12 de la carpeta SciELO (D087–D098), 1 documento exclusivo de Web of Science (D099) y 2 síntesis de buscadores con inteligencia artificial (D100; D101). Los metadatos bibliográficos se emparejaron con los archivos de exportación (DOI, título y autores); el emparejamiento de D099 se corrigió manualmente. Los registros bibliográficos de Scopus sin PDF están listados en `scopus_sin_pdf.json` y no se analizaron por no contar con el texto.

La distribución por año es: 2008: 12, 2013: 1, 2015: 1, 2020: 6, 2021: 5, 2022: 6, 2023: 4, 2024: 19, 2025: 23, 2026: 24. Hay 87 documentos en inglés y 12 en español. 66 documentos (65 %) son de 2024 a 2026, lo que implica que la acumulación de citas es limitada: 2962 citas Scopus en total para 86 documentos con dato, y 24 documentos concentran el 80 % de ellas.

### 2.2 Procedimiento por documento

Cada documento siguió seis pasos: extracción de texto con `pdftotext` y limpieza (se retiran listas de referencias, encabezados y avisos de descarga); lectura completa por tramos; redacción de un análisis en formato YAML con el esquema común; validación automática de mínimos de longitud y de estructura (objetivo, marco, metodología, resultados, discusión, antítesis, síntesis, puntos oscuros, zonas grises, ideas y valor; extensión mínima de la ficha de 800 palabras para documentos de menos de 15 páginas y de 1 500 para los de 15 o más; porcentaje de capa 3 de al menos 40 %); generación de la ficha en Markdown; y revisión de inconsistencias. Los 67 documentos de 15 páginas o más cumplieron el mínimo de 1 500 palabras y los demás el de 800 (cumplen 101 de 101).

### 2.3 Convenciones

- TRL, BRL, MRL, IRL y DRL se asignan con cita textual y página; cuando el documento no es tecnológico o comercial el valor es nulo con justificación. En las revisiones se asigna el nivel modal del campo revisado y así se declara.
- El SRL se calcula solo si hay al menos dos componentes con IRL (fórmula del analista: media de TRL × IRL sobre términos ordenados, dividida por 9 y acotada a [1, 9]); es una estimación documentada, no una medición. Se calculó para 79 documentos.
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

El corpus tiene 17 documentos núcleo (17 %), 50 adyacentes (50 %), 23 periféricos (23 %) y 11 ajenos (11 %). Los núcleos son los que combinan al menos dos de tres ejes: recuperación o resiliencia empresarial, gemelo digital o IoT, y escenario sísmico o posdesastre. Entre ellos están los modelos de tiempo de recuperación de empresas (D011) y de edificios (D053), los gemelos digitales de ciudad y comunitarios ante sismos (D034, D048, D070, D078, D080), las revisiones de gemelos para gestión posdesastre y cadenas de suministro (D013, D081), el estudio de resiliencia organizacional en la era digital (D082), la arquitectura 5G con cómputo en el borde para gemelos sísmicos (D064), la revisión de Industria 4.0 y riesgo de desastres (D099) y las dos síntesis de buscadores (D100, D101).

La extracción de texto tiene dos defectos que se registraron en las notas de cada ficha: tablas con columnas desalineadas (sobre todo en SciELO) y duplicación de líneas por maquetación a dos columnas (D099, páginas 3 a 12). Las cifras citadas en las fichas provienen del texto corrido y de las tablas legibles; cuando una tabla llegó ilegible no se infirieron valores.

## 4. Madurez multinivel

### 4.1 Distribución

Entre los 84 documentos técnicos con TRL asignado, la distribución es: TRL 2: 5, TRL 3: 22, TRL 4: 28, TRL 5: 11, TRL 6: 11, TRL 7: 6, TRL 8: 1. La mediana es 4. Los niveles altos (TRL 7 y 8) corresponden a revisiones y estudios de adopción de IoT y de soluciones digitales desplegadas (D005, D007, D026, D037, D044, D046, D051), no a sistemas validados en la recuperación de empresas. El BRL tiene mediana 2: 62 de 83 documentos (75 %) no presentan costos ni modelo de negocio. El IRL tiene mediana 3 (61 de 80 con IRL ≤ 3) y el DRL mediana 3, sin estudios de mercado.

### 4.2 Valles de la muerte

La clasificación por valle es: V1 (investigación sin aplicación) 66 documentos, V3 (tecnología sin negocio) 8, V2 (prototipo sin escalamiento) 7, V4 (componentes sin integración) 3 y sin valle 17 (documentos no tecnológicos). La severidad se distribuye en alta (28), media (55) y baja (18). La figura `fig_diagrama_valles.png` muestra que casi todos los documentos se ubican en la región donde el TRL excede al BRL en dos o más niveles o donde ambos son bajos.

La interpretación es la siguiente. La brecha no está en el sensado, en la comunicación ni en el cómputo, cuyas soluciones alcanzan TRL 4 a 7 con pruebas de laboratorio; está en la integración con datos heterogéneos (IRL ≤ 3), en la ausencia de modelos de negocio (BRL ≤ 2) y en la falta de evidencia en operación real. Las estrategias de salida propuestas en las fichas coinciden: pilotos en campo con métricas de continuidad, marcos abiertos de interoperabilidad y análisis de costos con empresas afectadas.

### 4.3 Perfil por grupo de relevancia

Las medianas por grupo (figura `fig_radar_madurez.png`; `csv/ml/madurez_medianas_por_grupo.csv`) son prácticamente idénticas entre núcleo y adyacentes (TRL 4, BRL 2, IRL 3, DRL 3) y menores en los periféricos (TRL 3, BRL 1). La proximidad temática al eje no se asocia, por tanto, con mayor madurez tecnológica.

## 5. Análisis con aprendizaje automático y procesamiento de lenguaje natural

### 5.1 Método

Se usó el texto limpio completo de los 101 documentos. Se eliminaron avisos de descarga y encabezados editoriales detectados como contaminación (el primer ensayo agrupó los documentos de IEEE por el aviso de licencia, por lo que se añadió un filtro y se repitió). Se calculó TF-IDF con unigramas y bigramas (mínimo 2 documentos, máximo 80 %, hasta 6 000 términos, ponderación sublineal) y listas de palabras vacías en inglés y español. Se aplicaron: k-means con k de 2 a 10 elegido por silueta con distancia coseno; agrupamiento jerárquico de Ward sobre una reducción SVD de 30 componentes; DBSCAN con distancia coseno (eps = percentil 60 de la distancia al tercer vecino); LDA con 6 temas sobre conteos; PCA y t-SNE (coseno) para proyección; redes de co-palabras (palabras clave de autor e índice, frecuencia ≥ 3) con detección de comunidades por modularidad voraz; red de coautoría; y concentración de citas (Pareto). La semilla aleatoria es 42.

### 5.2 Resultados con los 101 documentos

k-means elige k = 2 con silueta 0.23; la partición separa los 12 documentos de SciELO (español, biomédicos) de los 89 restantes, y coincide con el agrupamiento jerárquico (ARI = 1.00). DBSCAN encuentra 3 grupos y 15 documentos de ruido. Las dos primeras componentes del PCA explican 25.2 % de la varianza. La silueta de 0,23 no se debe a estructura temática interna sino a la diferencia de idioma y de dominio.

### 5.3 Sensibilidad: con y sin el bloque SciELO

Al excluir D087–D098, k-means elige k = 3 con silueta 0.06 y el acuerdo entre k-means y jerárquico baja a ARI = 0.77. Al excluir además las síntesis D100 y D101, k = 2, silueta 0.06 y ARI entre métodos 0.03. Con k fijo en 3, las particiones del conjunto completo y del conjunto sin SciELO coinciden de manera moderada (ARI = 0.58) y los 12 documentos de SciELO caen en un único grupo.

Se concluye: (a) incluir el bloque SciELO eleva artificialmente la separación de grupos; (b) en los 89 documentos pertinentes la estructura es difusa (silueta por debajo de 0,07 para todo k de 2 a 10), de modo que no existen familias temáticas nítidas sino un continuo con gradientes entre sensado sísmico, gemelos de infraestructura, organización y cadenas de suministro; y (c) los resultados descriptivos (medianas de madurez, patrones) no dependen del bloque SciELO porque se calcularon sobre los documentos técnicos.

### 5.4 Temas

Los 6 temas de LDA del conjunto sin SciELO, resumidos por sus términos principales, son: (0) refuerzo sísmico, recuperación y costos de edificios de concreto; (1) monitoreo de salud estructural, puentes y gemelos con computación en el borde; (2) gestión de desastres, terremotos y gemelos urbanos con UAV; (3) cadenas de suministro, Industria 4.0, sostenibilidad y construcción; (4) alerta temprana sísmica (EEW), LoRa y latencia; y (5) conocimiento, servicios y resiliencia organizacional. Los tres grupos de k-means (k = 3) corresponden a refuerzo sísmico y concreto; IoT, algoritmos, nodos y latencia; y desastres, recuperación, gemelos y organización. Los listados completos están en `csv/ml/ml_terminos_por_grupo.csv`.

### 5.5 Redes y bibliometría

La red de co-palabras tiene 70 nodos y 852 aristas, con 4 comunidades (modularidad 0.25, baja). El mapa de centralidad-densidad (`fig_mapa_centralidad_densidad.png`) ubica la comunidad de gemelo digital, monitoreo estructural e interoperabilidad como la más densa; la de IoT, aprendizaje automático y alerta temprana como la más central; y la de sismología, refuerzo, adopción tecnológica e Industria 4.0 como la menos central y densa. Hay 332 autores únicos en los documentos técnicos; solo 14 aparecen en dos o más documentos y hay 63 componentes de coautoría con más de dos autores, lo que indica un campo fragmentado sin núcleo de autores recurrentes. Las revistas con más documentos son *IEEE Internet of Things Journal* (6), *Sensors* (5), *Sustainability* (4), *International Journal of Disaster Risk Reduction* (3) y *Smart Cities* (3).

## 6. Triangulación de afirmaciones

La tabla `csv/triangulacion.csv` evalúa 14 afirmaciones transversales. Los resultados son:

- **T01. El procesamiento en el nodo o en el borde reduce la latencia de alerta y actualización frente a arquitecturas centralizadas** (6 documentos; 4 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **Triangulado con reservas**. Tres de seis documentos (D045, D049, D075) comparten autoría; la convergencia independiente la aportan D073, D064 y D066.
- **T02. La interoperabilidad y la calidad de datos son la barrera técnica principal de los gemelos digitales y del IoT en desastres** (10 documentos; 10 grupos independientes de autoría; TRL mediano 4.5). Veredicto: **Triangulado**. Convergencia alta, aunque D100 no es fuente independiente (es una síntesis automática cuya lista contiene a 86 documentos del lote).
- **T03. Los gemelos digitales y el IoT mejoran la resiliencia organizacional y la eficiencia operativa** (6 documentos; 6 grupos independientes de autoría; TRL mediano 6.0). Veredicto: **En tensión**. Posible sesgo de método común; ningún estudio mide desenlaces objetivos de empresa; el efecto causal no se identifica.
- **T04. El tiempo de reparación del edificio no basta como medida de recuperación empresarial; deben modelarse demoras e inactividad por tipo** (5 documentos; 4 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **Triangulado con reservas**. D040 y D053 comparten autoría (Galasso); la validación con empresas reales es escasa.
- **T05. Incluir pérdidas indirectas y recuperación cambia la decisión de refuerzo sísmico** (3 documentos; 3 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **Parcial**. Tres documentos con casos distintos; faltan datos empíricos de pérdidas por interrupción.
- **T06. Los gemelos digitales urbanos estiman daño y necesidades de respuesta en escenarios sísmicos** (6 documentos; 5 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **Parcial**. D048 y D080 comparten autoría; la evidencia depende de escenarios y de datos públicos.
- **T07. Las revisiones de gemelos digitales concluyen potencial alto con implementación incipiente** (7 documentos; 7 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **Triangulado**. Siete revisiones convergen; comparten sesgo de publicación hacia resultados favorables.
- **T08. Los efectos digitales sobre la resiliencia de cadenas de suministro son mayores en preparación y respuesta que en recuperación** (3 documentos; 3 grupos independientes de autoría; TRL mediano 6.0). Veredicto: **Parcial**. Dos fuentes cuantitativas o sistemáticas independientes; la mayoría de estudios de base son transversales.
- **T09. Los costos bajos del monitoreo estructural con IoT se demuestran solo en laboratorio o en estructuras individuales** (5 documentos; 4 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **Triangulado**. D039 y D086 comparten autoría; D023 es la única operación en campo.
- **T10. El orden de desempeño entre algoritmos de aprendizaje automático para alerta sísmica no es transferible entre estudios** (3 documentos; 3 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **En tensión**. Diferencias de tarea (intensidad frente a magnitud), datos y métricas; ninguna comparación directa con los mismos datos.
- **T11. UAV e IoT permiten restablecer comunicaciones y acelerar la evaluación de daños** (5 documentos; 5 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **Parcial**. Mayoría con simulación; escasa evidencia de operación en desastres reales.
- **T12. La adopción del IoT y del gemelo digital depende de liderazgo, habilidades y aceptación de las partes interesadas** (6 documentos; 6 grupos independientes de autoría; TRL mediano 7.0). Veredicto: **Triangulado con reservas**. La evidencia organizacional procede de contextos no sísmicos; faltan estudios en recuperación posterremoto.
- **T13. La prefabricación y la robótica contribuyen a la recuperación posdesastre** (1 documentos; 1 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **Fuente única**. Solo D099 trata el tema; ningún estudio del lote mide el efecto en la recuperación.
- **T14. La transferencia tecnológica como mecanismo tiene evidencia empírica en recuperación posterremoto** (2 documentos; 2 grupos independientes de autoría; TRL mediano 4.0). Veredicto: **Sin evidencia primaria**. Ningún documento del lote estudia empíricamente la transferencia tecnológica en recuperación posterremoto; es el vacío central del corpus.

Tres afirmaciones se triangulan sin reservas (interoperabilidad como barrera, revisiones convergentes sobre potencial frente a implementación incipiente, costos bajos solo en laboratorio). Dos están en tensión (efecto de IoT y gemelos en resiliencia organizacional; orden de algoritmos de alerta). Una tiene fuente única (prefabricación y robótica) y otra carece de evidencia primaria (transferencia tecnológica en recuperación posterremoto).

## 7. Patrones, tensiones y anomalías

La tabla `csv/patrones_tensiones.csv` documenta 19 elementos. Los más relevantes para decisiones:

- **P01 (patrón).** Madurez tecnológica baja y homogénea: la mediana de TRL es 4 en 84 documentos técnicos con TRL asignado (55 con TRL ≤ 4, 65 %); la mediana de BRL es 2 y la de IRL es 3. Implicación: El conjunto es evidencia de laboratorio y simulación; no hay base para estimar efectos en empresas.
- **P02 (patrón).** BRL ≤ 2 en 62 de 83 documentos con BRL asignado (75 %): casi ningún estudio presenta costos, modelos de negocio o análisis de adopción empresarial. Implicación: Valle de la muerte comercial como condición general del campo.
- **P04 (patrón).** Validación simulada o sintética como evidencia principal. Implicación: Las ganancias reportadas (latencia, precisión, bienestar) no se han observado en operación.
- **P09 (tensión).** Resiliencia organizacional como mediador lineal (D030) frente a propiedad emergente (D082). Implicación: Los diseños de evaluación de empresas posterremoto cambian según la conceptualización.
- **P11 (patrón).** Concentración de la evidencia de alerta sísmica de bajo costo en un grupo de autoría (Prasanna: D045, D049, D075). Implicación: La convergencia aparente sobre la latencia descentralizada es parcialmente no independiente.
- **P12 (patrón).** Otros agrupamientos de autoría compartida que reducen la independencia: Yu-Fu-Cui (D039, D086), Galasso (D040, D053), Korkmaz-Demirkesen (D048, D080), Abdalzaher-Krichen (D019, D060). Implicación: Cinco pares de documentos del lote no son confirmaciones independientes.
- **P13 (anomalía).** La síntesis D100 incluye como referencias a los 86 documentos D001-D086 (86 de 93 referencias); el corpus Scopus del lote coincide con su lista. Implicación: El lote no es independiente de la síntesis; D100 no puede validar al corpus y hay riesgo de sesgo de selección del buscador.
- **P14 (anomalía).** D100 declara alcance 2020-2024 pero 49 de 93 referencias son de 2025-2026 y hay referencias de 2013 y 2015. Implicación: El alcance declarado no se cumple; el resultado depende del índice en octubre de 2026.
- **P16 (patrón).** Ausencia explícita de métricas de recuperación o continuidad empresarial en 32 de 87 documentos técnicos (el vacío VAR lo declara de forma explícita). Implicación: El resultado final de interés (recuperación productiva) no se mide en gran parte de la literatura.
- **P19 (tensión).** Mayor robustez argumentativa en los documentos ajenos al tema (media 3,84 de 10 en el bloque SciELO frente a 3,19 en núcleo y 3,13 en adyacentes). Implicación: La relevancia temática no coincide con la calidad de reporte estadístico: los estudios biomédicos reportan intervalos y controles de calidad que los técnicos omiten.

### 7.1 Circularidad del corpus con la síntesis D100

La lista de 93 referencias de D100 se comparó por título con los 101 documentos. Se identificaron 86 coincidencias, que corresponden a todos los documentos D001–D086; siete referencias (9, 10, 15, 41, 68, 71 y 79) no tienen archivo en el lote. Esto indica que el corpus Scopus se construyó a partir de lo que esa síntesis recuperó, de modo que (a) la convergencia entre D100 y el corpus no es evidencia independiente; (b) los sesgos de recuperación del buscador (preferencia por documentos recientes: 49 de 93 referencias son de 2025 o 2026, a pesar del alcance declarado de 2020 a 2024; inclusión de documentos ajenos, como acuaponía, cadenas de alimentos y salud de aviación) se transmiten al lote; y (c) la literatura de recuperación empresarial posterremoto que no use los términos de la consulta queda subrepresentada. D101 comparte con D100 dos de sus tres referencias (D070 y D080).

### 7.2 Falacias

Se registraron 300 falacias en 101 documentos. La más frecuente es la generalización apresurada (58, 19 %), seguida de petición de principio (16), falsa causa (9) y selección sesgada (8). La interpretación es que las conclusiones exceden sistemáticamente la base empírica, sobre todo en estudios de validación única, en simulaciones y en encuestas transversales.

### 7.3 Relevancia frente a calidad de reporte

La robustez media (consistencia lógica 30 %, calidad de evidencia 30 %, validez de inferencia causal 25 %, generalizabilidad 15 %) es 3.84 en ajenos, 3.19 en núcleo, 3.13 en adyacentes y 2.24 en periféricos. La diferencia a favor del bloque ajeno se explica por la práctica de reporte (intervalos de confianza, controles de calidad externos, aprobación ética, declaración de limitaciones) y no por mayor relevancia. Esta asimetría sugiere adoptar guías de reporte para estudios tecnológicos.

## 8. Variables econométricas, vacíos y brechas

Se extrajeron 959 indicadores, 694 vacíos (siete tipos por documento: territorial, poblacional, temporal, metodológico, de variables, teórico y causal) y 391 brechas de oportunidad (Metodológico: 111, Conocimiento: 109, Mercado: 90, Tecnológico: 81). Los patrones de los vacíos son:

- **Territorial.** 33 de los 87 documentos técnicos declaran de forma explícita la ausencia de América Latina; la excepción es un caso de edificio patrimonial en Lima (D014). No hay datos de regiones sísmicas latinoamericanas para empresas.
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

1. **Patentes.** Los 103 PDF de las carpetas de las bases bibliográficas son artículos de revista; las 11 patentes se aportaron después en la carpeta `Patentes /` y se analizaron en un módulo separado (`patentes/`) mediante reconocimiento óptico de sus 4.048 páginas. Siguen pendientes la verificación del estado legal, la lectura frase por frase de los pasajes críticos y una búsqueda sistemática de patentes por clasificación; sin ellas, la transferencia tecnológica se analiza sobre todo desde la literatura.
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
6. Ampliar el módulo de patentes con verificación del estado legal, lectura frase por frase de los pasajes críticos y búsqueda sistemática.

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
