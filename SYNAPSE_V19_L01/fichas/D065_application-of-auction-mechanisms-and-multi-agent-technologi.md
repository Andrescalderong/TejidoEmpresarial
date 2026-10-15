# FB-L01-065 | D065 — Application of Auction Mechanisms and Multi-Agent Technologies for Resource and Task Allocation in Distributed Computing Systems

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/S1063779626701017.pdf` · 3 páginas · Relevancia para el eje del corpus: **Periférico** (Comunicación breve (3 páginas) sobre asignación descentralizada de recursos y tareas en sistemas de cómputo distribuido de IoT mediante subastas VCG y sistemas multiagente, con un escenario de optimización de tráfico urbano y pruebas de escalabilidad de 10 a 50 nodos de borde. Aporta un mecanismo de asignación de cómputo sin punto único de falla, pero no trata desastres, sismos ni empresas.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-065 / D065
- **Tipo de recurso:** Artículo breve de congreso o revista (Physics of Particles and Nuclei)
- **Referencia APA 7:** Tereschenko, D. V., & Korkhov, V. V. (2026). Application of Auction Mechanisms and Multi-Agent Technologies for Resource and Task Allocation in Distributed Computing Systems. *Physics of Particles and Nuclei*, *57*(4), 843-845. https://doi.org/10.1134/S1063779626701017
- **Autores:** Tereschenko, D.V. (59166206200); Korkhov, V.V. (57213605243)
- **Afiliaciones:** St. Petersburg State University, St. Petersburg, 199034, Russian Federation
- **Fecha de publicación:** 2026
- **Fuente/contenedor:** Physics of Particles and Nuclei · vol. 57(4)
- **Identificador persistente:** DOI 10.1134/S1063779626701017 · ISSN 10637796
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105044910644&doi=10.1134%2fS1063779626701017&partnerID=40&md5=577216ae46dc1b42828b8ef953124911
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 0

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Desarrollar un enfoque descentralizado de asignación de recursos y de tareas en sistemas de cómputo distribuido, en particular de IoT con cómputo en el borde, que combine sistemas multiagente con mecanismos de subasta para lograr asignación autoorganizada, justa y eficiente, mejorando la resiliencia y la eficiencia de las infraestructuras frente a los modelos centralizados, que crean cuellos de botella y puntos de falla. El texto lo plantea como un grafo de dispositivos IoT y nodos de borde con retardos de transferencia ponderados, y propone modelar la asignación como un mercado virtual con un agente subastador.

**Pregunta de investigación.** El texto no formula preguntas de investigación explícitas. La pregunta implícita es si un mercado virtual con agentes de dispositivos (compradores), agentes de nodos de borde (vendedores) y un agente subastador, con pagos VCG que inducen declaraciones veraces, escala con el número de nodos y mantiene eficiencia, equidad y tiempo de convergencia aceptables.

**Marco teórico.** El marco modela el sistema como un grafo de nodos de borde y dispositivos IoT con aristas ponderadas por retardos de transferencia. Cada tarea tiene requisitos de CPU, memoria, volumen de datos y plazo. La asignación se formula como un mercado virtual: los dispositivos ofertan según una utilidad que incluye el valor de la tarea, una penalización exponencial por retardo y el costo de energía, los nodos calculan el costo de ejecutar la tarea (cómputo, comunicación y carga) y el subastador elige al ganador. El mecanismo de Vickrey-Clarke-Groves (VCG) busca maximizar el bienestar social y es veraz, de modo que a los participantes les conviene declarar sus preferencias de manera honesta.

**Metodología.** La subasta opera en tres etapas: presentación de ofertas por los agentes de los dispositivos, evaluación de las ofertas por los nodos con una función de costo y determinación del ganador por el agente subastador. La función de utilidad usa el valor base de la tarea, un factor exponencial de penalización por retardo respecto del plazo y un costo de energía; el costo del nodo incluye cómputo, comunicación (con penalización por conexión indirecta) y un costo de carga que representa efectos laterales de la sobrecarga. Los pagos siguen VCG. Las pruebas se hicieron en bancos de pequeña (10 nodos y 20 dispositivos), mediana (25 nodos y 50 dispositivos) y gran escala (50 nodos y 100 dispositivos), con parámetros calibrados a características de equipos reales, y se midieron bienestar social, utilización de recursos, equidad con el índice de Jain y tiempo de convergencia. Se usó un escenario de optimización de tráfico urbano. El código se publica en un repositorio.

**Resultados principales.** Los resultados de la Tabla 1 muestran, para escalas pequeña, mediana y grande, un bienestar social de 89,2 %, 91,8 % y 90,3 %, una eficiencia (utilización) de 91,5 %, 88,7 % y 86,4 %, una equidad de Jain de 0,82, 0,84 y 0,81 y tiempos de convergencia de 45, 78 y 175 ms. Los autores concluyen que, al pasar de 10 a 50 nodos, la eficiencia se mantiene en el nivel de 85 a 90 % y el tiempo de convergencia crece de forma lineal, lo que confirma la aplicabilidad práctica. El escenario de tráfico urbano consiste en dispositivos que detectan eventos y nodos de borde que realizan preprocesamiento, reconocimiento de accidentes y predicción de congestión para el control automatizado de semáforos. No se informan comparaciones con otros métodos de asignación, repeticiones ni intervalos de confianza. El texto no entrega gráficos de convergencia ni desviaciones, de modo que las tendencias descritas se apoyan solo en tres filas de la tabla y en la declaración de los autores sobre la linealidad del tiempo. Los autores informan que el código de la simulación se encuentra en un repositorio público, lo que permitiría reproducir las corridas, aunque el texto no indica el número de semillas aleatorias ni la configuración de los nodos.

**Discusión y contribución.** Los autores sostienen que el enfoque combina optimalidad teórica con escalabilidad práctica, que ofrece una arquitectura sin punto único de falla, que considera la topología y la latencia de la red y que garantiza optimalidad y resiliencia al escalar. Señalan como direcciones prometedoras los esquemas de subasta híbridos y la transición a implementaciones industriales. La discusión es breve y no contrasta los hallazgos con trabajos previos de asignación en el borde ni con asignaciones centralizadas, por lo que las afirmaciones de optimalidad quedan sin comparador explícito en el texto. Tampoco se examinan costos de comunicación de las rondas de ofertas.

**Limitaciones declaradas.** Declaradas: ninguna sección de limitaciones; las líneas futuras apuntan a esquemas híbridos y a implementaciones industriales. No declaradas: sin comparación con algoritmos de asignación centralizados ni con otros mecanismos descentralizados; sin repeticiones ni intervalos de confianza; el tiempo de convergencia crece de 45 a 175 ms (casi cuatro veces) con cinco veces más nodos y no se prueba con cientos de nodos; la eficiencia baja de 91,5 % a 86,4 %, de modo que la descripción de estabilidad en 85 a 90 % ignora el valor inicial; no hay fallas de nodos ni tráfico adversarial; el escenario de tráfico se describe sin datos reales; texto de tres páginas con poca descripción experimental.

**Trabajo futuro.** Explícito: esquemas de subasta híbridos y transición a implementaciones industriales. Implícito: pruebas con mayor escala, fallas de nodos y comparación con métodos centralizados.

**Palabras clave.** Declaradas: No declaradas / no disponibles en el registro | Inferidas: subasta VCG, sistemas multiagente, cómputo en el borde, asignación de recursos, internet de las cosas, bienestar social, equidad de Jain, escalabilidad, descentralización

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un mercado virtual de subastas con pagos VCG entre agentes de dispositivos IoT, nodos de borde y un subastador asigna tareas de forma descentralizada, veraz y sin punto único de falla, con bienestar social cercano a 90 %, eficiencia de 86 % a 92 %, equidad de Jain entre 0,81 y 0,84 y tiempo de convergencia que crece de forma lineal entre 10 y 50 nodos, lo que respalda su aplicabilidad práctica en infraestructuras IoT resilientes.

**Antítesis identificada.** La evidencia es mínima: una tabla de tres escalas, sin repeticiones, sin comparación con alternativas y sin fallas simuladas. El texto afirma resiliencia y ausencia de punto único de falla por diseño, pero no prueba el comportamiento cuando un nodo o un enlace falla. El tiempo crece de 45 a 175 ms con cinco veces más nodos, y la eficiencia desciende de 91,5 % a 86,4 %, lo que cuestiona la afirmación de estabilidad. La veracidad de VCG depende de supuestos (agentes racionales, valores privados) no verificados con dispositivos reales, y la subasta introduce un subastador central cuya función no se discute como punto de falla.

**Síntesis propuesta.** La contribución sostenible es un diseño formal de asignación por subasta con propiedades teóricas conocidas (veracidad de VCG) y una demostración de escalabilidad moderada hasta 50 nodos en simulación. Para el corpus, importa como idea de asignación descentralizada de cómputo en el borde que podría repartir tareas de gemelos entre nodos sin servidor central, pero su evidencia es insuficiente para respaldar resiliencia ante fallas y no tiene vínculo con desastres ni empresas. En consecuencia, el documento solo puede usarse como hipótesis de diseño para repartir cómputo entre nodos de borde y no como evidencia sobre recuperación productiva. Su aporte futuro dependería de pruebas con fallas inyectadas.

**Áreas grises detectadas.**

1. Ausencia de comparación: la Tabla 1 muestra desempeño en tres escalas, pero el artículo no compara con un asignador centralizado ni con otros mecanismos descentralizados, de modo que no se puede estimar el costo de la descentralización en eficiencia ni en tiempo.
2. Tendencias de la tabla: la eficiencia baja de 91,5 % a 86,4 % y el tiempo sube de 45 a 175 ms al pasar de 10 a 50 nodos; el texto resume ambos como estabilidad y crecimiento lineal, aunque el aumento de tiempo (3,9 veces) y la caída de eficiencia podrían volverse limitantes con cientos de nodos.
3. Resiliencia no probada: se afirma una arquitectura sin punto único de falla, pero el subastador coordina todo el proceso y no se simulan fallas de nodos, del subastador ni de enlaces.
4. Supuestos del mecanismo: la veracidad de VCG requiere agentes racionales con valores privados y costos de cómputo de VCG poco triviales; no se discute su validez con dispositivos IoT limitados ni la sobrecarga de cálculo.

**Puntos oscuros aclarados.** Llama la atención que un texto de tres páginas afirme optimalidad teórica y escalabilidad práctica con una tabla de tres filas, sin repeticiones ni comparación. También es notable que la conclusión presente una arquitectura sin punto único de falla cuando el esquema usa un agente subastador que coordina todas las asignaciones. Los valores de la Tabla 1 muestran descenso de eficiencia y aumento de tiempo que el texto interpreta como estabilidad. El escenario de tráfico urbano se enuncia sin datos ni resultados específicos de accidentes o de congestión. Además, el cálculo de pagos VCG exige resolver la asignación óptima varias veces, lo cual aumenta el costo de cómputo en nodos limitados, aspecto que no se discute. Por último, el código se publica en un repositorio, lo que favorece la replicación, pero el texto no describe los parámetros calibrados. Tampoco se especifica cómo se comporta el esquema cuando falla el propio agente subastador.

**Ideas propositivas novedosas.**

1. Asignación de cómputo para un gemelo ligero de planta con fallas simuladas: aplicar el mecanismo de subasta a la distribución de tareas de un gemelo de continuidad entre nodos de borde de bajo costo en una pyme, y simular la pérdida de uno o más nodos durante la ejecución para medir tiempo de reasignación, tareas perdidas y retardo adicional. El resultado indicaría si la propiedad de ausencia de punto único de falla se cumple en la práctica y cuántos nodos de respaldo son necesarios para sostener las tareas críticas tras una interrupción de energía o comunicación. Se documentaría además el consumo energético de cada nodo para valorar la viabilidad en plantas con suministro limitado.
2. Comparación con asignación centralizada y con otros mecanismos: reproducir el banco de pruebas con una asignación centralizada óptima y con una subasta de primer precio, reportando bienestar, eficiencia, equidad, tiempo y consumo de energía con intervalos de confianza y diez repeticiones por escala, hasta 200 nodos. Con ello se podría medir el costo real de la descentralización y determinar a partir de qué tamaño de red la subasta VCG supera a las alternativas, información necesaria para decidir si conviene en gemelos de infraestructura. Los resultados alimentarían un criterio de decisión comparable con otros estudios de borde del corpus.

**Relaciones poco exploradas.**

1. Cómputo en el borde y comunicación (se relaciona con) D057 y D066: D057 optimiza el enrutamiento multisalto para gemelos y D066 propone una arquitectura de borde para decisiones en tiempo real; D065 aporta la asignación descentralizada de tareas entre nodos.
2. Agentes y gemelos (se relaciona con) D055: D055 propone gemelos basados en agentes con razonamiento; D065 usa agentes de mercado para asignar recursos de cómputo.

**Robustez argumentativa:** 1.4/10 (ponderación 30/30/25/15) — consistencia lógica 1/10; calidad de la evidencia 2/10; validez de inferencias causales 1/10; generalizabilidad 2/10.

**Valor estratégico:** 2/10 — Ofrece un diseño formal de asignación descentralizada por subasta y una demostración mínima de escalabilidad hasta 50 nodos. Su valor para el corpus es periférico y bajo: la evidencia es de una tabla sin repeticiones ni comparación, no trata resiliencia ante fallas pese a afirmarla y no se relaciona con sismos, desastres o empresas.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Conclusión más amplia que la evidencia (Se afirma optimalidad y resiliencia al escalar con una tabla de tres escalas sin fallas (Conclusiones, p. 3)); Interpretación favorable de la tendencia (La caída de eficiencia de 91,5 % a 86,4 % y el aumento de 45 a 175 ms se describen como estabilidad y crecimiento lineal (Resultados, p. 3)); Afirmación de ausencia de punto único de falla (Se afirma la ausencia de punto único de falla en un esquema con un subastador coordinador (Conclusiones, p. 3))
- **Bradford-Hill:** No aplica: es una demostración técnica de pocos resultados; no estima efectos causales.
- **TRL asignado:** 3 — 'Experiments were conducted on small (10 nodes, 20 devices), medium (25 nodes, 50 devices), and large (50 nodes, 100 devices) scale testbeds with parameters calibrated to real equipment characteristics' (p. 3)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (3 páginas). Las cifras de la Tabla 1 se leyeron en columnas ordenadas por fila (pequeña, mediana, grande); el orden se infiere de la secuencia 45, 78 y 175 ms. La razón de 3,9 veces entre tiempos es cálculo del analista.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un mercado virtual de subastas con pagos VCG entre agentes de dispositivos IoT, nodos de borde y un subastador asigna tareas de forma descentralizada, veraz y sin punto único de falla, con bienestar social cercano a 90 %, eficiencia de 86 % a 92 %, equidad de Jain entre 0,81 y 0,84 y tiempo de convergencia que crece de forma lineal entre 10 y 50 nodos, lo que respalda su aplicabilidad práctica en infraestructuras IoT resilientes.  | La evidencia es mínima: una tabla de tres escalas, sin repeticiones, sin comparación con alternativas y sin fallas simuladas. El texto afirma resiliencia y ausencia de punto único de falla por diseño, pero no prueba el comportamiento cuando un nodo o un enlace falla. El tiempo crece de 45 a 175 ms con cinco veces más nodos, y la eficiencia desciende de 91,5 % a 86,4 %, lo que cuestiona la afirmación de estabilidad. La veracidad de VCG depende de supuestos (agentes racionales, valores privados) no verificados con dispositivos reales, y la subasta introduce un subastador central cuya función no se discute como punto de falla.  | La contribución sostenible es un diseño formal de asignación por subasta con propiedades teóricas conocidas (veracidad de VCG) y una demostración de escalabilidad moderada hasta 50 nodos en simulación. Para el corpus, importa como idea de asignación descentralizada de cómputo en el borde que podría repartir tareas de gemelos entre nodos sin servidor central, pero su evidencia es insuficiente para respaldar resiliencia ante fallas y no tiene vínculo con desastres ni empresas. En consecuencia, el documento solo puede usarse como hipótesis de diseño para repartir cómputo entre nodos de borde y no como evidencia sobre recuperación productiva. Su aporte futuro dependería de pruebas con fallas inyectadas. | 1.4/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'VCG' es un mecanismo de pagos que induce a declarar el valor verdadero; 'bienestar social' es la suma de utilidades de la asignación; 'equidad de Jain' es un índice de reparto entre 0 y 1.
- **P2 Supuestos:** Supone que los agentes son racionales y declaran valores privados, que los bancos de pruebas representan equipos reales y que el subastador no es un punto de falla.
- **P3 Evidencia:** La evidencia es una tabla de tres escalas con bienestar de 89 % a 92 %, eficiencia de 86 % a 92 %, equidad de 0,81 a 0,84 y tiempos de 45 a 175 ms.
- **P4 Consecuencias:** Si es cierto, los nodos de borde pueden repartirse tareas sin servidor central; si es falso, el sistema puede fallar al aumentar la escala o al caer el subastador.
- **P5 Contraejemplos:** No se examinan fallas de nodos, comparación con asignación centralizada, escala de cientos de nodos ni datos reales de tráfico.
- **P6 Alternativas:** Alternativas: que un asignador centralizado con respaldo sea más sencillo; que la sobrecarga de VCG anule la ventaja; que otros mecanismos sean más baratos.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Bienestar social en pequeña / mediana / gran escala | 89,2 / 91,8 / 90,3 | % | 10, 25 y 50 nodos de borde | Tabla 1, p. 3 | Tabla | Media | Sin intervalos de confianza |
| Eficiencia de utilización en pequeña / mediana / gran escala | 91,5 / 88,7 / 86,4 | % | Descenso con la escala | Tabla 1, p. 3 | Tabla | Media | El texto habla de 85 a 90 % |
| Equidad de Jain | 0,82 / 0,84 / 0,81 | índice | Entre 0 y 1 | Tabla 1, p. 3 | Tabla | Media | Reparto similar entre escalas |
| Tiempo de convergencia | 45 / 78 / 175 | ms | 10, 25 y 50 nodos | Tabla 1, p. 3 | Tabla | Media | Crece 3,9 veces con 5 veces más nodos |
| Nodos y dispositivos en la mayor escala | 50 / 100 | nodos / dispositivos | Banco de pruebas | Resultados, p. 3 | Texto | Alta | Parámetros calibrados a equipos reales |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'Experiments were conducted on small (10 nodes, 20 devices), medium (25 nodes, 50 devices), and large (50 nodes, 100 devices) scale testbeds with parameters calibrated to real equipment characteristics' (p. 3) | Prueba de concepto en simulación o banco con parámetros calibrados; sin despliegue. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'Promising directions include the development of hybrid auction schemes and the transition to industrial implementations' (p. 3) | Transición industrial planteada como futuro; sin costos ni modelo de negocio. |
| IRL | 2 | Sí | 'Centralized solutions create bottlenecks and points of failure' (p. 1) | Se propone una arquitectura descentralizada; sin pruebas de integración con equipos reales. |
| DRL | 2 | Sí | 'Existing approaches to resource management in IoT often suffer from limited scalability and an inability to adapt to changing conditions' (p. 1) | Necesidad argumentada de forma general; sin demanda medida. |
| SRL | 1.0 | Sí | Componentes: Agentes y mecanismo de subasta VCG (TRL 3), Nodos de borde y dispositivos IoT (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 6.0; ÷9 → 0.67; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 3 con BRL 1 e IRL 2: prueba de concepto con una tabla, sin comparación, fallas ni costos. · Estrategia de salida: Comparación con alternativas, pruebas de fallas y despliegue en equipos reales.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Conclusión más amplia que la evidencia | Se afirma optimalidad y resiliencia al escalar con una tabla de tres escalas sin fallas (Conclusiones, p. 3) | Evidencia mínima |
| Interpretación favorable de la tendencia | La caída de eficiencia de 91,5 % a 86,4 % y el aumento de 45 a 175 ms se describen como estabilidad y crecimiento lineal (Resultados, p. 3) | Lectura generosa de la tabla |
| Afirmación de ausencia de punto único de falla | Se afirma la ausencia de punto único de falla en un esquema con un subastador coordinador (Conclusiones, p. 3) | No se prueba ni se discute |

**Recomendación:** Rechazar como evidencia (usar solo como hipótesis)

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Pagos VCG → declaración veraz → asignación eficiente | Resultado teórico conocido del mecanismo | Teoría de mecanismos | Pruebas con dispositivos reales | Racionalidad de agentes, costos de cómputo | 3 | Propiedad teórica, no verificada en el sistema |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Comparación con asignación centralizada y repeticiones con intervalos de confianza | Crítico | Alta | 8 |
| Tecnológico | Pruebas con fallas de nodos y del subastador y escala de cientos de nodos | Crítico | Media | 8 |
| Conocimiento | Aplicación a gemelos digitales y a entornos de desastre | Moderado | Media | 6 |
| Mercado | Costos de implementación en equipos industriales | Moderado | Baja | 5 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Mercado virtual de asignación con agentes de dispositivos, nodos y subastador | Diagrama | Tres tipos de agente | No aplica | Media |
| Tabla 1 | Análisis de escalabilidad | Tabla | Bienestar, eficiencia, equidad y tiempo en tres escalas | Tres filas | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Revisión de subastas y diseño de mecanismos en cómputo en el borde (Qiu et al.) | No especificado en documento | Academia | Estado del arte de mecanismos de subasta en el borde | Cobertura amplia | Sin implementación propia | Creciendo |

### B.9 Variables econométricas y vacíos

- **Y:** Bienestar social, eficiencia de utilización, equidad de Jain y tiempo de convergencia
- **X:** Escala del sistema (número de nodos y dispositivos)
- **Z (controles):** Parámetros calibrados a equipos reales; escenario de tráfico urbano
- **Datos:** Tres bancos de pruebas de 10, 25 y 50 nodos de borde
- **Método:** Subasta VCG con agentes y simulación
- **Efecto reportado:** Eficiencia de 86 % a 92 % y convergencia de 45 a 175 ms
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Tres escalas; sin repeticiones ni fallas

| Vacío | Tipo | Descripción |
|---|---|---|
| V-065-01 | TERR | Sin territorio; autores de la Universidad Estatal de San Petersburgo |
| V-065-02 | POBL | Sin usuarios ni empresas |
| V-065-03 | TEMP | Tiempos de convergencia en milisegundos |
| V-065-04 | MET | Tabla única sin repeticiones ni comparación |
| V-065-05 | VAR | Faltan fallas, costos de cómputo de VCG y consumo de energía |
| V-065-06 | TEOR | Teoría de mecanismos; sin teoría de resiliencia |
| V-065-07 | CAUS | Sin efecto causal estimado |
