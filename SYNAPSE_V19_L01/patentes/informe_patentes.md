# Módulo de patentes — SYNAPSE V19.0, lote L01

`MODE=COMPUTE FILES=TRUE BATCH=L01 MODULE=PATENTES DOCS_PATENTES=11 STATUS=COMPLETE_WITH_LIMITS`

## 1. Alcance y método

La carpeta `Patentes /` del repositorio contiene 11 documentos de patente en formato PDF, descargados de Lens.org (4 patentes concedidas con código B2 y 7 publicaciones de solicitud con código A1). Los archivos son imágenes escaneadas sin capa de texto. Se aplicó reconocimiento óptico de caracteres (RapidOCR, sobre imágenes de 150 ppp, lectura por columnas) a una parte de cada documento: la portada, las primeras 33 páginas (hojas de dibujos), las últimas 14 páginas (reivindicaciones) y una de cada 20 páginas intermedias. En total se leyeron 662 de 4,048 páginas (16.4 %), equivalentes a 353,633 palabras. El texto reconocido se conserva en `patentes/_ocr_texto/`.

Las patentes forman un módulo separado del lote de 101 documentos (DOCS=101 no cambia). Se identifican con claves P001 a P011, se les asignó una ficha de cuatro capas adaptada a documentos de patente y se evaluaron con las mismas dimensiones de madurez, vacíos y relaciones que los demás documentos. Las adaptaciones son tres: la referencia APA 7 usa el formato de patente; el estado legal no se asume (solo el código de tipo indica concesión); y los niveles TRL, IRL y DRL se limitan a lo que el texto sustenta, sin inferir madurez comercial de la titularidad.

Limitaciones de método. La lectura parcial implica que la ausencia de un término en las páginas leídas no equivale a ausencia en el documento; las frecuencias que se presentan son de las páginas leídas. La lectura óptica puede omitir líneas, por lo que se citan fragmentos literales solo cuando son legibles. El estado legal posterior de las solicitudes y la vigencia de las concedidas no pueden verificarse con los archivos.

## 2. Inventario

| ID | Número | Tipo | Titular | Presentación | Reivindicaciones (indep.) | Páginas | Relevancia |
|---|---|---|---|---|---|---|---|
| P001 | US 12,277,524 B2 | B2 | Strong Force VCN Portfolio 2019, LLC | 30 de agosto de 2021 | 30 (1) | 344 | Periférico |
| P002 | US 12,314,060 B2 | B2 | Strong Force VCN Portfolio 2019, LLC | 30 de noviembre de 2023 | 28 (1, 18) | 607 | Adyacente |
| P003 | US 12,567,082 B2 | B2 | Strong Force VCN Portfolio 2019, LLC | 7 de marzo de 2023 | 19 (1, 13) | 532 | Periférico |
| P004 | US 12,675,781 B2 | B2 | Strong Force VCN Portfolio 2019, LLC | 28 de febrero de 2022 | 21 (1, 16, 19) | 432 | Periférico |
| P005 | US 2022/0035342 A1 | A1 | Strong Force VCN Portfolio 2019, LLC | 30 de agosto de 2021 | 31 (1) | 353 | Periférico |
| P006 | US 2022/0036274 A1 | A1 | Strong Force VCN Portfolio 2019, LLC | 30 de agosto de 2021 | 15 (1) | 353 | Periférico |
| P007 | US 2022/0036275 A1 | A1 | Strong Force VCN Portfolio 2019, LLC | 30 de agosto de 2021 | 17 (1) | 353 | Periférico |
| P008 | US 2022/0036302 A1 | A1 | Strong Force VCN Portfolio 2019, LLC | 30 de agosto de 2021 | 20 (1) | 353 | Periférico |
| P009 | US 2022/0044204 A1 | A1 | Strong Force VCN Portfolio 2019, LLC | 30 de agosto de 2021 | 26 (1) | 354 | Periférico |
| P010 | US 2022/0058569 A1 | A1 | Strong Force VCN Portfolio 2019, LLC | 30 de agosto de 2021 | 8 (1) | 352 | Periférico |
| P011 | US 2022/0114310 A1 | A1 | International Business Machines Corporation | 12 de octubre de 2020 | 20 (1, 7, 14) | 15 | Periférico |

