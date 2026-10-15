# FB-L01-074 | D074 — IoT-Based Framework for Digital Twins in the Industry 5.0 Era

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/sensors-24-00594-v2.pdf` · 27 páginas · Relevancia para el eje del corpus: **Adyacente** (Propone un marco para gemelos digitales basados en IoT sobre el modelo de referencia IoT-A, con requisitos de Industria 5.0 (sostenibilidad, centralidad en las personas y resiliencia) incorporados como metadatos de la información, y una prueba de concepto de un gemelo de monitoreo en un sistema de cultivo vertical aeropónico. Aporta una definición operativa de resiliencia de sistemas IoT con gemelo digital y una revisión de la literatura que concluye que casi no existen contribuciones sobre resiliencia en IoT-A, pertinentes para el corpus, aunque el caso es agrícola, no hay mediciones y no se trata ni sismos ni recuperación empresarial.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-074 / D074
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Awouda, A., Traini, E., Bruno, G., & Chiabert, P. (2024). IoT-Based Framework for Digital Twins in the Industry 5.0 Era. *Sensors*, *24*(2), Article 594. https://doi.org/10.3390/s24020594
- **Autores:** Awouda, Ahmed (57211199929); Traini, Emiliano (57211199872); Bruno, Giulia (22033901600); Chiabert, Paolo (56024598200)
- **Afiliaciones:** Department of Management and Production Engineering, Politecnico di Torino, Turin, 10129, Italy
- **Fecha de publicación:** 2024
- **Fuente/contenedor:** Sensors · vol. 24(2)
- **Identificador persistente:** DOI 10.3390/s24020594 · ISSN 14248220
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85183169320&doi=10.3390%2fs24020594&partnerID=40&md5=61bf65bb6c58784dcdef6c4c10095fd9
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 79

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Proponer un marco para el desarrollo e implementación de gemelos digitales basados en IoT, a partir del Modelo de Referencia Arquitectónica de IoT (IoT-A o IoT-ARM), proyecto financiado por la Unión Europea entre 2010 y 2013, de modo que incluya los aspectos de la Industria 5.0, a saber, la sostenibilidad, la centralidad en las personas y la resiliencia, que los autores consideran ausentes en los marcos existentes. El marco busca servir de referencia para diseñar arquitecturas IoT centradas en gemelos digitales que permitan la sostenibilidad, la resiliencia y la centralidad humana del sistema de información, y se prueba mediante un gemelo de monitoreo de un cultivo vertical y una discusión de aplicaciones en manufactura y servicios.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son cómo contribuyeron los trabajos que citan IoT-A a los requisitos de la Industria 5.0 y a los gemelos digitales, cómo se pueden traducir la sostenibilidad, la centralidad humana y la resiliencia en requisitos y metadatos de un modelo de información IoT, y si el marco es aplicable a un caso real.

**Marco teórico.** El marco combina el modelo de referencia IoT-A, con sus modelos de dominio, de información y funcional, con el concepto de gemelo digital entendido como un conjunto de modelos adaptativos sincronizados con el sistema físico y con capacidad de actuar sobre él, distinto de la sombra digital de flujo unidireccional. La Industria 5.0, propuesta por la Comisión Europea en 2020, se define por la sostenibilidad, la centralidad en las personas y la resiliencia, esta última entendida como producción robusta capaz de resistir perturbaciones y sostener infraestructura crítica. Los autores derivan requisitos no funcionales y los asocian a indicadores: para la sostenibilidad, indicadores ambientales (huella de carbono, energía por mensaje) y económicos (costo de información); para la resiliencia, la capacidad de adaptarse a perturbaciones, un nivel suficiente de escalabilidad y la calidad estimada de los datos enviados; para la centralidad humana, el grado de participación y el impacto sobre las personas.

**Metodología.** La revisión de literatura siguió un proceso de citación hacia adelante en Scopus a partir del libro de IoT-A: se encontraron 237 documentos que citan el libro y 88 que citan capítulos, para 325, de los cuales un filtrado manual por título dejó 109 sin duplicados (32 artículos, 52 ponencias, 3 revisiones, 12 capítulos, 2 libros y 1 estudio), un filtrado por resumen dejó 28 que tocan gemelos digitales, Industria 5.0, sostenibilidad, centralidad humana o resiliencia, y una revisión profunda identificó cuáles contribuyen al modelo. El marco se construyó adaptando los modelos de dominio, de información y funcional, reemplazando la gestión de entidades virtuales por gestión de gemelos digitales en el modelo funcional de ocho grupos y añadiendo un bloque de metadatos de Industria 5.0 a los atributos del gemelo. La prueba de concepto es un módulo de cultivo aeropónico de lechuga con sensores de pH, conductividad eléctrica, nivel de agua, radiación fotosintéticamente activa, CO2, temperatura y humedad, un computador Raspberry Pi con el programa Mycodo, actuadores (calentador, humidificador, luces y bombas dosificadoras) y una plataforma IoT con MQTT, base de datos, analítica, tablero y módulo de gemelo.

**Resultados principales.** Los resultados de la revisión indican que, de los 28 documentos revisados en profundidad, solo 5 mencionan el concepto de gemelo digital y 2 lo tratan con aportes significativos, 11 introducen IoT-ARM y 3 hacen aportes considerables, y 11 tocan conceptos de Industria 5.0, pero ninguno la menciona de forma explícita, solo la sostenibilidad (2) y la centralidad humana, y no se encontraron contribuciones directas a la resiliencia. El marco resultante define un modelo de dominio con entidad física, entidad virtual, dispositivo inteligente, recursos y servicios, un modelo de información con atributos de entidad virtual y metadatos generales y de Industria 5.0, y un modelo funcional con ocho capas. En el caso, el gemelo de una planta de lechuga agrupa los atributos en ambientales, de productividad (peso fresco y seco, diámetro del tallo, área foliar), de calidad y de sostenibilidad ambiental, y para cada pilar de Industria 5.0 se consideran dos métricas: grado de participación humana e impacto en las personas, costo promedio por bit entregado y energía por bit, y escalabilidad y tolerancia a fallas. Los buses Modbus e I2C admiten hasta 255 dispositivos. El artículo no entrega mediciones del sistema, errores de predicción, ahorros, tiempos de respuesta ni evidencia de resiliencia.

**Discusión y contribución.** Los autores sostienen que el marco ofrece una colección estandarizada de instrumentos arquitectónicos que asegura interoperabilidad, compatibilidad y escalabilidad, que el modelo de dominio es robusto en distintos dominios, como la agricultura inteligente y las fábricas inteligentes, y que la capa de gestión del modelo funcional da el carácter de Industria 5.0, pues allí se supervisan el reporte de errores para la resiliencia, la salud del sistema para la sostenibilidad y las decisiones estratégicas. Reconocen que el uso de IoT-A para lograr los objetivos de la Industria 5.0 casi no se trata en la literatura y que los indicadores de sostenibilidad social y de resiliencia requieren refinamiento. Como trabajo futuro plantean validar el marco en tres casos de manufactura, agricultura y servicios, adaptar el marco dinámicamente a nuevos estándares y reforzar la seguridad y la privacidad.

**Limitaciones declaradas.** Declaradas: la validación en escenarios reales diversos está pendiente; las métricas para la sostenibilidad social y la resiliencia deben refinarse; la seguridad y la privacidad quedan fuera del alcance de este artículo. No declaradas: la prueba de concepto se describe pero no se reportan mediciones ni resultados, de modo que no se prueba la validez del marco; la revisión parte de citas de un solo libro, filtra por título y no cubre literatura sobre resiliencia de gemelos que no cite IoT-A; la resiliencia se reduce a escalabilidad, calidad de datos y tolerancia a fallas, sin definir cómo se mide la capacidad de adaptarse; el caso es un solo módulo agrícola en un ambiente controlado; no se evalúan costos de implementación ni de operación; la conexión con la centralidad humana se apoya en prácticas organizacionales que los propios autores consideran imposibles de abordar en el diseño de IoT.

**Trabajo futuro.** Explícito: refinar métricas de Industria 5.0, especialmente la sostenibilidad social y la resiliencia, validar en tres casos de manufactura, agricultura y servicios, explorar la adaptación dinámica a nuevos estándares y reforzar la seguridad y la privacidad. Implícito: mediciones de desempeño del gemelo, pruebas de fallas y comparación con otros marcos de referencia de IoT.

**Palabras clave.** Declaradas: aeroponics; digital twin; Industry 5.0; Internet of Things; IoT-ARM | Inferidas: gemelo digital, IoT, Industria 5.0, IoT-A, resiliencia, sostenibilidad, centralidad en las personas, aeroponía, MQTT, modelo de dominio

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un marco que extiende el modelo de referencia IoT-A con un gemelo digital como entidad virtual y con metadatos de sostenibilidad, centralidad humana y resiliencia permite diseñar sistemas IoT conformes con la Industria 5.0, llena un vacío de la literatura, donde de 28 documentos revisados ninguno trata la resiliencia, y se muestra viable en un gemelo de monitoreo de un cultivo vertical aeropónico, con aplicabilidad a manufactura y servicios.

**Antítesis identificada.** El artículo describe una prueba de concepto sin presentar datos, de modo que la afirmación de que prueba la validez del marco carece de evidencia, y sostiene la aplicabilidad a manufactura y servicios solo por la abstracción del modelo de dominio. La revisión, basada en las citas de un único libro y en filtrado manual por título, no puede afirmar que no existen contribuciones sobre resiliencia en la literatura de gemelos. La resiliencia se redefine como escalabilidad, calidad de datos y tolerancia a fallas, sin umbrales ni método de medición, lo que se aleja de la capacidad de resistir y recuperarse de perturbaciones que el propio texto define al inicio. El marco no considera eventos extremos, cortes de energía o de comunicaciones, ni costos, y el aspecto humano se limita a atributos de metadatos sin evaluación.

**Síntesis propuesta.** La contribución sostenible es un modelo conceptual ordenado que traduce requisitos de Industria 5.0 en metadatos de un gemelo digital sobre una arquitectura de referencia conocida, y una evidencia de que la literatura de ese marco casi no aborda la resiliencia. Para el corpus, aporta un vocabulario y una estructura de información en los que se podrían registrar indicadores de continuidad de un gemelo empresarial, y señala una brecha de métricas de resiliencia. Su alcance es de diseño, sin resultados, y no trata desastres ni recuperación, por lo que su utilidad depende de definir y medir la resiliencia con pruebas de falla, y de aplicar el marco a un caso de manufactura o de servicios con perturbaciones reales.

**Áreas grises detectadas.**

1. Evidencia de la prueba de concepto: el resumen declara que un gemelo de monitoreo de un sistema de cultivo vertical se desarrolló para probar la validez del marco, pero el caso solo describe el sistema, sus sensores, actuadores y atributos, sin reportar mediciones, errores del gemelo, tiempos de respuesta, consumo de energía ni comparación con una línea base.
2. Alcance de la revisión: la revisión parte de 325 documentos que citan el libro de IoT-A y se reduce por título y por resumen a 28, con lo cual excluye la literatura sobre gemelos digitales, resiliencia e Industria 5.0 que no cite IoT-A; la conclusión de que no hay contribuciones directas a la resiliencia se limita a ese subconjunto.
3. Definición operativa de resiliencia: el texto define la resiliencia como la capacidad de resistir y recuperarse de ataques, perturbaciones y fallas, pero la operacionaliza con la capacidad de adaptarse a perturbaciones, una escalabilidad suficiente y la calidad de los datos, y los metadatos de la prueba usan escalabilidad y tolerancia a fallas sin valores ni método de medición.
4. Generalización del marco: la afirmación de que el modelo de dominio es robusto en distintos dominios se sostiene en su abstracción, y la aplicación a manufactura y a servicios se deja como trabajo en curso, de modo que no se sabe qué ajustes requerirían los activos, las personas y las perturbaciones propias de una empresa.

**Puntos oscuros aclarados.** Llama la atención que un artículo cuyo aporte central es incorporar la resiliencia no presente un solo indicador medido de ella y que el único ejemplo de resiliencia desarrollado en el texto sean redes eléctricas y de transporte descritas en la literatura. También es notable que el marco descarte la entidad aumentada de IoT-A argumentando que no agrega información, sin analizar el efecto de esa decisión sobre la compatibilidad con el estándar. La lista de funciones de centralidad humana incluye prácticas de recursos humanos, como recompensas por creatividad y liderazgo de apoyo, que el propio texto califica de imposibles de considerar en el diseño de IoT. Además, el resumen presenta el marco como estándar de referencia, mientras que el texto lo describe como una propuesta sin adopción. El caso agrícola usa un calentador por el clima frío de la cámara, un detalle que muestra una instalación particular y no un escenario de perturbación. Por último, la sección de datos indica que los datos están en el manuscrito, pero el manuscrito no contiene datos de desempeño.

**Ideas propositivas novedosas.**

1. Indicadores de resiliencia medidos para un gemelo de planta: instrumentar el módulo del caso, o una línea de producción de una pyme, con cinco indicadores de resiliencia (tiempo de detección de falla, tiempo de recuperación de la sincronización del gemelo, porcentaje de datos perdidos, degradación de calidad de datos y tareas críticas mantenidas) y aplicar 30 fallas inyectadas de energía, de red y de sensor, registrando los valores en los metadatos de Industria 5.0. El resultado mostraría si la escalabilidad y la tolerancia a fallas descritas capturan la resiliencia, cuánto tarda un gemelo en recuperarse tras una interrupción y qué diseño reduce más la pérdida de información.
2. Aplicación del marco a la continuidad tras un evento extremo: adaptar el modelo de dominio a una empresa manufacturera con entidades físicas (máquinas, inventario, edificio) y atributos de continuidad (capacidad disponible, tiempo hasta reanudar), y probarlo con un simulacro de sismo o de corte prolongado durante dos jornadas, midiendo la calidad de la información que el gemelo ofrece a los responsables durante la emergencia. Con ello se podría comprobar si el marco sirve para decisiones de recuperación y qué atributos faltan, y se obtendría una guía de aplicación para empresas pequeñas con costos de implementación documentados.

**Relaciones poco exploradas.**

1. Resiliencia organizacional y gemelos (complementa) D082 y D083: D082 revisa los mecanismos de resiliencia organizacional y D083 trata IoT y sostenibilidad en sistemas de producción; D074 aporta una forma de registrar indicadores de resiliencia y sostenibilidad en un gemelo.
2. Marcos de IoT para gemelos (se relaciona con) D079 y D078: D079 revisa IoT, IA y gemelos en ciudades inteligentes y D078 presenta un ecosistema de gemelo comunitario; D074 propone una estructura de información y capas funcionales con carácter más general.

**Robustez argumentativa:** 2.1/10 (ponderación 30/30/25/15) — consistencia lógica 2/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 4/10 — Aporta un marco conceptual de gemelo digital IoT sobre IoT-A con metadatos de sostenibilidad, centralidad humana y resiliencia, y una revisión que identifica 28 documentos y la ausencia de contribuciones directas a la resiliencia. Su valor para el corpus es limitado porque el caso es un cultivo vertical sin mediciones, la revisión parte de un solo libro de referencia, la resiliencia se define con indicadores no medidos y no hay conexión con desastres, empresas o recuperación, pero ofrece un vocabulario y una estructura de información que pueden reutilizarse.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Validación asumida sin resultados (Se afirma que la prueba de concepto verifica la validez del marco sin reportar mediciones (Resumen, p. 1; Sec. 4, p. 16-23)); Ausencia de evidencia por muestreo limitado (Se concluye que no hay contribuciones directas a la resiliencia a partir de documentos que citan un solo libro (Sec. 2, p. 4)); Desplazamiento del concepto (La resiliencia se define como resistir y recuperarse y se mide con escalabilidad y calidad de datos (Sec. 3.2.3, p. 10))
- **Bradford-Hill:** No aplica: es un estudio de diseño; no se estima causalidad con datos observacionales.
- **TRL asignado:** 3 — 'a proof of concept of a monitoring digital twin for a vertical farming system has been developed to test the validity of the framework' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (27 páginas, hasta las referencias). Las páginas siguen los marcadores del PDF. Los recuentos de la revisión se tomaron de la Sec. 2 y no se pudieron contrastar con la Figura 1, que es un diagrama. El artículo se publicó en Sensors 2024, 24, 594.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un marco que extiende el modelo de referencia IoT-A con un gemelo digital como entidad virtual y con metadatos de sostenibilidad, centralidad humana y resiliencia permite diseñar sistemas IoT conformes con la Industria 5.0, llena un vacío de la literatura, donde de 28 documentos revisados ninguno trata la resiliencia, y se muestra viable en un gemelo de monitoreo de un cultivo vertical aeropónico, con aplicabilidad a manufactura y servicios.  | El artículo describe una prueba de concepto sin presentar datos, de modo que la afirmación de que prueba la validez del marco carece de evidencia, y sostiene la aplicabilidad a manufactura y servicios solo por la abstracción del modelo de dominio. La revisión, basada en las citas de un único libro y en filtrado manual por título, no puede afirmar que no existen contribuciones sobre resiliencia en la literatura de gemelos. La resiliencia se redefine como escalabilidad, calidad de datos y tolerancia a fallas, sin umbrales ni método de medición, lo que se aleja de la capacidad de resistir y recuperarse de perturbaciones que el propio texto define al inicio. El marco no considera eventos extremos, cortes de energía o de comunicaciones, ni costos, y el aspecto humano se limita a atributos de metadatos sin evaluación.  | La contribución sostenible es un modelo conceptual ordenado que traduce requisitos de Industria 5.0 en metadatos de un gemelo digital sobre una arquitectura de referencia conocida, y una evidencia de que la literatura de ese marco casi no aborda la resiliencia. Para el corpus, aporta un vocabulario y una estructura de información en los que se podrían registrar indicadores de continuidad de un gemelo empresarial, y señala una brecha de métricas de resiliencia. Su alcance es de diseño, sin resultados, y no trata desastres ni recuperación, por lo que su utilidad depende de definir y medir la resiliencia con pruebas de falla, y de aplicar el marco a un caso de manufactura o de servicios con perturbaciones reales.  | 2.1/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'IoT-A' es el modelo de referencia europeo de arquitectura IoT; 'entidad virtual' es la representación digital de una entidad física, que puede ser un gemelo digital si está sincronizada y puede actuar; 'sombra digital' es un modelo con flujo unidireccional; 'Industria 5.0' integra sostenibilidad, centralidad en las personas y resiliencia.
- **P2 Supuestos:** Supone que un marco abstracto es aplicable a distintos dominios, que escalabilidad, calidad de datos y tolerancia a fallas representan la resiliencia, y que describir una prueba de concepto equivale a validar el marco.
- **P3 Evidencia:** La evidencia son 28 documentos revisados, una descripción de modelos de dominio, información y funcional, y un caso de cultivo vertical sin datos de desempeño.
- **P4 Consecuencias:** Si es cierto, los diseñadores pueden construir gemelos conformes con la Industria 5.0 con una estructura común; si es falso, el marco puede ser un ejercicio de nomenclatura que no mejora la resiliencia ni la sostenibilidad.
- **P5 Contraejemplos:** No se examinan mediciones del sistema, fallas, costos, comparación con otros marcos, otros dominios ni la dimensión humana.
- **P6 Alternativas:** Alternativas: que otros marcos de referencia den una estructura equivalente; que la resiliencia se logre con redundancia física y no con metadatos; que el costo de documentar los indicadores supere su beneficio.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Documentos que citan IoT-A en la revisión inicial | 325 | documentos | 237 que citan el libro y 88 que citan capítulos | Sec. 2, p. 4 | Texto | Alta | Solo Scopus |
| Documentos tras el filtrado por título | 109 | documentos | 32 artículos, 52 ponencias y otros | Sec. 2, p. 4 | Texto | Alta | Filtrado manual |
| Documentos seleccionados por resumen | 28 | documentos | Gemelos, Industria 5.0, sostenibilidad, centralidad humana y resiliencia | Sec. 2, p. 4 | Texto | Alta | Criterios de extracción propios |
| Documentos con aportes significativos sobre gemelos digitales | 2 de 5 | documentos | Cinco mencionan el concepto | Sec. 2, p. 4 | Texto | Alta | Revisión profunda |
| Documentos que mencionan explícitamente Industria 5.0 | 0 de 11 | documentos | Once tocan conceptos relacionados | Sec. 2, p. 4 | Texto | Alta | Sin contribuciones sobre resiliencia |
| Grupos funcionales del modelo funcional | 8 | capas | Dispositivo, comunicación, servicios, gestión de gemelos, procesos, seguridad, organización de servicios y gestión | Sec. 3.5, p. 14-15 | Texto | Media | Sin pruebas |
| Métricas de Industria 5.0 por atributo | 6 | métricas | Dos por cada pilar | Sec. 4.3, p. 20 | Texto | Media | Sin valores |
| Dispositivos máximos por bus Modbus o I2C | 255 | dispositivos | Escalabilidad para un módulo aeropónico | Sec. 4.4, p. 22-23 | Texto | Media | Cálculo teórico |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'a proof of concept of a monitoring digital twin for a vertical farming system has been developed to test the validity of the framework' (p. 1) | Prueba de concepto descrita; sin mediciones que demuestren la función del marco. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'The economic sustainability, with the indicator for the cost of information (e.g., cost of sending a message)' (p. 10) | Se plantea un indicador de costo de la información; sin modelo de negocio, costos de implementación ni clientes. |
| IRL | 3 | Sí | 'The communication between the aeroponic system and the IoT platform is implemented using the MQTT protocol' (p. 22) | Integración de sensores, actuadores, plataforma IoT y gemelo descrita en el caso; sin pruebas de integración. |
| DRL | 2 | Sí | 'works in progress are aimed at applying this methodology to three use cases in manufacturing, agricultural, and service sectors' (p. 23) | Se anticipan usos en tres sectores; sin estudio de demanda. |
| SRL | 1.0 | Sí | Componentes: Marco de dominio, información y función con metadatos de Industria 5.0 (TRL 3), Módulo aeropónico con Raspberry Pi y plataforma IoT (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 9.0; ÷9 → 1.00; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 3 con BRL 1 e IRL 3: marco y prueba de concepto sin mediciones, sin costos y sin pruebas de fallas. · Estrategia de salida: Mediciones del gemelo, pruebas con fallas inyectadas, indicadores de resiliencia y validación en tres sectores.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Validación asumida sin resultados | Se afirma que la prueba de concepto verifica la validez del marco sin reportar mediciones (Resumen, p. 1; Sec. 4, p. 16-23) | Descripción presentada como prueba |
| Ausencia de evidencia por muestreo limitado | Se concluye que no hay contribuciones directas a la resiliencia a partir de documentos que citan un solo libro (Sec. 2, p. 4) | El subconjunto no representa la literatura |
| Desplazamiento del concepto | La resiliencia se define como resistir y recuperarse y se mide con escalabilidad y calidad de datos (Sec. 3.2.3, p. 10) | Los indicadores no capturan la recuperación |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Metadatos de Industria 5.0 en el gemelo → sistemas más sostenibles, humanos y resilientes | Argumentación conceptual | Mecanismo supuesto | Mediciones antes y después en casos reales | Prácticas organizacionales, redundancia, costos | 1 | Relación no sustentada |
| Arquitectura de referencia IoT-A → interoperabilidad y escalabilidad | Revisión de literatura y descripción del caso | Mecanismo de estandarización | Comparación con arquitecturas alternativas | Tamaño del sistema, protocolos | 2 | Beneficio plausible sin prueba |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Medición del desempeño del gemelo y de la resiliencia con fallas inyectadas | Crítico | Alta | 9 |
| Conocimiento | Definición operativa y umbrales de resiliencia para gemelos, con un caso de manufactura o servicios | Crítico | Media | 9 |
| Tecnológico | Seguridad y privacidad fuera del alcance y adaptación dinámica a estándares | Significativo | Media | 7 |
| Mercado | Costos de implementación y operación del marco en empresas pequeñas | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Resumen del proceso de revisión de literatura por citas de IoT-A en Scopus | Diagrama | 325 documentos reducidos a 28 | 325; 109; 28 | Media |
| Fig. 4 | Entidades virtuales en relación con gemelos y sombras digitales | Diagrama | Distinción entre sombra y gemelo | No aplica | Media |
| Fig. 7 | Modelo funcional de IoT con gestión de gemelos digitales | Diagrama | Ocho grupos funcionales | 8 | Media |
| Fig. 10-11 | Estructura de información del gemelo y metadatos del atributo temperatura | Diagramas | Metadatos generales y de Industria 5.0 | 6 métricas | Media |
| Fig. 12 | Arquitectura del sistema aeropónico desarrollado | Diagrama | Sensores, Raspberry Pi, MQTT y plataforma IoT | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Marcos de IoT para gemelos agrícolas basados en IoT-A (autores [28] y [29] del texto) | No especificado en documento | Academia | Arquitectura de gemelos digitales para agricultura | Base sobre la cual se construye el marco | Sin requisitos de Industria 5.0 | Estable |
| Otras arquitecturas de referencia de IoT con nube y niebla | No especificado en documento | Academia | Integración de IoT con computación en la nube | Comparadas en la literatura | No detalladas por los autores | Estable |
| Mycodo (sistema de monitoreo y automatización de código abierto) | No especificado en documento | Comunidad de código abierto | Control de entornos como invernaderos | Gratuito y abierto | Alcance de aplicación doméstico e industrial ligero | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Conformidad del sistema IoT con requisitos de Industria 5.0 (no medida)
- **X:** Aplicación del marco IoT-A extendido con gemelo digital y metadatos de Industria 5.0
- **Z (controles):** Dominio de aplicación, sensores, protocolos, personas involucradas
- **Datos:** Revisión de 28 documentos de 325 que citan IoT-A y un caso de cultivo aeropónico sin datos
- **Método:** Diseño de marco con revisión por citación hacia adelante y prueba de concepto
- **Efecto reportado:** No estimado
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin mediciones, sin comparación con otros marcos

| Vacío | Tipo | Descripción |
|---|---|---|
| V-074-01 | TERR | Italia (Turín) como lugar de los autores; el cultivo se desarrolla en una cámara de clima frío no especificada |
| V-074-02 | POBL | Una planta de lechuga y operadores del cultivo; sin empresas ni comunidades |
| V-074-03 | TEMP | Proyecto IoT-A de 2010 a 2013 y literatura posterior; sin horizonte de operación del caso |
| V-074-04 | MET | Revisión por citación de un libro y prueba de concepto sin mediciones |
| V-074-05 | VAR | Faltan indicadores de resiliencia medidos, costos, consumo y desempeño del gemelo |
| V-074-06 | TEOR | Arquitectura de referencia IoT-A y Industria 5.0; sin teoría de recuperación |
| V-074-07 | CAUS | Efecto del marco sobre sostenibilidad y resiliencia sin evidencia |
