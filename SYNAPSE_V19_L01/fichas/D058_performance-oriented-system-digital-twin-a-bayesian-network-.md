# FB-L01-058 | D058 — Performance-oriented system digital twin: a Bayesian network-based framework to customize Sub-digital twins

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/Performance-oriented system digital twin  a Bayesian network-based framework to customize Sub-digital twins.pdf` · 22 páginas · Relevancia para el eje del corpus: **Periférico** (Propone un marco de gemelo digital de sistema (SDT) para infraestructura basado en grafos de conocimiento y redes bayesianas, con un algoritmo que genera sub-gemelos personalizados por medida de desempeño y fuentes de datos disponibles, probado con un grafo hipotético y con la red de puentes del condado de Miami-Dade. Aporta una vía de escalabilidad computacional para gemelos de infraestructura con riesgo, pero no trata sismos, empresas ni recuperación productiva.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-058 / D058
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, 2025)
- **Referencia APA 7:** Cheng, M., Geng, Z., & Gao, H. O. (2025). Performance-oriented system digital twin: a Bayesian network-based framework to customize Sub-digital twins. *Structure and Infrastructure Engineering*, *21*(7-8), 1303-1323. https://doi.org/10.1080/15732479.2025.2504535
- **Autores:** Cheng, Minghui (57204875305); Geng, Ziheng (59644699800); Gao, H. Oliver (15922676800)
- **Afiliaciones:** Department of Civil & Architectural Engineering, University of Miami, Coral Gables, FL, United States; School of Architecture, University of Miami, Coral Gables, FL, United States; Systems Engineering, Cornell University, Ithaca, NY, United States; School of Civil and Environmental Engineering, Cornell University, Ithaca, NY, United States
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Structure and Infrastructure Engineering · vol. 21(7-8)
- **Identificador persistente:** DOI 10.1080/15732479.2025.2504535 · ISSN 15732479
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105005590560&doi=10.1080%2f15732479.2025.2504535&partnerID=40&md5=4cd22342821b1eb6e069276672cf6c75
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 2

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Proponer un marco de gemelo digital de sistema (SDT) orientado al desempeño para el modelado y la gestión de infraestructura inteligente, que resuelva los desafíos de almacenamiento y de cómputo que aparecen al construir gemelos con redes bayesianas (BN) de sistemas complejos. El marco busca representar sistemas complejos con grafos de conocimiento (KG) mutables, capturar correlaciones estadísticas entre subsistemas, permitir la evolución y transformación del sistema y generar sub-gemelos personalizados a partir de los KG según las medidas de desempeño seleccionadas y los datos disponibles, para apoyar decisiones ante eventos.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son cómo reducir el costo de almacenamiento y de inferencia de una red bayesiana que representa un sistema de infraestructura a escala de ciudad o condado, y si un sub-gemelo extraído para una medida de desempeño conserva la utilidad para actualizar y consultar el riesgo con una fracción del tamaño original.

**Marco teórico.** El marco combina tres elementos. Primero, la red bayesiana como herramienta probabilística para actualizar creencias con evidencia de monitoreo. Segundo, el grafo de conocimiento, que almacena conceptos y relaciones del sistema (incluida geometría espacial) y puede cambiar con el tiempo. Tercero, una filosofía de diseño orientada al desempeño y centrada en el usuario, en la que el SDT conserva el grafo y construye, cuando se requiere, un sub-gemelo para una medida de desempeño determinada. El riesgo de un puente se define como el producto de la probabilidad de falla y la consecuencia de la falla, con ontología que enlaza sistemas de puentes, tráfico y ríos.

**Metodología.** El algoritmo sigue tres pasos: seleccionar el subgrafo del KG relevante para la medida de desempeño y las fuentes de datos, construir la red bayesiana correspondiente y transformarla en el sub-gemelo. El ejemplo 1 usa un grafo hipotético de 36 nodos con dos componentes para demostrar versatilidad. El ejemplo 2 aplica el marco a la red de puentes de Miami-Dade, con fuentes de datos de calificaciones de condición de superestructura y subestructura, caudal y nivel de estaciones de río y tránsito diario promedio anual de estaciones de monitoreo; los nodos de río se conectan a puentes dentro de 5 km y cada puente se conecta a sus 10 estaciones de tránsito más cercanas. Se comparan el tamaño y el costo de memoria de la red bayesiana completa y de los sub-gemelos, sin validación con eventos reales. El algoritmo opera con tres recortes sucesivos: un primer recorte del grafo respecto del nodo de medida de desempeño, un segundo que elimina nodos sin influencia sobre ese nodo (con base en alcanzabilidad) y detecta fuentes de datos redundantes cuando una está bloqueada por otra, y un tercero que descarta ramas sin nodos de datos que no pueden activar inferencia bayesiana.

**Resultados principales.** En el ejemplo de la red de puentes, un SDT personalizado con un tamaño de 1 % del KG original puede crearse para uso práctico y mejora de forma significativa la eficiencia computacional. Se informa que la red bayesiana completa reestructurada ocuparía hasta 73 362,9 MB de memoria para las tablas de probabilidad condicional cuando los nodos tienen 4 estados discretos, mientras que la red transformada del tronco personalizado ocupa 625,3 MB. El ejemplo hipotético demuestra la construcción del SDT desde un grafo con dos componentes y la generación de sub-gemelos para distintas medidas de desempeño. No se reportan métricas de exactitud de la actualización del riesgo ni comparaciones con otros métodos de reducción de redes bayesianas. En el ejemplo hipotético, tres escenarios de datos disponibles muestran que algunas fuentes (por ejemplo, X5 y X11) resultan redundantes cuando existen otras (X17 y X19) que bloquean su influencia, mientras que en otro escenario todas son útiles, lo que ilustra que el algoritmo decide qué datos se usan según la medida de desempeño y los datos disponibles en cada escenario y no solo según la cercanía en el grafo. Los nodos puente intermedios se conservan cuando transmiten la influencia de nodos de datos a la medida de desempeño.

**Discusión y contribución.** Los autores sostienen que el marco ofrece escalabilidad y flexibilidad para el apoyo de decisiones con gemelos digitales de infraestructura a escala de sistema, porque conserva el conocimiento del sistema en un grafo y genera solo la parte necesaria para cada decisión. Reconocen que el marco depende de la disponibilidad de grafos de conocimiento a escala de ciudad, que la geometría de los componentes no se integra a una resolución fina y que no se incorporan sensores, simulaciones, modelos basados en datos ni control predictivo en la arquitectura del gemelo, y proponen integrar estándares BIM y generar los grafos de forma automática.

**Limitaciones declaradas.** Declaradas: los grafos de conocimiento a escala de ciudad son escasos en la práctica; falta la geometría de componentes a resolución fina (estándares BIM); el marco se centra en el cómputo a nivel de sistema sin sensores, simulaciones, modelos basados en datos ni control. No declaradas: sin validación de exactitud del riesgo frente a eventos observados; sin comparación con otros métodos de reducción de redes bayesianas; la discretización en 4 estados y la ontología de riesgo se fijan por supuesto; el riesgo de puentes considera inundación y tránsito, no sismos; el ejemplo de Miami-Dade usa datos disponibles públicamente sin evaluación del uso por decisores.

**Trabajo futuro.** Explícito: desarrollar metodologías de generación automática de grafos de conocimiento para sistemas de infraestructura, integrar estándares BIM para la geometría de los componentes e integrar tecnologías habilitadoras de gemelos (sensores, simulaciones, modelos basados en datos y control predictivo). Implícito: validación con eventos y evaluación con usuarios.

**Palabras clave.** Declaradas: Bayesian networks; bridge networks; complex systems; digital twins; infrastructure management; probabilistic inference; system reliability analysis; uncertainty quantification | Inferidas: gemelo digital, red bayesiana, grafo de conocimiento, sub-gemelo digital, infraestructura, riesgo de puentes, escalabilidad computacional, Miami-Dade, toma de decisiones, sistemas interdependientes

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un gemelo digital de sistema basado en un grafo de conocimiento mutable que genera, bajo demanda, sub-gemelos de redes bayesianas personalizados por medida de desempeño y por fuentes de datos disponibles permite gestionar infraestructura compleja con una fracción del costo computacional: en la red de puentes de Miami-Dade, un sub-gemelo de 1 % del grafo original reduce de forma drástica la memoria (de decenas de miles de megabytes a cientos) y soporta la actualización del riesgo con datos de condición, ríos y tránsito.

**Antítesis identificada.** El artículo demuestra eficiencia de almacenamiento, no utilidad para la decisión. No hay validación de que el riesgo actualizado con el sub-gemelo coincida con el de la red completa ni con eventos observados, ni comparación con técnicas de reducción de redes bayesianas conocidas. El riesgo modelado es de inundación y tráfico, sin amenazas sísmicas, y se fija por una ontología de supuestos. El requisito de un KG a escala de condado, reconocido como escaso, condiciona toda la propuesta, y no se integran sensores ni simulaciones que es lo que caracteriza a un gemelo digital. El título de gemelo digital se apoya en un modelo probabilístico estático actualizado con datos administrativos.

**Síntesis propuesta.** La contribución sostenible es una estrategia de escalabilidad para modelos probabilísticos de infraestructura, basada en extraer del grafo el subconjunto relevante para cada decisión, con una demostración de reducción de memoria de dos órdenes de magnitud en un caso real. Para el corpus, es, en consecuencia, una pieza de arquitectura útil para gemelos de ciudad (como D034 y D048), porque sugiere cómo mantener el sistema completo en un grafo y calcular localmente la parte necesaria, pero no aporta evidencia de exactitud ni de efecto en decisiones, ni extiende el concepto a recuperación empresarial, de modo que su aporte debe leerse como habilitador computacional y no como evidencia de beneficio para la decisión.

**Áreas grises detectadas.**

1. Exactitud del sub-gemelo: el artículo informa reducción de memoria (de 73 362,9 MB a 625,3 MB) y de tamaño (1 % del KG), pero no presenta la diferencia entre el riesgo calculado con el sub-gemelo y con la red completa o con datos observados; la utilidad para la decisión se supone.
2. Supuestos de la ontología: el riesgo de falla de un puente se define como producto de probabilidad y consecuencia, la probabilidad se relaciona con calificaciones de condición y flujo de ríos y la consecuencia con el tránsito diario; las relaciones, la discretización en 4 estados y los umbrales de distancia (5 km, 10 estaciones) se fijan sin análisis de sensibilidad.
3. Dependencia de grafos de conocimiento: el marco supone que existe un KG de escala urbana o de condado, algo que los autores reconocen como poco común; la generación del grafo, su mantenimiento y su calidad quedan fuera del estudio.
4. Alcance como gemelo digital: el marco no incluye sensores en tiempo real, simulaciones ni control, de modo que se parece más a un sistema de apoyo a la decisión probabilístico que a un gemelo sincronizado con la realidad; la afirmación de gemelo requiere una definición explícita.

**Puntos oscuros aclarados.** Llama la atención que el artículo presente una reducción de memoria de dos órdenes de magnitud como logro central sin mostrar que el riesgo actualizado sea el mismo en el sub-gemelo y en el sistema completo. También es notable que el riesgo de puentes se limite a inundaciones y tráfico, sin amenaza sísmica, pero se proponga el marco para eventos y escenarios en general. Los autores admiten que no se incluyen sensores, simulaciones ni control, que son rasgos definitorios de un gemelo digital, y que los grafos de conocimiento a escala de ciudad son escasos. Además, los parámetros de la ontología y de las conexiones espaciales (5 km, 10 estaciones, 4 estados) se fijan sin sensibilidad. Por último, no hay evaluación con usuarios ni demostración de que las decisiones cambien con el sub-gemelo, y el algoritmo que decide qué datos son redundantes puede descartar fuentes que serían útiles si fallan las demás.

**Ideas propositivas novedosas.**

1. Sub-gemelo de recuperación para una zona industrial sísmica: adaptar la ontología a riesgo sísmico y continuidad, con nodos de edificios (estado de daño), vías (accesibilidad), servicios (energía y agua) y empresas (dependencias), y generar sub-gemelos por medida de desempeño como tiempo de reapertura de un sector. El resultado sería un gemelo de continuidad escalable que permita consultar el estado de una cadena local sin cargar el modelo completo de la ciudad, y se validaría con datos de reapertura de empresas tras un sismo, comparando el tiempo de consulta y la memoria del sub-gemelo con los de un modelo completo.
2. Validación de exactitud del sub-gemelo: comparar las probabilidades posteriores del sub-gemelo con las de la red completa en un conjunto de escenarios de evidencia y medir el error de aproximación frente a la reducción de memoria, además de comparar con métodos conocidos de reducción de redes bayesianas. El resultado cuantificaría el compromiso entre exactitud y costo computacional y determinaría para qué tamaños de sub-gemelo el error es aceptable en decisiones de inspección y de priorización de recursos, e incluiría una prueba de robustez cuando se eliminan fuentes de datos para simular fallas de sensores y se mediría el tiempo de inferencia.

**Relaciones poco exploradas.**

1. Gemelo de sistema de infraestructura (complementa) D034 y D048: D034 y D048 modelan ciudades con sismos y estiman daño por edificio, y D058 aporta una estrategia de escalabilidad probabilística; ninguno incorpora recuperación empresarial.
2. Gemelos de infraestructura con riesgo (se relaciona con) D014 y D035: D014 y D035 construyen gemelos de estructuras individuales con sensores y actualización de modelos, mientras D058 trabaja a escala de red con datos administrativos.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 2/10; calidad de la evidencia 3/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 4/10 — Ofrece una estrategia de escalabilidad para gemelos probabilísticos de infraestructura a escala de red, con una reducción de memoria de dos órdenes de magnitud en un caso real. Su valor para el corpus es periférico-adyacente por la arquitectura, y se reduce por la falta de validación de exactitud, por el riesgo modelado (inundación y tráfico, no sismo), por la ausencia de sensores y por no abordar la recuperación.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Conclusión no derivada de la evidencia (Se concluye que el marco apoya decisiones bajo cualquier escenario con evidencia de reducción de memoria solamente (Resumen, p. 2; Sec. 7, p. 19-20)); Apelación a la novedad (Se denomina gemelo digital a un sistema probabilístico sin sensores en vivo ni simulación (Sec. 6, p. 19)); Generalización apresurada (Se propone el marco para sistemas de infraestructura en general a partir de un grafo hipotético y una red de puentes con riesgo de inundación (Sec. 4-5, p. 9-17))
- **Bradford-Hill:** No aplica: es un desarrollo metodológico con ejemplos; no estima efectos causales sobre decisiones.
- **TRL asignado:** 3 — 'For proof-of-concept, a hypothetical graph is first presented as a numerical example' (p. 2)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (21 páginas). La reducción de unas 117 veces (73 362,9 / 625,3) es cálculo del analista; los 73 362,9 MB se refieren a la red completa reestructurada con 4 estados y los 625,3 MB al tronco personalizado según el texto, y no se aclara si ese tronco coincide con el SDT de 1 % del KG. Las páginas siguen los marcadores del PDF.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un gemelo digital de sistema basado en un grafo de conocimiento mutable que genera, bajo demanda, sub-gemelos de redes bayesianas personalizados por medida de desempeño y por fuentes de datos disponibles permite gestionar infraestructura compleja con una fracción del costo computacional: en la red de puentes de Miami-Dade, un sub-gemelo de 1 % del grafo original reduce de forma drástica la memoria (de decenas de miles de megabytes a cientos) y soporta la actualización del riesgo con datos de condición, ríos y tránsito.  | El artículo demuestra eficiencia de almacenamiento, no utilidad para la decisión. No hay validación de que el riesgo actualizado con el sub-gemelo coincida con el de la red completa ni con eventos observados, ni comparación con técnicas de reducción de redes bayesianas conocidas. El riesgo modelado es de inundación y tráfico, sin amenazas sísmicas, y se fija por una ontología de supuestos. El requisito de un KG a escala de condado, reconocido como escaso, condiciona toda la propuesta, y no se integran sensores ni simulaciones que es lo que caracteriza a un gemelo digital. El título de gemelo digital se apoya en un modelo probabilístico estático actualizado con datos administrativos.  | La contribución sostenible es una estrategia de escalabilidad para modelos probabilísticos de infraestructura, basada en extraer del grafo el subconjunto relevante para cada decisión, con una demostración de reducción de memoria de dos órdenes de magnitud en un caso real. Para el corpus, es, en consecuencia, una pieza de arquitectura útil para gemelos de ciudad (como D034 y D048), porque sugiere cómo mantener el sistema completo en un grafo y calcular localmente la parte necesaria, pero no aporta evidencia de exactitud ni de efecto en decisiones, ni extiende el concepto a recuperación empresarial, de modo que su aporte debe leerse como habilitador computacional y no como evidencia de beneficio para la decisión.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Sub-gemelo' es un modelo extraído de un grafo para una medida de desempeño; 'grafo de conocimiento' almacena conceptos y relaciones del sistema; 'riesgo' es probabilidad de falla multiplicada por su consecuencia.
- **P2 Supuestos:** Supone que existe un grafo de conocimiento del sistema, que la discretización y la ontología son adecuadas y que el sub-gemelo conserva la información relevante.
- **P3 Evidencia:** La evidencia es una reducción de memoria en un ejemplo hipotético y en la red de puentes de Miami-Dade, sin medidas de exactitud.
- **P4 Consecuencias:** Si es cierto, los gestores pueden consultar riesgos locales con bajo costo; si es falso, pueden decidir con aproximaciones sin error conocido.
- **P5 Contraejemplos:** No se examinan exactitud, sismos, sensores en vivo, uso por decisores ni comparación con otros métodos.
- **P6 Alternativas:** Alternativas: que una red bayesiana jerárquica clásica logre la reducción; que el error del sub-gemelo sea mayor en eventos extremos; que los datos administrativos limiten la actualización.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Tamaño relativo del SDT personalizado frente al KG original | 1 | % | Red de puentes de Miami-Dade | Resumen, p. 2 | Texto | Alta | Mejora de eficiencia computacional |
| Memoria de la red bayesiana completa | 73 362,9 | MB | Con 4 estados discretos por nodo | Sec. 5, p. 16 | Texto | Alta | Tablas de probabilidad condicional |
| Memoria de la red del tronco personalizado | 625,3 | MB | Sub-gemelo transformado | Sec. 5, p. 16 | Texto | Alta | Reducción de unas 117 veces (cálculo del analista) |
| Nodos del grafo hipotético | 36 | nodos | Ejemplo 1 con dos componentes | Sec. 4, p. 9 | Texto | Alta | Demostración |
| Distancia máxima de conexión río-puente | 5 | km | Regla de conectividad del KG | Sec. 5, p. 15 | Texto | Alta | Sin sensibilidad |
| Estaciones de tránsito conectadas por puente | 10 | estaciones | Las más cercanas por vía | Sec. 5, p. 15 | Texto | Alta | Para estimar consecuencia |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'For proof-of-concept, a hypothetical graph is first presented as a numerical example' (p. 2) | Prueba de concepto con ejemplos ilustrativos; sin validación con eventos ni uso por decisores. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'a custom SDT with the size of 1% of the original KG can be created' (p. 2) | Eficiencia computacional demostrada, sin análisis de costos, usuarios ni modelo de negocio. |
| IRL | 3 | Sí | 'without incorporating other modeling enabling technologies within the DT architecture such as sensors, simulations' (p. 19) | Integra datos de tres sistemas (puentes, ríos y tránsito) en un KG; no integra sensores en tiempo real ni simulaciones. |
| DRL | 3 | Sí | 'Management of infrastructure systems is critical for serving the welfare of society' (p. 2) | Necesidad argumentada con literatura; sin demanda de usuarios medida. |
| SRL | 1.0 | Sí | Componentes: Grafo de conocimiento y red bayesiana (TRL 3), Algoritmo de sub-gemelos (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 9.0; ÷9 → 1.00; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 3 con BRL 1 e IRL 3: prueba de concepto con ejemplos, sin validación de exactitud, sin sensores y sin uso por decisores. · Estrategia de salida: Validación de exactitud frente a la red completa y eventos observados, y evaluación con usuarios.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Conclusión no derivada de la evidencia | Se concluye que el marco apoya decisiones bajo cualquier escenario con evidencia de reducción de memoria solamente (Resumen, p. 2; Sec. 7, p. 19-20) | No se evalúa la calidad de la decisión |
| Apelación a la novedad | Se denomina gemelo digital a un sistema probabilístico sin sensores en vivo ni simulación (Sec. 6, p. 19) | El alcance reconocido es menor que el título |
| Generalización apresurada | Se propone el marco para sistemas de infraestructura en general a partir de un grafo hipotético y una red de puentes con riesgo de inundación (Sec. 4-5, p. 9-17) | Dos ejemplos |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Sub-gemelo personalizado → menor costo de cómputo con riesgo actualizado útil | Reducción de memoria demostrada; utilidad supuesta | Mecanismo directo (reducción de nodos) | Medición de exactitud | Estructura del grafo, discretización | 2 | Eficiencia demostrada, exactitud no evaluada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Error de aproximación del sub-gemelo y comparación con métodos de reducción de redes bayesianas | Crítico | Media | 8 |
| Tecnológico | Integración de sensores, simulaciones y control en el SDT | Significativo | Media | 7 |
| Conocimiento | Ontologías de riesgo sísmico y de continuidad para redes de infraestructura y empresas | Crítico | Media | 8 |
| Mercado | Generación y mantenimiento de grafos de conocimiento a escala de ciudad | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 5 | Grafo de conocimiento hipotético con dos componentes | Grafo | 36 nodos | 36 nodos | Media |
| Fig. 12 | Uso de datos de varios sistemas para el riesgo de puentes | Ontología | Conceptos de puentes, tráfico y ríos | 3 sistemas | Alta |
| Fig. 14 | Ubicación de puentes, estaciones de tránsito y estaciones de río en Miami-Dade | Mapa | Conexiones del KG | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Gemelos digitales con redes bayesianas dinámicas para estructuras individuales | No especificado en documento | Academia | Actualización probabilística de estado estructural | Madurez a nivel de componente | No escalan a nivel de red | Creciendo |

### B.9 Variables econométricas y vacíos

- **Y:** Tamaño y memoria de la red bayesiana; riesgo de falla de puentes (producto de probabilidad y consecuencia)
- **X:** Medida de desempeño seleccionada y fuentes de datos disponibles
- **Z (controles):** Número de estados discretos, reglas de conectividad del KG
- **Datos:** Grafo hipotético de 36 nodos y datos públicos de puentes, ríos y tránsito de Miami-Dade
- **Método:** Extracción de subgrafos y transformación a red bayesiana
- **Efecto reportado:** Reducción de memoria de 73 362,9 MB a 625,3 MB con un sub-gemelo de 1 % del KG
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin sensibilidad ni validación de exactitud

| Vacío | Tipo | Descripción |
|---|---|---|
| V-058-01 | TERR | Miami-Dade (Estados Unidos); sin América Latina |
| V-058-02 | POBL | Gestores de infraestructura; sin empresas |
| V-058-03 | TEMP | Sin dinámica temporal ni horizonte de recuperación |
| V-058-04 | MET | Sin validación de exactitud ni sensibilidad de supuestos |
| V-058-05 | VAR | Faltan amenaza sísmica, sensores, costos y recuperación |
| V-058-06 | TEOR | Redes bayesianas y grafos de conocimiento; sin teoría de resiliencia económica |
| V-058-07 | CAUS | Sin evidencia causal sobre decisiones |