Diez de las once patentes (10) pertenecen a Strong Force VCN Portfolio 2019, LLC y una a International Business Machines Corporation. Los seis documentos P005 a P010 son publicaciones de solicitudes presentadas el 30 de agosto de 2021 como continuaciones de la solicitud internacional PCT/US2020/059227, con una descripción común de 82 hojas de dibujos y párrafos numerados hasta cerca de [2093]; difieren en el título y en las reivindicaciones. P001 es la patente concedida de otra solicitud de la misma familia (17/460,995, publicada como US 2022/0035341 A1, que no está en la carpeta). P002, P003 y P004 pertenecen a otras familias del mismo titular, con prioridades de 2021 a 2023. P011 pertenece a una familia distinta de IBM presentada en 2020.

## 3. Resultados

### 3.1 Contenido tecnológico de las reivindicaciones

La tabla indica si las reivindicaciones independientes y dependientes transcritas en las fichas mencionan cada tecnología.

| ID | Gemelo digital | Sensores o IoT | Aprendizaje automático o IA | Cadena de bloques o contratos inteligentes | RPA |
|---|---|---|---|---|---|
| P001 | Sí | Sí | Sí | No | Sí |
| P002 | Sí | Sí | Sí | No | No |
| P003 | Sí | Sí | Sí | Sí | Sí |
| P004 | Sí | No | Sí | Sí | No |
| P005 | Sí | Sí | Sí | No | Sí |
| P006 | Sí | Sí | No | Sí | Sí |
| P007 | Sí | Sí | No | Sí | No |
| P008 | Sí | Sí | No | Sí | Sí |
| P009 | Sí | Sí | Sí | Sí | Sí |
| P010 | Sí | No | Sí | No | No |
| P011 | Sí | No | Sí | No | No |

El gemelo digital aparece en las reivindicaciones de 11 de 11 patentes y los sensores o el IoT en 8. El aprendizaje automático o la inteligencia artificial figuran en 8, y la automatización robótica de procesos en 6. Las tres tecnologías que el corpus de 101 documentos asocia con la recuperación (gemelo digital, IoT y análisis de datos) están presentes, pero aplicadas a cadenas de valor, manufactura y mantenimiento de activos, no a recuperación tras un sismo.

### 3.2 Términos del eje del corpus en las páginas leídas

| ID | Páginas leídas | Gemelo digital | Sismo o terremoto | Desastre | Amenaza natural | Interrupción | Resiliencia | Recuperación | Pandemia |
|---|---|---|---|---|---|---|---|---|---|
| P001 | 62 | 459 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| P002 | 75 | 410 | 0 | 2 | 0 | 16 | 2 | 0 | 4 |
| P003 | 71 | 176 | 0 | 1 | 0 | 2 | 4 | 0 | 4 |
| P004 | 66 | 162 | 0 | 1 | 1 | 2 | 2 | 0 | 4 |
| P005 | 62 | 406 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| P006 | 62 | 403 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| P007 | 62 | 398 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| P008 | 62 | 398 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| P009 | 63 | 404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| P010 | 62 | 431 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| P011 | 15 | 86 | 1 | 0 | 3 | 0 | 0 | 0 | 0 |

El gemelo digital es el término más frecuente (3733 apariciones en 662 páginas leídas). Las menciones de sismo suman 1, las de desastre 4, las de interrupción 20, las de resiliencia 8 y las de recuperación 0. Estas frecuencias provienen de un muestreo y deben leerse como límites inferiores. Los pasajes identificados que sustentan la relación con el eje del corpus incluyen: la referencia a 'a natural disaster or epidemic' como evento externo que puede interrumpir operaciones y la lista de tareas de mitigación (proveedores múltiples, inventario de amortiguación, transporte alterno) en Cella et al., 2025a (P002); la inclusión de 'earthquakes' entre los factores ambientales posibles en Berti y DeLuca, 2022 (P011); la exposición a condiciones ambientales adversas o daño detectada por sensores en Cella y Locke, 2026 (P003), cuya descripción menciona además 'natural disasters' entre los eventos que activan la predicción de necesidades de recursos de flota. Con el muestreo realizado no se encontraron otras menciones de sismo.

### 3.3 Relevancia para el eje del corpus

