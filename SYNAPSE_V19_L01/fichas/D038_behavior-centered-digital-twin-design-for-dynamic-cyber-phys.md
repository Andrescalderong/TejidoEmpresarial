# FB-L01-038 | D038 — Behavior-Centered Digital-Twin Design for Dynamic Cyber-Physical System Development

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/CSIMQ_30_2.pdf` · 22 páginas · Relevancia para el eje del corpus: **Periférico** (Propone un enfoque metodológico de gemelo digital centrado en el comportamiento (modelado orientado a sujetos, S-BPM) para sistemas ciberfísicos y lo ilustra con un ejemplo de gestión de tráfico. Aporta conceptos para diseñar gemelos adaptables y validables con participación humana, pero no trata sismos, resiliencia empresarial ni recuperación productiva.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-038 / D038
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Stary, C., Elstermann, M., Fleischmann, A., & Schmidt, W. (2022). Behavior-Centered Digital-Twin Design for Dynamic Cyber-Physical System Development. *Complex Systems Informatics and Modeling Quarterly*, *2022*(30), Article 169. https://doi.org/10.7250/csimq.2022-30.02
- **Autores:** Stary, Christian (7003448093); Elstermann, Matthes (55155604200); Fleischmann, Albert (36018353600); Schmidt, Werner (55462029200)
- **Afiliaciones:** Business Informatics-Communications Engineering, Johannes Kepler University Linz, Linz, Austria; Institute for Information Management in Engineering, Karlsruhe Institute of Technology, Karlsruhe, Germany; InterAktiv Unternehmensberatung, Pfaffenhofen, Germany; Business School, Technische Hochschule Ingolstadt, Ingolstadt, Germany
- **Fecha de publicación:** 2022
- **Fuente/contenedor:** Complex Systems Informatics and Modeling Quarterly · vol. 2022(30)
- **Identificador persistente:** DOI 10.7250/csimq.2022-30.02 · ISSN 22559922
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85141817900&doi=10.7250%2fcsimq.2022-30.02&partnerID=40&md5=1a3850e34f5acabefc84494113e8a0ed
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 31

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Apoyar a desarrolladores, expertos de dominio y usuarios en la creación y adaptación de modelos de gemelo digital de un sistema ciberfísico (CPS, por sus siglas en inglés) de manera centrada en las personas, mediante la integración horizontal y vertical de componentes y de sus modelos de comportamiento. El estudio sostiene que un gemelo comprensible por actores no especialistas, ejecutable y validable permite probar el comportamiento del sistema antes de ponerlo en operación y adaptarlo cuando surjan requisitos nuevos. El objetivo práctico es mostrar la viabilidad del enfoque en un ejemplo de gestión de tráfico urbano.

**Pregunta de investigación.** El texto no formula preguntas de investigación en forma explícita. La pregunta implícita es si un lenguaje de modelado con un conjunto mínimo de elementos (acciones, envío y recepción de mensajes y relaciones temporales) puede especificar gemelos digitales de sistemas ciberfísicos heterogéneos que sean comprensibles para los interesados, ejecutables sin transformación adicional y adaptables en operación. También se pregunta cómo representar los cuatro tipos de comportamiento (predecible o impredecible, deseable o indeseable).

**Marco teórico.** El marco reúne tres componentes. Primero, la definición de gemelo digital como cuerpo sincronizado de información sobre estructura, función y comportamiento de una entidad física, con flujos de información que permiten convergencia entre estados físico y virtual, y la distinción entre sombra digital (flujo unidireccional) e hilo digital (bidireccional). Segundo, la tipología de comportamiento de Grieves y Vickers (predecible deseable, predecible indeseable, impredecible deseable e impredecible indeseable). Tercero, la gestión de procesos de negocio orientada a sujetos (S-BPM), cuya teoría núcleo describe sistemas como actores que se comunican mediante mensajes, y las cinco dimensiones del gemelo propuestas por Wu et al.

**Metodología.** El estudio sigue la ciencia del diseño con el marco operativo de Peffers et al., en la que cada ciclo de diseño produce un artefacto que alimenta una base de conocimiento. Se presentan tres ciclos sucesivos: la especificación del gemelo de los componentes del CPS, la ampliación con información de situaciones específicas o excepcionales y la captura de comportamiento inteligente con eventos complejos. El demostrador es un sistema de gestión de tráfico con nueve sujetos (cuatro detectores de vehículos, un colector, gestión de tráfico, gestión ambiental, control de intersección y semáforo), descrito mediante diagramas de interacción de sujetos y de comportamiento de sujetos, y ejecutado con herramientas de ejecución como SiSi. No se describe una muestra de usuarios, un protocolo de evaluación ni métricas de desempeño del modelo, y el caso 'se basa en varios estudios de ciudades inteligentes realizados en campo' sin detalle sobre su alcance, de modo que la reproducibilidad del demostrador depende de la descripción gráfica de los diagramas y de las herramientas de ejecución citadas (SiSi, Metasonic y UeberFlow), cuyo uso en el estudio solo se ilustra con una captura de pantalla.

**Resultados principales.** El estudio no reporta resultados cuantitativos. Muestra los diagramas de interacción de sujetos y de comportamiento del sistema de tráfico, su extensión a una segunda intersección con otros cuatro detectores, la incorporación de procesamiento de eventos complejos para tráfico y contaminación, y una captura de pantalla de la ejecución de un ciclo de control con el motor SiSi para verificar y validar la lógica de comportamiento. Los autores concluyen que el enfoque permite integración en profundidad y en amplitud, conectividad estandarizada por intercambio de mensajes, descomposición de operaciones complejas en entidades ejecutables y validables, validación de la corrección semántica y variabilidad de implementación entre actores humanos y tecnológicos. Una tabla vincula cada tipo de comportamiento con mecanismos del enfoque, por ejemplo guardas para eventos impredecibles e indeseables. Los autores no cuantifican ninguna mejora de desempeño, ni tiempos de especificación o ejecución, ni errores detectados en la validación, de manera que los resultados son demostraciones de capacidad conceptual y no medidas de efecto, lo que impide estimar beneficios en tiempo, costo o calidad del sistema. Se ilustra además que la validación puede ejecutarse antes de instanciar el sistema y que los modelos pueden reemplazarse en operación dentro de los límites de los diagramas de comportamiento, con intervención humana.

**Discusión y contribución.** Los autores sostienen que el modelado orientado a sujetos satisface los requisitos de un gemelo digital humano-comprensible porque separa el comportamiento de su implementación, permite ejecutar los modelos sin transformaciones y habilita la adaptación en operación con intervención humana. Argumentan que la comunicación basada en mensajes unifica componentes heterogéneos y que la validación previa reduce riesgos antes de la instanciación del CPS. Presentan la integración con procesamiento de eventos complejos como vía hacia comportamiento inteligente. El texto reconoce desafíos de flexibilidad en ecosistemas heterogéneos y señala que se requieren más casos para confirmar la generalidad del enfoque. La discusión no contrasta los resultados con enfoques alternativos de modelado ni con experiencias de campo.

**Limitaciones declaradas.** Declaradas: se necesitan más casos de aplicación para confirmar la generalidad; la flexibilidad en ecosistemas de componentes heterogéneos es un desafío. No declaradas: demostración con un sistema simulado y sin datos de campo; sin evaluación con usuarios de la comprensibilidad que se afirma; sin métricas de rendimiento, escalabilidad ni latencia; sin comparación con otros lenguajes de modelado (BPMN, SysML, UML); sin tratamiento de seguridad, calidad de datos de sensores ni fallos de conexión; fechas editoriales inconsistentes (recibido en octubre de 2022 y aceptado en abril de 2022).

**Trabajo futuro.** Explícito: más casos de aplicación para validar el enfoque y el análisis de requisitos adicionales para el desarrollo de CPS con gemelos digitales. Implícito: evaluación con usuarios, integración con datos reales de sensores y comparación con alternativas de modelado.

**Palabras clave.** Declaradas: Cyber-Physical System; Design-Integrated Engineering; Digital Twin; Modeling; Subject Orientation | Inferidas: gemelo digital, sistema ciberfísico, modelado orientado a sujetos, gestión de procesos de negocio, comportamiento predecible e impredecible, validación de modelos, gestión de tráfico, ingeniería integrada al diseño

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un gemelo digital de un sistema ciberfísico debe diseñarse como un modelo de comportamiento ejecutable y comprensible para los interesados, descrito como actores que se comunican por mensajes (modelado orientado a sujetos), de modo que se pueda validar antes de operar, adaptar en ejecución y asignar flexiblemente tareas a humanos o a tecnología; este enfoque integra componentes heterogéneos y cubre los cuatro tipos de comportamiento, incluidos los impredecibles.

**Antítesis identificada.** El artículo no aporta evidencia empírica de sus afirmaciones centrales. La comprensibilidad para personas con habilidades diagramáticas mínimas se afirma, pero no se mide con usuarios; la validación se limita a la ejecución de un ciclo de control de un sistema de tráfico de nueve sujetos, un caso de escala muy pequeña frente a las redes que justifican el discurso de ciudades inteligentes. La capacidad de manejar comportamiento impredecible se reduce a guardas y a umbrales predefinidos, de modo que lo impredecible se convierte en un caso anticipado. No se compara con alternativas de modelado ni se discuten los costos de especificar todos los mensajes explícitamente, que los autores mencionan como inconveniente al agregar detectores. Además, el gemelo descrito está acoplado a una simulación y no a datos reales con ruido, retraso o pérdida.

**Síntesis propuesta.** La contribución sostenible es conceptual: una forma de especificar el comportamiento de los componentes de un sistema ciberfísico y su interacción, con un lenguaje de pocos elementos, que permite ejecutar la especificación y discutirla con interesados no técnicos, y una lectura de la tipología de comportamiento que vincula las situaciones impredecibles con mecanismos de interrupción y adaptación. Para el corpus, el valor está en la idea de que un gemelo digital debe incluir reglas explícitas para fallos e interrupciones y en la participación humana en la adaptación, no en evidencia de desempeño ni en aplicación a infraestructura, desastres o empresas.

**Áreas grises detectadas.**

1. Evidencia de comprensibilidad: el criterio de diseño centrado en las personas exige que la notación sea utilizable con habilidades diagramáticas mínimas, pero el artículo no reporta ninguna prueba con usuarios, tiempos de aprendizaje o errores de interpretación; la afirmación se apoya en la simplicidad percibida de la notación.
2. Escala y realismo del demostrador: el caso de tráfico tiene nueve sujetos, luego se extiende a una segunda intersección con cuatro detectores y no se describe el volumen de mensajes, la latencia ni el comportamiento con datos reales de sensores; las referencias a estudios de campo de ciudades inteligentes no se detallan.
3. Tratamiento de lo impredecible: los comportamientos impredecibles indeseables se manejan con guardas y con eventos complejos con umbrales, es decir, con reglas que deben especificarse de antemano, de modo que la capacidad de absorber eventos realmente no previstos queda sin demostrar.
4. Relación con gemelos físicos: el artículo trata gemelos de comportamiento de sistemas ciberfísicos, no gemelos de estructuras o de procesos productivos; no se aclara cómo se integrarían datos de estado de activos físicos con el modelo de mensajes, ni cómo se sincroniza el estado cuando falla la conectividad.

**Puntos oscuros aclarados.** Llama la atención que el artículo afirme viabilidad y practicabilidad del enfoque sin reportar ningún dato de aplicación real, y que las fechas editoriales sean incoherentes (recibido el 31 de octubre de 2022 y aceptado el 14 de abril de 2022), lo que sugiere descuido en la revisión del manuscrito. También es notable que se defienda la participación humana en la adaptación y la comprensibilidad por parte de interesados sin experiencia, pero la evaluación del enfoque con tales interesados esté ausente. Los autores reconocen que declarar explícitamente cada mensaje es un inconveniente cuando se añaden detectores, lo cual cuestiona la escalabilidad del enfoque sin abordar el problema con generación automática o con plantillas. La tipología de comportamiento citada de Grieves y Vickers se presenta como marco central, pero las categorías impredecibles quedan reducidas a ejemplos ilustrativos de tráfico. Por último, el título anuncia diseño centrado en el comportamiento para el desarrollo dinámico de sistemas ciberfísicos, mientras el artículo documenta un solo ejemplo de gestión de tráfico simulado.

**Ideas propositivas novedosas.**

1. Plantilla de comportamiento para gemelos de empresas ante interrupciones: adaptar la tipología de comportamiento (predecible o impredecible, deseable o indeseable) a la continuidad de una planta productiva tras un sismo, definiendo para cada tipo qué mensajes entre sensores, proveedores, personal y servicios públicos deben especificarse y qué guardas permiten interrumpir procesos. El resultado sería un catálogo de eventos y reglas de interrupción que una pyme puede revisar sin conocimientos de modelado y que sirve como base de un gemelo mínimo de recuperación. La validación consistiría en simular tres escenarios de interrupción (corte eléctrico, cierre de acceso, pérdida de proveedor) y registrar si el catálogo cubre las decisiones que los gestores toman en la práctica y cuáles eventos quedan sin regla.
2. Evaluación comparada de comprensibilidad en contexto de emergencia: diseñar un experimento con 20 a 30 gestores de pymes que interpreten y modifiquen modelos de comportamiento orientados a sujetos frente a un diagrama de flujo convencional, midiendo errores, tiempos y confianza en un escenario de falla de conectividad. Esto pondría a prueba la afirmación central de comprensibilidad y aportaría evidencia comparable entre notaciones sobre si el enfoque es adecuado para entornos de recuperación tras desastres, donde los operadores trabajan con información incompleta.

**Relaciones poco exploradas.**

1. Gemelo de comportamiento (complementa) los gemelos de estado estructural del corpus (D034, D035): mientras estos modelan daño y respuesta de edificios y puentes con datos físicos, D038 aporta una forma de especificar la lógica de decisión y de interrupción que usaría un gemelo al operar, aunque sin integración con modelos físicos.
2. Participación humana en la adaptación (converge con) los estudios de gobernanza y resiliencia organizacional del corpus (D029, D037): D038 propone mantener a las personas en el ciclo de adaptación, y D037 concluye que en entornos digitalmente maduros la gobernanza pesa más que la tecnología; ninguno mide el efecto sobre la recuperación.

**Robustez argumentativa:** 2.1/10 (ponderación 30/30/25/15) — consistencia lógica 2/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 4/10 — Ofrece un enfoque metodológico para especificar gemelos digitales de comportamiento, con un lenguaje mínimo, ejecutable y adaptable con participación humana, y una lectura útil de la tipología de comportamiento ante eventos impredecibles. Su valor para el corpus es periférico porque no trata sismos, empresas ni recuperación, y porque la demostración es un ejemplo de tráfico sin datos reales ni evaluación con usuarios; sirve como referencia metodológica para diseñar reglas de interrupción y de adaptación de gemelos de continuidad.

**Conexiones inter-documentales.**

- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 43 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Afirmación sin evidencia (Se declara que el enfoque es comprensible con habilidades diagramáticas mínimas, sin ninguna prueba con usuarios (Sec. 2, p. 3; Sec. 4.5, p. 17-18)); Generalización apresurada (Se infiere factibilidad y practicabilidad para sistemas ciberfísicos complejos a partir de un ejemplo de tráfico de nueve sujetos (Resumen, p. 1; Sec. 4.3, p. 10)); Apelación a la novedad / a la tecnología (Se presentan las promesas del gemelo digital para la innovación empresarial sin evaluar beneficios ni costos (Sec. 5, p. 18))
- **Bradford-Hill:** No aplica: es un artículo de diseño conceptual; no estima relación causal alguna entre el uso del enfoque y mejoras en desarrollo, operación o resiliencia de sistemas.
- **TRL asignado:** 3 — 'Figure 9 shows the use of the Sisi execution engine in order to first verify and then validate the behavior logic of the traffic management system' (p. 16)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (22 páginas con referencias). Las figuras de diagramas S-BPM no son legibles en la extracción. Las fechas 'Received: 31 October 2022; Accepted: 14 April 2022' aparecen así en el documento.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un gemelo digital de un sistema ciberfísico debe diseñarse como un modelo de comportamiento ejecutable y comprensible para los interesados, descrito como actores que se comunican por mensajes (modelado orientado a sujetos), de modo que se pueda validar antes de operar, adaptar en ejecución y asignar flexiblemente tareas a humanos o a tecnología; este enfoque integra componentes heterogéneos y cubre los cuatro tipos de comportamiento, incluidos los impredecibles.  | El artículo no aporta evidencia empírica de sus afirmaciones centrales. La comprensibilidad para personas con habilidades diagramáticas mínimas se afirma, pero no se mide con usuarios; la validación se limita a la ejecución de un ciclo de control de un sistema de tráfico de nueve sujetos, un caso de escala muy pequeña frente a las redes que justifican el discurso de ciudades inteligentes. La capacidad de manejar comportamiento impredecible se reduce a guardas y a umbrales predefinidos, de modo que lo impredecible se convierte en un caso anticipado. No se compara con alternativas de modelado ni se discuten los costos de especificar todos los mensajes explícitamente, que los autores mencionan como inconveniente al agregar detectores. Además, el gemelo descrito está acoplado a una simulación y no a datos reales con ruido, retraso o pérdida.  | La contribución sostenible es conceptual: una forma de especificar el comportamiento de los componentes de un sistema ciberfísico y su interacción, con un lenguaje de pocos elementos, que permite ejecutar la especificación y discutirla con interesados no técnicos, y una lectura de la tipología de comportamiento que vincula las situaciones impredecibles con mecanismos de interrupción y adaptación. Para el corpus, el valor está en la idea de que un gemelo digital debe incluir reglas explícitas para fallos e interrupciones y en la participación humana en la adaptación, no en evidencia de desempeño ni en aplicación a infraestructura, desastres o empresas.  | 2.1/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Gemelo digital' es un modelo sincronizado de estructura, función y comportamiento de una entidad física; 'comportamiento' es la secuencia de acciones y mensajes de actores humanos o artificiales; 'subject' es un actor que ejecuta acciones y se comunica.
- **P2 Supuestos:** Supone que un modelo de pocos elementos es comprensible para interesados no técnicos, que el comportamiento de sistemas heterogéneos se puede encapsular como intercambio de mensajes y que lo impredecible se puede cubrir con guardas y eventos complejos.
- **P3 Evidencia:** La evidencia es un ejemplo de un sistema de tráfico de nueve sujetos, con diagramas y una captura de pantalla de ejecución, sin datos medidos, sin usuarios y sin comparación con otros enfoques.
- **P4 Consecuencias:** Si es cierto, los equipos pueden diseñar, validar y adaptar gemelos con participación de interesados; si es falso, pueden construir modelos que solo especialistas interpretan y que no resisten eventos reales no previstos.
- **P5 Contraejemplos:** No se examinan despliegues reales, fallos de comunicación, calidad de datos de sensores, escalabilidad con cientos de sujetos ni la comparación con BPMN, SysML u otros lenguajes.
- **P6 Alternativas:** Alternativas: que un lenguaje estándar con herramientas más difundidas logre los mismos resultados; que el cuello de botella sea la calidad de los datos y no el modelado de comportamiento; que la comprensión del modelo dependa más del entrenamiento que de la notación.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Sujetos en el demostrador de tráfico | 9 | sujetos | Cuatro detectores, colector, gestión de tráfico, gestión ambiental, control de intersección y semáforo | Sec. 4.3, p. 10 | Texto | Alta | Sistema simulado |
| Detectores añadidos en la extensión | 4 | detectores | Segunda intersección del sistema de tráfico | Sec. 4.3, p. 12-13 | Texto | Alta | Extensión conceptual |
| Ciclos de diseño presentados | 3 | ciclos | Especificación, situaciones excepcionales y comportamiento inteligente | Sec. 2, p. 4 | Texto | Alta | Ciencia del diseño |
| Tipos de comportamiento considerados | 4 | categorías | Predecible o impredecible, deseable o indeseable | Sec. 3.2, p. 5-6 | Texto | Alta | Tomado de Grieves y Vickers |
| Dimensiones del gemelo digital citadas | 5 | dimensiones | Entidad física, virtual, servicios, datos y conexión | Sec. 3.3, p. 7 | Texto | Alta | Tomado de Wu et al. |
| Dimensiones de capacidad del gemelo analizadas | 5 | dimensiones | Profundidad y amplitud de integración, conectividad, inteligencia, validación y variabilidad de implementación | Sec. 4.4, p. 13 | Texto | Media | Marco propio |
| Resultados cuantitativos de desempeño | 0 | métricas | El artículo no reporta tiempos, latencias ni errores | Sec. 4, p. 10-18 | Texto | Alta | Ausencia verificada |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'Figure 9 shows the use of the Sisi execution engine in order to first verify and then validate the behavior logic of the traffic management system' (p. 16) | Prueba de concepto en simulación con un ciclo de control; sin datos de campo ni despliegue. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'DTs bring about the promise to help improve business operation and facilitate recognizing innovation opportunities' (p. 18) | Promesa de valor sin análisis de mercado, costos ni modelo de negocio. |
| IRL | 3 | Sí | 'The connectivity is standardized through message exchanging, and thereby, allows coupling of heterogeneous components' (p. 18) | Integración descrita por intercambio de mensajes en un ejemplo; sin pruebas con dispositivos reales ni con interfaces industriales. |
| DRL | 2 | Sí | 'for smart city operation traffic organizers, emergency services, facility and road management, drivers, and many other stakeholders are involved' (p. 2) | Necesidad argumentada de forma conceptual por la diversidad de interesados; sin demanda medida de usuarios. |
| SRL | 1.17 | Sí | Componentes: Modelo de comportamiento orientado a sujetos (TRL 3), Motor de ejecución y validación (SiSi) (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 10.5; ÷9 → 1.17; nivel acotado a [1,9] = 1.17 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 3 con BRL 1 e IRL 3: prueba de concepto sin datos reales, sin evaluación con usuarios y sin análisis de costos. · Estrategia de salida: Pilotos con sensores reales, evaluación con usuarios no especialistas y comparación con lenguajes de modelado alternativos.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Afirmación sin evidencia | Se declara que el enfoque es comprensible con habilidades diagramáticas mínimas, sin ninguna prueba con usuarios (Sec. 2, p. 3; Sec. 4.5, p. 17-18) | Criterio de diseño tratado como resultado |
| Generalización apresurada | Se infiere factibilidad y practicabilidad para sistemas ciberfísicos complejos a partir de un ejemplo de tráfico de nueve sujetos (Resumen, p. 1; Sec. 4.3, p. 10) | Escala del caso insuficiente para el alcance declarado |
| Apelación a la novedad / a la tecnología | Se presentan las promesas del gemelo digital para la innovación empresarial sin evaluar beneficios ni costos (Sec. 5, p. 18) | Beneficio asumido |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Modelado de comportamiento ejecutable → validación previa y menor riesgo de falla del CPS | Argumento de diseño con un ejemplo ilustrativo | Plausibilidad | Fuerza, comparación, experimento | Calidad de requisitos, competencia del equipo, complejidad del sistema | 1 | Hipótesis no probada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Evaluación empírica con usuarios y comparación con alternativas de modelado | Crítico | Media | 8 |
| Tecnológico | Integración con datos reales de sensores, pérdida de conectividad y escalabilidad | Crítico | Media | 8 |
| Conocimiento | Aplicación a gemelos de continuidad ante desastres y a empresas pequeñas | Crítico | Media | 8 |
| Mercado | Costos de especificación y mantenimiento de los modelos de comportamiento | Significativo | Baja | 6 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Tabla 1 | Tipos de comportamiento del gemelo según Grieves y Vickers | Tabla | Predecible o impredecible, deseable o indeseable | 4 categorías | Alta |
| Fig. 2 | Estructura de comunicación del sistema de gestión de tráfico | Diagrama | Nueve sujetos y sus mensajes | 9 sujetos | Alta |
| Fig. 3 | Diagrama de interacción de sujetos | Diagrama | Sujetos y mensajes | No aplica | Media |
| Fig. 4 | Comportamiento del sujeto de detección de vehículos | Diagrama | Secuencia de acciones y guardas | No aplica | Media |
| Fig. 6 | Sistema de tráfico extendido | Diagrama | Segunda intersección y cuatro detectores adicionales | 4 detectores | Media |
| Fig. 9 | Captura de pantalla de la ejecución SiSi | Captura de pantalla | Ciclo de control de tráfico | No aplica | Media |
| Tabla 2 | Captura de tipos de comportamiento en el desarrollo de CPS | Tabla | Mecanismos del enfoque por tipo | 4 categorías | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Enfoques basados en modelos con UML para generar sistemas de información del gemelo (citados en la Sec. 3.3) | No especificado en documento | Academia | Generación automática de la conexión entre CPS y gemelo | Automatización y estandarización | Menor comprensibilidad para no especialistas | Estable |
| Modelado empresarial y gestión de capacidades (Sandkuhl et al.) | No especificado en documento | Academia | Aspectos organizacionales de gemelos | Perspectiva de negocio | Sin ejecución | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** No aplica: no hay variable de resultado estimada
- **X:** No aplica
- **Z (controles):** No aplica
- **Datos:** Ejemplo ilustrativo de gestión de tráfico con nueve sujetos; sin datos observados
- **Método:** Ciencia del diseño con caso de demostración
- **Efecto reportado:** No estimado
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin evaluación empírica ni análisis de sensibilidad

| Vacío | Tipo | Descripción |
|---|---|---|
| V-038-01 | TERR | Sin territorio definido; los autores son de Austria y Alemania y el ejemplo es genérico de ciudad inteligente |
| V-038-02 | POBL | Sin usuarios, empresas ni población definida; se mencionan interesados de forma genérica |
| V-038-03 | TEMP | Sin horizonte temporal ni evaluación longitudinal |
| V-038-04 | MET | Sin evaluación con usuarios, métricas de desempeño ni comparación con alternativas |
| V-038-05 | VAR | Faltan variables de latencia, escalabilidad, costos y calidad de datos |
| V-038-06 | TEOR | Teoría de comunicación de actores y ciencia del diseño; sin teoría de resiliencia ni de recuperación |
| V-038-07 | CAUS | Sin evidencia causal sobre el efecto del enfoque en el desarrollo o la operación de sistemas |
