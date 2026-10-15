# FB-L01-076 | D076 — Deep Learning Image-Based Classification for Post-Earthquake Damage Level Prediction Using UAVs

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/sensors-25-05406.pdf` · 23 páginas · Relevancia para el eje del corpus: **Adyacente** (Evalúa un clasificador de imágenes ligero (MobileNetV3-Small con ajuste fino) para predecir tres niveles de daño en edificios tras un terremoto con imágenes de vehículos aéreos no tripulados (UAV), sobre un conjunto de datos fusionado de tres fuentes, y lo despliega en una Raspberry Pi 5 con medidas de cuadros por segundo. Aporta evaluación rápida de daño en el borde, útil para priorizar inspección y rescate, y es pertinente a la fase de respuesta inmediata, aunque las imágenes proceden de bases no aéreas, la evaluación no se conecta con la recuperación empresarial ni con tiempos de reocupación y el vuelo real no se prueba.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-076 / D076
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Alsaaran, N., & Soudani, A. (2025). Deep Learning Image-Based Classification for Post-Earthquake Damage Level Prediction Using UAVs. *Sensors*, *25*(17), Article 5406. https://doi.org/10.3390/s25175406
- **Autores:** Alsaaran, Norah (57222659399); Soudani, Adel (6602550839)
- **Afiliaciones:** Computer Science Department, College of Computer and Information Sciences, King Saud University, Riyadh, 11543, Saudi Arabia
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Sensors · vol. 25(17)
- **Identificador persistente:** DOI 10.3390/s25175406 · ISSN 14248220
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105015894696&doi=10.3390%2fs25175406&partnerID=40&md5=bac98945f252684f5043628093b2c265
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 6

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Investigar el uso del modelo convolucional ligero MobileNetV3-Small para la predicción en tiempo real del nivel de daño posterremoto con imágenes capturadas por vehículos aéreos no tripulados (UAV), de modo que el procesamiento pueda hacerse a bordo y se oriente de manera eficiente el trabajo de los equipos de búsqueda y rescate. El modelo clasifica tres niveles (sin daño o menor, moderado y severo) y se evalúa en un conjunto de datos fusionado de tres bases de imágenes de daño posterremoto, con comparación frente a cinco modelos ligeros, estudios previos y una prueba de despliegue en Raspberry Pi 5.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si un modelo ligero con transferencia de aprendizaje y ajuste fino de las últimas cinco capas alcanza una exactitud adecuada para clasificar tres niveles de daño, cuánto cuesta en operaciones de coma flotante frente a otros modelos ligeros, y si puede ejecutarse en un dispositivo embebido a una velocidad compatible con una aplicación en tiempo real.

**Marco teórico.** El marco combina el aprendizaje profundo en visión por computador, la transferencia de aprendizaje y el cómputo en el borde. Los autores sostienen que la inspección manual posterremoto es lenta, costosa y peligrosa, que los UAV pueden transmitir imágenes y construir mapas de daño, que las redes convolucionales extraen automáticamente grietas, desplazamientos y deformaciones y que modelos como MobileNet equilibran desempeño y complejidad. Las categorías de daño se definen por indicios visuales: leve (grietas superficiales y desprendimiento de revoque), moderado (grietas visibles en muros o columnas, deformación parcial) y severo (muros colapsados, refuerzo expuesto, inclinación o colapso total). La revisión de trabajos incluye EmergencyNet, WATT-EffNet, EFFC-Net, DiRecNetV2, variantes de YOLO para daño en edificios y trabajos con datos del terremoto de Hatay-Maraş de 2023.

**Metodología.** El modelo parte de MobileNetV3-Small preentrenado en ImageNet, con todas las capas congeladas al inicio, un clasificador final adaptado a tres clases y ajuste fino de las últimas cinco capas del extractor de características y del clasificador. Los datos fusionan MEDIC (imágenes de redes sociales filtradas para terremotos), la base Disaster Scenes Database y el conjunto de Ünlü et al. Alrededor de 30 % se limpió manualmente (ambigüedad, etiquetas incorrectas y valores atípicos) y el modelo entrenado en ese subconjunto asistió en la clasificación del 70 % restante, con revisión manual posterior, para un conjunto final de 10 243 imágenes. La división estratificada es de 8195 para entrenamiento, 1024 para validación y 1024 para prueba, con tasa de aprendizaje de 0,0001, tamaño de entrada de 224 por 224, lote de 32, decaimiento de pesos de 0,00001, desconexión de 0,2 y optimizador Adam, con pesos de clase en la función de pérdida. El modelo se entrenó cinco veces, y se comparó con MobileNetV2, MobileNetV3, SqueezeNet, ShuffleNetV2 y EfficientNet-B0, con modelos de estudios previos y con EmergencyNet en una Raspberry Pi 5 con cámara.

**Resultados principales.** Los resultados indican que el modelo con ajuste fino logra un F1 ponderado de 0,93 y una exactitud de 0,93 en la prueba, con F1 de 0,85 para sin daño o menor, de 0,62 para moderado y de 0,97 para severo, y que supera a los modelos de referencia, cuyo F1 ponderado va de 0,85 a 0,90. La clase moderada, con 953 imágenes, tiene precisión de 0,60 y recall de 0,64, y la clase severa, con 8718 imágenes (85 % del conjunto), tiene precisión de 0,97 y recall de 0,96. El modelo requiere 61,6 millones de operaciones de coma flotante, 1,65 millones de parámetros y 6,29 MB, y MobileNetV3 sin ajuste fino requiere 61,5 millones. En comparación con estudios previos, el F1 sobre la base Disaster Scenes es de 0,65 frente a 0,63 de una red Faster R-CNN con ResNet-50, y la exactitud sobre el conjunto de Ünlü es de 0,73 frente a 0,66 de VGG19. En la Raspberry Pi 5 el modelo procesa 3,21 cuadros por segundo con 0,3117 s por imagen, frente a 5,11 cuadros por segundo de SqueezeNet y 6,11 de EmergencyNet, que tiene un F1 ponderado de 0,87. Los autores atribuyen el bajo desempeño en las clases minoritarias al desbalance de datos.

**Discusión y contribución.** Los autores sostienen que el modelo ofrece un equilibrio entre exactitud y eficiencia apto para el despliegue a bordo, que el ajuste fino de las últimas cinco capas mejora el F1 en 0,04 puntos frente al ajuste solo del clasificador a un costo mínimo de operaciones, que la combinación de tres bases es novedosa y que el despliegue en Raspberry Pi 5 confirma la viabilidad en dispositivos de borde. Reconocen que la clase moderada es difícil por solapamiento de rasgos con las clases adyacentes y por el desbalance, que SqueezeNet y EmergencyNet son más rápidos y que su modelo tiene mayor exactitud pero menor velocidad. Concluyen que la información en tiempo real permite a los equipos de rescate priorizar esfuerzos y entregar ayuda a las zonas más afectadas.

**Limitaciones declaradas.** Declaradas: el desbalance de clases persiste a pesar de las técnicas aplicadas y limita el desempeño en las clases moderada y sin daño o menor; el modelo es más lento que SqueezeNet y EmergencyNet en la Raspberry Pi. No declaradas: las imágenes proceden de redes sociales, de bases de escenas y de fotografías de edificios y no son imágenes aéreas de UAV, de modo que se desconoce el desempeño con el ángulo, la altura y la resolución de un vuelo; el etiquetado se apoyó en el propio modelo para el 70 % de las imágenes, lo que introduce circularidad entre las etiquetas y el modelo evaluado; los conteos de la Tabla 1 no coinciden con las descripciones de los conjuntos del texto; el desempeño en conjuntos independientes (F1 de 0,65 y exactitud de 0,73) es mucho menor que 0,93, lo que sugiere dependencia de la fuente dominante; 85 % de las imágenes son de daño severo; no hay división por evento o por sitio; no se reportan intervalos de confianza de las cinco corridas; la prueba de despliegue mide la velocidad con imágenes del conjunto de prueba y no con vuelo; no se evalúa el consumo de energía ni la geolocalización; la clasificación de edificios individuales no se vincula con la ocupación, la actividad económica ni los tiempos de reocupación.

**Trabajo futuro.** Explícito: explorar optimizaciones para mejorar la robustez del modelo en condiciones ambientales variables y la eficiencia general del sistema de evaluación basado en UAV. Implícito: validación con imágenes aéreas de campañas reales, pruebas en vuelo, consumo de energía, pruebas en otras plataformas embebidas como Jetson e integración con mapas de daño y sistemas de gestión de emergencia.

**Palabras clave.** Declaradas: convolutional neural network (CNN); deep learning; earthquake; edge computing; MobileNet; real-time damage assessment; unmanned aerial vehicle (UAV) | Inferidas: UAV, aprendizaje profundo, evaluación de daño posterremoto, MobileNetV3, clasificación de imágenes, cómputo en el borde, Raspberry Pi, ajuste fino, conjunto de datos desbalanceado, rescate

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un modelo MobileNetV3-Small con transferencia de aprendizaje y ajuste fino de las últimas cinco capas clasifica tres niveles de daño posterremoto con un F1 ponderado de 0,93, supera a cinco modelos ligeros de referencia con solo 61,6 millones de operaciones de coma flotante y 6,29 MB, y se ejecuta en una Raspberry Pi 5 a 3,21 cuadros por segundo, lo que permite una evaluación de daño en el borde para orientar a los equipos de búsqueda y rescate.

**Antítesis identificada.** El desempeño de 0,93 se obtiene sobre un conjunto fusionado en el que 85 % de las imágenes son severas, cuyas etiquetas se refinaron con el propio modelo, y baja a 0,65 de F1 y 0,73 de exactitud en conjuntos independientes, lo que indica dependencia de la fuente y no capacidad general. Las imágenes no son aéreas ni de UAV, de manera que el título y la motivación no se contrastan con el escenario declarado. La clase moderada, la más útil para priorizar inspecciones, obtiene un F1 de 0,62. La prueba de despliegue mide 3,21 cuadros por segundo con imágenes del conjunto, sin vuelo ni energía, y modelos más simples son más rápidos. El resultado no se conecta con decisiones de reocupación, tiempos de inspección ni actividad económica.

**Síntesis propuesta.** La contribución sostenible es una comparación reproducible de modelos ligeros para clasificar daño visible en imágenes, con una línea base de eficiencia en una computadora de placa única y una evidencia clara de la dificultad de la clase intermedia. Para el corpus, importa por mostrar que la evaluación visual automática de daño puede ejecutarse en el borde con hardware barato y por su relación con la rapidez de inspección, un insumo de la recuperación. No obstante, el desempeño informado depende de un conjunto desbalanceado y parcialmente etiquetado por el propio modelo, y su utilidad para la recuperación empresarial exige validación con imágenes aéreas de campañas reales, división por evento y conexión con los tiempos de inspección y de reapertura.

**Áreas grises detectadas.**

1. Dominio de las imágenes: el estudio se plantea para un UAV que sobrevuela una ruta predefinida, pero las imágenes provienen de MEDIC (redes sociales), de Disaster Scenes Database y del conjunto de Ünlü et al., que incluyen fotografías a nivel de calle y de edificios, de modo que el desempeño con las vistas aéreas, la altura de vuelo, la oclusión y el movimiento no se mide.
2. Circularidad del etiquetado: después de limpiar manualmente alrededor del 30 % de las imágenes, el modelo entrenado con ese subconjunto asistió en la clasificación del 70 % restante, que luego se revisó y se incorporó al conjunto; las etiquetas de entrenamiento, validación y prueba pueden reflejar los sesgos del modelo y sobrestimar su desempeño.
3. Distribución de clases y de fuentes: 8718 de las 10 243 imágenes finales son severas (85 %), la clase moderada tiene 953 imágenes, y los conteos de la Tabla 1 (por ejemplo, 8666 imágenes asignadas a una fuente que el texto describe con 900) no coinciden con las descripciones, de modo que no se puede saber qué fuente domina ni si la división por conjunto se mezcla entre fuentes.
4. Desempeño fuera del conjunto fusionado: sobre la base Disaster Scenes con la partición de un estudio previo el F1 es de 0,65 y sobre la base de Ünlü la exactitud es de 0,73, frente a 0,93 en el conjunto fusionado, lo que sugiere que la cifra principal no generaliza a conjuntos independientes y que la comparación con modelos previos (detección con Faster R-CNN, clasificación con VGG19) tiene objetivos distintos.

**Puntos oscuros aclarados.** Llama la atención que el resumen afirme una reducción de 58,8 % de las operaciones frente a ShuffleNetV2 cuando los valores de la Tabla 7 (61,5 y 151,7 millones) dan alrededor de 59,5 %, y que se indique un aumento de 0,2 % por el ajuste fino cuando la tabla muestra una diferencia de 0,1 millones, equivalente a 0,16 %. También es notable que se califique de tiempo real una velocidad de 3,21 cuadros por segundo obtenida en una Raspberry Pi con imágenes almacenadas, y que se afirme que el desempeño del modelo equilibra precisión y recall cuando la clase moderada tiene 0,60 y 0,64. El texto menciona un AUC de 0,91 y luego de 0,93 para la clase moderada. El entrenamiento se detuvo en la época 12 en un lugar y en la época 28 en otro. Además, el artículo celebra la primera combinación de tres bases de datos como novedad, aunque la fusión es la causa de las inconsistencias de etiquetas que obligaron a limpiar el 30 % de las imágenes y a reetiquetar más de 1300. Por último, el uso de un modelo que predice el daño de edificios no considera la información sobre qué edificios albergan actividad económica. La conclusión afirma que el modelo es el segundo con menos parámetros entre los de referencia, aunque la Tabla 7 lo sitúa tercero tras SqueezeNet (0,70 millones) y ShuffleNetV2 (1,30 millones), y que opera en plataformas como Jetson, que no se probaron.

**Ideas propositivas novedosas.**

1. Validación con imágenes aéreas por evento y por sitio: reunir imágenes de UAV de al menos dos terremotos recientes, con etiquetas de daño asignadas por ingenieros con una escala estándar y con división por evento y por barrio, y evaluar el modelo sin reentrenamiento, con ajuste fino por evento y con calibración de probabilidades, reportando F1 por clase con intervalos de confianza de 95 % y cinco repeticiones. El resultado mostraría cuánto de la cifra de 0,93 se mantiene fuera de las fuentes de entrenamiento, y si la clase moderada puede mejorarse con aumento de datos o con un criterio de decisión que priorice el recall de daño moderado y severo.
2. De los mapas de daño a la reapertura de empresas: combinar la clasificación de daño de los edificios con el registro de actividades económicas de un distrito de ejemplo y estimar, en un simulacro con 100 edificios, el tiempo hasta la primera inspección de los edificios comerciales cuando se prioriza por nivel de daño y número de empresas frente a un recorrido manual. Se mediría el tiempo ahorrado, el número de empresas que pueden reabrir antes y los errores de clasificación que desvían recursos, información para decidir si la evaluación automática se justifica para las autoridades y para las cámaras de comercio.

**Relaciones poco exploradas.**

1. Evaluación de daño en el borde (complementa) D060 y D086: D060 clasifica la intensidad sísmica en el borde y D086 usa inteligencia de borde para clasificar anomalías en monitoreo estructural inalámbrico; D076 aporta la clasificación visual de daño en edificios con un modelo ligero.
2. Revisiones de UAV e IoT (se relaciona con) D050 y D056: las revisiones D050 y D056 discuten UAV e IoT en gestión de desastres sin recuperación empresarial; D076 ofrece un caso concreto con resultados cuantitativos y un despliegue en hardware barato.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Aporta una evaluación comparada de seis modelos ligeros para clasificar tres niveles de daño posterremoto, con F1 ponderado de 0,93, 61,6 millones de operaciones, 6,29 MB y una prueba de despliegue en Raspberry Pi 5 (3,21 cuadros por segundo). Su valor para el corpus es moderado porque las imágenes no son aéreas, las etiquetas se asistieron con el propio modelo, 85 % de los datos son de daño severo, el desempeño en conjuntos independientes baja a 0,65 de F1 y 0,73 de exactitud, y no hay vínculo con la recuperación empresarial, pero ilustra la evaluación rápida de daño en el borde.

**Conexiones inter-documentales.**

- **COMPLEMENTA** D042 (IoT y UAV en la gestión de desastres sísmicos (revisión)): D076 clasifica daño posterremoto en imágenes de UAV con aprendizaje profundo ligero y D042 revisa IoT y UAV en la gestión del terremoto [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 59 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Circularidad en el etiquetado (El modelo asistió en clasificar el 70 % de las imágenes que luego se usan para evaluarlo (Sec. 4.1, p. 10)); Dominio no coincidente (Se presenta como solución para UAV con imágenes de redes sociales y escenas (Resumen, p. 1; Sec. 4.1, p. 8-9)); Tiempo real asumido (Se califica de tiempo real una velocidad de 3,21 cuadros por segundo con imágenes del conjunto (Sec. 6, p. 20))
- **Bradford-Hill:** No aplica: es un estudio computacional; no se estima causalidad con datos observacionales.
- **TRL asignado:** 4 — 'It was successfully deployed and tested on a Raspberry Pi 5, demonstrating its feasibility for edge-device applications' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (23 páginas). Los conteos de la Tabla 1 se leyeron con filas y columnas desordenadas y no coinciden con las descripciones de los conjuntos del texto; se citan solo los totales de las Tablas 3 y 5. La reducción de 59,5 % de operaciones frente a ShuffleNetV2 la calculó el analista con la Tabla 7. Las páginas siguen los marcadores del PDF. La conclusión del texto reitera la reducción de 58,8 % frente al modelo de referencia con menos operaciones y menciona mejoras de exactitud de 3,20 % a 18,90 % y un reentrenamiento en una tarea de clasificación de desastres naturales sin detalles.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un modelo MobileNetV3-Small con transferencia de aprendizaje y ajuste fino de las últimas cinco capas clasifica tres niveles de daño posterremoto con un F1 ponderado de 0,93, supera a cinco modelos ligeros de referencia con solo 61,6 millones de operaciones de coma flotante y 6,29 MB, y se ejecuta en una Raspberry Pi 5 a 3,21 cuadros por segundo, lo que permite una evaluación de daño en el borde para orientar a los equipos de búsqueda y rescate.  | El desempeño de 0,93 se obtiene sobre un conjunto fusionado en el que 85 % de las imágenes son severas, cuyas etiquetas se refinaron con el propio modelo, y baja a 0,65 de F1 y 0,73 de exactitud en conjuntos independientes, lo que indica dependencia de la fuente y no capacidad general. Las imágenes no son aéreas ni de UAV, de manera que el título y la motivación no se contrastan con el escenario declarado. La clase moderada, la más útil para priorizar inspecciones, obtiene un F1 de 0,62. La prueba de despliegue mide 3,21 cuadros por segundo con imágenes del conjunto, sin vuelo ni energía, y modelos más simples son más rápidos. El resultado no se conecta con decisiones de reocupación, tiempos de inspección ni actividad económica.  | La contribución sostenible es una comparación reproducible de modelos ligeros para clasificar daño visible en imágenes, con una línea base de eficiencia en una computadora de placa única y una evidencia clara de la dificultad de la clase intermedia. Para el corpus, importa por mostrar que la evaluación visual automática de daño puede ejecutarse en el borde con hardware barato y por su relación con la rapidez de inspección, un insumo de la recuperación. No obstante, el desempeño informado depende de un conjunto desbalanceado y parcialmente etiquetado por el propio modelo, y su utilidad para la recuperación empresarial exige validación con imágenes aéreas de campañas reales, división por evento y conexión con los tiempos de inspección y de reapertura.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Nivel de daño' es una de tres categorías visuales (menor, moderado o severo); 'ajuste fino' es continuar el entrenamiento de las últimas capas de un modelo preentrenado; 'FLOPs' son operaciones de coma flotante por inferencia; 'F1 ponderado' promedia el F1 de cada clase según su número de imágenes.
- **P2 Supuestos:** Supone que imágenes de redes sociales y de escenas representan el vuelo de un UAV, que las etiquetas asistidas por el modelo son correctas, que 3,21 cuadros por segundo es tiempo real y que el daño visible indica el daño estructural.
- **P3 Evidencia:** La evidencia son 1024 imágenes de prueba de un conjunto de 10 243, cinco corridas de entrenamiento, comparaciones con cinco modelos y dos estudios previos, y una prueba de velocidad en una Raspberry Pi 5.
- **P4 Consecuencias:** Si es cierto, los equipos de rescate pueden priorizar con clasificación en el borde; si es falso, el modelo puede subestimar el daño moderado y fallar con imágenes aéreas reales, lo que desvía recursos.
- **P5 Contraejemplos:** No se examinan imágenes aéreas reales, división por evento, vuelo, energía, geolocalización ni decisiones de reocupación.
- **P6 Alternativas:** Alternativas: que un modelo de segmentación o detección dé información más útil que la clasificación por imagen; que una inspección híbrida con muestreo sea más confiable; que el cuello de botella sea el vuelo y la logística y no la clasificación.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| F1 ponderado del modelo con ajuste fino | 0,93 | índice | Exactitud también de 0,93; cinco corridas | Tabla 5, p. 14 | Tabla | Media | Conjunto fusionado de 10 243 imágenes |
| F1 de la clase moderada | 0,62 | índice | Precisión de 0,60 y recall de 0,64 | Tabla 5, p. 14 | Tabla | Alta | 953 imágenes |
| Proporción de imágenes de daño severo en el conjunto final | 85 | % | 8718 de 10 243 imágenes | Tabla 3, p. 11 | Tabla | Alta | Desbalance |
| Operaciones de coma flotante del modelo | 61,6 | millones | MobileNetV3 sin ajuste fino: 61,5 millones | Tabla 7, p. 18 | Tabla | Alta | Menor que ShuffleNetV2 con 151,7 millones |
| Parámetros y tamaño del modelo | 1,65 y 6,29 | millones y MB | SqueezeNet con 0,70 millones | Tabla 7, p. 18 | Tabla | Alta | Modelo ligero |
| Cuadros por segundo en Raspberry Pi 5 | 3,21 | cuadros/s | 0,3117 s por imagen; SqueezeNet con 5,11 cuadros/s | Tabla 10, p. 20 | Tabla | Media | Imágenes del conjunto, sin vuelo |
| Exactitud sobre el conjunto de Ünlü et al. | 0,73 frente a 0,66 | índice | Modelo propio frente a VGG19 | Tabla 9, p. 19 | Tabla | Media | Mucho menor que 0,93 |
| F1 ponderado sobre Disaster Scenes Database | 0,65 frente a 0,63 | índice | Modelo propio frente a Faster R-CNN con ResNet-50 | Tabla 8, p. 18 | Tabla | Media | Tareas distintas |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'It was successfully deployed and tested on a Raspberry Pi 5, demonstrating its feasibility for edge-device applications' (p. 1) | Validación de componentes en laboratorio con imágenes de bases públicas y despliegue en hardware embebido; sin pruebas en vuelo. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'Traditional post-earthquake damage assessment methods involve manual inspection, which is time-consuming, resource-intensive, and hazardous in severely affected areas' (p. 1) | Se plantea la ventaja frente a la inspección manual; sin costos, clientes ni modelo de negocio. |
| IRL | 3 | Sí | 'a camera module was connected to the Raspberry Pi, enabling the capture of real-time images, which were subsequently processed by the model for classification' (p. 19) | Integración de cámara, placa y modelo probada en laboratorio; sin integración con un UAV ni con una estación de control. |
| DRL | 2 | Sí | 'This allows operators to monitor the situation in real time and receive alerts if severe damage is detected' (p. 2) | Se describe el uso previsto por operadores de emergencia; sin estudio de usuarios. |
| SRL | 1.17 | Sí | Componentes: Modelo ligero de clasificación de daño (TRL 4), Plataforma embebida con cámara (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 10.5; ÷9 → 1.17; nivel acotado a [1,9] = 1.17 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 4 con BRL 1 e IRL 3: modelo y hardware probados por separado con imágenes no aéreas, sin vuelo, sin energía y sin costos. · Estrategia de salida: Imágenes aéreas por evento, pruebas en vuelo, calibración de probabilidades y conexión con decisiones de inspección.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Circularidad en el etiquetado | El modelo asistió en clasificar el 70 % de las imágenes que luego se usan para evaluarlo (Sec. 4.1, p. 10) | Las etiquetas pueden reflejar el sesgo del modelo |
| Dominio no coincidente | Se presenta como solución para UAV con imágenes de redes sociales y escenas (Resumen, p. 1; Sec. 4.1, p. 8-9) | El desempeño aéreo no se mide |
| Tiempo real asumido | Se califica de tiempo real una velocidad de 3,21 cuadros por segundo con imágenes del conjunto (Sec. 6, p. 20) | No se prueba en vuelo ni con restricciones de energía |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Ajuste fino de cinco capas → mejor F1 ponderado | Comparación con el ajuste solo del clasificador (0,93 frente a 0,89) | Mecanismo de adaptación al dominio | Comparación en conjuntos independientes | Fuga de etiquetas, desbalance | 3 | Efecto plausible en el conjunto fusionado |
| Clasificación en el borde → priorización más rápida de rescate | Argumento de la introducción | Mecanismo supuesto | Simulacros con tiempos de inspección | Logística, comunicaciones, calidad de las imágenes | 1 | Relación no sustentada con datos |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | División por evento y por sitio, etiquetas independientes del modelo y reportes con intervalos de confianza | Crítico | Media | 9 |
| Tecnológico | Imágenes aéreas reales, pruebas en vuelo y consumo de energía | Crítico | Media | 8 |
| Conocimiento | Relación entre el nivel de daño visible y el tiempo de reocupación y de reapertura de empresas | Crítico | Alta | 9 |
| Mercado | Costos de la operación y adopción por autoridades de emergencia | Significativo | Media | 6 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Escenario de aplicación de clasificación de daño con UAV y modelos ligeros | Esquema | Vuelo, procesamiento a bordo y estación de control | No aplica | Media |
| Fig. 4 | Matriz de confusión del modelo adaptado | Matriz | Confusión entre clases menor y moderada | 0,93 de exactitud | Alta |
| Fig. 6 | Curvas ROC y AUC por clase | Gráfico | AUC de 0,99 (menor), 0,91-0,93 (moderado), 0,97 (severo) | 0,91-0,99 | Media |
| Tabla 6 | Métricas de exactitud del modelo y de los modelos de referencia | Tabla | F1 ponderado de 0,85 a 0,90 frente a 0,93 | 0,93 | Alta |
| Tabla 10 | Cuadros por segundo y tiempo de inferencia en Raspberry Pi 5 | Tabla | 3,21 cuadros por segundo | 3,21 | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| EmergencyNet para clasificación de escenas de emergencia | No especificado en documento | Academia | Clasificación rápida en dispositivos de bajo costo | 6,11 cuadros por segundo | F1 ponderado de 0,87 en este conjunto | Estable |
| Modelos YOLO para daño en edificios (YOLOv5s-Seg, DB-YOLOv5, YOLOv6s-GRE) | China | Academia | Segmentación y detección de daño con UAV | Localización de daño | Mayor complejidad según los autores | Creciente |
| VGG19, VGG16 y NASNet para daño posterremoto (Ünlü et al.) | No especificado en documento | Academia | Clasificación de edificios dañados y normales | Referencia previa | Modelo de 139,6 millones de parámetros | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** F1 ponderado, exactitud, FLOPs y cuadros por segundo
- **X:** Modelo (MobileNetV3 con ajuste fino frente a modelos de referencia) y estrategia de ajuste
- **Z (controles):** Fuente de datos, desbalance de clases, tamaño de entrada, hardware
- **Datos:** 10 243 imágenes de tres bases públicas con etiquetas refinadas; 1024 para prueba
- **Método:** Clasificación supervisada con transferencia de aprendizaje y cinco corridas
- **Efecto reportado:** F1 ponderado de 0,93 frente a 0,85-0,90 de modelos de referencia
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Cinco corridas sin intervalos; comparación en conjuntos independientes con F1 de 0,65 y exactitud de 0,73

| Vacío | Tipo | Descripción |
|---|---|---|
| V-076-01 | TERR | Imágenes de eventos diversos sin país específico; autores en Arabia Saudita |
| V-076-02 | POBL | Edificios dañados en imágenes; sin ocupantes ni empresas |
| V-076-03 | TEMP | Imágenes posteriores a eventos sin evolución temporal; inferencia de 0,3 s por imagen |
| V-076-04 | MET | Conjunto fusionado con etiquetas asistidas por el modelo y 85 % de una clase |
| V-076-05 | VAR | Faltan imágenes aéreas, energía, costos, geolocalización y tiempos de inspección |
| V-076-06 | TEOR | Aprendizaje profundo y evaluación de daño; sin teoría de recuperación |
| V-076-07 | CAUS | Efecto de la clasificación sobre la rapidez de rescate o de reapertura sin evidencia |
