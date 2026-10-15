# FB-L01-055 | D055 — Adaptive hybrid reasoning for agent-based digital twins of distributed multi-robot systems

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/marah-challenger-2024-adaptive-hybrid-reasoning-for-agent-based-digital-twins-of-distributed-multi-robot-systems.pdf` · 28 páginas · Relevancia para el eje del corpus: **Periférico** (Propone un enfoque de gemelos digitales basados en agentes con razonamiento adaptativo de dos niveles (reactivo y racional, BDI) para sistemas multirrobot, implementado en una plataforma de simulación y control y probado en un caso de almacén logístico. Aporta una arquitectura de gemelo con razonamiento y una medida de brecha simulación-realidad, pero el dominio es robótica de laboratorio y no trata sismos, infraestructura ni recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-055 / D055
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, edición especial)
- **Referencia APA 7:** Marah, H., & Challenger, M. (2024). Adaptive hybrid reasoning for agent-based digital twins of distributed multi-robot systems. *Simulation*, *100*(9), 931-957. https://doi.org/10.1177/00375497231226436
- **Autores:** Marah, Hussein (57188847344); Challenger, Moharram (55910368200)
- **Afiliaciones:** Department of Computer Science, University of Antwerp, Belgium; AnSyMo/CoSys Core-Lab, Flanders Make Strategic Research Center, Belgium
- **Fecha de publicación:** 2024
- **Fuente/contenedor:** Simulation · vol. 100(9)
- **Identificador persistente:** DOI 10.1177/00375497231226436 · ISSN 00375497
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85184242838&doi=10.1177%2f00375497231226436&partnerID=40&md5=1b48be3480161bb3eb46caa48653e758
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 20

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Introducir un enfoque para desplegar gemelos digitales (DT) basados en agentes en sistemas ciberfísicos, que incorpore mecanismos de razonamiento inteligente y adaptativo para que los gemelos puedan razonar, adaptarse y actuar en entornos complejos y dinámicos. El enfoque integra conceptos, entidades y relaciones del marco de modelado y simulación de Zeigler desde la perspectiva de los DT basados en agentes, una arquitectura expandible y escalable y una estrategia de razonamiento de dos niveles (reactivo y racional), y se demuestra con una plataforma de simulación y control de un sistema multirrobot.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son cómo estructurar un gemelo digital como agente con razonamiento, cómo se comparan los modelos reactivo y racional en una misión con restricciones de energía y trayectoria, y qué brecha existe entre el comportamiento del agente digital y el del robot físico.

**Marco teórico.** El marco combina tres elementos. Primero, el marco de modelado y simulación (MSF) de Zeigler, reinterpretado para gemelos con agentes físicos y digitales. Segundo, la teoría de agentes inteligentes y sistemas multiagente, con agentes reactivos (reglas condición-acción) y agentes racionales con creencias, deseos e intenciones (BDI). Tercero, los sistemas ciberfísicos y multirrobot con un sistema de posicionamiento de banda ultraancha (UWB). El gemelo se concibe como una réplica que refleja el estado del agente físico y puede decidir por él, bajo el supuesto de que el robot físico sigue el comportamiento de su agente digital. La arquitectura distingue un mundo cibernético, con una capa de activos digitales gestionada por un sistema multiagente que contiene agentes digitales y agentes abstractos (de razonamiento, de simulación, de visualización y de aprendizaje), y un mundo físico con los agentes físicos.

**Metodología.** La implementación usa la plataforma de agentes JADE con el complemento BDI4JADE, una interfaz gráfica de simulación y control y robots prototipo con sensores ultrasónicos, de batería y UWB. Se realizaron dos experimentos. El primero compara un agente digital reactivo con uno racional (BDI) en una misión con cuatro destinos y cuatro estaciones de carga, con un mensaje de batería baja enviado en un punto fijo de la trayectoria. El segundo compara un agente digital con el agente físico de un robot operativo para estimar la brecha simulación-realidad mediante la distancia de Fréchet entre trayectorias. El caso de estudio es un almacén logístico inteligente que exige exactitud, tiempo y eficiencia energética. No se describen repeticiones ni análisis estadístico. La plataforma incluye una interfaz gráfica de simulación y control con menú de definición de casos, destinos globales cargados desde archivo y destinos exclusivos definidos de forma dinámica, estaciones de carga globales y un modelo de razonamiento asignable a cada agente digital. Los sensores del prototipo (ultrasónico para obstáculos, de batería y UWB para localización) alimentan las reglas del agente reactivo y las creencias del agente racional.

**Resultados principales.** En el primer experimento, el agente BDI completó la misión en unos 44 s con 9900 unidades de distancia y el agente reactivo en 57 s con 13 380 unidades, lo que se interpreta como mejor planificación del agente racional. En el segundo experimento se observó una diferencia entre las trayectorias del agente digital y del robot físico, cuantificada con la distancia de Fréchet, que los autores atribuyen a fricción, peso y dinámica de movimiento, así como a anomalías y vibración de las señales UWB; se asume que el agente físico sigue al digital. Las figuras muestran la interfaz, el menú principal, los casos y el comportamiento de los agentes. El texto explica que el agente reactivo percibe obstáculos, batería y posición y sigue la ruta más adecuada, mientras el racional forma deseos e intenciones y planifica sus acciones, y el texto describe cómo cada agente responde al mensaje de batería baja enviado en un punto de la trayectoria. Los autores concluyen que el enfoque es aplicable y eficiente para la planificación adaptativa, la gestión autónoma de recursos y la toma de decisiones lógica flexible, y que la plataforma permite observar al mismo tiempo la simulación y el robot real.

**Discusión y contribución.** Los autores sostienen que un marco bien fundamentado para construir gemelos de sistemas ciberfísicos distribuidos requiere una arquitectura flexible, modular y adaptable, y que su enfoque, basado en agentes y en el marco de Zeigler, lo ofrece. Afirman que los razonamientos reactivo y racional son complementarios, porque operan con mecanismos cognitivos distintos y pueden asignarse sobre la marcha a los sistemas físicos según la situación, y que la plataforma permite monitorear a los agentes en simulación y en el mundo real. Concluyen que el enfoque es escalable y extensible a otros sistemas ciberfísicos y que el razonamiento mejora el rendimiento de los gemelos de los robots en casos simples, como el análisis de escenarios hipotéticos, y en decisiones más complejas. Proponen como trabajo futuro ampliar la plataforma y las capacidades de razonamiento.

**Limitaciones declaradas.** Declaradas: los robots son prototipos de prueba de concepto afectados por condiciones del entorno, con vibración y anomalías en el sistema UWB, y los experimentos asumen que el agente físico sigue al digital. Se reconoce trabajo futuro para ampliar la plataforma. No declaradas: un solo escenario con dos robots y una repetición aparente; sin análisis estadístico ni comparación con otras arquitecturas de gemelos o de planificación; el caso del almacén es simulado en un entorno de laboratorio; sin evaluación de escalabilidad con decenas de robots; la afirmación de usabilidad no se evalúa con usuarios; sin costos.

**Trabajo futuro.** Explícito: ampliar la plataforma de simulación y control, incorporar más funciones de razonamiento y mejorar el posicionamiento. Implícito: pruebas con más robots, comparación con otras arquitecturas, aprendizaje de los agentes y despliegue en entornos reales.

**Palabras clave.** Declaradas: Agent-based modeling; digital twins; multi-agent systems; multi-robot systems; reasoning | Inferidas: gemelo digital, sistemas multiagente, razonamiento BDI, sistemas multirrobot, sistemas ciberfísicos, marco de modelado y simulación de Zeigler, brecha simulación-realidad, distancia de Fréchet, almacén inteligente

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Los gemelos digitales concebidos como agentes con razonamiento de dos niveles, reactivo y racional (BDI), dentro del marco de modelado y simulación de Zeigler y sobre una arquitectura modular, permiten planificación adaptativa, gestión autónoma de recursos y decisiones flexibles en sistemas multirrobot; en la comparación realizada, el agente racional completó la misión más rápido (44 s frente a 57 s) y con menos distancia (9900 frente a 13 380 unidades) que el reactivo.

**Antítesis identificada.** La evidencia es una demostración en un solo escenario con dos robots y sin repeticiones ni análisis estadístico. La diferencia entre agentes reactivo y racional se obtiene en una misión con rutas predefinidas y un evento de batería baja fijado por los autores, de modo que mide el diseño de cada regla y no una superioridad general. La brecha simulación-realidad se evalúa con una distancia de Fréchet sin referencia de aceptabilidad, y se asume que el agente físico sigue al digital, lo que elimina parte del problema que el gemelo debería resolver. La afirmación de escalabilidad y de extensibilidad a otros sistemas ciberfísicos no se prueba, y no se compara con otras arquitecturas de gemelos o con planificadores establecidos.

**Síntesis propuesta.** La contribución sostenible, con las cautelas anteriores, es una arquitectura de referencia para gemelos digitales con razonamiento, con una implementación abierta en plataformas de agentes, y una metodología para medir la brecha entre el gemelo y la entidad física, que puede replicarse en otros dominios con trayectorias o series de tiempo comparables. Para el corpus, aporta, por tanto, una idea transferible: un gemelo de continuidad puede combinar reglas reactivas (ante alertas) y razonamiento racional (planes de recuperación), y debe medirse su desviación frente a la realidad. No ofrece evidencia en infraestructura, desastres ni empresas, y su uso en el proyecto es conceptual.

**Áreas grises detectadas.**

1. Alcance de los experimentos: la comparación entre razonamiento reactivo y racional se basa en una misión de cuatro destinos y cuatro estaciones de carga y un evento de batería baja en un punto fijo; sin repeticiones, variación de escenarios ni estadística, no se puede generalizar la diferencia de 44 s frente a 57 s.
2. Brecha simulación-realidad: la distancia de Fréchet entre trayectorias del agente digital y del robot físico se usa como medida de diferencia, pero el texto asume que el agente físico sigue al digital y atribuye las discrepancias a fricción, peso y vibración del sistema UWB, sin umbral de aceptación ni análisis de causas.
3. Escalabilidad: se afirma que la arquitectura es expandible y escalable, pero las pruebas usan dos robots; no hay medidas de carga de mensajes, latencia ni consumo de recursos con más agentes.
4. Transferencia a otros dominios: se propone la aplicabilidad a sistemas ciberfísicos distribuidos, pero el único caso es un almacén simulado con robots de laboratorio; no se examinan sistemas con fallas de comunicación, datos ruidosos o entornos de desastre.

**Puntos oscuros aclarados.** Llama la atención que el artículo concluya usabilidad y eficiencia del enfoque con dos experimentos, uno de los cuales compara dos agentes en una misión fija y otro mide una brecha sin valor de referencia. También es notable que se asuma que el agente físico sigue al digital en ambos experimentos, lo que reduce el papel de la incertidumbre del mundo real que el gemelo debería manejar. La diferencia de tiempos entre agentes puede reflejar el diseño de reglas del agente reactivo y no una propiedad del razonamiento. Además, el texto admite anomalías en el sistema UWB y vibraciones del prototipo, pero no las cuantifica ni las trata. Por último, el título y el resumen aluden a razonamiento híbrido adaptativo y el cuerpo describe dos mecanismos independientes asignables según el caso, sin un mecanismo de decisión que adapte la elección entre ellos de forma automática, de modo que el adjetivo 'híbrido' se refiere a la coexistencia de dos modelos y no a una integración probada.

**Ideas propositivas novedosas.**

1. Gemelo de continuidad con razonamiento de dos niveles: adaptar la arquitectura a una planta de manufactura o a un almacén tras un sismo, con agentes reactivos para respuestas inmediatas (cortar energía, detener líneas) y agentes racionales para planes de reanudación (secuencia de reapertura de áreas, uso de inventario). Se podría simular con datos de una pyme y medir tiempo de reanudación y uso de recursos de cada nivel, así como el efecto de pérdida de conectividad entre agentes, para identificar qué reglas conviene precargar en el borde y qué decisiones requieren un coordinador central, con repeticiones y estadística para evitar la limitación del estudio original.
2. Brecha gemelo-realidad como indicador de confianza: usar una medida de distancia como la de Fréchet entre la trayectoria planificada del gemelo y la ejecutada en planta para activar alarmas de desfase y recalibración. En un piloto con robots móviles de bajo costo en un almacén de una pyme se podría fijar un umbral de aceptación y medir cuántas veces el gemelo requiere corrección, lo que ofrecería un indicador de calidad del gemelo transferible a gemelos de infraestructura y de procesos productivos, junto con una estimación del costo de mantener la sincronización con la planta durante un mes de operación.

**Relaciones poco exploradas.**

1. Gemelo con razonamiento y decisión (se relaciona con) D038 y D018: D038 propone gemelos conductuales con validación en un caso de tráfico y D018 combina inteligencia artificial agéntica y gemelos en redes eléctricas; D055 aporta razonamiento BDI con una medida de brecha.
2. Calidad de datos del sensor (se relaciona con) D039 y D043: D055 reporta anomalías y vibración en el sistema UWB como fuente de brecha, y D039 y D043 tratan errores de sensores en monitoreo mediante aprendizaje.

**Robustez argumentativa:** 2.1/10 (ponderación 30/30/25/15) — consistencia lógica 2/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 3/10 — Ofrece una arquitectura de gemelo con agentes y razonamiento de dos niveles y un procedimiento para medir la brecha simulación-realidad. Su valor para el corpus es periférico: el dominio es robótica de laboratorio, la evidencia es de un solo escenario sin repeticiones y no hay relación con sismos, infraestructura o empresas. Sirve como referencia de diseño para gemelos que deben decidir y de medida de desviación frente a la realidad, siempre con validación adicional.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Generalización apresurada (Se concluye aplicabilidad, escalabilidad y eficiencia a partir de dos robots y una misión fija (Resumen, p. 1; Sec. 7, p. 23)); Supuesto que elimina el problema (Se asume que el agente físico sigue al digital para medir la brecha, lo que reduce la incertidumbre del mundo real (Sec. 6, p. 16)); Comparación sin repetición (Se interpreta una diferencia de 13 s entre agentes en una sola corrida como mejor razonamiento (Sec. 6.1, p. 21))
- **Bradford-Hill:** No aplica: es una demostración de ingeniería sin diseño causal; la comparación entre agentes se limita a una corrida.
- **TRL asignado:** 4 — 'an implemented simulation and control platform for a multi-robot system demonstrates the approach’s applicability and feasibility' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (28 páginas). La reducción de 26 % en distancia es cálculo del analista (1 - 9900/13 380). Algunas figuras y tablas no son legibles.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Los gemelos digitales concebidos como agentes con razonamiento de dos niveles, reactivo y racional (BDI), dentro del marco de modelado y simulación de Zeigler y sobre una arquitectura modular, permiten planificación adaptativa, gestión autónoma de recursos y decisiones flexibles en sistemas multirrobot; en la comparación realizada, el agente racional completó la misión más rápido (44 s frente a 57 s) y con menos distancia (9900 frente a 13 380 unidades) que el reactivo.  | La evidencia es una demostración en un solo escenario con dos robots y sin repeticiones ni análisis estadístico. La diferencia entre agentes reactivo y racional se obtiene en una misión con rutas predefinidas y un evento de batería baja fijado por los autores, de modo que mide el diseño de cada regla y no una superioridad general. La brecha simulación-realidad se evalúa con una distancia de Fréchet sin referencia de aceptabilidad, y se asume que el agente físico sigue al digital, lo que elimina parte del problema que el gemelo debería resolver. La afirmación de escalabilidad y de extensibilidad a otros sistemas ciberfísicos no se prueba, y no se compara con otras arquitecturas de gemelos o con planificadores establecidos.  | La contribución sostenible, con las cautelas anteriores, es una arquitectura de referencia para gemelos digitales con razonamiento, con una implementación abierta en plataformas de agentes, y una metodología para medir la brecha entre el gemelo y la entidad física, que puede replicarse en otros dominios con trayectorias o series de tiempo comparables. Para el corpus, aporta, por tanto, una idea transferible: un gemelo de continuidad puede combinar reglas reactivas (ante alertas) y razonamiento racional (planes de recuperación), y debe medirse su desviación frente a la realidad. No ofrece evidencia en infraestructura, desastres ni empresas, y su uso en el proyecto es conceptual.  | 2.1/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Gemelo digital basado en agentes' es una réplica con autonomía de decisión; 'razonamiento reactivo' aplica reglas condición-acción; 'razonamiento racional (BDI)' planifica con creencias, deseos e intenciones; 'brecha simulación-realidad' es la diferencia entre trayectorias.
- **P2 Supuestos:** Supone que el agente físico sigue al digital, que una misión fija es representativa y que la distancia de Fréchet resume la brecha.
- **P3 Evidencia:** La evidencia es una comparación de dos agentes en una misión (44 s frente a 57 s) y una medida de brecha en un robot prototipo.
- **P4 Consecuencias:** Si es cierto, los gemelos pueden tomar decisiones adaptativas con razonamiento escalonado; si es falso, la ventaja se limita al escenario probado.
- **P5 Contraejemplos:** No se examinan repeticiones, otros planificadores, más robots, fallas de comunicación ni dominios distintos de la logística.
- **P6 Alternativas:** Alternativas: que un planificador clásico logre mejores resultados; que las diferencias dependan de las reglas elegidas; que la brecha sea mayor en entornos no controlados.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Tiempo de misión del agente racional (BDI) | 44 | s | Misión con cuatro destinos y cuatro estaciones de carga | Sec. 6.1, p. 21 | Texto | Media | Una corrida; 9900 unidades de distancia |
| Tiempo de misión del agente reactivo | 57 | s | Misma misión y restricciones | Sec. 6.1, p. 21 | Texto | Media | 13 380 unidades de distancia |
| Distancia recorrida: BDI frente a reactivo | 9900 / 13 380 | unidades | Misma misión | Sec. 6.1, p. 21 | Texto | Media | Reducción cercana a 26 % (cálculo del analista) |
| Robots en los experimentos | 2 | robots | Uno reactivo y uno racional | Sec. 6, p. 15-16 | Texto | Alta | Prototipos de laboratorio |
| Destinos y estaciones de carga definidos | 4 / 4 | elementos | Experimento de razonamiento | Sec. 6.1, p. 17 | Texto | Alta | Sin variación de escenario |
| Experimentos realizados | 2 | experimentos | Razonamiento y brecha simulación-realidad | Sec. 6, p. 15-16 | Texto | Alta | Sin repeticiones descritas |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'an implemented simulation and control platform for a multi-robot system demonstrates the approach’s applicability and feasibility' (p. 1) | Prototipo en laboratorio con robots de prueba de concepto; sin entorno operativo. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'Warehouse management demands employing intelligent and automated methods to reduce the load on workers and achieve efficiency, accuracy, and low cost' (p. 15) | Beneficio enunciado sin análisis de mercado ni costos. |
| IRL | 3 | Sí | 'a MAS toolchain called JADE and BDI4JADE plugin are utilized to develop and deploy the agent-oriented DTs' (p. 23) | Integración de agentes, plataforma y robots en un prototipo; anomalías en el posicionamiento UWB. |
| DRL | 2 | Sí | 'Incorporating intelligent and adaptive reasoning mechanisms into DTs is crucial to enable them to reason, adapt, and take efficacious actions' (p. 1) | Necesidad argumentada; sin demanda de usuarios medida. |
| SRL | 1.33 | Sí | Componentes: Gemelo digital basado en agentes (TRL 4), Plataforma de simulación y control con robots (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 12.0; ÷9 → 1.33; nivel acotado a [1,9] = 1.33 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 4 con BRL 1 e IRL 3: prototipo de laboratorio con dos robots, sin repeticiones ni análisis de costos. · Estrategia de salida: Pruebas con más robots, escenarios variados, comparación con otras arquitecturas y entornos reales.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Generalización apresurada | Se concluye aplicabilidad, escalabilidad y eficiencia a partir de dos robots y una misión fija (Resumen, p. 1; Sec. 7, p. 23) | Base experimental mínima |
| Supuesto que elimina el problema | Se asume que el agente físico sigue al digital para medir la brecha, lo que reduce la incertidumbre del mundo real (Sec. 6, p. 16) | Experimento condicionado por el supuesto |
| Comparación sin repetición | Se interpreta una diferencia de 13 s entre agentes en una sola corrida como mejor razonamiento (Sec. 6.1, p. 21) | Sin estadística ni variación |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Razonamiento racional (BDI) → menor tiempo y distancia de misión | Una comparación en una misión | Plausibilidad (planificación frente a reglas) | Repeticiones, otros escenarios | Diseño de reglas del agente reactivo, escenario | 1 | Diferencia sin soporte estadístico |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Repeticiones, escenarios variados y comparación con otras arquitecturas de gemelos | Crítico | Media | 8 |
| Tecnológico | Escalabilidad con más agentes y mejora del posicionamiento | Significativo | Media | 7 |
| Conocimiento | Aplicación de gemelos con razonamiento a continuidad y recuperación ante interrupciones | Significativo | Media | 7 |
| Mercado | Costos y beneficios en almacenes reales | Moderado | Baja | 5 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 3 | Mecanismo de operación del agente reactivo | Diagrama | Percepción, reglas y acción | No aplica | Media |
| Fig. 7 | Menú principal de la plataforma de simulación y control | Captura de pantalla | Definición de casos | No aplica | Baja |
| Tablas de experimento | Tiempo y distancia de agentes reactivo y racional | Tabla | 44 s y 57 s | 44; 57 | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Arquitecturas de gemelos digitales para robótica (sección 3.4) | No especificado en documento | Academia | Gemelos para sistemas robóticos | Cobertura temática | Sin razonamiento BDI integrado | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Tiempo de misión y distancia recorrida; distancia de Fréchet entre trayectorias
- **X:** Tipo de razonamiento (reactivo o racional)
- **Z (controles):** Misión, destinos y estaciones de carga fijados
- **Datos:** Dos experimentos con robots prototipo
- **Método:** Comparación descriptiva de un caso y medida de brecha
- **Efecto reportado:** 44 s frente a 57 s y 9900 frente a 13 380 unidades de distancia
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin repeticiones ni análisis estadístico

| Vacío | Tipo | Descripción |
|---|---|---|
| V-055-01 | TERR | Laboratorio universitario; territorio no especificado en documento |
| V-055-02 | POBL | Sin usuarios ni empresas |
| V-055-03 | TEMP | Misiones de segundos; sin operación prolongada |
| V-055-04 | MET | Sin repeticiones, sin estadística y con supuesto de seguimiento del agente físico |
| V-055-05 | VAR | Faltan costos, energía medida, fallas de comunicación y escalabilidad |
| V-055-06 | TEOR | Marco de modelado y simulación de Zeigler; sin teoría de resiliencia |
| V-055-07 | CAUS | Sin evidencia causal más allá del caso |
