# FB-L01-080 | D080 — A Digital Twin Approach to Sustainable Disaster Management: Case of Cayirova

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/sustainability-17-09626.pdf` · 24 páginas · Relevancia para el eje del corpus: **Núcleo** (Desarrolla un gemelo digital de código abierto para la gestión de desastres sísmicos en el distrito industrial de Çayırova (Kocaeli, Türkiye), que integra datos geoespaciales, de edificios, demográficos y de una red de sensores IoT (acelerómetros, galgas, sensores ambientales y de energía) en una base PostGIS, con paneles de riesgo sísmico, simulación de escenarios (Mw ≥ 7,0) y alineación con los ODS 9, 11, 13 y 17. Reúne gemelo digital, IoT, sismo, respuesta y recuperación en un caso real financiado por el municipio, que es el núcleo de la temática del corpus, aunque las cifras de desempeño (87 % de exactitud, 99,2 % de disponibilidad) se informan sin método ni línea base.)

> Copia idéntica (MD5) en: `WOS_Tejido Empresarial/sustainability-17-09626.pdf`

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-080 / D080
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Korkmaz, M., Akyildiz, Y. E., Demirkesen, S., Toprak, S., Nowak, P., & Ciftci, B. (2025). A Digital Twin Approach to Sustainable Disaster Management: Case of Cayirova. *Sustainability (Switzerland)*, *17*(21), Article 9626. https://doi.org/10.3390/su17219626
- **Autores:** Korkmaz, Mustafa (57203318277); Akyildiz, Yasemin Ezgi (60191314800); Demirkesen, Sevilay (56331319900); Toprak, Selcuk (6603885431); Nowak, Paweł (56527884300); Ciftci, Bunyamin (60190913800)
- **Afiliaciones:** Department of Civil Engineering, Igdir University, Igdir, 76000, Turkey; Department of Civil Engineering, Gebze Technical University, Gebze, 41400, Turkey; Civil Engineering Faculty, Division of Production Engineering and Construction Management, Warsaw University of Technology, Warsaw, 00-661, Poland
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Sustainability (Switzerland) · vol. 17(21)
- **Identificador persistente:** DOI 10.3390/su17219626 · ISSN 20711050
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105021551129&doi=10.3390%2fsu17219626&partnerID=40&md5=c61a0164d719d911945bc7a00e063436
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 12

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Desarrollar un marco de gemelo digital (DT) de código abierto para la gestión de desastres sísmicos en el distrito de Çayırova, en Kocaeli (Türkiye), una de las regiones más activas sísmicamente del país, con el fin de reforzar la resiliencia local integrando datos de múltiples fuentes en un entorno digital unificado que apoye la evaluación de riesgo, la planificación de respuesta y la coordinación de la recuperación. El modelo busca servir como base de datos digital de respaldo en emergencias, contribuir a prácticas urbanas sostenibles, reducir el número de personas afectadas y las pérdidas económicas directas, y alinear las decisiones con los objetivos de desarrollo sostenible.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Sus tres propósitos declarados son diseñar y presentar un gemelo digital de código abierto para la gestión de desastres centrada en terremotos en Çayırova, demostrar cómo puede apoyar la evaluación del riesgo sísmico y la planificación para reducirlo y alinear los procesos de decisión con los ODS pertinentes.

**Marco teórico.** El marco combina el ciclo de gestión de desastres (mitigación, preparación, respuesta y recuperación), la definición de gemelo digital como modelo virtual actualizado con datos en tiempo real y los ODS. Los autores sostienen que los estudios de gemelos se concentran en grandes metrópolis con infraestructura de datos extensa (Londres, Singapur, Shanghái), que las ciudades pequeñas y medianas industriales están subrepresentadas y que la mayoría de los trabajos se limita a arquitecturas conceptuales o visualizaciones sin flujos operativos de gestión del riesgo. Se vincula el gemelo con las metas 11.5 y 11.B, 13.1, 9.1 y 9.4 y 17.6 y 17.17, y se reconocen riesgos de calidad de datos, dependencia de la nube, costos y continuidad en emergencias.

**Metodología.** El estudio adopta un estudio de caso con métodos mixtos de análisis espacial, simulación y evaluación cualitativa. El hardware es híbrido: una estación de trabajo local (procesador Ryzen 9 7950X, tarjeta RTX 4070 Ti, 64 GB de memoria y 2 TB de almacenamiento) y un servidor en la nube (8 CPU virtuales, 32 GB y 1 TB) con PostGIS en AWS o DigitalOcean. El modelo se construye con QGIS y Autodesk InfraWorks con simulación en Unreal Engine. El flujo de datos integra cinco familias de entrada (vectoriales, ráster, 3D, nubes de puntos y tabulares/demográficas) en un esquema por etapas, armonizadas a UTM 35N y WGS 84, con un identificador estable de edificio, interpolación areal ponderada para desagregar datos del censo, imputación jerárquica de atributos faltantes, bitácora de procedencia y vistas materializadas. La red de sensores propuesta incluye acelerómetros, galgas y medidores de desplazamiento, sensores ambientales y medidores de energía que transmiten por LoRaWAN, Wi-Fi o 5G y MQTT, con puertas de enlace de borde tipo Raspberry Pi o Jetson Nano.

**Resultados principales.** Los resultados se presentan como el funcionamiento del modelo y tableros: capturas del modelo, un tablero de riesgo sísmico con detecciones, réplicas, pronósticos probabilísticos e indicadores de respuesta, un tablero de gestión de la infraestructura IoT, un tablero de simulación de escenarios (deterministas y probabilísticos, incendios posterremoto y fallas de infraestructura) con daño predicho, tiempo de respuesta y recomendaciones automáticas de evacuación y recursos médicos, y un panel de atributos por edificio con índices de vulnerabilidad. En un escenario sísmico con magnitud mayor o igual a 7,0, el modelo indica que alrededor de 18 % de los edificios de concreto reforzado de mediana altura sufre daño de menor a moderado, en particular en zonas residenciales anteriores al año 2000, que los corredores de transporte críticos se mantienen funcionales, que la exactitud entre daño simulado y observado es de 87 % y que la disponibilidad fue de 99,2 % en pruebas de varios usuarios con cinco escenarios concurrentes. El texto concluye que las prioridades deben ser la inspección rápida de edificios y las unidades móviles y no las evacuaciones masivas. No se explican la fuente del daño observado, la métrica de exactitud ni el número de sensores instalados. El modelo se describe como en funcionamiento sobre el distrito.

**Discusión y contribución.** Los autores sostienen que el estudio implementó con infraestructura concreta de hardware y software los enfoques conceptuales de la literatura, que el sistema va más allá de un SIG tradicional porque recalibra parámetros con datos de sensores y ofrece retroalimentación entre el nivel digital y el físico, que la arquitectura híbrida de estación local y nube permite simulaciones de alta fidelidad y acceso de varios usuarios, y que la alineación con los ODS convierte al gemelo en habilitador estratégico de sostenibilidad y resiliencia. Reconocen que el despliegue masivo de sensores exige considerar costo, mantenimiento y confiabilidad de red, que la nube introduce dependencias y costos y riesgos en emergencias, que la calidad de los datos determina la exactitud y que la integración con los ODS es indicativa y no cuantifica impactos de largo plazo.

**Limitaciones declaradas.** Declaradas: la exactitud depende de la calidad y de la resolución temporal de los datos, que varían entre municipios; el costo, el mantenimiento y la confiabilidad de la red de sensores; la dependencia de la nube en términos de seguridad, costo y continuidad durante emergencias; el modelo prioriza escalabilidad y accesibilidad frente a la fidelidad de la simulación; la vinculación con los ODS es indicativa y no cuantifica impactos de largo plazo; la analítica predictiva y el aprendizaje automático quedan para trabajo futuro. No declaradas: la exactitud de 87 % entre daño simulado y observado no tiene definición de métrica, evento observado, muestra ni método de comparación, y el artículo trata un escenario hipotético de magnitud 7,0; la disponibilidad de 99,2 % se mide en pruebas de laboratorio de cinco escenarios y no refleja operación en una emergencia; la integración de datos en vivo de sensores se presenta como propuesta y como capacidad actual en secciones distintas; se denomina de código abierto a un sistema que usa software propietario (InfraWorks, Unreal Engine) y cuyos datos se ofrecen bajo consentimiento del municipio financiador; no hay costos de desarrollo ni de operación; el estudio fue financiado por el municipio caso y declara no tener conflictos de interés; no se modelan las empresas ni las cadenas de suministro de la zona industrial.

**Trabajo futuro.** Explícito: mejorar la interoperabilidad de datos con estándares nacionales e internacionales, integrar inteligencia artificial y analítica predictiva para pronóstico adaptativo del riesgo, y medir los impactos ambientales y sociales de largo plazo de los gemelos para gestión de desastres, con métricas de contribución a los indicadores de los ODS. Implícito: validación con eventos reales, datos en vivo de la red de sensores y módulos de interrupción empresarial.

**Palabras clave.** Declaradas: digital model; digital twin; disaster management; seismic risks | Inferidas: gemelo digital, gestión de desastres, riesgo sísmico, IoT, QGIS, InfraWorks, PostGIS, ODS, Çayırova, resiliencia urbana

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un gemelo digital de código abierto para un distrito industrial de tamaño medio, construido con datos geoespaciales, de edificios y demográficos, una red de sensores IoT y una arquitectura híbrida de estación local y nube, permite simular escenarios sísmicos (Mw ≥ 7,0) con una exactitud de 87 % frente a daño observado, mantener 99,2 % de disponibilidad con varios usuarios y apoyar la respuesta, la recuperación y la planificación alineadas con los ODS, de modo que ofrece un modelo replicable para ciudades fuera de las grandes metrópolis.

**Antítesis identificada.** Las cifras que sustentan la tesis carecen de método: no se define la métrica de exactitud, no se identifica el evento observado con el que se compara un escenario hipotético, y la disponibilidad se mide en pruebas de laboratorio. El artículo propone la integración de sensores y a la vez describe tableros con detecciones en vivo, de modo que no queda claro si hay datos reales en operación. El sistema se declara de código abierto, pero depende de software propietario y de datos sujetos a consentimiento del municipio que financió el estudio. No hay costos, ni modelo de interrupción de empresas pese a tratarse de una zona industrial, y la conclusión de que las prioridades son la inspección y las unidades móviles y no las evacuaciones proviene del modelo no validado. La alineación con los ODS es declarativa.

**Síntesis propuesta.** La contribución sostenible es una arquitectura operativa, con pipeline de datos documentado, bitácora de procedencia, tableros y un diseño de red de sensores, para un distrito industrial de tamaño medio, que muestra cómo integrar geodatos, inventario de edificios y simulación en una plataforma accesible. Para el corpus, es la pieza que más se acerca a la unión de gemelo digital, IoT, sismo y recuperación en un caso real, y su valor está en el diseño de datos y en la agenda que deja abierta, más que en las cifras de desempeño, que no se pueden evaluar. Su utilidad para la recuperación empresarial requiere validación contra un evento real, publicación de la métrica y de los datos, y módulos de interrupción de empresas y de cadenas de suministro.

**Áreas grises detectadas.**

1. Exactitud de 87 %: el texto afirma una alta exactitud de predicción entre daño simulado y observado, pero no define la métrica (por edificio, por estado de daño o por zona), no identifica el evento sísmico con daño observado ni el número de edificios comparados, y el escenario evaluado es un terremoto hipotético de magnitud mayor o igual a 7,0, de modo que la cifra no puede interpretarse.
2. Estado real de la red de sensores: la sección de diseño indica que el estudio propone integrar adquisición en tiempo real con sensores y describe la integración de datos en vivo como extensión futura, mientras que los resultados y la discusión describen detecciones en vivo, retroalimentación en tiempo real y recalibración continua; no se indica cuántos sensores existen, dónde están ni qué datos mostraron.
3. Naturaleza de código abierto y acceso a datos: el título del objetivo habla de un sistema de código abierto, pero el modelo usa Autodesk InfraWorks y Unreal Engine, y los datos se entregan a solicitud con el consentimiento del municipio de Çayırova, que financió la investigación; no se indica qué componentes y datos están disponibles públicamente.
4. Pruebas de disponibilidad: la disponibilidad de 99,2 % se refiere a pruebas de estrés con cinco escenarios concurrentes, sin duración, carga, tipo de fallas ni condiciones de red, y el propio texto reconoce que la dependencia de la nube puede ser crítica cuando la comunicación se interrumpe en emergencias.

**Puntos oscuros aclarados.** Llama la atención que el resumen presente el modelo como esperado para crear cadenas logísticas sostenibles y reducir pérdidas económicas, mientras que los resultados no incluyen ninguna estimación económica ni de interrupción productiva pese a tratarse de un distrito industrial. También es notable que el texto describa un tablero de riesgo con eventos y réplicas recientes y pronósticos probabilísticos de sismos secundarios sin explicar el origen de esos datos, y que el panel se titule con el nombre de la provincia y no del distrito. La conclusión de que el sistema reduce los tiempos de respuesta y minimiza pérdidas humanas y materiales no tiene medición. El financiamiento del municipio objeto del estudio y la declaración de ausencia de conflictos de interés conviven con la entrega de datos condicionada a su consentimiento. Además, la introducción sostiene que el gemelo identifica poblaciones marginadas e integra datos demográficos, pero la desagregación del censo a edificios se hace por interpolación areal, sin evaluación de error. Por último, la definición de gemelo adoptada exige un modelo que actualiza con datos en tiempo real, y el artículo la aplica sin mostrar los datos.

**Ideas propositivas novedosas.**

1. Validación del escenario con el terremoto de Kocaeli de 1999 o con un evento reciente: construir una tabla de daño observado por edificio (inspecciones de seguridad posterremoto) para una muestra de 500 o más edificios del distrito, ejecutar el escenario correspondiente en el gemelo y reportar la matriz de confusión por estado de daño, la exactitud y el índice kappa con intervalos de confianza. El resultado mostraría si la exactitud de 87 % se mantiene con una métrica definida, qué estados de daño se confunden y si el modelo sirve para priorizar inspecciones y para el cálculo del tiempo de cierre de edificios.
2. Módulo de interrupción productiva y piloto de sensores: añadir al gemelo atributos de las empresas de la zona industrial (actividad, empleados, dependencia de energía y de proveedores, existencias peligrosas) y vincular el daño por edificio con días de cierre y pérdidas de producción, con una instalación piloto de 10 a 20 sensores durante seis meses que mida latencia, falsos disparos y disponibilidad real de la red. Con esto se podría estimar la pérdida por interrupción en escenarios de magnitud 6,5 y 7,0 y calcular cuánto reduce un orden de inspección priorizado el tiempo de reapertura, información para empresas y municipios sobre el valor del gemelo.

**Relaciones poco exploradas.**

1. Gemelos comunitarios y revisiones de ciudades inteligentes (complementa) D078 y D079: D078 presenta un gemelo comunitario para tornados con datos públicos y D079 revisa los gemelos urbanos y su falta de evidencia de retorno; D080 aporta un caso sísmico con IoT y un pipeline de datos documentado.
2. Gemelo sísmico con sensores y red (se relaciona con) D064 y D073: D064 diseña un gemelo para edificios con 5G y retardos medidos y D073 mide la latencia de alerta con IoT y nube; D080 propone usar LoRaWAN, 5G, MQTT y puertas de enlace de borde en un distrito industrial, sin medir latencias.

**Robustez argumentativa:** 2.1/10 (ponderación 30/30/25/15) — consistencia lógica 2/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 7/10 — Aporta una arquitectura completa de gemelo digital sísmico para un distrito industrial de tamaño medio, con pipeline de datos de cinco familias, bitácora de procedencia, red de sensores y tableros de riesgo y escenarios, financiada por el municipio caso y alineada con cuatro ODS. Su valor para el corpus es alto por reunir gemelo digital, IoT, sismo y recuperación en un caso real, y se reduce porque la exactitud de 87 % y la disponibilidad de 99,2 % carecen de método, la red de sensores aparece como propuesta y como operativa, el sistema declarado de código abierto usa software propietario y no hay costos ni modelo de interrupción empresarial.

**Conexiones inter-documentales.**

- **EXTIENDE** D048 (Gemelo digital como imagen operativa común para respuesta sísmica): replica la lógica de imagen operativa común en un distrito industrial con sensores IoT y arquitectura híbrida; comparte autoría (Korkmaz, Demirkesen) con D048, por lo que no es una confirmación independiente [juicio del analista; citación verificada de D080 a D048; autoría compartida]
- **DEPENDE_DE** D006 (Gemelo digital para gestión de desastres e inteligencia artificial): retoma la propuesta de gemelo digital de ciudad en desastre como referencia conceptual [juicio del analista; citación verificada de D080 a D006]
- **PRECEDE** D101 (Síntesis automática: gemelos digitales, Industria 4.0 y resiliencia po): relación inversa de D101 DEPENDE_DE D080: la tercera referencia de D101 es el estudio de caso de Cayirova (D080) [juicio del analista]
- **DEPENDE_DE** D072 (Gemelo digital para gestión de desastres con modelado híbrido y simili): cita a D072 en su lista de referencias (verificado por coincidencia de título); D072: Gemelo digital para gestión de desastres con modelado híbrido y simili [citación verificada]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 19 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Cifra de exactitud sin método (Se afirma 87 % de exactitud entre daño simulado y observado para un escenario hipotético (Sec. 4, p. 19; Sec. 5, p. 21)); Propuesta presentada como capacidad operativa (La integración de sensores se propone en el diseño y se describe como funcionando en resultados y discusión (Sec. 2.2.2, p. 13; Sec. 3, p. 15; Sec. 4, p. 19)); Etiqueta de código abierto con componentes propietarios (Se declara un gemelo de código abierto que usa software propietario y datos sujetos a consentimiento (Resumen, p. 1; Sec. 2.2.1, p. 10; Data Availability, p. 22))
- **Bradford-Hill:** No aplica: es un estudio de desarrollo con simulación; no se estima causalidad con datos observacionales.
- **TRL asignado:** 4 — 'providing a flexible foundation for future extensions, including live IoT data integration and AI-driven risk assessment' (p. 11)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (24 páginas). Las tablas y listas se leyeron con saltos de línea; las cifras se tomaron de los párrafos de la discusión y las conclusiones. El nombre del panel (Kocaeli Seismic Risk Dashboard) se cita tal como aparece. Las páginas siguen los marcadores del PDF.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un gemelo digital de código abierto para un distrito industrial de tamaño medio, construido con datos geoespaciales, de edificios y demográficos, una red de sensores IoT y una arquitectura híbrida de estación local y nube, permite simular escenarios sísmicos (Mw ≥ 7,0) con una exactitud de 87 % frente a daño observado, mantener 99,2 % de disponibilidad con varios usuarios y apoyar la respuesta, la recuperación y la planificación alineadas con los ODS, de modo que ofrece un modelo replicable para ciudades fuera de las grandes metrópolis.  | Las cifras que sustentan la tesis carecen de método: no se define la métrica de exactitud, no se identifica el evento observado con el que se compara un escenario hipotético, y la disponibilidad se mide en pruebas de laboratorio. El artículo propone la integración de sensores y a la vez describe tableros con detecciones en vivo, de modo que no queda claro si hay datos reales en operación. El sistema se declara de código abierto, pero depende de software propietario y de datos sujetos a consentimiento del municipio que financió el estudio. No hay costos, ni modelo de interrupción de empresas pese a tratarse de una zona industrial, y la conclusión de que las prioridades son la inspección y las unidades móviles y no las evacuaciones proviene del modelo no validado. La alineación con los ODS es declarativa.  | La contribución sostenible es una arquitectura operativa, con pipeline de datos documentado, bitácora de procedencia, tableros y un diseño de red de sensores, para un distrito industrial de tamaño medio, que muestra cómo integrar geodatos, inventario de edificios y simulación en una plataforma accesible. Para el corpus, es la pieza que más se acerca a la unión de gemelo digital, IoT, sismo y recuperación en un caso real, y su valor está en el diseño de datos y en la agenda que deja abierta, más que en las cifras de desempeño, que no se pueden evaluar. Su utilidad para la recuperación empresarial requiere validación contra un evento real, publicación de la métrica y de los datos, y módulos de interrupción de empresas y de cadenas de suministro.  | 2.1/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'SRDT' (Seismic Risk Digital Twin) es el gemelo de riesgo sísmico de Çayırova; 'exactitud de 87 %' es la coincidencia entre daño simulado y observado, sin métrica definida; 'disponibilidad' es la proporción de tiempo en que el sistema respondió en la prueba de varios usuarios; 'datos en tiempo real' son los flujos de sensores por MQTT.
- **P2 Supuestos:** Supone que un escenario hipotético puede compararse con daño observado, que las pruebas de laboratorio representan la disponibilidad en una emergencia, que los datos de sensores están integrados y que el código abierto y el acceso a datos son compatibles con su operación.
- **P3 Evidencia:** La evidencia son capturas de tableros, una descripción del pipeline y del hardware, un escenario de magnitud mayor o igual a 7,0 y tres cifras (18 %, 87 % y 99,2 %) sin método.
- **P4 Consecuencias:** Si es cierto, el municipio puede priorizar inspecciones y unidades móviles con datos y simulaciones; si es falso, la cifra de exactitud puede no representar el desempeño y la plataforma puede quedar inoperante cuando falle la nube o la red.
- **P5 Contraejemplos:** No se examinan la métrica de exactitud, el evento observado, el número de sensores, los costos, la interrupción de empresas ni el desempeño sin conectividad.
- **P6 Alternativas:** Alternativas: que una herramienta de SIG con curvas de fragilidad dé resultados similares a menor costo; que el valor principal esté en la integración de datos y no en la simulación; que la operación sin nube sea más importante que la sofisticación.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Exactitud entre daño simulado y observado | 87 | % | Escenario sísmico de magnitud mayor o igual a 7,0 | Sec. 4, p. 19; Sec. 5, p. 21 | Texto | Baja | Métrica y evento observado no definidos |
| Disponibilidad en pruebas de varios usuarios | 99,2 | % | Cinco escenarios concurrentes | Sec. 4, p. 19; Sec. 5, p. 21 | Texto | Baja | Pruebas de laboratorio |
| Edificios de concreto de mediana altura con daño menor a moderado | 18 | % | Más frecuente en zonas anteriores al año 2000 | Sec. 4, p. 19 | Texto | Media | Resultado del modelo |
| Familias de datos integradas | 5 | familias | Vectoriales, ráster, 3D, nubes de puntos y tabulares | Sec. 2.2.2, p. 11 | Texto | Alta | Esquema por etapas en PostGIS |
| Tipos de sensores de la red propuesta | 4 | tipos | Acelerómetros, galgas y desplazamiento, ambientales y medidores de energía | Sec. 2.2.2, p. 13 | Texto | Media | Cantidad de sensores no reportada |
| Protocolos de comunicación de los sensores | 3 | protocolos | LoRaWAN, Wi-Fi o 5G y MQTT | Sec. 2.2.1, p. 10 | Texto | Alta | Latencias no medidas |
| Capacidad del servidor en la nube | 8 CPU y 32 GB | recursos | 1 TB de almacenamiento | Sec. 2.2.1, p. 11 | Texto | Alta | Sin costos |
| ODS con los que se alinea el gemelo | 4 | ODS | ODS 9, 11, 13 y 17 | Sec. 1, p. 5 | Texto | Media | Alineación declarativa |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'providing a flexible foundation for future extensions, including live IoT data integration and AI-driven risk assessment' (p. 11) | Prototipo funcional en laboratorio y con datos reales de edificios; la integración de datos IoT en vivo se presenta como extensión futura. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'Initial costs for sensor procurement and installation may be substantial, and ongoing maintenance is required to ensure data quality and system reliability' (p. 14) | Se reconocen costos de sensores y mantenimiento; no hay estimación de costos, modelo de financiamiento ni valor monetario. |
| IRL | 3 | Sí | 'this study proposes the integration of real-time data acquisition through the deployment of sensors and sensor networks' (p. 13) | La integración de sensores está propuesta y diseñada; la integración con datos reales en operación no se demuestra. |
| DRL | 4 | Sí | 'This research was funded by Cayirova Municipality' (p. 21) | El municipio, que sería el usuario, financió el desarrollo; sin estudio de uso por parte del personal de emergencias. |
| SRL | 1.33 | Sí | Componentes: Modelo geoespacial 3D y base de datos PostGIS (TRL 5), Red de sensores IoT y tablero de seguimiento (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 12.0; ÷9 → 1.33; nivel acotado a [1,9] = 1.33 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 2 e IRL 3: sistema desarrollado con financiamiento del usuario pero sin datos de sensores en operación, sin costos y con cifras de desempeño sin método. · Estrategia de salida: Validación con un evento real, instalación piloto de sensores, publicación de métricas y datos, y módulo de interrupción empresarial.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Cifra de exactitud sin método | Se afirma 87 % de exactitud entre daño simulado y observado para un escenario hipotético (Sec. 4, p. 19; Sec. 5, p. 21) | No se define métrica ni evento observado |
| Propuesta presentada como capacidad operativa | La integración de sensores se propone en el diseño y se describe como funcionando en resultados y discusión (Sec. 2.2.2, p. 13; Sec. 3, p. 15; Sec. 4, p. 19) | Inconsistencia entre secciones |
| Etiqueta de código abierto con componentes propietarios | Se declara un gemelo de código abierto que usa software propietario y datos sujetos a consentimiento (Resumen, p. 1; Sec. 2.2.1, p. 10; Data Availability, p. 22) | El alcance de la apertura no se aclara |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Uso del gemelo en la respuesta → menores tiempos de respuesta y menores pérdidas humanas y materiales | Afirmación en las conclusiones | Mecanismo supuesto | Evaluación en simulacros o eventos con línea base | Capacidades de respuesta, calidad de datos, conectividad | 1 | Relación no medida |
| Daño por escenario sísmico → priorización de inspecciones y unidades móviles | Resultados del modelo con 18 % de edificios con daño menor a moderado | Mecanismo de modelado | Datos de daño observado | Tipología, año de construcción, calidad de datos | 2 | Plausible con modelo no validado |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Definición de la métrica de exactitud y validación con un evento real, con matriz de confusión | Crítico | Media | 9 |
| Tecnológico | Datos en vivo de sensores, operación sin nube y medición de latencias y disponibilidad real | Crítico | Media | 8 |
| Conocimiento | Módulo de interrupción productiva y cadenas de suministro en la zona industrial | Crítico | Alta | 9 |
| Mercado | Costos de desarrollo, mantenimiento y operación por municipio y modelo de acceso a datos | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 3 | Enfoque híbrido del sistema con estación local y nube | Diagrama | Hardware local, nube y sensores | No aplica | Media |
| Fig. 5 | Flujo de integración y procesamiento de datos | Diagrama | Cinco familias de datos hacia vistas materializadas | 5 familias | Media |
| Fig. 8 | Tablero de riesgo sísmico con detecciones, réplicas e indicadores de respuesta | Captura de pantalla | Panel operativo del gemelo | No especificado | Baja |
| Fig. 10 | Pestaña de simulación y análisis de escenarios con IoT integrado | Captura de pantalla | Escenarios, daño predicho y tiempo de respuesta | No especificado | Baja |
| Tabla 1 | Contribución del gemelo a los ODS 11, 13, 9 y 17 | Tabla | Metas 11.5, 11.B, 13.1, 9.1, 9.4, 17.6 y 17.17 | 4 ODS | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Gemelos de ciudades de Londres, Singapur y Shanghái | No especificado en documento | Gobierno | Gemelos urbanos de gran escala | Infraestructura de datos extensa | Concentrados en metrópolis según los autores | Creciente |
| Gemelo urbano inteligente de Ford y Wolf | No especificado en documento | Academia | Simulación y sensado para gestión de ciudades | Enfoque conceptual integrado | Sin implementación concreta según los autores | Estable |
| Gemelo híbrido físico y basado en datos (Yun et al.) | No especificado en documento | Academia | Predicción de desastres con corrección de errores | Mayor exactitud de predicción | Evaluado en incendios, no en sismos | Creciente |

### B.9 Variables econométricas y vacíos

- **Y:** Daño predicho de edificios, exactitud de predicción (%) y disponibilidad del sistema (%)
- **X:** Gemelo digital de riesgo sísmico con datos integrados y sensores IoT
- **Z (controles):** Escenario de magnitud, tipología y año de construcción, calidad de los datos, conectividad
- **Datos:** Datos geoespaciales, de edificios, demográficos y de transporte de Çayırova integrados en PostGIS; red de sensores propuesta
- **Método:** Estudio de caso con modelado 3D, simulación de escenarios y pruebas de uso
- **Efecto reportado:** 18 % de edificios de concreto de mediana altura con daño menor a moderado; exactitud de 87 %; disponibilidad de 99,2 %
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin métrica, repeticiones ni línea base declaradas

| Vacío | Tipo | Descripción |
|---|---|---|
| V-080-01 | TERR | Distrito de Çayırova, Kocaeli (Türkiye) |
| V-080-02 | POBL | Población y edificios del distrito; sin empresas ni cadenas de suministro específicas |
| V-080-03 | TEMP | Escenario de un sismo de magnitud mayor o igual a 7,0; sin trayectoria de recuperación |
| V-080-04 | MET | Estudio de caso con cifras de desempeño sin método y sensores como propuesta |
| V-080-05 | VAR | Faltan costos, interrupción productiva, latencias, número de sensores y métricas de ODS |
| V-080-06 | TEOR | Gemelo digital y gestión de desastres; sin teoría de recuperación económica |
| V-080-07 | CAUS | Efecto del gemelo sobre la respuesta y las pérdidas sin evidencia |