Ninguna patente se clasifica como núcleo. P002 se clasifica como adyacente por tratar la interrupción de la cadena de valor como objeto de predicción y mitigación con un gemelo digital alimentado por sensores. Las demás se clasifican como periféricas (10 documentos): comparten tecnología (gemelos digitales, sensores, aprendizaje automático, contratos inteligentes) pero no el dominio de recuperación productiva tras sismos. La clasificación no es una valoración de calidad de las patentes.

### 3.4 Madurez

Todas las patentes se evaluaron con TRL 2 (concepto formulado y descrito), IRL 2 y DRL 2, porque las páginas leídas no contienen pruebas experimentales, integración probada ni conjuntos de datos reales. El BRL, el MRL y el SRL no se determinan: los documentos no contienen datos de mercado, de manufactura ni componentes evaluados por separado. La titularidad por una empresa comercial no se interpretó como madurez de negocio. El valle de la muerte aplicable es V1 (investigación sin aplicación), limitado a lo que el texto permite afirmar.

## 4. Análisis dialéctico del módulo

La tesis es que los gemelos digitales alimentados por sensores y gestionados con aprendizaje automático y automatización de procesos permiten automatizar decisiones de cadena de valor que reducen interrupciones, lo que sustentaría la continuidad operativa tras un evento. La antítesis es que una patente delimita lo reivindicable y no lo comprobado: las 11 patentes no informan de datos de desempeño, las listas de realizaciones son amplias y el disparador de la reivindicación 1 de Cella et al., 2025a es un umbral de demanda y las reivindicaciones 5 y 6 añaden la determinación de una interrupción mediante simulación, sin que las páginas leídas describan un modelo de daño físico. La síntesis es que el módulo aporta un inventario técnico de funciones (recolección de datos, simulación, recomendación, ejecución automática, contratación automatizada) que puede traducirse en requisitos de un sistema de continuidad empresarial, y que la hipótesis de que dichas funciones reduzcan el tiempo de reanudación tras un sismo permanece sin evidencia en este material.

Preguntas socráticas del módulo. ¿Qué parte de las reivindicaciones describe funciones ya implementadas y cuál describe una cobertura de protección? Los documentos no permiten responder. ¿Qué cambia en el diseño si el disparador es el daño y no la demanda? Cambia el modelo de simulación del gemelo, que debería representar la pérdida de capacidad productiva y logística, y los modelos de recuperación del corpus (por ejemplo, D011) proporcionan esa estructura. ¿Qué hipótesis rival explicaría la misma utilidad con menor complejidad? Reglas de inventario de seguridad y contratos paramétricos de seguro pueden cubrir parte de la función sin gemelo digital, alternativa que ningún documento del módulo evalúa.

## 5. Conexión con el corpus de 101 documentos

Se registraron 33 relaciones tipificadas entre patentes y documentos del lote o entre patentes (COMPLEMENTA 29, CONFIRMA 4). Las relaciones con documentos del corpus son de complementariedad en su mayoría: las patentes aportan el nivel de implementación técnica (funciones, interfaces) que las revisiones y los estudios empíricos del corpus no desagregan, mientras que el corpus aporta modelos de recuperación y evidencia de asociaciones que las patentes no tienen. Las conexiones principales son las siguientes.

- **D081 y D037** (resiliencia de la cadena de suministro y gemelos digitales): las tareas de mitigación de Cella et al., 2025a y las pruebas de estrés de Cella y Locke, 2026 se corresponden con capacidades que D081 clasifica por etapa de resiliencia; D081 advierte que el rebote y el crecimiento tienen menos evidencia, y las patentes no la suplen.
- **D011 y D053** (recuperación empresarial y tiempos de recuperación): ofrecen la estructura de bloqueos y tiempos que falta a los disparadores de las patentes.
- **D004 y D028** (revisiones de gemelos digitales): coinciden en la ausencia de evidencia empírica de desempeño; las patentes reproducen la misma brecha en otra clase documental.
- **D068, D020 y D014** (monitorización estructural): el sistema de colocación de sensores recomendada por aprendizaje de Cella et al., 2022e puede contrastarse con los criterios de la literatura de monitorización.
- **D023 y D034** (gemelos de puentes y de ciudades sísmicas): Berti y DeLuca, 2022 propone iniciar un gemelo por similitud ambiental, idea que podría extenderse a parámetros sísmicos.

