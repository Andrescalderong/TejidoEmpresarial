# FB-L01-062 | D062 — RescueNav: AI-Powered AAV Trajectory Planning With LoRa Connectivity for IoT-Based Disaster Communications

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/RescueNav_AI-Powered_AAV_Trajectory_Planning_With_LoRa_Connectivity_for_IoT-Based_Disaster_Communications.pdf` · 8 páginas · Relevancia para el eje del corpus: **Adyacente** (Propone RescueNav, un marco de planificación de trayectoria de vehículos aéreos autónomos (AAV) que actúan como estaciones base móviles de IoT con enlaces LoRa para restablecer comunicaciones tras desastres, con aprendizaje por refuerzo (Q-learning con repetición priorizada) y pruebas de campo con un dron. Aporta una solución de conectividad posdesastre para sensores y gemelos cuando falla la red terrestre, pero no trata empresas ni recuperación productiva.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-062 / D062
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, IEEE Internet of Things Journal)
- **Referencia APA 7:** Raja, G., Jambukeswaran Bhooma, M., Ragul Kumar, S., & Dev, K. (2026). RescueNav: AI-Powered AAV Trajectory Planning With LoRa Connectivity for IoT-Based Disaster Communications. *IEEE Internet of Things Journal*, *13*(9), 18239-18246. https://doi.org/10.1109/JIOT.2025.3644155
- **Autores:** Raja, Gunasekaran (24824293300); Jambukeswaran Bhooma, Mugundh (59364566900); Ragul Kumar, Selva (60651958400); Dev, Kapal (57190336390)
- **Afiliaciones:** Anna University, NGNLab, Department of Computer Technology, MIT Campus, Chennai, 600044, India; Munster Technological University, ADAPT Centre, Department of Computer Science, Cork, T12 P928, Ireland; University of Johannesburg, Institute of Intelligent Systems, Johannesburg, 2006, South Africa; Chitkara University Institute of Engineering and Technology, Chitkara University, Centre for Research Impact and Outcome, Punjab, Rajpura, 140401, India
- **Fecha de publicación:** 2026
- **Fuente/contenedor:** IEEE Internet of Things Journal · vol. 13(9)
- **Identificador persistente:** DOI 10.1109/JIOT.2025.3644155 · ISSN 23274662
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105025477258&doi=10.1109%2fJIOT.2025.3644155&partnerID=40&md5=753b8306a51b12651f3c30849d05fd51
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 1

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Introducir RescueNav, un marco de planificación de trayectoria de vehículos aéreos autónomos (AAV) basado en intención que integra restricciones específicas de la señal LoRa con la toma de decisiones por aprendizaje por refuerzo, para que el AAV actúe como estación base móvil de IoT y restablezca la conectividad en zonas afectadas por desastres donde la infraestructura convencional ha colapsado. El estudio busca mantener la conectividad con línea de vista, maximizar la cobertura y conservar la energía del AAV, formalizando la intención del operador dentro de la optimización de la trayectoria y no tratando la comunicación como un factor secundario.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si integrar las restricciones de propagación LoRa y del terreno en el aprendizaje de la trayectoria mejora la intensidad de señal, el caudal y la recompensa acumulada frente a Q-learning estándar, si el algoritmo es suficientemente ligero para el hardware a bordo y si funciona en pruebas de campo con una plataforma real.

**Marco teórico.** El marco combina las redes basadas en intención (intent-based networking), que traducen requisitos de misión de alto nivel como mantener la conectividad o minimizar el retardo en configuraciones operativas, la comunicación de baja potencia y largo alcance (LoRa), con variabilidad de señal por terreno, interferencia y energía limitada, y el aprendizaje por refuerzo con una tabla Q y repetición de experiencia priorizada (PER). El módulo de proveedor de espacio de acciones dinámico (DASP) ajusta las acciones disponibles según la densidad local de obstáculos y la variación de señal, y un módulo de línea de vista adaptativo (ALoS) incorpora la comunicación en la trayectoria. El contexto es la pérdida de infraestructura de comunicaciones tras terremotos, inundaciones, tsunamis, incendios y huracanes.

**Metodología.** El estado del AAV incluye posición (x, y, z), energía restante y intensidad de señal, con ocho acciones discretas (servir a usuarios, cuatro movimientos horizontales, ascender, descender y regresar a la base). El aprendizaje usa una tabla Q con política epsilon-greedy (epsilon inicial de 1,0, decaimiento de 0,99 y mínimo de 0,05), un búfer circular de repetición de 10 000 transiciones, lotes de 32, tasa de aprendizaje de 0,1 y factor de descuento de 0,95, con entrenamiento hasta 500 episodios o 95 % de celdas alcanzables exploradas. La recompensa es una función moldeada con términos de señal, cobertura (beta de 10) y penalización por colisión o inactividad (lambda de 5). Las simulaciones usaron una cuadrícula de 100 por 100 con 15 % de obstáculos y decaimiento de señal por distancia inversa. Las pruebas de campo usaron una plataforma Holybro S500 V2 con Pixhawk 6C, Raspberry Pi 4B, módulos LoRa y un sensor LiDAR para la profundidad. Se compara con Q-learning estándar.

**Resultados principales.** Los experimentos con la plataforma real muestran que RescueNav mejora la intensidad de señal mediana en un factor de 4, aumenta el caudal en 42 % y logra una recompensa acumulada 55 % mayor que el Q-learning estándar. El texto indica que el módulo DASP evalúa la densidad local de obstáculos con el LiDAR en un radio de 5 m para ajustar dirección y altitud, y que el algoritmo aprende políticas conscientes de energía y conectividad dentro de los límites de cómputo a bordo. Las celdas con señal inferior a 30 dBm se consideran propensas a interferencia. Se presentan simulaciones de cobertura en la cuadrícula y comparaciones de recompensa, intensidad y caudal. El artículo no informa el número de repeticiones de campo, la duración de los vuelos ni la distribución de los resultados, y los experimentos se realizan con un solo AAV. En el módulo de exploración, el AAV recorre una cuadrícula bidimensional con acciones de movimiento a celdas libres y recibe recompensa por cada celda nueva visitada (beta de 10) y penalización por colisión o inactividad (lambda de 5), con mapas de profundidad y de intensidad de señal que guían el movimiento. Los autores reportan que la política converge cuando la tabla Q se estabiliza, sin aproximación de funciones.

**Discusión y contribución.** Los autores sostienen que RescueNav avanza más allá de los estudios previos de AAV con LoRa porque unifica confiabilidad de comunicación, conciencia de energía y optimización basada en intención en un solo marco de aprendizaje por refuerzo, validado en campo. Reconocen como trabajo futuro el aprendizaje cooperativo de varios AAV con modelos federados, la seguridad de la comunicación con cadena de bloques ligera, la asignación adaptativa de recursos en el borde con latencias de 10 ms o menos, evaluaciones con 10 000 y 100 000 nodos y comparaciones con NB-IoT y LTE-M. Subrayan que los resultados destacan el potencial del aprendizaje por refuerzo basado en intención para la comunicación resiliente en escenarios posdesastre.

**Limitaciones declaradas.** Declaradas: la evaluación se limita a un AAV y se plantea como trabajo futuro la cooperación entre varios, la seguridad, el cómputo en el borde con baja latencia, las densidades de 10 000 y 100 000 nodos y la comparación con otras tecnologías. No declaradas: la línea base es Q-learning estándar, sin comparación con trayectorias planificadas clásicas o con relevos fijos; las pruebas de campo son de un solo dron y sin repeticiones descritas; el entorno de simulación es una cuadrícula de 100 por 100 con modelo simple de decaimiento de señal; sin pruebas en un terreno real de desastre ni con interferencias reales; el término 'mejora de 4 veces' de la señal mediana depende de la línea base y de la geometría; sin análisis de costo, de regulación del espectro ni del tiempo de despliegue.

**Trabajo futuro.** Explícito: aprendizaje cooperativo de varios AAV con modelos federados, seguridad ligera con cadena de bloques, asignación de recursos en el borde con latencia de 10 ms o menos, evaluaciones con 10 000 y 100 000 nodos y comparación con NB-IoT y LTE-M. Implícito: pruebas en terrenos reales de desastre y con regulación de espacio aéreo.

**Palabras clave.** Declaradas: Autonomous aerial vehicle (AAV); intent-based networking; long range (LoRa); post-disaster relief; reinforcement learning (RL); trajectory optimization | Inferidas: vehículo aéreo autónomo, LoRa, aprendizaje por refuerzo, comunicaciones posdesastre, redes basadas en intención, planificación de trayectoria, cobertura, energía, IoT, terremoto

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un marco de planificación de trayectoria de AAV que incorpora de forma directa las restricciones de propagación LoRa, el terreno y la energía en un aprendizaje por refuerzo ligero (Q-learning con repetición priorizada y espacio de acciones dinámico) restablece la conectividad IoT posdesastre con mejor desempeño que el Q-learning estándar (señal mediana cuatro veces mayor, 42 % más de caudal y 55 % más de recompensa acumulada), con validación de campo en una plataforma de bajo costo.

**Antítesis identificada.** La evidencia es limitada a un solo AAV, a una línea base débil (Q-learning estándar) y a una cuadrícula simulada con modelo simple de señal. Las pruebas de campo no informan repeticiones, duración ni variabilidad, y el factor de 4 en la señal mediana depende de la geometría y de la línea base. No se compara con trayectorias clásicas ni con relevos fijos o múltiples AAV, y los entornos de desastre reales (escombros, interferencia, vientos) no se reproducen. La afirmación de resiliencia para comunicaciones críticas se apoya en el desempeño en un escenario pequeño, y los costos, el tiempo de despliegue y las normas de espacio aéreo no se examinan.

**Síntesis propuesta.** La contribución sostenible es una prueba de concepto de que un aprendizaje por refuerzo tabular, con restricciones de señal en la recompensa y un espacio de acciones adaptado al entorno, es ejecutable en hardware ligero y mejora las métricas de conectividad frente a una versión estándar. Para el corpus, la contribución importa, en consecuencia, como pieza de conectividad: un gemelo o un sistema de alerta que depende de la red necesita una vía de respaldo cuando la infraestructura cae. La evidencia no demuestra desempeño operativo en un terremoto ni valor para empresas, y sus resultados deben leerse como indicio de factibilidad técnica con hardware de bajo costo.

**Áreas grises detectadas.**

1. Línea base y repeticiones: la mejora se mide frente a Q-learning estándar, sin comparar con trayectorias planificadas clásicas, relevos fijos o varios AAV; las pruebas de campo no informan número de vuelos, duración ni variabilidad, de modo que los factores de 4 en señal, 42 % en caudal y 55 % en recompensa no tienen intervalos de confianza.
2. Realismo del entorno: la simulación usa una cuadrícula de 100 por 100 con 15 % de obstáculos y decaimiento por distancia inversa, y las pruebas de campo usan un solo dron; no se evalúa el rendimiento con escombros, vegetación densa, vientos o interferencia real.
3. Escalabilidad: los autores plantean como trabajo futuro la evaluación con 10 000 y 100 000 nodos y con varios AAV; la afirmación de que la solución es escalable no se prueba con el único AAV de los experimentos.
4. Aplicabilidad operativa: no se informan costos, tiempo de despliegue ni requisitos regulatorios de vuelo; la utilidad para decisiones de continuidad de empresas o de servicios depende de estas condiciones.

**Puntos oscuros aclarados.** Llama la atención que el resumen destaque una mejora de cuatro veces en la señal mediana y un 55 % más de recompensa acumulada sin indicar la variabilidad ni el número de pruebas de campo. También es notable que la línea base sea el Q-learning estándar, un método simple, de modo que la mejora mide en parte el efecto de añadir información de señal a la recompensa. Los experimentos con un solo dron no permiten evaluar la coordinación entre AAV, que los autores consideran trabajo futuro. La cuadrícula de 100 por 100 con 15 % de obstáculos es un entorno muy simplificado respecto de un terreno de desastre. Además, la intención del operador se formaliza como un conjunto de objetivos en la recompensa, sin que se estudie cómo el operador cambia esa intención durante la misión. Por último, el artículo no discute el consumo de energía del propio cómputo de aprendizaje a bordo.

**Ideas propositivas novedosas.**

1. Respaldo de conectividad para gemelos de infraestructura: probar RescueNav como enlace de contingencia entre sensores de un edificio o puente instrumentado y un servidor de gemelo cuando la red terrestre se interrumpe tras un sismo simulado, midiendo la cantidad de datos recuperados, el retardo y el consumo de energía. El resultado indicaría cuántos minutos de datos de monitoreo se preservan con un AAV, con repeticiones y desviación, y qué tipo de sensores (vibración, inclinación) son compatibles con el ancho de banda de LoRa, información clave para dimensionar un gemelo de continuidad que no dependa de la red pública y para decidir cuántos AAV o relevos hacen falta por zona.
2. Comparación con relevos fijos y con trayectorias clásicas: repetir los experimentos con una línea base de relevos LoRa fijos instalados antes del evento y con una trayectoria planificada por rejilla, y reportar intensidad de señal, caudal, costo y tiempo hasta el restablecimiento. Con intervalos de confianza, al menos diez vuelos por condición y registro del consumo de batería, se podría determinar si el costo de un AAV con aprendizaje se justifica frente a relevos preinstalados para zonas industriales de una región sísmica, con una estimación de costo total por cobertura de hectárea.

**Relaciones poco exploradas.**

1. Comunicaciones posdesastre con UAV (se relaciona con) D022 y D042: D022 revisa la recuperación de comunicaciones con UAV mediante PRISMA y D042 integra sensado IoT y UAV; D062 aporta un algoritmo concreto de trayectoria con LoRa y pruebas de campo.
2. Conectividad del gemelo (complementa) D036 y D057: D036 revisa tecnologías de comunicación para gemelos digitales (UAV, RIS, mmWave) y D057 optimiza el enrutamiento multisalto; D062 aborda el restablecimiento cuando la infraestructura falla.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Ofrece un algoritmo ligero de trayectoria de AAV con restricciones LoRa y pruebas de campo con una plataforma de bajo costo, que mejora la señal y el caudal frente a Q-learning estándar. Su valor para el corpus es adyacente por la conectividad posdesastre de sensores y gemelos; se reduce por la línea base simple, las pruebas de un solo dron sin repeticiones descritas, el entorno simplificado y la ausencia de costos y de evaluación en terremotos.

**Conexiones inter-documentales.**

- **COMPLEMENTA** D022 (UAV y restauración de comunicaciones posdesastre): D062 planifica trayectorias de AAV con LoRa por aprendizaje por refuerzo y D022 revisa UAV como estaciones base aéreas para restablecer comunicaciones; D062 se valida con simulaciones y pruebas de campo con una plataforma dron-LoRa y D022 sintetiza estudios con evidencia empírica a nivel de sistema [juicio del analista]
- **COMPLEMENTA** D001 (IoT-UAV para respuesta a desastres): relación inversa de D001 COMPLEMENTA D062: D001 optimiza la ruta y la energía de un UAV para recolectar datos y D062 la trayectoria y la conectividad; ambos con simulación [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 61 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Línea base débil (La mejora se mide frente a Q-learning estándar, sin trayectorias clásicas ni relevos fijos (Resumen, p. 1; Sec. V, p. 6-7)); Generalización apresurada (Se concluye potencial para comunicación resiliente en escenarios posdesastre con un solo dron y una cuadrícula simulada (Sec. VI, p. 7)); Afirmación sin intervalos (Se reportan factores de 4, 42 % y 55 % sin variabilidad ni número de repeticiones (Resumen, p. 1))
- **Bradford-Hill:** No aplica: es un estudio de ingeniería; la relación entre la trayectoria aprendida y la mejora de señal es mecánica, pero no se estima efecto en operaciones de desastre.
- **TRL asignado:** 5 — 'Experiments with a Holybro S500 V2 platform equipped with a Pixhawk, Raspberry Pi, and LoRa modules demonstrate that RescueNav improves median signal strength by 4×' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (8 páginas). Algunas figuras de resultados no son legibles; las mejoras se tomaron del resumen. Las páginas siguen los marcadores del PDF. El texto menciona terremotos entre los desastres de contexto sin pruebas específicas.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un marco de planificación de trayectoria de AAV que incorpora de forma directa las restricciones de propagación LoRa, el terreno y la energía en un aprendizaje por refuerzo ligero (Q-learning con repetición priorizada y espacio de acciones dinámico) restablece la conectividad IoT posdesastre con mejor desempeño que el Q-learning estándar (señal mediana cuatro veces mayor, 42 % más de caudal y 55 % más de recompensa acumulada), con validación de campo en una plataforma de bajo costo.  | La evidencia es limitada a un solo AAV, a una línea base débil (Q-learning estándar) y a una cuadrícula simulada con modelo simple de señal. Las pruebas de campo no informan repeticiones, duración ni variabilidad, y el factor de 4 en la señal mediana depende de la geometría y de la línea base. No se compara con trayectorias clásicas ni con relevos fijos o múltiples AAV, y los entornos de desastre reales (escombros, interferencia, vientos) no se reproducen. La afirmación de resiliencia para comunicaciones críticas se apoya en el desempeño en un escenario pequeño, y los costos, el tiempo de despliegue y las normas de espacio aéreo no se examinan.  | La contribución sostenible es una prueba de concepto de que un aprendizaje por refuerzo tabular, con restricciones de señal en la recompensa y un espacio de acciones adaptado al entorno, es ejecutable en hardware ligero y mejora las métricas de conectividad frente a una versión estándar. Para el corpus, la contribución importa, en consecuencia, como pieza de conectividad: un gemelo o un sistema de alerta que depende de la red necesita una vía de respaldo cuando la infraestructura cae. La evidencia no demuestra desempeño operativo en un terremoto ni valor para empresas, y sus resultados deben leerse como indicio de factibilidad técnica con hardware de bajo costo.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Intención' es el objetivo de misión del operador (mantener conectividad, maximizar cobertura, conservar energía); 'DASP' ajusta las acciones según los obstáculos; 'recompensa moldeada' incluye la calidad de la señal.
- **P2 Supuestos:** Supone que un modelo de señal por distancia inversa y una cuadrícula representan el terreno, que el Q-learning estándar es una línea base adecuada y que un solo dron indica el comportamiento general.
- **P3 Evidencia:** La evidencia es una simulación en cuadrícula y pruebas de campo con una plataforma Holybro, con mejoras de 4 veces en señal, 42 % en caudal y 55 % en recompensa.
- **P4 Consecuencias:** Si es cierto, un AAV barato puede restablecer conectividad LoRa tras un desastre; si es falso, la mejora puede ser menor en terrenos reales o frente a alternativas simples.
- **P5 Contraejemplos:** No se examinan repeticiones, relevos fijos, varios AAV, terreno real de desastre, costos ni regulación.
- **P6 Alternativas:** Alternativas: que relevos preinstalados sean más baratos y fiables; que la mejora dependa de la línea base; que el cómputo a bordo limite la autonomía.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Mejora de la intensidad de señal mediana | 4 | veces | Frente a Q-learning estándar | Resumen, p. 1 | Texto | Media | Sin intervalos de confianza |
| Mejora del caudal | 42 | % | Pruebas con plataforma real | Resumen, p. 1 | Texto | Media | Número de repeticiones no informado |
| Mejora de la recompensa acumulada | 55 | % | Frente a Q-learning estándar | Resumen, p. 1 | Texto | Media | Métrica del algoritmo |
| Cuadrícula de simulación y obstáculos | 100 × 100 / 15 | celdas / % | Entorno simulado | Sec. IV, p. 5 | Texto | Alta | Decaimiento por distancia inversa |
| Tamaño del búfer de repetición / lote | 10 000 / 32 | transiciones / muestras | Parámetros de entrenamiento | Sec. IV, p. 5 | Texto | Alta | Epsilon mínimo de 0,05 |
| Episodios de entrenamiento máximos | 500 | episodios | O hasta explorar 95 % de celdas alcanzables | Sec. IV, p. 5 | Texto | Alta | Q-table |
| Radio de evaluación de obstáculos con LiDAR | 5 | m | Densidad local de obstáculos | Sec. IV, p. 6 | Texto | Alta | Para el módulo DASP |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 5 | Sí | 'Experiments with a Holybro S500 V2 platform equipped with a Pixhawk, Raspberry Pi, and LoRa modules demonstrate that RescueNav improves median signal strength by 4×' (p. 1) | Validación de componentes en entorno relevante con una plataforma real de bajo costo; sin operación en desastre. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'AAVs have emerged as an effective alternative due to their agility, rapid deployment, and low operational costs' (p. 1) | Se afirma bajo costo operativo, sin cifras ni modelo de negocio. |
| IRL | 4 | Sí | 'A dynamic action space provider (DASP) further adapts decision-making by adjusting available actions based on obstacle density and local signal variation' (p. 2) | Integración de plataforma de vuelo, cómputo a bordo, LiDAR y módulos LoRa probada en campo; sin integración con sistemas de usuarios finales. |
| DRL | 3 | Sí | 'Reliable communication plays a crucial role in effective disaster response, yet damaged infrastructure often leads to complete isolation of affected regions' (p. 1) | Necesidad argumentada con literatura; sin demanda de usuarios medida. |
| SRL | 2.22 | Sí | Componentes: Algoritmo de trayectoria con aprendizaje por refuerzo (TRL 5), Enlace LoRa y plataforma AAV (TRL 5) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 20.0; ÷9 → 2.22; nivel acotado a [1,9] = 2.22 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 5 con BRL 2: prototipo probado en campo con un dron, sin costos, sin repeticiones descritas y sin evaluación en terremotos. · Estrategia de salida: Pruebas con varios AAV y repeticiones, comparación con relevos fijos y evaluación en un ejercicio de simulacro.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Línea base débil | La mejora se mide frente a Q-learning estándar, sin trayectorias clásicas ni relevos fijos (Resumen, p. 1; Sec. V, p. 6-7) | Magnifica la ventaja del método |
| Generalización apresurada | Se concluye potencial para comunicación resiliente en escenarios posdesastre con un solo dron y una cuadrícula simulada (Sec. VI, p. 7) | Escenario pequeño |
| Afirmación sin intervalos | Se reportan factores de 4, 42 % y 55 % sin variabilidad ni número de repeticiones (Resumen, p. 1) | Precisión aparente |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Incorporar la señal en la recompensa → trayectorias con mejor conectividad | Comparación con Q-learning estándar | Mecanismo directo | Repeticiones, línea base clásica | Terreno, interferencia, viento | 3 | Efecto plausible, magnitud sin intervalos |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Repeticiones de campo, intervalos de confianza y línea base clásica | Crítico | Media | 8 |
| Tecnológico | Coordinación de varios AAV, seguridad y escala de miles de nodos | Significativo | Media | 7 |
| Conocimiento | Valor de la conectividad de respaldo para gemelos, sensores y empresas | Significativo | Media | 8 |
| Mercado | Costos, regulación del espacio aéreo y tiempo de despliegue | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. de arquitectura | Marco RescueNav con DASP, ALoS y planificador de trayectoria | Diagrama | Módulos del marco | No aplica | Media |
| Resultados de simulación | Cobertura, recompensa y señal en la cuadrícula | Gráficos | Comparación con Q-learning estándar | 55 % de recompensa | Media |
| Resultados de campo | Intensidad de señal y caudal con la plataforma real | Gráficos | Mejoras de señal y caudal | 4 veces; 42 % | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Trabajos previos de AAV con LoRa (meta aprendizaje por refuerzo y comportamiento de antenas) | No especificado en documento | Academia | Trayectoria y comunicación tratadas por separado | Cobertura de aspectos individuales | Comportamiento reactivo ante cambios del entorno | Creciendo |
| Algoritmos de ruta con conciencia de energía (Pan y colegas) y optimización de altitud con calidad de enlace (Zhang y colegas) | No especificado en documento | Academia | Trayectoria con restricciones energéticas y de enlace | Formulaciones de optimización | No usan aprendizaje en línea con LoRa | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Intensidad de señal mediana, caudal y recompensa acumulada
- **X:** Algoritmo (RescueNav o Q-learning estándar)
- **Z (controles):** Densidad de obstáculos, energía, tamaño de la cuadrícula
- **Datos:** Simulaciones en cuadrícula de 100 por 100 y pruebas de campo con una plataforma dron-LoRa
- **Método:** Q-learning tabular con repetición priorizada y espacio de acciones dinámico
- **Efecto reportado:** Señal mediana 4 veces mayor, caudal 42 % mayor y recompensa 55 % mayor frente a Q-learning estándar
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin repeticiones descritas ni intervalos de confianza

| Vacío | Tipo | Descripción |
|---|---|---|
| V-062-01 | TERR | Sin territorio de desastre específico; autores en India, Irlanda y Sudáfrica |
| V-062-02 | POBL | Usuarios IoT en zonas afectadas; sin empresas |
| V-062-03 | TEMP | Misiones de minutos; sin operación sostenida |
| V-062-04 | MET | Un dron, línea base simple, sin repeticiones descritas |
| V-062-05 | VAR | Faltan costos, tiempo de despliegue, regulación y desempeño con varios AAV |
| V-062-06 | TEOR | Redes basadas en intención y aprendizaje por refuerzo; sin teoría de continuidad |
| V-062-07 | CAUS | Sin efecto en operaciones reales |
