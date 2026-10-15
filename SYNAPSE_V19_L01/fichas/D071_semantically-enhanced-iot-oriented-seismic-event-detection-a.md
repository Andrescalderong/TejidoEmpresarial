# FB-L01-071 | D071 — Semantically Enhanced IoT-Oriented Seismic Event Detection: An Application to Colima and Vesuvius Volcanoes

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/Semantically_Enhanced_IoT-Oriented_Seismic_Event_Detection_An_Application_to_Colima_and_Vesuvius_Volcanoes.pdf` · 15 páginas · Relevancia para el eje del corpus: **Adyacente** (Presenta un marco orientado a IoT que recolecta señales sísmicas, las clasifica con redes neuronales (perceptrón multicapa y red convolucional) y las almacena en una base de conocimiento basada en una ontología propia (VEO) construida sobre SSN/SOSA, con datos de los volcanes Vesubio y Colima. Aporta interoperabilidad semántica y detección automática de eventos sísmicos, pertinentes para la alerta y la integración de datos de sensores, aunque los datos provienen de redes de observatorios y no de dispositivos IoT, el dominio es volcánico y no hay vínculo con edificios, empresas ni recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-071 / D071
- **Tipo de recurso:** Artículo científico (journal peer-reviewed)
- **Referencia APA 7:** Falanga, M., De Lauro, E., Petrosino, S., Rincon-Yanez, D., & Senatore, S. (2022). Semantically Enhanced IoT-Oriented Seismic Event Detection: An Application to Colima and Vesuvius Volcanoes. *IEEE Internet of Things Journal*, *9*(12), 9789-9803. https://doi.org/10.1109/JIOT.2022.3148786
- **Autores:** Falanga, Mariarosaria (57202696111); De Lauro, Enza (55996184700); Petrosino, Simona (6603151489); Rincon-Yanez, Diego (57205705016); Senatore, Sabrina (7003512928)
- **Afiliaciones:** University of Salerno, Department of Information and Electrical Engineering and Applied Mathematics, Fisciano, 84084, Italy; Universities and Research, Ministry of Education, Rome, 00153, Italy; Istituto Nazionale di Geofisica e Vulcanologia, Sezione di Napoli, Osservatorio Vesuviano, Naples, 80126, Italy
- **Fecha de publicación:** 2022
- **Fuente/contenedor:** IEEE Internet of Things Journal · vol. 9(12)
- **Identificador persistente:** DOI 10.1109/JIOT.2022.3148786 · ISSN 23274662
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85124207158&doi=10.1109%2fJIOT.2022.3148786&partnerID=40&md5=cabce966565890029cc114d73501b343
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 27

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Introducir un marco orientado a IoT que permita recolectar datos sísmicos, procesarlos y almacenarlos en una base de conocimiento, apoyado en una ontología denominada Volcano Event Ontology (VEO) que modela el dominio sísmico a partir de la ontología de redes de sensores SSN/SOSA. El marco incorpora un módulo de clasificación para detectar eventos volcano-tectónicos, de largo periodo, explosiones submarinas y voladuras de cantera, y permite consultar los eventos detectados por medio de SPARQL, con el propósito de facilitar la interoperabilidad de datos heterogéneos y apoyar la toma de decisiones en crisis volcánicas.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si una ontología puede integrar de forma homogénea datos de sensores sísmicos tradicionales y de dispositivos IoT, y si un perceptrón multicapa o una red convolucional unidimensional clasifican con alta exactitud los tipos de eventos sísmicos de los volcanes Vesubio y Colima.

**Marco teórico.** El marco combina el paradigma IoT, las tecnologías de la web semántica y el aprendizaje automático. Los autores sostienen que el IoT enfrenta heterogeneidad de dispositivos y metadatos incompletos, que las ontologías aportan interoperabilidad sintáctica y semántica, y que los sensores de bajo costo, como los acelerómetros MEMS y los teléfonos inteligentes (por ejemplo, MyShake), son una alternativa a los sismómetros costosos, en particular en países en desarrollo. Se revisan ontologías de dominio, ontologías volcánicas y trabajos de clasificación sísmica con redes neuronales, máquinas de vectores de soporte, agrupamiento, modelos ocultos de Markov y aprendizaje profundo en Vesubio, Stromboli, Etna, Colima y otros volcanes. La arquitectura tiene cuatro capas: adquisición de datos, modelado semántico, clasificación y recuperación de datos geofísicos.

**Metodología.** Los datos provienen de las redes de estaciones del Observatorio Vesubiano del INGV en el Vesubio (1999 a 2021) y de redes temporal y permanente en Colima (noviembre de 2005 a abril de 2006), remuestreadas a 100 Hz y normalizadas a ventanas de 2400 puntos (24 s). El conjunto tiene 4008 señales: 416 volcano-tectónicas, 464 voladuras, 363 de largo periodo del Vesubio y 2765 de largo periodo de Colima, más de 28 000 muestras de ruido, y se aumentó con inversión de polaridad. Se extrajeron características con codificación predictiva lineal. El perceptrón tiene una capa oculta de 42 neuronas, lote de 50, tasa de 0,001 y 640 iteraciones; la red convolucional tiene nueve bloques con filtros de 128, 128, 256 y 512, lote de 128 y 200 épocas con optimizador Adam. Los datos se dividieron 70:20:10 para entrenamiento, validación y prueba, y se reportaron precisión, exhaustividad y F1 macropromedio en ocho experimentos, de clasificación binaria, de cuatro clases y de seis clases. La ontología define clases de contexto, colección y conocimiento, incluidas veo:Event, veo:City y veo:AlertLevel.

**Resultados principales.** Los resultados indican que ambos clasificadores distinguen con exactitud las señales de ruido y de eventos en los experimentos binarios, que el desempeño baja ligeramente al aumentar el número de clases, y que en el experimento 8, que busca reconocer la firma del volcán (Vesubio, Colima y ruido), la red convolucional alcanza 0,98 de precisión, exhaustividad y F1. En el experimento 6, con todas las clases individuales, el modelo obtiene 93 % de F1, que los autores comparan con 93,5 % de exactitud con desviación de 0,50 de un trabajo sobre el volcán Ubinas con bosque aleatorio y máquinas de vectores en 109 609 eventos. Para el volcán Llaima, SeismicNet alcanza F1 de 91,75 % y 93,02 %. Los autores afirman que el desempeño de ambos modelos es siempre mayor de 90 % de F1 con señales sin transformar. El texto no incluye valores de la Tabla I legibles por experimento, intervalos de confianza ni repeticiones, no evalúa tiempos de consulta SPARQL, tamaño de la base de conocimiento ni latencia, y no reporta resultados con datos de dispositivos IoT. Los experimentos 1 a 3 son binarios y reportan separación de ruido y eventos con curvas de entrenamiento y matrices de confusión en la Figura 6, y los experimentos 4 a 7 amplían el número de clases.

**Discusión y contribución.** Los autores sostienen que el marco muestra flexibilidad y alta exactitud, que la sinergia entre inteligencia artificial y tecnologías semánticas ofrece una infraestructura formal para anotar patrones sísmicos descubiertos y que el enfoque puede extenderse a un dominio de sensores más amplio, incluidas aplicaciones y dispositivos IoT, para construir una base de conocimiento que apoye la alerta sísmica. Señalan que el reconocimiento de eventos de largo periodo es relevante porque marca la reactivación volcánica, que el modelo distingue incluso las pequeñas diferencias entre los largos periodos de dos volcanes y que podría ser un paso hacia una base de datos global de firmas volcánicas. Sostienen que su desempeño es comparable al de enfoques con muchas más características.

**Limitaciones declaradas.** Declaradas: los sensores IoT para movimiento del suelo aún no están extendidos y no hay datos disponibles, de modo que se usan datos de las instituciones geofísicas; el desarrollo completo de todo el sistema, incluida la capa de recuperación de datos, queda como trabajo futuro. No declaradas: los experimentos son offline con datos históricos y no hay prueba de tiempo real ni de latencia de extremo a extremo; la inversión de polaridad duplica trazas y no se indica si la división 70:20:10 se hizo antes del aumento, lo que puede filtrar copias entre entrenamiento y prueba; las clases tienen orígenes de estaciones distintos, de modo que el clasificador puede aprender la estación y no el evento; no hay validación cruzada ni repeticiones; las comparaciones con otros estudios usan conjuntos y métricas distintos (F1 frente a exactitud); la ontología y las consultas no se evalúan en rendimiento ni uso por usuarios; el nivel de alerta y la ciudad afectada se modelan pero no se calculan; no se discuten falsos positivos en un entorno de crisis.

**Trabajo futuro.** Explícito: completar el desarrollo del sistema, incluida la capa de recuperación de datos geofísicos, extender el marco a dispositivos IoT y a otros tipos de datos geofísicos (GPS, inclinómetros, datos geodésicos y satelitales). Implícito: pruebas en tiempo real, uso de datos de sensores de bajo costo y una base global de firmas volcánicas.

**Palabras clave.** Declaradas: Internet of Things (IoT)-based sensor networks; machine learning; ontology; seismic domain; Vesuvius and Colima volcanoes | Inferidas: IoT, detección de eventos sísmicos, ontología, SSN/SOSA, web semántica, aprendizaje automático, redes neuronales convolucionales, Vesubio, Colima, base de conocimiento

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Una ontología sobre SSN/SOSA que integre datos de redes sísmicas y de futuros dispositivos IoT, junto con un clasificador de eventos por aprendizaje profundo, permite detectar y almacenar de forma homogénea eventos volcano-tectónicos, de largo periodo y voladuras con F1 superior a 90 %, y alcanza 0,98 en el reconocimiento de la firma de volcán con una red convolucional, lo que ofrece una base de conocimiento consultable para apoyar la alerta en crisis volcánicas.

**Antítesis identificada.** El marco se presenta como orientado a IoT, pero todos los datos provienen de redes de observatorios, los autores reconocen que no hay datos de sensores IoT, y la validación es offline con registros históricos, sin latencia ni prueba en tiempo real. El aumento por inversión de polaridad y la división aleatoria pueden contaminar la prueba, las clases proceden de estaciones diferentes y puede haber aprendizaje de la estación, y los resultados no tienen repeticiones ni intervalos. La comparación con otros estudios mezcla métricas y conjuntos. La ontología, que es la contribución semántica, no se evalúa en rendimiento ni en utilidad, y el nivel de alerta se declara sin calcularse. El vínculo con edificios, ciudades o empresas queda en una clase de la ontología sin uso.

**Síntesis propuesta.** La contribución sostenible es un diseño de ontología reutilizable, apoyado en estándares, que formaliza la cadena desde la señal del sensor hasta el evento clasificado, y una comparación de dos clasificadores con alta exactitud en datos históricos de dos volcanes. Para el corpus, importa porque ofrece un patrón de interoperabilidad semántica entre sensores heterogéneos que puede servir a gemelos digitales y a sistemas de alerta, y porque muestra la distancia entre la promesa de IoT de bajo costo y los datos realmente usados. Su valor práctico requiere pruebas en tiempo real, con datos de dispositivos de bajo costo y con evaluación de la ontología, y su relación con la recuperación empresarial es indirecta.

**Áreas grises detectadas.**

1. Presencia real de IoT: el título y el resumen presentan un marco orientado a IoT, pero la sección de adquisición reconoce que los sensores IoT ambientales para movimiento del suelo no están extendidos y que no hay datos disponibles; todos los registros proceden de estaciones de observatorios con registradores y telemetría, de modo que el componente IoT es una proyección y no un resultado.
2. Posible fuga de datos por aumento: el conjunto se duplica invirtiendo la polaridad de cada traza y se divide 70:20:10, pero el texto no indica si la división se hizo antes del aumento; una traza y su copia invertida en conjuntos distintos inflarían el desempeño, que llega a 0,98 de F1 en el experimento 8.
3. Aprendizaje de la estación y no del evento: cada clase proviene de estaciones concretas (voladuras en CPV, TRZ y NL9; largo periodo de Colima en otras), y las diferencias de instrumento, ruido y muestreo pueden bastar para clasificar, en particular en el experimento 8, que distingue Vesubio de Colima, por lo que el resultado no demuestra una firma sísmica del volcán.
4. Evaluación de la capa semántica: la ontología y las consultas SPARQL se describen como el aporte central, pero no se reportan tamaño de la base de conocimiento, tiempos de consulta, completitud de la anotación ni evaluación con usuarios, y las clases veo:City y veo:AlertLevel no se alimentan ni se prueban.

**Puntos oscuros aclarados.** Llama la atención que el resumen afirme una integración de sensores IoT cuando el propio texto indica que no hay datos de ese tipo. También es notable que se compare un F1 de 93 % con una exactitud de 93,5 % de otro estudio con un conjunto de 109 609 eventos, y que se concluya un desempeño comparable. El remuestreo se describe como 100 Hz con un intervalo de 0,1 s, que es inconsistente, y el número de filtros del último bloque de la red se escribe como 521 en el texto cuando el resto de la secuencia sugiere 512. La Tabla I, que contiene las métricas por experimento, se extrae sin sus valores, de modo que solo se verifican los números citados en el texto. Además, el conjunto incluye más de 28 000 muestras de ruido frente a 4008 eventos, y los experimentos se equilibran de maneras distintas sin justificar el criterio. Por último, la selección de una estación de referencia por tipo de señal, con la mejor relación señal-ruido, hace que los datos de entrenamiento sean más limpios que los que recibiría una red de sensores de bajo costo.

**Ideas propositivas novedosas.**

1. Validación por estación y por periodo: repetir los ocho experimentos con la división por estación y por año, sin aumento por inversión de polaridad en el conjunto de prueba, y reportar F1 con intervalos de confianza de 95 % y diez repeticiones. El resultado indicaría cuánto del desempeño de 0,93 a 0,98 se debe a la señal sísmica y cuánto a la estación o a la fuga de datos, y permitiría decidir si el clasificador sirve para sensores de bajo costo sin calibración, condición necesaria para un despliegue en edificios y zonas industriales. El código y los índices de las trazas de cada partición se publicarían para su replicación.
2. Capa semántica para gemelos de continuidad: extender VEO con clases de edificio, empresa y proceso productivo, de modo que un evento detectado alimente una consulta SPARQL que devuelva qué activos y empresas están en el área y su nivel de alerta, y medir con 1000 consultas el tiempo de respuesta, la completitud de la anotación y la facilidad de uso para operadores. Con ello se podría comprobar si la ontología sirve como capa de interoperabilidad entre sensores sísmicos y datos de gemelos digitales, y qué parte del valor de la alerta llega a quienes deciden la continuidad de operaciones. Las consultas y los resultados se documentarían con ejemplos reproducibles.

**Relaciones poco exploradas.**

1. Detección sísmica en nodos y en el borde (complementa) D049 y D060: D049 procesa la detección en el nodo y D060 clasifica intensidad en el borde; D071 aporta la capa semántica y la comparación de dos clasificadores sobre eventos volcánicos.
2. Alerta sísmica con IoT en la nube (se relaciona con) D073 y D075: D073 evalúa EEW con IoT en la nube y su latencia y D075 una red LoRa multisalto; D071 contribuye con interoperabilidad semántica, aunque sin latencia ni tiempo real.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Aporta una ontología reutilizable (VEO) sobre SSN/SOSA y una comparación de MLP y CNN con 4008 señales de dos volcanes, con F1 de 93 % en seis clases y 0,98 en el experimento 8. Su valor para el corpus es moderado porque el componente IoT no se prueba con dispositivos, la validación es offline con posible fuga de datos y aprendizaje de la estación, la ontología no se evalúa y el dominio volcánico no se conecta con edificios, empresas o recuperación, pero ofrece un patrón de interoperabilidad semántica para sensores sísmicos.

**Conexiones inter-documentales.**

- **EXTIENDE** D031 (IoT semántico y alerta temprana de amenazas geológicas): D071 desarrolla la semántica de IoT para detección sísmica (ontología SSN/SOSA y clasificador profundo) que D031 planteaba como arquitectura de alerta temprana [juicio del analista]
- **PRECEDE** D019 (IoT y alerta temprana en la gestión de desastres sísmicos): es citado por D019 (verificado por coincidencia de título) [citación verificada]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 70 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Etiqueta sin respaldo empírico (El marco se presenta como orientado a IoT, pero no se usan dispositivos ni datos IoT (Resumen, p. 1; Sec. V, p. 6)); Comparación de métricas no equivalentes (Un F1 de 93 % se compara con una exactitud de 93,5 % de otro conjunto (Sec. VII.D, p. 12)); Posible confusión entre estación y evento (Las clases proceden de estaciones distintas y el experimento 8 distingue volcanes (Sec. V, p. 6; Sec. VII.D, p. 12))
- **Bradford-Hill:** No aplica: es un estudio de diseño y clasificación; no se estima causalidad con datos observacionales.
- **TRL asignado:** 4 — 'The complete development of the whole system is a future planned activity' (p. 6)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (13 páginas con marcadores del PDF; las páginas de la revista son 9789 a 9801). La Tabla I se extrajo sin sus valores, por lo que solo se citan las métricas que figuran en el texto. El número de filtros '521' del texto se cita como aparece y se señala como probable error; el remuestreo '100 Hz (t = 0,1 s)' también se señala como inconsistente.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Una ontología sobre SSN/SOSA que integre datos de redes sísmicas y de futuros dispositivos IoT, junto con un clasificador de eventos por aprendizaje profundo, permite detectar y almacenar de forma homogénea eventos volcano-tectónicos, de largo periodo y voladuras con F1 superior a 90 %, y alcanza 0,98 en el reconocimiento de la firma de volcán con una red convolucional, lo que ofrece una base de conocimiento consultable para apoyar la alerta en crisis volcánicas.  | El marco se presenta como orientado a IoT, pero todos los datos provienen de redes de observatorios, los autores reconocen que no hay datos de sensores IoT, y la validación es offline con registros históricos, sin latencia ni prueba en tiempo real. El aumento por inversión de polaridad y la división aleatoria pueden contaminar la prueba, las clases proceden de estaciones diferentes y puede haber aprendizaje de la estación, y los resultados no tienen repeticiones ni intervalos. La comparación con otros estudios mezcla métricas y conjuntos. La ontología, que es la contribución semántica, no se evalúa en rendimiento ni en utilidad, y el nivel de alerta se declara sin calcularse. El vínculo con edificios, ciudades o empresas queda en una clase de la ontología sin uso.  | La contribución sostenible es un diseño de ontología reutilizable, apoyado en estándares, que formaliza la cadena desde la señal del sensor hasta el evento clasificado, y una comparación de dos clasificadores con alta exactitud en datos históricos de dos volcanes. Para el corpus, importa porque ofrece un patrón de interoperabilidad semántica entre sensores heterogéneos que puede servir a gemelos digitales y a sistemas de alerta, y porque muestra la distancia entre la promesa de IoT de bajo costo y los datos realmente usados. Su valor práctico requiere pruebas en tiempo real, con datos de dispositivos de bajo costo y con evaluación de la ontología, y su relación con la recuperación empresarial es indirecta.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'VEO' es la ontología del evento volcánico que describe estaciones, señales, eventos y alertas; 'SSN/SOSA' es el vocabulario estándar para sensores y observaciones; 'evento de largo periodo' es una señal asociada a procesos de fluidos y presurización; 'F1' es la media armónica de precisión y exhaustividad.
- **P2 Supuestos:** Supone que los registros de observatorios representan los datos de sensores IoT futuros, que la división de datos no filtra información, que la estación no determina la clase y que la ontología facilita decisiones en crisis.
- **P3 Evidencia:** La evidencia son 4008 señales de dos volcanes, ocho experimentos con MLP y CNN y la descripción de una ontología, sin pruebas en tiempo real ni evaluación de la capa semántica.
- **P4 Consecuencias:** Si es cierto, la detección y la anotación semántica pueden integrarse con sensores de bajo costo y apoyar las alertas; si es falso, el desempeño puede caer con sensores ruidosos y con estaciones nuevas.
- **P5 Contraejemplos:** No se examinan datos de sensores IoT, latencia, falsos positivos en crisis, validación por estación, rendimiento de consultas ni usuarios.
- **P6 Alternativas:** Alternativas: que el clasificador aprenda la estación; que un modelo con características clásicas baste; que el valor principal esté en la integración de datos y no en la clasificación.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Señales en el conjunto de datos | 4008 | señales | Formato SAC, remuestreadas a 100 Hz | Sec. VII.A, p. 9 | Texto | Alta | Más de 28 000 muestras de ruido |
| Eventos volcano-tectónicos y voladuras del Vesubio | 416 y 464 | eventos | Más 363 de largo periodo | Sec. VII.A, p. 10 | Texto | Alta | Antes del aumento |
| Eventos de largo periodo de Colima | 2765 | eventos | Noviembre de 2005 a abril de 2006 | Sec. VII.A, p. 10 | Texto | Alta | Antes del aumento |
| Longitud de la ventana de entrada | 2400 | puntos | Equivalente a 24 s a 100 Hz | Sec. VII.A, p. 9 | Texto | Alta | Incluye 400 muestras de aislamiento |
| F1 de la red convolucional en el experimento 8 | 0,98 | índice | Vesubio, Colima y ruido; precisión y exhaustividad iguales | Sec. VII.D, p. 12 | Texto | Media | Posible fuga de datos |
| F1 del experimento 6 (todas las clases) | 93 | % | Frente a 93,5 % de exactitud en Ubinas | Sec. VII.D, p. 12 | Texto | Media | Métricas no comparables |
| Neuronas ocultas del perceptrón multicapa | 42 | neuronas | Lote de 50, tasa de 0,001 y 640 iteraciones | Sec. VII.B, p. 9 | Texto | Alta | Hiperparámetros declarados |
| División de datos | 70:20:10 | porcentaje | Entrenamiento, validación y prueba | Sec. VII.C, p. 10 | Texto | Alta | Sin validación cruzada |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'The complete development of the whole system is a future planned activity' (p. 6) | Validación de los módulos centrales en laboratorio con datos históricos; sin sistema completo ni pruebas en operación. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'The main benefit is due to the low-cost technologies compared with the high cost of installation and maintenance of the traditional high-sensitive seismometers' (p. 6) | Se argumenta un beneficio de costo sin cifras, modelo de negocio ni clientes. |
| IRL | 3 | Sí | 'the environmental, IoT-based sensors for ground motion measurement are not yet widespread (and no data are available, to the best of our knowledge)' (p. 6) | Se integran datos de dos redes de observatorios en una ontología; los dispositivos IoT no se integran. |
| DRL | 3 | Sí | 'our framework is designed indeed to support human experts, providing comprehensive access to the knowledge base for a prompt alert in cases of volcanic crises' (p. 12) | Se identifica una necesidad operativa de observatorios; sin estudio de adopción. |
| SRL | 1.17 | Sí | Componentes: Adquisición de datos y clasificación por aprendizaje automático (TRL 4), Ontología VEO y base de conocimiento (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 10.5; ÷9 → 1.17; nivel acotado a [1,9] = 1.17 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 1 e IRL 3: módulos validados con datos históricos sin dispositivos IoT, sin tiempo real y sin modelo de negocio. · Estrategia de salida: Piloto con sensores de bajo costo, pruebas en tiempo real, validación por estación y evaluación de la capa semántica.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Etiqueta sin respaldo empírico | El marco se presenta como orientado a IoT, pero no se usan dispositivos ni datos IoT (Resumen, p. 1; Sec. V, p. 6) | Promesa descrita como resultado |
| Comparación de métricas no equivalentes | Un F1 de 93 % se compara con una exactitud de 93,5 % de otro conjunto (Sec. VII.D, p. 12) | Métricas y conjuntos distintos |
| Posible confusión entre estación y evento | Las clases proceden de estaciones distintas y el experimento 8 distingue volcanes (Sec. V, p. 6; Sec. VII.D, p. 12) | Resultado que puede reflejar la fuente |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Ontología e interoperabilidad semántica → mejor integración y apoyo a la decisión | Diseño de VEO sin evaluación | Mecanismo plausible | Evaluación de rendimiento de consultas y estudio con usuarios | Calidad de metadatos, estandarización | 2 | Relación supuesta sin evidencia |
| Red neuronal sobre señales → clasificación de eventos | F1 de 90 % a 98 % en experimentos offline | Asociación predictiva | Validación por estación y en tiempo real | Estación, instrumento, aumento de datos | 3 | Asociación fuerte en datos históricos |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Validación por estación y por periodo, sin fuga por aumento de datos y con repeticiones | Crítico | Media | 9 |
| Tecnológico | Datos y pruebas con sensores IoT de bajo costo y en tiempo real, con latencia | Crítico | Media | 9 |
| Conocimiento | Evaluación de la ontología y vínculo con edificios, ciudades y empresas | Significativo | Media | 8 |
| Mercado | Costos y adopción por observatorios y autoridades de protección civil | Significativo | Media | 6 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Mapa del Vesubio con estaciones y ejemplos de formas de onda | Mapa y gráfico | Estaciones de tres y una componente | No aplica | Media |
| Fig. 3 | Descripción lógica del marco | Diagrama | Capas de adquisición, semántica, clasificación y recuperación | 4 capas | Media |
| Fig. 4 | Clases centrales de VEO | Diagrama | Modelos de contexto, colección y conocimiento | No aplica | Media |
| Fig. 6 | Exactitud, pérdida y matrices de confusión de MLP y CNN en los experimentos 1, 3, 6 y 8 | Gráficos | Alto desempeño en ambos modelos | 0,98 de F1 en el experimento 8 | Media |
| Tabla I | Diseño experimental y métricas por experimento | Tabla | Ocho experimentos con precisión, exhaustividad y F1 | No legible en la extracción | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| MyShake (aplicación para teléfonos inteligentes) | No especificado en documento | Academia | Detección de sismos con teléfonos | Bajo costo y cobertura | No integra semántica según el texto | Creciente |
| Clasificación de eventos del volcán Ubinas con bosque aleatorio y máquinas de vectores | Perú | Academia | Clasificación de 109 609 eventos con 102 características | Gran conjunto de datos | Extracción costosa de características según los autores | Estable |
| SeismicNet para el volcán Llaima | Chile | Academia | Red profunda para clasificar señales volcánicas | F1 de 91,75 % a 93,02 % | Conjunto distinto | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Precisión, exhaustividad y F1 de la clasificación de eventos sísmicos
- **X:** Modelo (MLP o CNN) y configuración de clases del experimento
- **Z (controles):** Estación, tipo de señal, aumento de datos, tamaño de clases
- **Datos:** 4008 señales de las redes del INGV-OV (Vesubio, 1999 a 2021) y de Colima (2005 a 2006) más de 28 000 muestras de ruido
- **Método:** Clasificación supervisada con ocho experimentos y división 70:20:10
- **Efecto reportado:** F1 de 93 % en seis clases y 0,98 en el experimento 8 con la CNN
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin repeticiones, intervalos ni validación cruzada; posible fuga por aumento de datos

| Vacío | Tipo | Descripción |
|---|---|---|
| V-071-01 | TERR | Volcán Vesubio (Nápoles, Italia) y volcán de Colima (México) |
| V-071-02 | POBL | Eventos sísmicos y ruido; población expuesta mencionada sin análisis |
| V-071-03 | TEMP | Registros del Vesubio de 1999 a 2021 y de Colima de noviembre de 2005 a abril de 2006 |
| V-071-04 | MET | Experimentos offline con datos históricos, sin tiempo real ni sensores IoT |
| V-071-05 | VAR | Faltan latencia, falsos positivos, costos y datos de sensores de bajo costo |
| V-071-06 | TEOR | Web semántica y aprendizaje automático; sin teoría de continuidad de operaciones |
| V-071-07 | CAUS | Efecto de la alerta semántica sobre las decisiones sin evidencia |