## 6. Discusión de controversias

Primera controversia: valor probatorio. Una patente concedida acredita novedad y actividad inventiva ante una oficina, no eficacia. Tratar las patentes como evidencia de madurez tecnológica sobrestima el nivel de preparación. Por ello el módulo las clasifica como estado de la técnica. Segunda controversia: amplitud de las reivindicaciones. Las listas dependientes enumeran decenas de funciones (en Cella et al., 2025b, 29 dependientes), lo que puede interpretarse como cobertura defensiva; el texto leído no permite distinguir funciones implementadas de funciones solo reivindicadas. Tercera controversia: familias repetidas. Seis documentos comparten descripción, de modo que sus frecuencias de términos no son observaciones independientes; contarlas como seis fuentes duplicaría el peso de un mismo texto. Cuarta controversia: libertad de operación. La existencia de reivindicaciones amplias sobre plataformas de cadena de valor con gemelos digitales puede condicionar desarrollos posteriores; este informe no constituye un análisis jurídico y no determina infracción ni libertad de operación.

## 7. Premortem y escenarios

Premortem. Causas probables de que la incorporación de las patentes lleve a conclusiones erróneas: (1) tratar la titularidad comercial como evidencia de uso; (2) extrapolar a sismos a partir de menciones aisladas; (3) contar como independientes documentos de una misma familia; (4) leer solo una parte del documento y concluir ausencia; (5) asumir estado legal vigente. Contingencias: mantener las patentes como módulo separado, registrar la cobertura de lectura, ponderar por familia y verificar el estado legal en una base oficial antes de cualquier uso jurídico o comercial.

| Futuro | Objetivo | Tres opciones viables |
|---|---|---|
| A. Se acumula evidencia empírica sobre gemelos digitales en recuperación | Medir desempeño | Piloto con empresas de una zona sísmica; caso con datos de simulacros; evaluación con datos abiertos de cadenas de suministro |
| A. Se acumula evidencia empírica sobre gemelos digitales en recuperación | Integrar con modelos de recuperación | Acoplar parámetros del gemelo con los bloqueos de D011; calibrar con D053; validar con registros de reanudación |
| A. Se acumula evidencia empírica sobre gemelos digitales en recuperación | Reducir costo de inicialización | Plantillas por similitud sísmica como en P011; bibliotecas abiertas de gemelos; reutilización entre activos similares |
| B. La evidencia sigue siendo escasa | Mantener vigilancia tecnológica | Registro anual de patentes y solicitudes; alertas por clasificación G06Q y G16Y; revisión de estado legal |
| B. La evidencia sigue siendo escasa | Acotar la hipótesis | Reducir el alcance a una función (inventario de seguridad); probar un solo disparador; comparar con reglas simples |
| B. La evidencia sigue siendo escasa | Priorizar documentos de mayor valor | Concentrar la lectura completa en P002, P003 y P009; ampliar OCR completo; consultar listados oficiales de reivindicaciones |
| C. Las reivindicaciones amplias condicionan el desarrollo | Evaluar libertad de operación | Análisis jurídico por abogado de patentes; revisión de estado legal; diseño alternativo sin las funciones reivindicadas |
| C. Las reivindicaciones amplias condicionan el desarrollo | Usar alternativas abiertas | Gemelos con estándares abiertos; contratos paramétricos de seguro; reglas de inventario sin plataforma propietaria |
| C. Las reivindicaciones amplias condicionan el desarrollo | Cooperar con titulares | Licencias de investigación; acuerdos de transferencia; pilotos conjuntos con universidades |

## 8. ¿Qué se me escapa?

Se escapan seis aspectos. (1) La mayor parte del texto de cada patente no se leyó (cobertura 16.4 %); una lectura completa por OCR de unas 4,048 páginas aumentaría la cobertura y permitiría un conteo exacto de términos. (2) El estado legal de las solicitudes y la vigencia de las concedidas. (3) Las publicaciones previas faltantes de la familia, como US 2022/0035341 A1. (4) Patentes de otros titulares y de otras jurisdicciones sobre gemelos digitales aplicados a edificios y a recuperación sísmica; la carpeta contiene una muestra que no es una búsqueda sistemática. (5) El análisis de citas hacia delante y hacia atrás entre patentes y literatura científica del corpus. (6) La verificación por un abogado de patentes de la interpretación de las reivindicaciones. Rutas de solución: OCR completo por lotes, consulta de registros oficiales (USPTO) para el estado legal, búsqueda sistemática por clasificación (G06Q 10, G05B 19, G16Y) y revisión jurídica.

