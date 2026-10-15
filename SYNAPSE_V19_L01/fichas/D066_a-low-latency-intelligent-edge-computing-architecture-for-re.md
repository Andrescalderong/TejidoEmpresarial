# FB-L01-066 | D066 — A low-latency intelligent edge computing architecture for real-time decision-making in large-scale IoT networks

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/s10791-026-10133-w.pdf` · 24 páginas · Relevancia para el eje del corpus: **Periférico** (Propone ELARA, una arquitectura de cómputo en el borde con extracción federada de características, descarga adaptativa de tareas, orquestación por aprendizaje por refuerzo y microclústeres con consenso, evaluada por simulación con datos de manufactura inteligente. Aporta una referencia técnica de baja latencia y de recuperación ante fallas de nodos que podría sostener gemelos digitales de planta, pero no trata sismos, desastres, recuperación productiva ni empresas, y su validación es simulada.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-066 / D066
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Jia, Y. (2026). A low-latency intelligent edge computing architecture for real-time decision-making in large-scale IoT networks. *Discover Computing*, *29*(1), Article 278. https://doi.org/10.1007/s10791-026-10133-w
- **Autores:** Jia, Yanming (60578872000)
- **Afiliaciones:** School of Information and Electronic Engineering, Shangqiu Institute of Technology, ShangQiu, 476000, China
- **Fecha de publicación:** 2026
- **Fuente/contenedor:** Discover Computing · vol. 29(1)
- **Identificador persistente:** DOI 10.1007/s10791-026-10133-w · ISSN 29482992
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105039473747&doi=10.1007%2fs10791-026-10133-w&partnerID=40&md5=9ec41c28c6b90f3b990796c25cde57f8
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 0

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Resolver el problema de lograr un procesamiento distribuido, inteligente y escalable en redes IoT de gran escala, con confiabilidad, eficiencia y coordinación entre nodos heterogéneos, que los sistemas centrados en la nube no atienden por sus retardos de comunicación, la sobrecarga de red y la falta de flexibilidad ante cargas dinámicas. Para ello el autor introduce ELARA (Edge-Level Adaptive Reasoning Architecture), una infraestructura híbrida que optimiza la ubicación del cómputo y acelera la inferencia en tiempo real, y que se apoya en una arquitectura de microclústeres con consenso para tolerar fallas sin depender de una nube centralizada.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si la combinación de extracción federada de características, descarga adaptativa y orquestación por refuerzo reduce la latencia, el ancho de banda y la energía frente a tres métodos de referencia, y si los microclústeres con consenso aceleran la recuperación tras fallas de nodos sin una coordinación central.

**Marco teórico.** El marco articula la computación en el borde y en la niebla (edge-fog-cloud) con el aprendizaje federado y el aprendizaje por refuerzo profundo. La arquitectura tiene un nivel de dispositivos que preprocesa y extrae características, un motor de descarga adaptativa que decide si una tarea se ejecuta localmente, en el microclúster o en módulos remotos, una capa de consenso distribuido para sincronización de estado, elección de líder y recuperación, una capa de niebla para balanceo de carga, un corredor de mensajes con prioridades y una nube para entrenamiento global. La sección de trabajos relacionados revisa trabajos de planificación en tiempo real, arquitecturas híbridas, ciberseguridad, agricultura y energía, y resume los antecedentes en la Tabla 1 con indicadores cualitativos de decisión en tiempo real, seguridad y eficiencia de recursos. El autor identifica como brecha la falta de enfoques integrales, la validación mayoritaria por simulación y la escasa atención a seguridad y escalabilidad.

**Metodología.** La metodología describe tres módulos entrenados en secuencia. El extractor local de características se entrena con aprendizaje supervisado dentro de un proceso federado, con agregación por promedio federado ponderado en los coordinadores de microclúster, dimensión de características fijada en 64, entre 2 y 5 épocas locales, lote de 32 y optimizador Adam. La descarga adaptativa usa un clasificador de dos capas con 32 neuronas ocultas que recibe carga de trabajo, capacidad disponible, latencia de red, energía restante y longitud de cola, y se entrena en línea con entropía cruzada binaria. La orquestación de recursos se formula como un proceso de decisión de Markov resuelto con una red Q profunda, con factor de descuento de 0,99, memoria de repetición de 100 000 transiciones, lote de 64 y actualización de la red objetivo cada 1000 pasos. La evaluación se hizo en un entorno simulado de borde y niebla de manufactura inteligente, con un conjunto de unos 120 000 registros de unas 30 horas muestreados a 1 Hz con 24 variables, y se compararon CEA, DSS y DFJSP bajo las mismas topologías, trazas de carga y restricciones de recursos. Se reportan ocho indicadores, 20 repeticiones con semillas distintas, intervalos de confianza de 95 % y pruebas t pareadas bilaterales con nivel de significancia de 0,05.

**Resultados principales.** Los resultados indican que ELARA alcanza una latencia de extremo a extremo de 39 a 52 ms, un ahorro de ancho de banda de hasta 48 % y de energía de hasta 31 %, entre 850 y 932 muestras por segundo de inferencia, tasas de finalización de tareas de 93 a 98 %, precisión de descarga de 89 a 93 % y un tiempo de recuperación ante fallas de 132 a 152 ms, y supera a CEA, DSS y DFJSP en todos los indicadores. En la Tabla 2, el microclúster de varios nodos de borde muestra una latencia promedio de 39,5 ms (desviación 2,6) frente a 152,4 ms (6,3) de la ejecución en la nube, 68,7 ms de una unidad de borde simple y 57,9 ms de un nivel híbrido borde-nube. La Tabla 6 reporta precisión de descarga de ELARA de 92, 90, 89, 93 y 91 % en cinco escenarios (fábrica inteligente, salud, movilidad, comercio minorista y control de red eléctrica), frente a 68 a 79 % de los métodos de referencia, y la Tabla 7 reporta velocidades de inferencia de 850 a 932 muestras por segundo frente a 500 a 600 de los demás. La energía por tarea se situó entre 7,5 y 10,0 J. El autor declara que todas las mejoras fueron significativas (p < 0,05) frente a las tres bases en todas las situaciones evaluadas. El texto no entrega valores numéricos de p, tamaños de efecto ni pruebas de corrección por comparaciones múltiples, y varias cifras se presentan solo en figuras de barras sin tabla de datos.

**Discusión y contribución.** El autor sostiene que la combinación de extracción federada, descarga adaptativa y orquestación por refuerzo mejora la capacidad de respuesta, la estabilidad y la eficiencia, y que ELARA es adecuado para manufactura inteligente, vigilancia médica, movilidad autónoma y control de infraestructura crítica. Afirma que el costo de coordinación por consenso es limitado porque el consenso se aplica solo a la sincronización de estado, la elección de líder y la recuperación, y que crece de forma lineal con el tamaño del microclúster. Sostiene además que el diseño es agnóstico del dominio porque solo requiere sustituir los extractores de características y los modelos de inferencia ligeros. Como trabajo futuro propone modelos de borde más ligeros, privacidad diferencial o cómputo multipartito seguro, implementaciones a gran escala y pruebas de larga duración fuera de simulaciones controladas, orquestación inspirada en la computación cuántica y orquestación consciente de energía verde.

**Limitaciones declaradas.** Declaradas: se requieren implementaciones a gran escala y pruebas de larga duración en entornos dinámicos para probar ELARA fuera de las simulaciones controladas, y se debe reforzar la privacidad con técnicas formales. No declaradas: la evaluación es solo simulada; los métodos de referencia (CEA, DSS, DFJSP) son métodos de planificación o de apoyo a decisiones que no son soluciones de descarga en el borde, de modo que la comparación no es equivalente; el conjunto de datos corresponde únicamente a manufactura inteligente, pero la Tabla 6 reporta cinco escenarios sin explicar cómo se generaron los de salud, movilidad, comercio y red eléctrica; el número de nodos, la topología y la carga no se detallan; la tasa de aprendizaje de los modelos no se especifica; no se midió la sobrecarga del entrenamiento federado ni de la red Q profunda en dispositivos reales; las afirmaciones de resistencia a fallas bizantinas y ataques de inferencia no se prueban; el ahorro de ancho de banda se informa también como 245 312 MB/min, cifra incompatible con un ahorro porcentual sin su referencia; la referencia [31] se usa a la vez para una arquitectura vehicular y para el repositorio de datos.

**Trabajo futuro.** Explícito: modelos de borde ligeros de mayor contexto, privacidad diferencial o cómputo multipartito seguro, despliegues a gran escala y pruebas de larga duración, planificación inspirada en la computación cuántica, colaboración entre clústeres y orquestación consciente de energía verde. Implícito: validación con hardware real, bases de comparación de descarga en el borde y estudio de las fallas bizantinas.

**Palabras clave.** Declaradas: Distributed architecture; Edge computing; Federated intelligence; IoT; Real-time systems; Reinforcement learning | Inferidas: cómputo en el borde, IoT, aprendizaje federado, aprendizaje por refuerzo, descarga de tareas, microclústeres con consenso, latencia, recuperación ante fallas, manufactura inteligente, orquestación de recursos

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Una arquitectura descentralizada de borde que extrae características localmente con aprendizaje federado, decide la descarga de tareas con un clasificador adaptativo y orquesta recursos con una red Q profunda dentro de microclústeres con consenso reduce la latencia de extremo a extremo a 39 a 52 ms, ahorra hasta 48 % de ancho de banda y 31 % de energía, sostiene tasas de finalización de tareas de 93 a 98 % y recupera el servicio tras fallas en 132 a 152 ms, con mejor desempeño que tres métodos de referencia.

**Antítesis identificada.** La evidencia procede exclusivamente de una simulación sobre un conjunto de datos de manufactura de unas 30 horas, y las pruebas de significancia no sustituyen la validación en hardware con redes reales. Los métodos de referencia no son competidores directos de la descarga en el borde, lo que favorece al método propuesto. La Tabla 6 reporta cinco escenarios de dominios distintos sin datos de esos dominios, y la declaración de que la arquitectura es agnóstica carece de prueba. La resistencia a fallas bizantinas y a ataques de inferencia se afirma sin experimentos. El ahorro de ancho de banda de 245 312 MB/min no coincide con el 48 % del resumen, y los hiperparámetros incompletos limitan la replicación. Las fallas simuladas no se describen, por lo que el tiempo de recuperación de 132 a 152 ms no se puede asociar a un tipo de falla ni a un corte de energía o de comunicaciones.

**Síntesis propuesta.** La contribución sostenible es un diseño modular y bien parametrizado de orquestación en el borde, cuya combinación de microclústeres con consenso, descarga aprendida y extracción de características reduce la latencia frente a una ejecución en la nube en el entorno simulado. Para el corpus, la pieza interesa porque ofrece un patrón de arquitectura que podría repartir las tareas de un gemelo digital entre nodos locales y mantener el servicio ante fallas de nodos, un requisito de las empresas tras un sismo. No obstante, la evidencia no respalda la superioridad frente a soluciones de borde especializadas, no examina cortes de energía ni de comunicaciones, y debe tratarse como hipótesis de diseño que requiere prueba con hardware, fallas inyectadas y datos de un contexto de desastre.

**Áreas grises detectadas.**

1. Equivalencia de los métodos de referencia: CEA es un planificador de decisiones en tiempo real, DSS es una taxonomía de apoyo a decisiones con ahorro de energía y DFJSP es una planificación de taller flexible por refuerzo; ninguno es una solución de descarga en el borde, de modo que las ganancias de 39 a 52 ms frente a ellos no permiten concluir que ELARA supere a la descarga adaptativa especializada.
2. Origen de los escenarios múltiples: la Tabla 6 reporta cinco escenarios (fábrica inteligente, salud, movilidad, comercio minorista y control de red eléctrica) pero el conjunto de datos descrito es de manufactura inteligente; el texto no explica cómo se obtuvieron los demás y la afirmación de que la arquitectura es agnóstica del dominio no se prueba.
3. Naturaleza de las fallas: la recuperación de 132 a 152 ms se informa sin indicar qué fallas se inyectaron, en cuántos nodos, si hubo cortes de energía o de comunicaciones ni cuántas tareas se perdieron, de modo que no puede compararse con las interrupciones largas que ocurren tras un sismo.
4. Coherencia de las cifras de ancho de banda: el resumen habla de un ahorro de hasta 48 %, el texto reduce el consumo a 245 312 MB/min y la Ecuación 13 define el ahorro como porcentaje respecto del tráfico bruto; el texto no entrega el valor base ni la unidad de la figura, lo que impide verificar el ahorro.

**Puntos oscuros aclarados.** Llama la atención que un artículo que afirma la tolerancia a fallas bizantinas y la protección contra ataques de inferencia no incluya un solo experimento de seguridad. También es notable que la sección de trabajos relacionados presente los estudios previos con una tabla de marcas cualitativas, sin criterios explícitos de selección, y que la afirmación de que ELARA es la primera solución en integrar tres elementos se apoye en esa tabla. La referencia [31] cumple dos funciones, como trabajo sobre arquitecturas vehiculares de borde y niebla y como repositorio de conjuntos de datos industriales, lo que sugiere un error de citación. Las ecuaciones 1 a 20 son modelos lineales de combinación de términos con coeficientes sin valores, sin una conexión explícita con los resultados. Además, la dependencia de una red Q profunda y de aprendizaje federado en dispositivos con pocos recursos plantea costos de entrenamiento y de energía que el texto afirma proporcionales al tamaño del modelo sin medirlos. Por último, la validación con 20 repeticiones y pruebas t pareadas se presenta como evidencia de robustez, aunque las repeticiones comparten el mismo conjunto de datos y la misma simulación.

**Ideas propositivas novedosas.**

1. Gemelo de planta con microclúster tolerante a cortes: desplegar el patrón de microclúster con consenso en tres o cinco nodos de borde de bajo costo de una pyme, ejecutar un gemelo ligero de continuidad con datos reales de sensores y someterlo a cortes controlados de energía, pérdida de enlace a la nube y fallas de nodos. Se medirían tareas perdidas, tiempo de reasignación y latencia, y se compararían con una descarga adaptativa especializada de la literatura. El resultado indicaría el número mínimo de nodos y el costo para sostener la decisión local de una empresa tras una interrupción grave. Se registraría también el consumo de energía de cada nodo.
2. Banco de pruebas de descarga para escenarios de desastre: construir un banco abierto con perfiles de carga y fallas de comunicación propios de un posterremoto (enlaces intermitentes, nodos con batería, picos de tráfico de alerta) y evaluar ELARA, una descarga adaptativa de referencia y una ejecución centralizada con 30 repeticiones, reportando latencia, energía, finalización de tareas y recuperación con intervalos de confianza. Con ello se podría determinar a partir de qué nivel de degradación de la red conviene el microclúster frente a la nube y proponer criterios de diseño para plantas que deben reanudar operaciones. El banco se publicaría con datos y código.

**Relaciones poco exploradas.**

1. Cómputo en el borde en el corpus (complementa) D064 y D065: D064 usa el borde 5G para detectar daño con retardos medidos de 2,1 ms y D065 propone asignación por subasta entre nodos de borde; D066 aporta una orquestación aprendida con microclústeres y una caracterización de recuperación ante fallas de nodos, aunque solo en simulación.
2. Fallas y continuidad del servicio (se relaciona con) D049 y D060: D049 procesa la detección sísmica en el nodo y D060 clasifica la intensidad en el borde; D066 ofrece un patrón de consenso y reasignación de tareas que podría dar resiliencia a esos nodos.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 4/10 — Aporta una arquitectura de borde con descarga adaptativa, orquestación por refuerzo y microclústeres con consenso, evaluada con 20 repeticiones y pruebas pareadas, y reporta una latencia de 39 a 52 ms y una recuperación ante fallas de 132 a 152 ms. Su valor para el corpus es limitado porque no trata sismos ni empresas, usa solo simulación con datos de manufactura, compara con métodos que no son de descarga en el borde y presenta cifras de ancho de banda incoherentes; sirve como patrón de diseño para gemelos digitales de planta tolerantes a fallas.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Comparación con referencias no equivalentes (CEA, DSS y DFJSP se usan como bases de descarga en el borde aunque son planificadores y taxonomías (Sec. 4, p. 14)); Generalización sin evidencia (Se afirma que la arquitectura es agnóstica del dominio y se reportan cinco escenarios con un único conjunto de manufactura (Sec. 4.A, p. 15; Tabla 6, p. 20)); Afirmación sin prueba (Se atribuye resistencia a fallas bizantinas y a ataques de inferencia sin experimento (Sec. 3.B, p. 11))
- **Bradford-Hill:** No aplica: es un diseño con evaluación por simulación; no se estima causalidad con datos observados.
- **TRL asignado:** 3 — 'To test ELARA in real-world scenarios, Large-scale implementations and long-term testing in dynamic environments will also be required to test ELARA outside of controlled simulations' (p. 22)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (24 páginas, hasta las referencias). Las tablas 6 y 7 se leyeron con filas desordenadas; los valores de ELARA se tomaron del texto y de las filas legibles. La cifra de ancho de banda de 245 312 MB/min se cita tal como aparece y se marca como incoherente. Las páginas siguen los marcadores del PDF.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Una arquitectura descentralizada de borde que extrae características localmente con aprendizaje federado, decide la descarga de tareas con un clasificador adaptativo y orquesta recursos con una red Q profunda dentro de microclústeres con consenso reduce la latencia de extremo a extremo a 39 a 52 ms, ahorra hasta 48 % de ancho de banda y 31 % de energía, sostiene tasas de finalización de tareas de 93 a 98 % y recupera el servicio tras fallas en 132 a 152 ms, con mejor desempeño que tres métodos de referencia.  | La evidencia procede exclusivamente de una simulación sobre un conjunto de datos de manufactura de unas 30 horas, y las pruebas de significancia no sustituyen la validación en hardware con redes reales. Los métodos de referencia no son competidores directos de la descarga en el borde, lo que favorece al método propuesto. La Tabla 6 reporta cinco escenarios de dominios distintos sin datos de esos dominios, y la declaración de que la arquitectura es agnóstica carece de prueba. La resistencia a fallas bizantinas y a ataques de inferencia se afirma sin experimentos. El ahorro de ancho de banda de 245 312 MB/min no coincide con el 48 % del resumen, y los hiperparámetros incompletos limitan la replicación. Las fallas simuladas no se describen, por lo que el tiempo de recuperación de 132 a 152 ms no se puede asociar a un tipo de falla ni a un corte de energía o de comunicaciones.  | La contribución sostenible es un diseño modular y bien parametrizado de orquestación en el borde, cuya combinación de microclústeres con consenso, descarga aprendida y extracción de características reduce la latencia frente a una ejecución en la nube en el entorno simulado. Para el corpus, la pieza interesa porque ofrece un patrón de arquitectura que podría repartir las tareas de un gemelo digital entre nodos locales y mantener el servicio ante fallas de nodos, un requisito de las empresas tras un sismo. No obstante, la evidencia no respalda la superioridad frente a soluciones de borde especializadas, no examina cortes de energía ni de comunicaciones, y debe tratarse como hipótesis de diseño que requiere prueba con hardware, fallas inyectadas y datos de un contexto de desastre.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'ELARA' es la arquitectura propuesta; 'microclúster con consenso' es un grupo local de nodos de borde que acuerdan estado, líder y recuperación; 'descarga adaptativa' es decidir si una tarea se ejecuta localmente, en un nodo cercano o en un módulo remoto; 'recuperación ante fallas' es el tiempo que el sistema tarda en restablecer el servicio tras la falla de un nodo o tarea.
- **P2 Supuestos:** Supone que la simulación con datos de manufactura representa redes IoT masivas, que los tres métodos de referencia son comparables, que el consenso local mantiene un costo constante y que los resultados de un dominio se transfieren a otros sin cambiar la arquitectura.
- **P3 Evidencia:** La evidencia son ocho indicadores de simulación con 20 repeticiones, intervalos de confianza de 95 % y pruebas t pareadas con p < 0,05, una tabla de latencia por modelo de procesamiento y cinco escenarios de precisión de descarga, sin hardware real.
- **P4 Consecuencias:** Si es cierto, los nodos de borde de una planta podrían decidir en milisegundos y recuperarse rápido de fallas sin la nube; si es falso, el sistema puede tener costos de entrenamiento y de coordinación que los dispositivos pequeños no soportan y fallar ante cortes largos.
- **P5 Contraejemplos:** No se examinan comparaciones con soluciones de descarga especializadas, fallas bizantinas, ataques de inferencia, hardware real, consumo del aprendizaje federado ni cortes de energía o de comunicaciones.
- **P6 Alternativas:** Alternativas: que una heurística simple de descarga logre resultados similares; que el beneficio provenga más de la extracción de características que del refuerzo; que la nube con respaldo local sea suficiente para pymes.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Latencia de extremo a extremo de ELARA | 39-52 | ms | Rango en los escenarios evaluados | Resumen, p. 1; Sec. 4.B, p. 16 | Texto | Alta | Simulación de manufactura |
| Latencia promedio del microclúster de borde frente a la nube | 39,5 frente a 152,4 | ms | Desviaciones 2,6 y 6,3 | Tabla 2, p. 7 | Tabla | Alta | Modelos de procesamiento distribuido |
| Ahorro de ancho de banda | hasta 48 | % | Respecto de la transmisión de datos brutos | Resumen, p. 1 | Texto | Media | Cifra de la figura incoherente |
| Ahorro de energía | hasta 31 | % | Frente a métodos de referencia | Resumen, p. 1 | Texto | Media | Energía por tarea de 7,5 a 10,0 J |
| Tasa de finalización de tareas | 93-98 | % | Bajo carga variable | Sec. 4.E, p. 19 | Texto | Media | Sin definición de tarea fallida |
| Tiempo de recuperación ante fallas | 132-152 | ms | Detección, aislamiento, conmutación y sincronización | Sec. 4.G, p. 20 | Texto | Media | Fallas no descritas |
| Precisión de descarga | 89-93 | % | Cinco escenarios en la Tabla 6 | Tabla 6, p. 20 | Tabla | Media | Escenarios sin datos propios |
| Repeticiones experimentales | 20 | repeticiones | Semillas y barajados distintos | Sec. 4, p. 21 | Texto | Alta | Intervalos de confianza de 95 % |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'To test ELARA in real-world scenarios, Large-scale implementations and long-term testing in dynamic environments will also be required to test ELARA outside of controlled simulations' (p. 22) | Prueba de concepto analítica y experimental en simulación; sin prototipo en hardware ni pruebas en entorno operativo. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'ELARA is a practical step to complete autonomy, self-optimization, and energy-efficient IoT edge ecosystems' (p. 22) | Se plantean aplicaciones sin análisis de costos, clientes ni modelo de negocio. |
| IRL | 3 | Sí | 'All baselines were introduced in the same simulation setting, network topology, workload traces, and hardware resource constraints as ELARA to be fair' (p. 14) | Integración de módulos probada en un entorno simulado; sin integración con dispositivos y redes reales. |
| DRL | 2 | Sí | 'Large-scale implementations and long-term testing in dynamic environments will also be required' (p. 22) | Necesidad técnica argumentada; sin estudio de demanda ni de despliegue. |
| SRL | 1.0 | Sí | Componentes: Extracción federada de características (TRL 3), Motor de descarga adaptativa y orquestación por refuerzo (TRL 3), Microclústeres con consenso (TRL 3) | SRL=Σ(TRLi×IRLij)/4 términos ordenados = 9.0; ÷9 → 1.00; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 3 con BRL 1 e IRL 3: arquitectura y resultados simulados sin prototipo en hardware, sin costos ni evidencia de fallas reales. · Estrategia de salida: Prototipo en nodos de borde reales, fallas inyectadas, comparación con descarga especializada y análisis de costos.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Comparación con referencias no equivalentes | CEA, DSS y DFJSP se usan como bases de descarga en el borde aunque son planificadores y taxonomías (Sec. 4, p. 14) | Favorece al método propuesto |
| Generalización sin evidencia | Se afirma que la arquitectura es agnóstica del dominio y se reportan cinco escenarios con un único conjunto de manufactura (Sec. 4.A, p. 15; Tabla 6, p. 20) | Escenarios sin datos propios |
| Afirmación sin prueba | Se atribuye resistencia a fallas bizantinas y a ataques de inferencia sin experimento (Sec. 3.B, p. 11) | Propiedad no medida |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Descarga adaptativa y microclústeres → menor latencia y mejor finalización de tareas | Comparación con tres bases en simulación con 20 repeticiones | Mecanismo directo | Pruebas en hardware con redes reales | Carga, topología, calidad de red | 3 | Efecto plausible en simulación |
| Consenso de microclúster → recuperación rápida ante fallas | Tiempo de recuperación de 132 a 152 ms | Mecanismo directo | Fallas inyectadas de tipos distintos | Tipo y duración de la falla, energía, comunicaciones | 2 | Relación sin descripción de las fallas |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Validación en hardware real, fallas inyectadas y bases de comparación de descarga en el borde | Crítico | Media | 9 |
| Tecnológico | Costos de entrenamiento federado y de la red Q profunda en dispositivos de bajo costo, y seguridad frente a fallas bizantinas | Crítico | Media | 8 |
| Conocimiento | Comportamiento ante cortes de energía y de comunicaciones propios de un desastre | Crítico | Alta | 9 |
| Mercado | Costos de despliegue y viabilidad para pequeñas y medianas empresas | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Flujo de razonamiento adaptativo multinivel de ELARA | Diagrama | Preprocesamiento, descarga, consenso y salida de decisiones | No aplica | Media |
| Fig. 2 | Pila de procesamiento IoT distribuido de varias capas | Diagrama | Capas de dispositivos, borde, niebla y nube | No aplica | Media |
| Fig. 3-8 | Latencia, ancho de banda, energía, finalización, utilización y recuperación | Gráficos de barras | ELARA frente a CEA, DSS y DFJSP | 39-52 ms; 7,5-10,0 J por tarea; 93-98 %; 132-152 ms | Media |
| Tabla 2 | Latencia, fluctuación y deriva de sincronización por modelo de procesamiento | Tabla | Microclúster de borde con 39,5 ms frente a 152,4 ms de la nube | 39,5; 152,4 | Alta |
| Tabla 6-7 | Precisión de descarga y velocidad de inferencia en cinco escenarios | Tabla | ELARA con 89 a 93 % y 850 a 932 muestras por segundo | 89-93 %; 850-932 | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| CEA (planificación de decisiones en tiempo real) | No especificado en documento | Academia | Planificación de tareas con frescura de datos | Referencia publicada | No es solución de descarga en el borde | Estable |
| DFJSP con aprendizaje por refuerzo jerárquico | No especificado en documento | Academia | Planificación de taller flexible dinámico | Buena calidad de planificación | Dominio de manufactura de taller | Estable |
| Arquitectura vehicular de borde y niebla de Hassan et al. (2025) | No especificado en documento | Academia | Coordinación jerárquica de tráfico | Optimización centralizada | Sobrecarga de coordinación declarada por el autor | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Latencia de extremo a extremo (ms), ancho de banda, energía por tarea (J), finalización de tareas (%), recuperación ante fallas (ms) y precisión de descarga (%)
- **X:** Uso de ELARA frente a CEA, DSS y DFJSP
- **Z (controles):** Carga de trabajo, topología, restricciones de ancho de banda y recursos, semillas aleatorias
- **Datos:** Conjunto industrial público de unos 120 000 registros de unas 30 horas a 1 Hz con 24 variables, en una simulación de borde y niebla
- **Método:** Simulación con 20 repeticiones, intervalos de confianza de 95 % y pruebas t pareadas bilaterales
- **Efecto reportado:** Latencia de 39 a 52 ms; ahorro de ancho de banda de hasta 48 %; ahorro de energía de hasta 31 %; precisión de descarga de 89 a 93 %
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** 20 repeticiones y pruebas pareadas en el mismo conjunto de datos; sin validación externa ni valores p

| Vacío | Tipo | Descripción |
|---|---|---|
| V-066-01 | TERR | No especificado en documento; autor en Shangqiu, China, sin territorio de despliegue |
| V-066-02 | POBL | Dispositivos IoT simulados; sin empresas ni usuarios |
| V-066-03 | TEMP | Unas 30 horas de datos; milisegundos de latencia; sin operación prolongada |
| V-066-04 | MET | Solo simulación, un conjunto de manufactura y bases no equivalentes |
| V-066-05 | VAR | Faltan costos, consumo medido en hardware, tipo de falla y cortes de energía o de comunicaciones |
| V-066-06 | TEOR | Computación en el borde y aprendizaje por refuerzo; sin teoría de resiliencia empresarial |
| V-066-07 | CAUS | Efecto de la tolerancia a fallas sobre la continuidad operativa sin evidencia |
