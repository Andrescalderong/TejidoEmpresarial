# FB-L01-057 | D057 — Multihop Routing for IoT-Based Digital Twin: Novel Metaheuristic Approaches

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/Multihop_Routing_for_IoT-Based_Digital_Twin_Novel_Metaheuristic_Approaches.pdf` · 14 páginas · Relevancia para el eje del corpus: **Periférico** (Formula el problema MOUNTAIN de enrutamiento multisalto en sistemas de gemelo digital basados en IoT (minimizar energía con restricciones de precisión del gemelo y de retardo) y propone dos algoritmos evolutivos, uno de tarea única (STEA) y uno multitarea (MTEA), evaluados en simulación sintética. Aporta la capa de optimización de red entre sensores y gemelo, pero es un estudio de simulación sin vínculo con sismos, infraestructura o empresas.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-057 / D057
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, IEEE Internet of Things Journal)
- **Referencia APA 7:** Cong Dao, T., Cong Luong, N., Hung Nguyen, N., Li, X., Niyato, D., & In Kim, D. (2025). Multihop Routing for IoT-Based Digital Twin: Novel Metaheuristic Approaches. *IEEE Internet of Things Journal*, *12*(15), 30493-30506. https://doi.org/10.1109/JIOT.2025.3573710
- **Autores:** Cong Dao, Tran (60015392900); Cong Luong, Nguyen (57188862862); Hung Nguyen, Ngoc (57204050466); Li, Xingwang (56152312500); Niyato, Dusit (8919714700); In Kim, Dong (35476060100)
- **Afiliaciones:** Phenikaa University, Faculty of Computer Science, Hanoi, 12116, Viet Nam; Center for Environmental Intelligence, College of Engineering and Computer Science, VinUniversity, Hanoi, 10000, Viet Nam; Henan Polytechnic University, School of Physics and Electronic Information Engineering, Jiaozuo, 454000, China; Nanyang Technological University, College of Computing and Data Science, Jurong West, Singapore; Sungkyunkwan University, Department of Electrical and Computer Engineering, Suwon, 16419, South Korea
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** IEEE Internet of Things Journal · vol. 12(15)
- **Identificador persistente:** DOI 10.1109/JIOT.2025.3573710 · ISSN 23274662
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105006886720&doi=10.1109%2fJIOT.2025.3573710&partnerID=40&md5=f6fd457ed71e5ed15c1e49558f635417
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 10

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Optimizar el enrutamiento multisalto en sistemas de internet de las cosas (IoT) con gemelo digital, en el problema denominado MOUNTAIN, donde múltiples dispositivos de la red física transmiten datos de forma frecuente al gemelo de red digital (DNT) gestionado por un servidor central. El estudio busca reducir el consumo total de energía de la red manteniendo una transmisión de datos robusta, equilibrando precisión del gemelo y costos de comunicación, mediante dos algoritmos evolutivos: uno que resuelve cada instancia de forma independiente (STEA) y otro que resuelve varias instancias a la vez e intercambia información entre búsquedas (MTEA).

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si una representación de soluciones y operadores genéticos específicos permiten hallar rutas multisalto de menor consumo energético que algoritmos de referencia, si la optimización multitarea acelera la convergencia y mejora la calidad frente a la de tarea única, y cómo cambia el desempeño con el número de dispositivos, de relevos y de bloques de recursos.

**Marco teórico.** El marco combina el concepto de gemelo digital de red (una réplica de la red física que requiere datos actualizados de los dispositivos) con modelos de energía de transmisión multisalto, restricciones de precisión del gemelo (umbral de 0,6), de retardo máximo (0,1 s) y de recursos de radio (bloques de recursos), y con la teoría de computación evolutiva y optimización multitarea evolutiva. El problema se formula como minimización de la energía total sujeta a esas restricciones, con una topología de árbol de enrutamiento hacia la estación base y con dispositivos que pueden actuar como relevos. El modelo de sistema considera un gemelo de red digital generado y controlado por un servidor central, transmisión de enlace ascendente por acceso múltiple por división de frecuencia (FDMA), una tasa de transmisión que depende del ancho de banda del bloque de recursos, la potencia y la ganancia del canal con pérdida de trayecto y sombreado, y una tasa de error de transmisión que aparece por la aleatoriedad del canal.

**Metodología.** Se formula el problema MOUNTAIN y se diseñan una codificación de soluciones basada en árboles de enrutamiento y operadores genéticos de cruce y mutación específicos, para STEA, y una codificación unificada que permite resolver varias instancias a la vez y transferir información entre ellas, para MTEA. Los experimentos usan conjuntos de datos sintéticos con K dispositivos distribuidos de manera uniforme en un área de 200 m por 200 m, con la estación base en el centro (100, 100) y un subconjunto de M dispositivos con capacidad de relevo. Los parámetros de restricción (umbral de precisión 0,6, límite de latencia 0,1 s y parámetro de sensibilidad) se heredan de trabajos previos. Se comparan STEA y MTEA con cuatro referencias: aleatoria, voraz, un algoritmo genético y el algoritmo de optimización de buitres africanos (AVOA), midiendo energía total, retardo, convergencia y tiempo de ejecución al variar el número de dispositivos, de relevos y de bloques de recursos.

**Resultados principales.** MTEA converge en alrededor de 30 iteraciones y STEA en unas 40, y ambos alcanzan soluciones de menor energía que las referencias; MTEA obtiene la mejor calidad de solución y converge más rápido que STEA. Al aumentar el número de dispositivos, la energía total de la red crece, y STEA y MTEA mantienen el menor consumo en todos los casos frente a los algoritmos aleatorio, voraz, genético y AVOA. Con más dispositivos con capacidad de relevo, el consumo de energía de los algoritmos propuestos disminuye, y con más bloques de recursos aprovechan mejor la capacidad disponible. El algoritmo voraz logra retardos ligeramente menores en algunos puntos, a costa de mayor energía. Los tiempos de ejecución de STEA y MTEA son mayores que los de los algoritmos aleatorio y voraz, pero se consideran aceptables. En el análisis de retardo, MTEA mantiene un aumento mínimo al crecer el número de dispositivos, mientras el algoritmo voraz tiene retardos algo menores en algunos puntos con mayor energía. Los autores concluyen que los algoritmos reducen la energía y mejoran la estabilidad de la red, y afirman ser los primeros en investigar el enrutamiento multisalto en sistemas de gemelo digital basados en IoT, con dos contribuciones principales: la formulación del problema y los dos algoritmos metaheurísticos.

**Discusión y contribución.** Los autores atribuyen el desempeño superior a la representación de soluciones y a los operadores genéticos, que equilibran exploración y explotación, y el mejor resultado de MTEA a su mecanismo de transferencia de conocimiento entre tareas. Sostienen que los métodos contribuyen a infraestructuras de IoT sostenibles que soportan gemelos de alta fidelidad, y reconocen que el aumento de densidad puede incrementar interferencia y congestión. Señalan como trabajo futuro la extensión a entornos heterogéneos y dinámicos y la optimización entre capas con técnicas de capa física. Reconocen que, por la aleatoriedad del canal, los datos recibidos por el servidor pueden contener errores, lo que justifica la restricción de precisión del gemelo, y que la ejecución de los algoritmos propuestos requiere más tiempo de cómputo que las referencias simples.

**Limitaciones declaradas.** Declaradas: uso de conjuntos de datos sintéticos con distribución uniforme de dispositivos y condiciones de red estáticas. No declaradas: sin datos de despliegues reales ni de pérdida de enlaces; escala de 200 m por 200 m con un número limitado de dispositivos; comparación con cuatro referencias, no con otros algoritmos evolutivos multiobjetivo ni con protocolos estándar de enrutamiento; el tiempo de cómputo de la optimización puede ser incompatible con reconfiguración rápida en emergencias; sin análisis de significancia estadística de las diferencias; sin consideración de fallas de nodos ni de conectividad degradada.

**Trabajo futuro.** Explícito: extensión a entornos heterogéneos y dinámicos y optimización entre capas que combine el enrutamiento con técnicas de capa física. Implícito: pruebas con topologías reales, fallas de nodos y escenarios de reconfiguración.

**Palabras clave.** Declaradas: Digital twin; energy minimization; evolutionary algorithm; Internet of Things (IoT); multihop routing | Inferidas: enrutamiento multisalto, gemelo digital, internet de las cosas, algoritmo evolutivo, optimización multitarea, eficiencia energética, red de gemelo digital, retardo, precisión del gemelo, metaheurística

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Los algoritmos evolutivos STEA y MTEA, con una codificación de árboles de enrutamiento y operadores genéticos diseñados para el problema, hallan rutas multisalto que reducen el consumo de energía de redes IoT con gemelo digital más que los algoritmos de referencia (aleatorio, voraz, genético y AVOA), manteniendo la precisión del gemelo y el retardo, y el enfoque multitarea de MTEA converge más rápido y con mejor calidad al compartir información entre instancias.

**Antítesis identificada.** El resultado es una comparación de simulación con parámetros heredados y un escenario pequeño y estático. Se mide el objetivo diseñado para el problema, y las referencias no incluyen protocolos de enrutamiento estándar ni otros métodos multiobjetivo, por lo que la superioridad se establece frente a un conjunto limitado. No se reporta significancia estadística ni desviación entre ejecuciones en el texto leído. La distribución uniforme en 200 m por 200 m no representa despliegues urbanos o de infraestructura, donde los enlaces varían. El mayor tiempo de ejecución de los métodos propuestos puede ser incompatible con la reconfiguración en tiempo real, y no se discute el efecto de fallas de nodos, que es el escenario relevante tras un desastre.

**Síntesis propuesta.** La contribución sostenible es una formulación del problema de enrutamiento para gemelos de red con restricciones de precisión y retardo, y una familia de algoritmos que, en el escenario simulado, reduce la energía frente a referencias simples y se beneficia de la transferencia entre tareas. Para el corpus, su valor es de contexto: señala que la actualización del gemelo es un problema de optimización de energía y retardo, y que el diseño de red condiciona la precisión del gemelo. No ofrece evidencia en infraestructura ni sobre resiliencia ante fallas, y sus conclusiones de eficiencia energética no deben extrapolarse a entornos de desastre sin pruebas adicionales.

**Áreas grises detectadas.**

1. Realismo de los escenarios: los datos son sintéticos, con dispositivos distribuidos uniformemente en 200 m por 200 m y una estación base central; no se prueban topologías irregulares, obstáculos ni pérdida de enlaces, y los parámetros de restricción se heredan de trabajos previos sin sensibilidad propia.
2. Referencias de comparación: los algoritmos aleatorio y voraz son simples y el genético y el AVOA son metaheurísticas genéricas; no se compara con protocolos estándar de enrutamiento para redes de sensores ni con otros métodos multiobjetivo, por lo que el margen de mejora puede sobrestimarse.
3. Costo computacional: STEA y MTEA requieren más tiempo de ejecución que las referencias; el texto lo considera aceptable, pero no se mide frente al tiempo disponible para reconfigurar la red tras un evento o con cientos de dispositivos.
4. Robustez ante fallas: la conclusión de mejor estabilidad de la red se apoya en el consumo de energía y la convergencia, no en pruebas con pérdida de nodos o de enlaces, que son el escenario crítico para gemelos de infraestructura tras un desastre.

**Puntos oscuros aclarados.** Llama la atención que se afirme mejor estabilidad de la red cuando las pruebas solo miden energía, retardo y convergencia en una red estática. También es notable que el escenario se limite a 200 m por 200 m con dispositivos uniformes, lejos de despliegues de infraestructura, y que se reconozca como limitación pero se formulen conclusiones de sostenibilidad general. La ventaja de MTEA sobre STEA se explica por transferencia de conocimiento sin analizar cuándo esa transferencia puede perjudicar. Además, el algoritmo voraz logra menor retardo en algunos puntos, lo que muestra un compromiso que los autores resuelven priorizando la energía sin discutir si en aplicaciones de emergencia el retardo es más crítico. Finalmente, la mejora de energía de los algoritmos propuestos se reporta en gráficas sin intervalos de confianza ni número de repeticiones, y el artículo se declara pionero sin contrastar con estudios de enrutamiento en gemelos de red que podrían ser relevantes.

**Ideas propositivas novedosas.**

1. Optimización de enrutamiento con fallas de nodos: replicar el problema con una probabilidad de falla de nodos y enlaces tras un evento sísmico y medir cuánto aumenta la energía y cuánta precisión del gemelo se pierde, comparando STEA y MTEA con reconfiguración rápida basada en reglas. El resultado indicaría si la optimización evolutiva es útil en emergencias o si debe sustituirse por heurísticas simples, e identificaría el umbral de nodos perdidos que hace perder el gemelo de una planta o de un edificio. Se reportaría el tiempo de reconfiguración de cada método y la proporción de datos que llegan con error, para decidir qué método instalar en un nodo coordinador de bajo costo.
2. Gemelo de red para pymes con sensores de bajo costo: aplicar la formulación a una red de sensores de bajo costo en una nave industrial, con topología irregular y obstáculos, y medir energía, vida útil de baterías y precisión del gemelo. Un piloto permitiría estimar cuántos relevos hacen falta para mantener la precisión mínima de 0,6 y cuánto cuesta mantener la red, lo que daría un indicador económico de la capa de comunicación de un gemelo ligero. La evaluación se repetiría con y sin interferencia de maquinaria industrial, que es una fuente de pérdida de enlaces en naves reales.

**Relaciones poco exploradas.**

1. Conectividad del gemelo (se relaciona con) D036: D036 revisa tecnologías de comunicación para gemelos digitales (RIS, UAV, mmWave), y D057 optimiza el enrutamiento multisalto entre sensores y gemelo; ambos tratan la capa que sostiene la sincronización.
2. Procesamiento y comunicación en el borde (se relaciona con) D049: D049 mide latencias de una arquitectura descentralizada de alerta sísmica con sensores de bajo costo y D057 optimiza energía y retardo de rutas; comparten la restricción de energía y latencia.

**Robustez argumentativa:** 2.1/10 (ponderación 30/30/25/15) — consistencia lógica 2/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 3/10 — Aporta una formulación y algoritmos de optimización de enrutamiento para gemelos de red con restricciones de precisión y retardo, con evidencia de simulación. Su valor para el corpus es periférico: el escenario es sintético, estático y pequeño, no hay fallas ni infraestructura y no se relaciona con sismos o empresas. Sirve como referencia de la dimensión energética y de retardo de la comunicación sensor-gemelo, y como ejemplo de que la calidad del gemelo depende del diseño de la red, un aspecto que los estudios de gemelos de infraestructura del corpus suelen dar por supuesto.

**Conexiones inter-documentales.**

- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 80 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Conclusión más amplia que la evidencia (Se afirma mejor estabilidad de la red con pruebas que miden energía, retardo y convergencia en una red estática (Resumen, p. 1; Sec. VI, p. 12)); Comparación con referencias débiles (La superioridad se establece frente a un algoritmo aleatorio, uno voraz y dos metaheurísticas genéricas (Sec. V, p. 10-12)); Generalización apresurada (Se concluye sostenibilidad para infraestructuras IoT desde una simulación de 200 m por 200 m (Sec. VI, p. 12))
- **Bradford-Hill:** No aplica: es un estudio de optimización con simulación; no se estima ningún efecto causal sobre el desempeño de gemelos reales.
- **TRL asignado:** 3 — 'Our study has limitations, including the use of synthetic datasets with uniform device distributions and static network conditions' (p. 12)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (14 páginas). Las figuras de resultados no son legibles; las descripciones se tomaron del texto de la sección V. No se reportan cifras numéricas de ahorro de energía en el texto leído.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Los algoritmos evolutivos STEA y MTEA, con una codificación de árboles de enrutamiento y operadores genéticos diseñados para el problema, hallan rutas multisalto que reducen el consumo de energía de redes IoT con gemelo digital más que los algoritmos de referencia (aleatorio, voraz, genético y AVOA), manteniendo la precisión del gemelo y el retardo, y el enfoque multitarea de MTEA converge más rápido y con mejor calidad al compartir información entre instancias.  | El resultado es una comparación de simulación con parámetros heredados y un escenario pequeño y estático. Se mide el objetivo diseñado para el problema, y las referencias no incluyen protocolos de enrutamiento estándar ni otros métodos multiobjetivo, por lo que la superioridad se establece frente a un conjunto limitado. No se reporta significancia estadística ni desviación entre ejecuciones en el texto leído. La distribución uniforme en 200 m por 200 m no representa despliegues urbanos o de infraestructura, donde los enlaces varían. El mayor tiempo de ejecución de los métodos propuestos puede ser incompatible con la reconfiguración en tiempo real, y no se discute el efecto de fallas de nodos, que es el escenario relevante tras un desastre.  | La contribución sostenible es una formulación del problema de enrutamiento para gemelos de red con restricciones de precisión y retardo, y una familia de algoritmos que, en el escenario simulado, reduce la energía frente a referencias simples y se beneficia de la transferencia entre tareas. Para el corpus, su valor es de contexto: señala que la actualización del gemelo es un problema de optimización de energía y retardo, y que el diseño de red condiciona la precisión del gemelo. No ofrece evidencia en infraestructura ni sobre resiliencia ante fallas, y sus conclusiones de eficiencia energética no deben extrapolarse a entornos de desastre sin pruebas adicionales.  | 2.1/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'MOUNTAIN' es el problema de enrutamiento multisalto con gemelo digital; 'tarea única' resuelve una instancia por vez; 'multitarea' resuelve varias a la vez compartiendo información; 'precisión del gemelo' es la fidelidad exigida a los datos.
- **P2 Supuestos:** Supone que la simulación uniforme representa redes reales, que los parámetros heredados son adecuados y que menor energía implica mejor estabilidad.
- **P3 Evidencia:** La evidencia son curvas de simulación comparando seis algoritmos en un área de 200 m por 200 m, sin pruebas estadísticas visibles ni datos reales.
- **P4 Consecuencias:** Si es cierto, las redes de gemelos pueden operar con menos energía; si es falso, la mejora puede no mantenerse con topologías reales o con fallas.
- **P5 Contraejemplos:** No se examinan fallas de nodos, topologías reales, otros protocolos de enrutamiento ni tiempos de reconfiguración.
- **P6 Alternativas:** Alternativas: que un protocolo estándar iguale el desempeño; que el costo computacional anule la ventaja; que la precisión del gemelo dependa más de la frecuencia de actualización.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Iteraciones de convergencia de MTEA / STEA | 30 / 40 | iteraciones | Aproximadamente | Sec. V, p. 11 | Texto | Media | Dato aproximado del texto |
| Área de simulación | 200 × 200 | m | Estación base en (100, 100) | Sec. V, p. 10 | Texto | Alta | Distribución uniforme |
| Umbral de precisión del gemelo | 0,6 | adimensional | Heredado de trabajos previos | Sec. V, p. 10 | Texto | Alta | Parámetro An |
| Límite de latencia | 0,1 | s | Parámetro Ln heredado | Sec. V, p. 10 | Texto | Alta | Sin sensibilidad propia |
| Algoritmos de referencia | 4 | algoritmos | Aleatorio, voraz, genético y AVOA | Sec. V, p. 10 | Texto | Alta | Comparación en energía y retardo |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'Our study has limitations, including the use of synthetic datasets with uniform device distributions and static network conditions' (p. 12) | Prueba de concepto en simulación con datos sintéticos; sin despliegue. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'reducing energy consumption and improving network stability' (p. 1) | Beneficio en energía sin análisis de costos ni modelo de negocio. |
| IRL | 2 | Sí | 'the accuracy threshold An = 0.6 and latency limit Ln = 0.1 s were shown to effectively balance data fidelity and communication cost' (p. 10) | Se integra la precisión del gemelo con la red mediante parámetros heredados; sin pruebas de integración. |
| DRL | 2 | Sí | 'Given the limited energy resources of IoT devices, our approach considers both energy efficiency and communication reliability' (p. 1) | Necesidad argumentada por restricción de energía; sin demanda de usuarios. |
| SRL | 1.0 | Sí | Componentes: Algoritmos evolutivos de enrutamiento (TRL 3), Gemelo de red digital (TRL 2) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 5.0; ÷9 → 0.56; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 3 con BRL 1 e IRL 2: simulación sintética estática sin fallas, sin costos y sin integración real. · Estrategia de salida: Pruebas con topologías reales, fallas de nodos y comparación con protocolos estándar.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Conclusión más amplia que la evidencia | Se afirma mejor estabilidad de la red con pruebas que miden energía, retardo y convergencia en una red estática (Resumen, p. 1; Sec. VI, p. 12) | La estabilidad no se evalúa con fallas |
| Comparación con referencias débiles | La superioridad se establece frente a un algoritmo aleatorio, uno voraz y dos metaheurísticas genéricas (Sec. V, p. 10-12) | Sin protocolos estándar |
| Generalización apresurada | Se concluye sostenibilidad para infraestructuras IoT desde una simulación de 200 m por 200 m (Sec. VI, p. 12) | Escenario no representativo |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Enrutamiento optimizado → menor energía de la red | Simulación comparativa | Mecanismo directo (modelo de energía) | Pruebas con topologías reales | Modelo de propagación, densidad, interferencia | 3 | Efecto dentro del modelo, sin validación externa |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Significancia estadística, topologías reales y comparación con protocolos estándar | Crítico | Media | 8 |
| Tecnológico | Robustez ante fallas de nodos y reconfiguración rápida | Crítico | Media | 8 |
| Conocimiento | Vínculo entre precisión del gemelo, red y decisiones de continuidad | Significativo | Media | 7 |
| Mercado | Costos de relevos y de mantenimiento de la red | Moderado | Baja | 5 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 5 | Consumo de energía frente al número de dispositivos | Gráfico | Comparación de seis algoritmos | No aplica | Media |
| Fig. 6 | Consumo de energía frente al número de dispositivos con capacidad de relevo | Gráfico | Efecto de los relevos | No aplica | Media |
| Fig. 7 | Consumo de energía frente al número máximo de bloques de recursos | Gráfico | Efecto de los recursos de radio | No aplica | Media |
| Fig. 9 | Tiempo de ejecución de los algoritmos | Gráfico | Costo computacional | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| AVOA (algoritmo de optimización de buitres africanos) | No especificado en documento | Academia | Metaheurística de optimización global | Generalidad | No diseñado para el problema | Estable |
| Algoritmos genético, voraz y aleatorio | No especificado en documento | Academia | Referencias de comparación | Simplicidad | Menor calidad de solución | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Consumo total de energía de la red y retardo de transmisión
- **X:** Algoritmo de enrutamiento (STEA, MTEA y referencias)
- **Z (controles):** Número de dispositivos, de relevos y de bloques de recursos
- **Datos:** Conjuntos de datos sintéticos en un área de 200 m por 200 m
- **Método:** Simulación comparativa de algoritmos de optimización
- **Efecto reportado:** Menor energía de STEA y MTEA frente a referencias; convergencia en 30 a 40 iteraciones
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Variación de parámetros del escenario; sin significancia estadística ni fallas

| Vacío | Tipo | Descripción |
|---|---|---|
| V-057-01 | TERR | Sin territorio; datos sintéticos |
| V-057-02 | POBL | Sin usuarios ni empresas |
| V-057-03 | TEMP | Sin dinámica temporal; red estática |
| V-057-04 | MET | Datos sintéticos, referencias limitadas y sin pruebas estadísticas visibles |
| V-057-05 | VAR | Faltan fallas de nodos, interferencia real, costos y vida útil de baterías |
| V-057-06 | TEOR | Optimización evolutiva y multitarea; sin teoría de resiliencia |
| V-057-07 | CAUS | Sin evidencia causal sobre decisiones |