## 9. Valor estratégico

El módulo fija qué parte del conocimiento sobre gemelos digitales e IoT en cadenas de valor está documentada como estado de la técnica y qué parte está respaldada por evidencia. Para la decisión de inversión o de investigación, indica que las funciones técnicas existen como diseños protegidos, que ninguna está respaldada por datos de desempeño en el material leído, y que el vacío central del corpus (medir el efecto sobre el tiempo de reanudación de empresas tras un sismo) no se cierra con este material. El valor práctico es de insumo para especificar requisitos y para orientar una búsqueda de patentes con cobertura sistemática.

## 10. Referencias

Berti, J. G., & DeLuca, L. S. (2022). *Initiating a digital twin based on cognitive location and environmental impact* (U.S. Patent Application Publication No. 2022/0114310 A1). U.S. Patent and Trademark Office.

Cella, C. H., & Locke, A. S. (2026). *Autonomous smart contract execution platform* (U.S. Patent No. 12,567,082 B2). U.S. Patent and Trademark Office.

Cella, C. H., Bliven, B., Sharma, K., & El-Tahry, T. S. (2026). *Distributed ledger for additive manufacturing in value chain networks* (U.S. Patent No. 12,675,781 B2). U.S. Patent and Trademark Office.

Cella, C. H., Cardno, A., Parenti, J., Locke, A. S., Kell, B., El-Tahry, T. S., Fortin, L., Jr., Bunin, A., Sharma, K., Charon, T., Malchev, H., Vetter, E. P., Stein, D., & Goodman, B. D. (2025a). *Value chain network planning using machine learning and digital twin simulation* (U.S. Patent No. 12,314,060 B2). U.S. Patent and Trademark Office.

Cella, C. H., Spitz, R., & El-Tahry, T. S. (2022a). *Control tower and enterprise management platform with robotic process automation systems managing product outcomes and activities* (U.S. Patent Application Publication No. 2022/0035342 A1). U.S. Patent and Trademark Office.

Cella, C. H., Spitz, R., & El-Tahry, T. S. (2022b). *Managing demand factors and infrastructure facilities of control tower and enterprise management platform* (U.S. Patent Application Publication No. 2022/0036274 A1). U.S. Patent and Trademark Office.

Cella, C. H., Spitz, R., & El-Tahry, T. S. (2022c). *Network and data facilities of control tower and enterprise management platform with adaptive intelligence* (U.S. Patent Application Publication No. 2022/0036302 A1). U.S. Patent and Trademark Office.

Cella, C. H., Spitz, R., & El-Tahry, T. S. (2025b). *Control tower and enterprise management platform with robotic process automation systems* (U.S. Patent No. 12,277,524 B2). U.S. Patent and Trademark Office.

Cella, C. H., Spitz, R., El-Tahry, T. S., Cardno, A., Parenti, J., Bliven, B., & Dobrowitsky, J. (2022d). *Artificial intelligence system for control tower and enterprise management platform managing logistics system* (U.S. Patent Application Publication No. 2022/0058569 A1). U.S. Patent and Trademark Office.

Cella, C. H., Spitz, R., El-Tahry, T. S., Cardno, A., Parenti, J., Bliven, B., & Dobrowitsky, J. (2022e). *Artificial intelligence system for control tower and enterprise management platform managing sensors and cameras* (U.S. Patent Application Publication No. 2022/0044204 A1). U.S. Patent and Trademark Office.

Cella, C. H., Spitz, R., El-Tahry, T. S., Cardno, A., Parenti, J., Bliven, B., & Dobrowitsky, J. (2022f). *Internet of things resources and network and data facilities for control tower and enterprise management platform with adaptive intelligence* (U.S. Patent Application Publication No. 2022/0036275 A1). U.S. Patent and Trademark Office.
