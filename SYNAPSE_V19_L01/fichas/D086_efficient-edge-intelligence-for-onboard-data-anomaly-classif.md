# FB-L01-086 | D086 — Efficient edge intelligence for onboard data anomaly classification in wireless structural health monitoring using knowledge distillation on low-cost IoT nodes

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/yu-et-al-2025-efficient-edge-intelligence-for-onboard-data-anomaly-classification-in-wireless-structural-health.pdf` · 20 páginas · Relevancia para el eje del corpus: **Adyacente** (Desarrolla y prueba un clasificador de anomalías de datos que corre en un nodo IoT de bajo costo (LiftNode) para monitoreo estructural inalámbrico; es tecnología de sensado e inteligencia en el borde aplicable a infraestructura, pero no estudia sismos, empresas ni recuperación productiva.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-086 / D086
- **Tipo de recurso:** Artículo científico (investigación aplicada, journal peer-reviewed)
- **Referencia APA 7:** Yu, X., Zhao, Y., Cui, S., He, X., Fu, Y., & Yang, Q. (2025). Efficient edge intelligence for onboard data anomaly classification in wireless structural health monitoring using knowledge distillation on low-cost IoT nodes. *Structural Health Monitoring*, Article 14759217251349533. https://doi.org/10.1177/14759217251349533
- **Autores:** Yu, Xiao (58817077400); Zhao, Yuqing (60032620500); Cui, Shuaiwen (57218711499); He, Xinhao (57221284231); Fu, Yuguang (57191156904); Yang, Qun (60032620600)
- **Afiliaciones:** School of Civil and Environmental Engineering, Nanyang Technological University, Singapore, Singapore; College of Computing and Data Science, Nanyang Technological University, Singapore, Singapore; Graduate School of Engineering, Tohoku University, Sendai, Japan; Department of Civil and Environmental Engineering, The University of Auckland, Auckland, New Zealand
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Structural Health Monitoring
- **Identificador persistente:** DOI 10.1177/14759217251349533 · ISSN 14759217
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105012747278&doi=10.1177%2f14759217251349533&partnerID=40&md5=d972c1bc039eff8e73de04a82badcfd2
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 9

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Proponer un enfoque descentralizado que integra aprendizaje automático y computación en el borde para clasificar anomalías de datos directamente en nodos IoT de bajo costo de redes inalámbricas de monitoreo de salud estructural (SHM). El estudio busca dos resultados: un extractor de características y clasificador pequeño, obtenido por destilación de conocimiento desde un modelo maestro, y un marco de despliegue que compile y ejecute el modelo en microcontroladores con memoria y energía limitadas, con precisión comparable a la de un computador.

**Pregunta de investigación.** [INFERIDA] ¿Puede un modelo de aprendizaje profundo destilado clasificar siete tipos de datos de aceleración de un puente en un microcontrolador de bajo costo con una precisión similar a la de un modelo grande ejecutado en computador, sin enviar los datos brutos a una estación central?

**Marco teórico.** El marco combina tres líneas de literatura: la detección de anomalías en datos de SHM (métodos estadísticos, aprendizaje no supervisado y supervisado, redes convolucionales y autocodificadores), la computación en el borde como esquema descentralizado frente al procesamiento centralizado en estaciones de trabajo o nube, y la destilación de conocimiento basada en respuesta con etiquetas duras y blandas. Contrasta los nodos basados en computadores de placa única (Raspberry Pi, Jetson) con los basados en microcontroladores (MCU), y sostiene que estos últimos son los adecuados para despliegues extensos con baterías. No formula una teoría nueva; adapta el codificador transformador sin codificación posicional y con normalización por lotes, y usa las herramientas STM32Cube.AI y X-CUBE-AI para el despliegue.

**Metodología.** El diseño es experimental con datos secundarios. Usa un conjunto de datos de un puente atirantado de gran luz en China, proporcionado por la comunidad IPC-SHM: aceleraciones de 38 acelerómetros durante 31 días a 20 Hz, organizadas en series de una hora con 72 000 puntos cada una (28 272 instancias) y siete clases (normal y seis anomalías: faltante, mínima, valor atípico, cuadrada, tendencia y deriva). Para corregir el desbalance, reduce todas las clases al tamaño de la minoritaria (523 muestras de valores atípicos), lo que deja 3 661 muestras, que divide en entrenamiento, validación y prueba en proporción 7:1,5:1,5. Extrae tres estadísticos (media, rango y desviación estándar) e histogramas, normaliza a [−1, 1] y procesa los vectores de 1 024 dimensiones con un codificador transformador seguido de un clasificador de capas de 64 y 32 neuronas. Entrena el modelo maestro (EECM) con búsqueda en rejilla y parada temprana, y destila un modelo estudiante (DLCM) con pérdida combinada de entropía cruzada y divergencia de Kullback-Leibler. Convierte el modelo a ONNX, lo evalúa en la nube de desarrolladores de STM32 y lo carga en el nodo LiftNode (STM32 Cortex-M de hasta 480 MHz), donde mide precisión, tiempo de inferencia y memoria con las 550 muestras de prueba. Compara con un modelo base (BCM) sin destilación y con dos estudios previos.

**Resultados principales.** El modelo maestro EECM alcanza 96,4 % de precisión en la prueba y un tamaño de 17,31 M; el modelo base BCM llega a 93,6 % y el estudiante destilado DLCM a 96,36 %, con 69 711 parámetros en el modelo de Python y 68 112 en los modelos en C. En el nodo LiftNode, el DLCM mantiene 96,36 % de precisión con 296,9 KB de memoria flash de 1 MB y 4,25 KB de RAM de 340 KB. El tiempo de inferencia de las 550 muestras es 339,35 s en el microcontrolador (0,62 s por muestra según el texto) frente a 3,55 s en la simulación x86 y 0,61 s en Python. El modelo maestro supera 98 % en todas las clases salvo los valores atípicos, categoría que el texto atribuye a similitud de distribución con la clase mínima y a posible error de etiquetado manual. La comparación con trabajos previos muestra que el modelo propuesto es menor que el más pequeño reportado por Mondal et al. (0,7 MB) y más preciso que el de Chou et al. (93,3 %). El artículo reconoce que el marco no admite modelos con gran huella de memoria ni formas dinámicas de tensores.

**Discusión y contribución.** Los autores interpretan que la destilación permite trasladar al nodo un modelo con precisión cercana a la del maestro y con menor tamaño, y que usar características estadísticas e histogramas de series unidimensionales evita la carga de memoria de las representaciones en imagen (por ejemplo, 147 KB para una imagen de 224 por 224 frente a 4 KB del vector de entrada). Sostienen que la solución es adecuada para despliegues masivos de bajo costo en infraestructura civil y que corrige la dependencia de computadores de placa única que requieren alimentación de red. Dejan sin discutir tres puntos: la validez externa de un solo puente y un solo conjunto de datos, el efecto de reducir las clases a 523 muestras sobre la prevalencia real de anomalías y el desempeño en campo, ya que las pruebas en el nodo parecen usar muestras almacenadas. El texto contiene además inconsistencias de unidades en tiempos de inferencia, en la tabla y el cuerpo.

**Limitaciones declaradas.** No se declara una sección de limitaciones. Reconoce que el marco de despliegue no maneja modelos con huellas de memoria grandes ni formas dinámicas de tensores (p. 12), y que la clase de valores atípicos pudo verse afectada por errores de etiquetado manual (p. 15).

**Trabajo futuro.** Evaluar la escalabilidad del método en diversos escenarios y la interoperabilidad con redes de sensores heterogéneas; realizar evaluaciones de largo plazo de confiabilidad, robustez y eficiencia de ciclo de vida en entornos reales; desarrollar diagnóstico de fallas de sensor a bordo para rastrear las causas de las anomalías y diseñar estrategias de recuperación (p. 19).

**Palabras clave.** Declaradas: data anomaly classification; Edge intelligence; knowledge distillation; structural health monitoring; wireless internet of things | Inferidas: inteligencia en el borde, destilación de conocimiento, nodo IoT, microcontrolador, anomalías de datos, monitoreo estructural, transformador, STM32, clasificación de series de tiempo, puente atirantado

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** La destilación de conocimiento permite ejecutar en un microcontrolador de bajo costo un clasificador de siete tipos de anomalías de datos de aceleración con 96,36 % de precisión, similar a la de un modelo maestro de 17,31 M, y sin transmitir los datos brutos a una estación central.

**Antítesis identificada.** La evidencia procede de un único conjunto de datos de un solo puente con 38 sensores y 31 días, reducido por submuestreo a 3 661 muestras de las 28 272 originales, lo que altera la prevalencia real de anomalías: en operación la clase normal domina y la precisión equilibrada de 96 % no permite inferir tasas de falsas alarmas. Los modelos se comparan sobre una partición de prueba, sin intervalos de confianza reportados, y la diferencia de 0,04 puntos entre el DLCM y el EECM carece de prueba de significancia. El tiempo de inferencia en el nodo es de 0,62 s por muestra, a lo que se suma el almacenamiento temporal de 72 000 puntos para calcular los vectores de características; el artículo no mide consumo de energía en el nodo, y esto es el criterio que justifica el uso de microcontroladores. La declaración de ser el primero en lograr clasificación a bordo con nodos de bajo costo no se sustenta con una revisión sistemática. Además, la prueba en el nodo parece usar muestras almacenadas, no datos en operación continua.

**Síntesis propuesta.** El trabajo demuestra la factibilidad técnica de ejecutar un clasificador pequeño en un microcontrolador y aporta un procedimiento replicable de conversión a ONNX y despliegue con herramientas del fabricante, lo que cierra una brecha entre el entrenamiento en computador y el sensor. Su alcance es el de una prueba de concepto de laboratorio con datos reales, no el de un sistema validado en campo. Para el corpus de recuperación productiva, el resultado sugiere que la calidad de los datos en la capa de sensores puede garantizarse a bajo costo, lo que fortalece la cadena de datos de gemelos digitales; la síntesis propone evaluar el sistema con tasas realistas de anomalías, energía medida y operación continua, y vincular la calidad del dato con decisiones de reapertura tras un evento sísmico.

**Áreas grises detectadas.**

1. Validez externa: el modelo se entrena y prueba con datos de un solo puente (38 acelerómetros, 31 días) y se afirma idoneidad para infraestructura civil en general; el texto no prueba transferencia a otros puentes, sensores o tipos de anomalía, y no informa si las particiones separan sensores o días, lo que podría permitir fuga de información entre entrenamiento y prueba.
2. Prevalencia y falsas alarmas: el conjunto se reduce a 523 muestras por clase (3 661 en total) y se reporta precisión global de 96 %; en operación real las anomalías son raras y el costo de falsos positivos sobre una clase normal dominante no se estima, de modo que la utilidad de campo no puede deducirse de las métricas presentadas.
3. Inconsistencias en la medición del tiempo de inferencia: el texto reporta 0,61 ms y 0,61 s para 550 muestras en Python, 0,07 ms por muestra en x86 y 0,62 s por muestra en el microcontrolador, mientras que la tabla indica 0,011 ms, 0,065 ms y 6,17 ms; el cociente de la tabla no coincide con los totales, y esto impide establecer la latencia real del nodo.
4. Energía y operación continua no medidas: el argumento central a favor de los microcontroladores es el bajo consumo y la operación con baterías, pero el artículo no reporta consumo del nodo, vida de batería ni comportamiento en campo; la prueba 'bajo condiciones operativas reales' no describe el procedimiento ni la fuente de las muestras.

**Puntos oscuros aclarados.** El artículo atribuye la mejora del estudiante sobre el modelo base (93,6 % frente a 96,36 %) a la destilación, pero no aísla esa causa: el BCM y el DLCM difieren en arquitectura, y el texto no reporta intervalos ni repeticiones. Una ablación (estudiante con la misma arquitectura, entrenado solo con etiquetas duras) determinaría si la ganancia proviene de la transferencia de conocimiento o de otros ajustes. Además, el estudiante conserva la precisión del maestro con 69 711 parámetros frente a un maestro de 17,31 M (unidad no precisada), un resultado que sugiere que el problema de clasificación es fácil con las características elegidas y que gran parte de la capacidad del maestro es innecesaria; en tal caso, un clasificador clásico de bajo costo (árboles o bosques aleatorios) podría igualar el resultado sin destilación, hipótesis que no se contrasta. Por último, el texto propone separar las anomalías de los eventos estructurales, pero no examina si el clasificador confunde un evento real, como un sismo, con una anomalía de sensor y descarta datos valiosos, riesgo crítico para la recuperación posterior a un desastre.

**Ideas propositivas novedosas.**

1. Validación con tasas realistas y datos de varios puentes: evaluar el DLCM en conjuntos de datos de al menos tres estructuras, con particiones por sensor y por día, sin submuestreo de la clase normal, y reportar precisión, sensibilidad por clase, falsas alarmas por semana y matrices de confusión con intervalos de confianza por remuestreo. Fundamento: el estudio usa un solo puente y una clase normal reducida de unas 12 000 a 523 muestras. Verificabilidad: los conjuntos de datos del IPC-SHM y de otros puentes permiten réplica y comparación con el BCM y con clasificadores clásicos. Utilidad: define si el nodo puede operar sin intervención humana y cuántas falsas alarmas genera, requisito para que un gestor de infraestructura o una empresa incorpore la calidad del dato en su continuidad operativa.
2. Protocolo de calidad del dato ante eventos extremos: construir un conjunto de prueba con registros de sismos reales o simulados en que la respuesta estructural sea grande y comprobar si el clasificador la rotula como anomalía de sensor (valor atípico, tendencia o deriva). Fundamento: el texto no examina la confusión entre eventos estructurales y fallas de sensor. Verificabilidad: tablas vibratorias, registros sísmicos públicos y la misma arquitectura del nodo permiten medir la tasa de descarte erróneo. Utilidad: protege la cadena de datos de un gemelo digital durante la emergencia y establece una condición mínima para usar inteligencia en el borde en infraestructura sísmicamente expuesta, donde descartar datos válidos retrasa la evaluación de daños y la reapertura de operaciones.

**Relaciones poco exploradas.**

1. Destilación de conocimiento (reduce) el tamaño del modelo desde 17,31 M (unidad no precisada) hasta 296,9 KB de memoria flash, con una pérdida de precisión de 0,04 puntos en la partición evaluada; la relación causal con la destilación no se aísla de otros cambios de arquitectura.
2. Procesamiento en el borde (reduce) la carga de transmisión de datos brutos y la latencia hacia la estación central, según el argumento del texto, aunque la latencia medida en el nodo es de 0,62 s por muestra y no se compara con el esquema centralizado.

**Robustez argumentativa:** 4.2/10 (ponderación 30/30/25/15) — consistencia lógica 5/10; calidad de la evidencia 4/10; validez de inferencias causales 4/10; generalizabilidad 3/10.

**Valor estratégico:** 4/10 — Aporta un procedimiento replicable para desplegar clasificadores en microcontroladores de bajo costo (conversión a ONNX, evaluación en la nube de STM32, generación de proyecto y prueba en la placa) y un caso con 296,9 KB de memoria flash y 4,25 KB de RAM. Es tecnología adyacente al corpus, pues fortalece la calidad del dato en capas de sensado de gemelos digitales, pero no mide energía, costos ni operación en campo ni considera eventos sísmicos.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Generalización apresurada ('ideal for large-scale cost-effective structural health monitoring applications' a partir de un puente y 550 muestras (Conclusión, p. 18)); Falsa causa (post hoc) (Atribuye la mejora de 93,6 % a 96,36 % a la destilación sin ablación (p. 15)); Afirmación de primicia no verificada ('none of the existing studies have successfully implemented and achieved promising results' (p. 3))
- **Bradford-Hill:** No aplica: el estudio compara arquitecturas de modelos y no estima relaciones causales sobre resultados de interés; la atribución de la mejora a la destilación no se aísla con ablaciones ni repeticiones.
- **TRL asignado:** 4 — 'Finally, the model is tested on the computing board of LiftNode under actual operating conditions to ensure it performs as expected in the real world' (p. 12)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (20 páginas de la revista, con marcadores del PDF). Ecuaciones y Tabla 1 se extrajeron con símbolos degradados. Inconsistencias señaladas: tiempos de inferencia (0,61 ms y 0,61 s en Python; 0,07 ms frente a 0,065 ms en x86; 0,62 s frente a 6,17 ms en STM32), unidad del tamaño del maestro ('17.31 M'), y 0,29 MB del resumen frente a 296,9 KB de memoria flash.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| La destilación de conocimiento permite ejecutar en un microcontrolador de bajo costo un clasificador de siete tipos de anomalías de datos de aceleración con 96,36 % de precisión, similar a la de un modelo maestro de 17,31 M, y sin transmitir los datos brutos a una estación central.  | La evidencia procede de un único conjunto de datos de un solo puente con 38 sensores y 31 días, reducido por submuestreo a 3 661 muestras de las 28 272 originales, lo que altera la prevalencia real de anomalías: en operación la clase normal domina y la precisión equilibrada de 96 % no permite inferir tasas de falsas alarmas. Los modelos se comparan sobre una partición de prueba, sin intervalos de confianza reportados, y la diferencia de 0,04 puntos entre el DLCM y el EECM carece de prueba de significancia. El tiempo de inferencia en el nodo es de 0,62 s por muestra, a lo que se suma el almacenamiento temporal de 72 000 puntos para calcular los vectores de características; el artículo no mide consumo de energía en el nodo, y esto es el criterio que justifica el uso de microcontroladores. La declaración de ser el primero en lograr clasificación a bordo con nodos de bajo costo no se sustenta con una revisión sistemática. Además, la prueba en el nodo parece usar muestras almacenadas, no datos en operación continua.  | El trabajo demuestra la factibilidad técnica de ejecutar un clasificador pequeño en un microcontrolador y aporta un procedimiento replicable de conversión a ONNX y despliegue con herramientas del fabricante, lo que cierra una brecha entre el entrenamiento en computador y el sensor. Su alcance es el de una prueba de concepto de laboratorio con datos reales, no el de un sistema validado en campo. Para el corpus de recuperación productiva, el resultado sugiere que la calidad de los datos en la capa de sensores puede garantizarse a bajo costo, lo que fortalece la cadena de datos de gemelos digitales; la síntesis propone evaluar el sistema con tasas realistas de anomalías, energía medida y operación continua, y vincular la calidad del dato con decisiones de reapertura tras un evento sísmico.  | 4.2/10 |

### B.2 Interrogación socrática

- **P1 Definición:** Define 'inteligencia en el borde' como ejecución de modelos de aprendizaje automático en el nodo IoT y 'anomalía de datos' mediante siete clases etiquetadas manualmente en el conjunto del IPC-SHM.
- **P2 Supuestos:** Supone que la precisión sobre una partición balanceada refleja el desempeño en operación, que las muestras de prueba representan los datos que llegan en continuo y que las etiquetas manuales son correctas.
- **P3 Evidencia:** La evidencia es de laboratorio con un conjunto de datos de un puente: 96,36 % de precisión del DLCM, 550 muestras de prueba, 296,9 KB de flash y 4,25 KB de RAM; sin repeticiones ni medición de energía.
- **P4 Consecuencias:** Si es cierto, las redes de SHM podrían filtrar y clasificar datos en el sensor y transmitir menos; si es falso, se arriesga descartar datos válidos o producir falsas alarmas en una clase normal dominante.
- **P5 Contraejemplos:** No se examinan otros puentes, sensores de menor calidad, eventos sísmicos que se parezcan a anomalías ni un clasificador clásico de referencia.
- **P6 Alternativas:** Hipótesis rivales: la alta precisión se debe a que las clases son fáciles de separar con estadísticos e histogramas; la ganancia atribuida a la destilación proviene de diferencias de arquitectura y no de la transferencia de conocimiento.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Precisión del DLCM en computador | 96,37 | % | Python, 550 muestras de prueba | Resumen, p. 1; Tabla 1, p. 17 | Texto | Media | Una sola partición, sin intervalos |
| Precisión del DLCM en el nodo LiftNode | 96,36 | % | Microcontrolador STM32, 550 muestras | Resumen, p. 1; p. 16 | Texto | Media | Muestras almacenadas; no operación continua |
| Precisión del modelo maestro EECM | 96,4 | % | Prueba con transformador | p. 15 | Texto | Media | Misma partición |
| Precisión del modelo base BCM | 93,6 | % | Sin destilación | p. 15 | Texto | Media | Arquitectura distinta al DLCM |
| Tamaño del modelo en memoria flash | 296,9 | KB | De 1 MB disponible en LiftNode | p. 17 | Texto | Alta | El resumen reporta 0,29 MB |
| Uso de RAM en el nodo | 4,25 | KB | De 340 KB disponibles | p. 17 | Texto | Alta | No incluye búfer de 72 000 puntos |
| Tamaño del modelo maestro | 17,31 | M | Unidad no precisada en el texto | p. 14 | Texto | Baja | Unidad ambigua (parámetros o MB) |
| Parámetros del DLCM (Python / C) | 69 711 / 68 112 | parámetros | Tabla 1 | Tabla 1, p. 17 | Tabla | Alta | Diferencia de 1 599 sin explicación |
| Tiempo de inferencia de 550 muestras en el nodo | 339,35 | s | 0,62 s por muestra según el texto | p. 16 | Texto | Media | La tabla reporta 6,17 ms por muestra |
| Muestras del conjunto balanceado | 3 661 | muestras | 523 por clase | p. 13 | Texto | Alta | Reducción desde 28 272 instancias |
| Instancias originales del conjunto | 28 272 | instancias | 38 acelerómetros × 31 días × 24 horas | p. 12 | Texto | Alta | Un solo puente |
| Frecuencia de muestreo | 20 | Hz | 72 000 puntos por serie de una hora | p. 12 | Texto | Alta | Datos de aceleración |
| Consumo de energía del nodo | No especificado en documento | N/A | Argumento de bajo consumo sin medición | Sec. Edge intelligence, pp. 8-12 | Texto | Baja | No se reporta energía ni vida de batería |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'Finally, the model is tested on the computing board of LiftNode under actual operating conditions to ensure it performs as expected in the real world' (p. 12) | Sistema (modelo y nodo) validado en laboratorio con datos reales de un puente; la prueba en la placa usa 550 muestras y no hay despliegue continuo en campo. |
| MRL | N/A | No | No aplica | Sin manufactura; LiftNode se describe como prototipo en desarrollo. |
| BRL | 1 | Sí | 'The proposed study offers the advantages of lower cost and higher energy efficiency' (p. 18) | Se afirma menor costo que los computadores de placa única sin cifras de costo ni modelo de negocio. |
| IRL | 4 | Sí | 'the DLCM, with its lightweight architecture, fits well within the memory limitations of the MCU-based resource-constrained IoT node' (p. 17) | Integración de extracción de características, modelo en C y microcontrolador comprobada en placa; sin sensores ni comunicación en el ciclo de prueba. |
| DRL | 2 | Sí | 'Thus, the timely detection and classification of these data anomalies are vital to safeguarding IoT networks from their detrimental effects' (p. 2) | Se identifica la necesidad técnica; sin estudio de adopción por operadores de infraestructura. |
| SRL | 1.78 | Sí | Componentes: Modelo destilado de clasificación de anomalías (DLCM) (TRL 4), Nodo IoT LiftNode con STM32 y X-CUBE-AI (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 16.0; ÷9 → 1.78; nivel acotado a [1,9] = 1.78 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 1 e IRL 4: prueba de concepto de laboratorio con datos de un puente y 550 muestras, sin energía medida, costos, operación continua ni piloto de campo. · Estrategia de salida: Piloto en campo con medición de energía, operación continua y comparación con la clasificación centralizada; análisis de costos del nodo.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Generalización apresurada | 'ideal for large-scale cost-effective structural health monitoring applications' a partir de un puente y 550 muestras (Conclusión, p. 18) | Sobreextiende la validez del resultado de laboratorio |
| Falsa causa (post hoc) | Atribuye la mejora de 93,6 % a 96,36 % a la destilación sin ablación (p. 15) | Confunde diferencias de arquitectura con efecto de la transferencia de conocimiento |
| Afirmación de primicia no verificada | 'none of the existing studies have successfully implemented and achieved promising results' (p. 3) | No hay revisión sistemática que respalde la afirmación |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Destilación de conocimiento → precisión del modelo estudiante | Comparación DLCM 96,36 % frente a BCM 93,6 % (p. 15) | Fuerza, plausibilidad | Experimento controlado, consistencia, especificidad | Diferencias de arquitectura, partición única | 2 | Correlacional |
| Cómputo en el borde → menor latencia y carga de transmisión | Argumento comparativo con el esquema centralizado (p. 8) | Plausibilidad | Medición directa, temporalidad, experimento | Capacidad de red, energía | 2 | Correlacional |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Tecnológico | Falta validación en campo con operación continua, medición de energía y datos de varios puentes | Crítico | Media | 8 |
| Metodológico | Ausencia de ablaciones, repeticiones e intervalos de confianza para atribuir la mejora a la destilación | Significativo | Alta | 6 |
| Conocimiento | Confusión entre eventos estructurales extremos y anomalías de sensor no evaluada | Crítico | Media | 8 |
| Mercado | Sin análisis de costos de nodos MCU frente a computadores de placa única ni de adopción por operadores | Significativo | Media | 6 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Figura 1 | Marco de desarrollo del modelo | Diagrama | Flujo de modelo maestro, destilación y despliegue | Esquema de proceso | Alta |
| Figura 11 | Matrices de confusión de DLCM, EECM y BCM | Matriz | Precisión por clase en la prueba | 96,36 %, 96,4 % y 93,6 % | Alta |
| Tabla 1 | Precisión y tiempo del DLCM en distintas plataformas | Tabla | Python, x86 y STM32 | Precisión 96,37 %, 96,36 % y 96,36 % | Media |
| Figura 14 | Precisión frente a tamaño del modelo entre modelos | Gráfico | Comparación con Mondal et al. y Chou et al. | Puntos por modelo | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Wang et al. (placa NVIDIA Xavier NX para detección de anomalías) | No especificado en documento | Academia | Inteligencia en el borde con computador de placa única | Recursos de cómputo amplios | Requiere energía de red y mayor costo | Estable |
| Mondal et al. (GoogLeNet comprimido, 0,7 MB) | No especificado en documento | Academia | Clasificación de anomalías con imágenes de tiempo-frecuencia | Alta precisión | Modelo mayor y pérdida de precisión al comprimir | Estable |
| Chou et al. (reconocimiento de patrones, 93,3 %) | No especificado en documento | Academia | Modelo de tamaño reducido | Tamaño pequeño | Precisión moderada | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Precisión de clasificación, tiempo de inferencia y uso de memoria
- **X:** Arquitectura del modelo (EECM, BCM, DLCM), destilación y plataforma (Python, x86, STM32)
- **Z (controles):** Particiones de datos, hiperparámetros, balanceo de clases
- **Datos:** Aceleraciones de 38 sensores de un puente atirantado chino durante 31 días; 3 661 muestras balanceadas
- **Método:** Entrenamiento supervisado con destilación de conocimiento y despliegue en microcontrolador
- **Efecto reportado:** Precisión del DLCM de 96,36 % frente a 93,6 % del BCM; memoria flash de 296,9 KB
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin repeticiones ni análisis estadístico; una partición

| Vacío | Tipo | Descripción |
|---|---|---|
| V-086-01 | TERR | Un puente en China; autores en Singapur, Japón y Nueva Zelanda; sin zonas sísmicas de América Latina |
| V-086-02 | POBL | Sin empresas, operadores ni usuarios del sistema |
| V-086-03 | TEMP | Datos de 31 días; sin monitoreo de largo plazo |
| V-086-04 | MET | Una partición, sin ablaciones ni repeticiones ni intervalos de confianza |
| V-086-05 | VAR | Faltan energía, vida de batería, costos, falsas alarmas y prevalencia real de anomalías |
| V-086-06 | TEOR | Aprendizaje automático y SHM; sin teoría de continuidad operativa |
| V-086-07 | CAUS | Efecto de la clasificación a bordo sobre decisiones de mantenimiento o reapertura sin evidencia |
