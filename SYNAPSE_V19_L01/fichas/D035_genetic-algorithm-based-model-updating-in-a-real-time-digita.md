# FB-L01-035 | D035 — Genetic Algorithm-Based Model Updating in a Real-Time Digital Twin for Steel Bridge Monitoring

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/applsci-15-04074.pdf` · 15 páginas · Relevancia para el eje del corpus: **Adyacente** (Calibra con un algoritmo genético el modelo de elementos finitos de un puente ferroviario de acero a partir de frecuencias y formas modales medidas con acelerómetros, como base de un gemelo digital de monitoreo estructural; aporta una técnica de actualización de modelo con datos reales, pero con tiempo de procesamiento no real, un solo puente y sin sismos ni recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-035 / D035
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Rahmat Rabi, R., & Monti, G. (2025). Genetic Algorithm-Based Model Updating in a Real-Time Digital Twin for Steel Bridge Monitoring. *Applied Sciences (Switzerland)*, *15*(8), Article 4074. https://doi.org/10.3390/app15084074
- **Autores:** Rahmat Rabi, Raihan (57300211800); Monti, Giorgio (7102316843)
- **Afiliaciones:** Department of Structural Engineering and Geotechnics, Sapienza University of Rome, Via A. Gramsci 53, Roma, 00197, Italy; Department of Civil Engineering, Xi’an Jiaotong Liverpool University, Suzhou, 215000, China
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Applied Sciences (Switzerland) · vol. 15(8)
- **Identificador persistente:** DOI 10.3390/app15084074 · ISSN 20763417
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105003735230&doi=10.3390%2fapp15084074&partnerID=40&md5=5a54cd75194cf303aea6f68233090091
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 26

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Desarrollar un gemelo digital en tiempo real de un puente ferroviario de acero de tres tramos, construido con un modelo de elementos finitos de alta fidelidad en OpenSeesPy e instrumentado con acelerómetros, y mejorar su fidelidad con una estrategia de actualización del modelo basada en algoritmos genéticos que optimiza el módulo de elasticidad del acero para minimizar las discrepancias entre frecuencias y formas modales medidas y simuladas. El propósito es ofrecer una metodología escalable de monitoreo estructural para mantenimiento predictivo, detección temprana de daño y gestión del ciclo de vida de puentes.

**Pregunta de investigación.** El artículo no formula preguntas de investigación. La pregunta implícita es si la identificación modal operacional por SSI combinada con un algoritmo genético que ajusta el módulo de elasticidad por grupos de elementos permite alinear un modelo de elementos finitos con las propiedades dinámicas medidas de un puente real y sostener un gemelo digital.

**Marco teórico.** El marco combina el gemelo digital como réplica virtual sincronizada con sensores, el análisis modal operacional (identificación de subespacio estocástico, SSI, de solo respuesta) para extraer frecuencias y formas modales de vibraciones ambientales y de tránsito, y la actualización de modelos mediante optimización. La calibración se plantea como la minimización de una función objetivo combinada del error de frecuencias y del criterio de aseguramiento modal (MAC) con pesos iguales (α igual a β igual a 0,5, según una prueba de sensibilidad de relaciones 1:1, 2:1 y 1:2), con el módulo de elasticidad como parámetro sintético que absorbe efectos de conexiones, corrosión y fatiga. El paradigma es de ingeniería estructural aplicada con enfoque de identificación de sistemas, sin una teoría de decisión de mantenimiento.

**Metodología.** El caso es un puente ferroviario de armaduras de acero de tres tramos simplemente apoyados (28,54 m los laterales y 34,72 m el central) sobre pilas de mampostería. El modelo de elementos finitos se construyó con OpenSeesPy 3.5 a partir de datos de diseño y un módulo de elasticidad de 200 GPa, con la interfaz STKO. Los datos provienen de acelerómetros triaxiales con muestreo de 1 kHz (el resumen menciona 18 acelerómetros y el texto de métodos, 12 sensores triaxiales). Se extrajeron frecuencias y formas modales con SSI y diagramas de estabilización a partir de respuestas de vibración libre. La calibración empleó PyGAD con 1000 generaciones máximas, población de 20, seis genes (módulos de elasticidad por grupos de elementos), selección por torneo, cruce de dos puntos, mutación aleatoria de probabilidad 0,1 y criterio de parada por saturación de 50 generaciones, con módulos limitados a más o menos 30 % del valor de diseño. No se describen duración de la campaña de medición, condiciones ambientales ni validación con datos no usados en la calibración.

**Resultados principales.** Antes de la calibración, el modelo mostró diferencias de frecuencia de hasta 20 % respecto de las medidas (por ejemplo, 10,86 Hz del modelo frente a 8,85 Hz medidos en el primer modo, con 18,51 % de error y MAC de 0,73; y 19,50 Hz frente a 16,03 Hz en otro modo, con 17,79 % de error y MAC de 0,88), y un MAC mínimo de 0,19 en el primer modo del segundo tramo. Con la calibración, los errores de frecuencia bajaron a menos de 5 % (por ejemplo, 0,00 % en el primer modo con MAC de 0,97, y 2,85 % en el modo de 16,03 Hz) y el MAC mínimo alcanzó 0,93, según el texto. Los módulos de elasticidad calibrados por grupo (arriostramientos, vías, cuerdas superior e inferior y montantes) quedaron entre unos 178 y 205 GPa, es decir, dentro de la banda de más o menos 30 % que se permitió. La prueba de sensibilidad de pesos indicó que la relación 1:1 minimizó los errores de frecuencia (RMSE menor que 0,5 Hz) y de MAC (mayor que 0,95). Los autores consideran que el gemelo refleja con precisión el comportamiento dinámico del puente, aunque no muestran validación con mediciones independientes.

**Discusión y contribución.** Los autores sostienen que la integración de SSI, el modelo de elementos finitos y el algoritmo genético produce un gemelo de alta fidelidad adecuado para monitoreo en tiempo real y aplicable a otros puentes e infraestructuras críticas, y que el modelo calibrado constituye una línea base confiable para detectar cambios estructurales en el tiempo y apoyar decisiones de mantenimiento. Reconocen como limitaciones la sensibilidad al ruido de los parámetros modales, los efectos ambientales (temperatura y humedad) sobre propiedades y condiciones de borde, y el uso de un único parámetro de calibración que sintetiza efectos locales sin identificar la naturaleza del daño. Proponen ampliar a más parámetros, a otros puentes y a técnicas de aprendizaje.

**Limitaciones declaradas.** Declaradas: sensibilidad al ruido de SSI, efectos ambientales no modelados y un solo parámetro de calibración que sintetiza efectos locales. No declaradas: ausencia de validación con datos independientes; duración de la medición y sensores no consistentes (18 frente a 12); calibración por lotes y no en tiempo real; sin pruebas de detección de daño; un único puente.

**Trabajo futuro.** Incorporar efectos ambientales, calibrar más parámetros (incluidas condiciones de borde), extender a otras tipologías de puentes, integrar aprendizaje automático y evaluar la detección de daño y el mantenimiento predictivo con datos de largo plazo.

**Palabras clave.** Declaradas: digital twin; genetic algorithms; model updating; real-time monitoring; sensor data integration; structural health monitoring (SHM) | Inferidas: gemelo digital, monitoreo de salud estructural, algoritmo genético, actualización de modelo, identificación de subespacio estocástico, puente ferroviario, acelerómetros, criterio de aseguramiento modal, OpenSeesPy, PyGAD

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un modelo de elementos finitos calibrado con un algoritmo genético a partir de frecuencias y formas modales identificadas por SSI reproduce el comportamiento dinámico de un puente ferroviario de acero con errores de frecuencia menores de 5 % y MAC mayor que 0,93, lo que proporciona una línea base fiable para un gemelo digital de monitoreo y mantenimiento predictivo.

**Antítesis identificada.** El ajuste es de interpolación: se optimizan seis parámetros de rigidez para reproducir un conjunto reducido de modos, con datos usados también para evaluar, sin validación con mediciones independientes ni con otra campaña o condición de carga, de modo que un error menor de 5 % mide la capacidad de ajuste y no la capacidad predictiva. El módulo de elasticidad actúa como parámetro comodín que absorbe errores de condiciones de borde, masa, conexiones y apoyos de mampostería, lo que limita la interpretación física de los valores calibrados y la utilidad para detectar daño localizado. Se afirma 'tiempo real' pese a que la calibración es un proceso de optimización por lotes con 1000 generaciones y población de 20, y no se informan tiempos de cómputo. Hay inconsistencias en el reporte (18 acelerómetros en el resumen y 12 en el texto; MAC mayor que 0,93 y mayor que 0,95) y no se muestra ninguna prueba con daño real o simulado.

**Síntesis propuesta.** La contribución sólida es una cadena reproducible y de código abierto (OpenSeesPy, PyGAD, SSI) para llevar un modelo de elementos finitos a coincidir con las frecuencias medidas de un puente real, con cifras de mejora y de rango de parámetros. Debe leerse como calibración de línea base de un gemelo y no como gemelo de tiempo real ni como sistema de detección de daño. Para el corpus, la síntesis consiste en tomar este procedimiento como etapa previa de cualquier gemelo estructural posterior a un sismo (calibrar con mediciones de vibración ambiental antes y después del evento) y en exigir validación fuera de muestra y pruebas de sensibilidad al daño, midiendo el cambio de frecuencias asociado a niveles de daño conocidos.

**Áreas grises detectadas.**

1. Validación fuera de muestra: la calibración y la evaluación usan las mismas frecuencias y formas modales identificadas, y el texto no presenta una campaña independiente, otra condición de carga ni modos no usados en la optimización para probar la capacidad predictiva del modelo calibrado.
2. Parámetro sintético y localización: el único parámetro calibrado es el módulo de elasticidad por grupos de elementos (seis genes), con una banda de más o menos 30 %, que absorbe efectos de conexiones y de apoyos; no se discuten identificabilidad, unicidad de la solución ni sensibilidad de la función objetivo a otros parámetros.
3. Consistencia del reporte: se mencionan 18 acelerómetros en el resumen y 12 sensores triaxiales en la descripción del sistema; el MAC mínimo post calibración se informa como mayor que 0,93 en el resumen y las conclusiones y mayor que 0,95 en la prueba de sensibilidad; no se indica la duración ni la fecha de la medición.
4. Alcance de 'tiempo real': el título y las conclusiones hablan de gemelo en tiempo real, pero el proceso descrito es de identificación y calibración por lotes con un algoritmo evolutivo, sin latencia de actualización, frecuencia de recalibración ni demostración de seguimiento de cambios en el tiempo.

**Puntos oscuros aclarados.** Llama la atención que la calibración reduzca a 0,00 % el error de frecuencia del primer modo con solo seis parámetros y que, a la vez, el artículo presente la mejora como evidencia de que el gemelo 'refleja la condición verdadera' del puente. Una explicación plausible es que con pocos modos y grados de libertad de calibración el algoritmo encuentra combinaciones de rigidez que ajustan los datos sin que representen propiedades reales, y que la restricción a un solo tipo de parámetro obliga a compensar errores de modelación (condiciones de borde de las pilas de mampostería, masa de la vía) con la rigidez del acero. Esto sugiere que los módulos calibrados (178 a 205 GPa) no deben interpretarse como degradación del material, y que su valor como línea base depende de que las condiciones ambientales y operativas sean comparables. Para un uso posterior a un sismo, la dificultad es mayor: el cambio de frecuencias causado por daño puede ser del mismo orden que el error residual del modelo o que la variación ambiental.

**Ideas propositivas novedosas.**

1. Prueba de sensibilidad al daño del gemelo calibrado: introducir en el modelo reducciones conocidas de rigidez localizadas (por ejemplo, 5 %, 10 % y 20 % en diferentes elementos) y estimar si el cambio de frecuencias y de MAC supera el error residual y la variación ambiental, y repetir con una campaña de medición con daño simulado en el puente (masas añadidas o cambios de apoyo). Fundamento: el artículo asegura que el modelo permite detección temprana de daño pero no prueba esa capacidad. Verificabilidad: simulación y ensayo controlado. Utilidad: define umbrales de detección que pueden usarse en un gemelo posterior a un sismo, y permite estimar la proporción de falsas alarmas y de daños no detectados que cada umbral produciría en operación.
2. Calibración con validación cruzada temporal y ambiental: calibrar con una ventana de datos y evaluar con ventanas posteriores y con diferentes temperaturas, reportando el error de predicción de los modos no usados y el rango de variación de los módulos calibrados. Fundamento: el artículo evalúa con los datos de ajuste y reconoce efectos ambientales no modelados. Verificabilidad: campañas de medición de al menos un ciclo anual. Utilidad: cuantifica la incertidumbre de la línea base y permite incluir intervalos de confianza en el gemelo para decisiones de intervención.

**Relaciones poco exploradas.**

1. Idealización de condiciones de borde y de masa del modelo (explica) la discrepancia inicial de hasta 20 % en frecuencias: la calibración del módulo de elasticidad compensa esas diferencias, con valores calibrados dentro de la banda de más o menos 30 %.
2. Variaciones ambientales (temperatura y humedad) (modifican) propiedades y condiciones de borde y por ello pueden confundirse con daño: los autores lo reconocen como limitación, sin cuantificarlo.

**Robustez argumentativa:** 3.3/10 (ponderación 30/30/25/15) — consistencia lógica 4/10; calidad de la evidencia 3/10; validez de inferencias causales 3/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Aporta un procedimiento claro, con software abierto y parámetros reportados, para calibrar un modelo de elementos finitos de un puente real con datos de acelerómetros, con mejoras cuantificadas de frecuencia y MAC. Su valor para el corpus es de método de calibración de un gemelo estructural; se reduce porque no hay validación independiente, el uso de tiempo real no se demuestra, existen inconsistencias de reporte y no se prueba la detección de daño ni su uso tras un sismo.

**Conexiones inter-documentales.**

- **CONFIRMA** D009 (Gemelos digitales y monitoreo de salud estructural (SHM)): relación inversa de D009 CONFIRMA D035: ambos reconstruyen el comportamiento dinámico de puentes con modelos actualizados por datos con errores de hasta 5 % (D009: 1 % a 5 %; D035: menos de  [juicio del analista]
- **COMPLEMENTA** D023 (Gemelo digital con SHM e IoT en puentes): relación inversa de D023 COMPLEMENTA D035: D023 mantiene medición continua con LoRaWAN y D035 actualiza el modelo por algoritmo genético en el puente de acero; ambos aportan a gemelos de puente [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 49 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Confusión entre ajuste y predicción (Se concluye que el modelo 'refleja la condición real' del puente porque reproduce los datos usados para calibrarlo (Resumen, p. 1; Sec. 5, p. 11-12)); Apelación a 'tiempo real' (Se califica de 'tiempo real' un proceso de calibración por lotes con optimización evolutiva (Título; Sec. 6, p. 12-13)); Generalización apresurada (Se afirma que la metodología es adaptable a otras infraestructuras críticas a partir de un puente (Sec. 6, p. 13))
- **Bradford-Hill:** No aplica: es un estudio de calibración sin diseño causal; la relación entre el módulo calibrado y la condición real del puente no se contrasta con datos independientes.
- **TRL asignado:** 5 — 'a real-time digital twin for a three-span steel railway bridge, utilizing a high-fidelity finite element (FE) model built using OpenSeesPy' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (15 páginas más referencias). Algunas partes del texto aparecen duplicadas por superposición de capas en la extracción; las tablas 4 y 5 se leyeron de forma parcial. Las ubicaciones del puente (Italia) se infieren de la afiliación de los autores y no del texto del caso.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un modelo de elementos finitos calibrado con un algoritmo genético a partir de frecuencias y formas modales identificadas por SSI reproduce el comportamiento dinámico de un puente ferroviario de acero con errores de frecuencia menores de 5 % y MAC mayor que 0,93, lo que proporciona una línea base fiable para un gemelo digital de monitoreo y mantenimiento predictivo.  | El ajuste es de interpolación: se optimizan seis parámetros de rigidez para reproducir un conjunto reducido de modos, con datos usados también para evaluar, sin validación con mediciones independientes ni con otra campaña o condición de carga, de modo que un error menor de 5 % mide la capacidad de ajuste y no la capacidad predictiva. El módulo de elasticidad actúa como parámetro comodín que absorbe errores de condiciones de borde, masa, conexiones y apoyos de mampostería, lo que limita la interpretación física de los valores calibrados y la utilidad para detectar daño localizado. Se afirma 'tiempo real' pese a que la calibración es un proceso de optimización por lotes con 1000 generaciones y población de 20, y no se informan tiempos de cómputo. Hay inconsistencias en el reporte (18 acelerómetros en el resumen y 12 en el texto; MAC mayor que 0,93 y mayor que 0,95) y no se muestra ninguna prueba con daño real o simulado.  | La contribución sólida es una cadena reproducible y de código abierto (OpenSeesPy, PyGAD, SSI) para llevar un modelo de elementos finitos a coincidir con las frecuencias medidas de un puente real, con cifras de mejora y de rango de parámetros. Debe leerse como calibración de línea base de un gemelo y no como gemelo de tiempo real ni como sistema de detección de daño. Para el corpus, la síntesis consiste en tomar este procedimiento como etapa previa de cualquier gemelo estructural posterior a un sismo (calibrar con mediciones de vibración ambiental antes y después del evento) y en exigir validación fuera de muestra y pruebas de sensibilidad al daño, midiendo el cambio de frecuencias asociado a niveles de daño conocidos.  | 3.3/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Gemelo digital en tiempo real' es aquí un modelo de elementos finitos calibrado con frecuencias y formas modales medidas; 'actualización del modelo' es la optimización de parámetros para igualar el modelo a las mediciones.
- **P2 Supuestos:** Supone que el módulo de elasticidad por grupos de elementos basta para representar la discrepancia, que las frecuencias identificadas son confiables y que el modelo calibrado representa la condición del puente.
- **P3 Evidencia:** La evidencia son frecuencias y MAC antes y después de la calibración, con errores menores de 5 % en los datos usados para ajustar.
- **P4 Consecuencias:** Si es cierto, el modelo calibrado puede ser una línea base para detectar cambios; si es falso, los cambios de frecuencia por clima o por daño podrían confundirse con el error residual.
- **P5 Contraejemplos:** No se examinan casos de daño, ni la capacidad predictiva con datos independientes, ni modelos con otros parámetros calibrados.
- **P6 Alternativas:** Alternativas: que condiciones de borde expliquen la discrepancia; que otro parámetro (masa o rigidez de apoyos) explique mejor los datos; que un modelo más simple ajuste igual.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Luces de los tramos | 28,54 / 34,72 | m | Laterales de 28,54 m y central de 34,72 m | Sec. 2, p. 3 | Texto | Alta | Tres tramos simplemente apoyados |
| Módulo de elasticidad inicial del acero | 200 | GPa | Valor de diseño según certificados | Sec. 4, p. 6 | Texto | Alta | Rango de variación de ±30 % |
| Frecuencia de muestreo | 1 | kHz | Acelerómetros triaxiales | Sec. 4, p. 7 | Texto | Alta | 12 sensores según el texto; 18 según el resumen |
| Error de frecuencia inicial máximo | 20 | % | Modelo sin calibrar frente a mediciones | Sec. 4, p. 7 | Texto | Alta | Primer modo: 18,51 % |
| Error de frecuencia tras la calibración | menos de 5 | % | Máximo reportado 2,85 % en el ejemplo | Tabla 5, p. 12 | Tabla | Alta | Sin validación independiente |
| MAC mínimo posterior a la calibración | 0,93 | adimensional | Mínimo inicial de 0,19 | Sec. 5, p. 11-12 | Texto | Alta | También se reporta mayor que 0,95 |
| Generaciones y población del algoritmo genético | 1000 / 20 | generaciones / individuos | Seis genes; parada por saturación de 50 | Tabla 3, p. 10 | Tabla | Alta | Tiempo de cómputo no informado |
| Módulos calibrados | 178 a 205 | GPa | Por grupo de elementos (arriostramientos, vías, cuerdas y montantes) | Tabla 4, p. 11 | Tabla | Media | Valores de la tabla de lectura parcial |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 5 | Sí | 'a real-time digital twin for a three-span steel railway bridge, utilizing a high-fidelity finite element (FE) model built using OpenSeesPy' (p. 1) | Prototipo con datos de un puente real; calibración por lotes sin validación independiente ni operación continua. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'offering a scalable framework for real-time SHM in complex structural systems' (p. 1) | Sin evidencia de mercado, costos ni modelo de negocio. |
| IRL | 4 | Sí | 'The integration of OpenSeesPy for FE modeling and PyGAD for optimization proves to be an efficient approach' (p. 13) | Integración de herramientas de modelado, identificación y optimización en un flujo reproducible; sin sincronización continua ni pruebas de operación. |
| DRL | 2 | Sí | 'Aging global infrastructure, particularly with regard to bridges, demands innovative approaches' (p. 1) | Necesidad argumentada con literatura; sin demanda de usuarios medida. |
| SRL | 2.22 | Sí | Componentes: Modelo de elementos finitos calibrado (TRL 5), Sistema de acelerómetros e identificación modal (TRL 5) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 20.0; ÷9 → 2.22; nivel acotado a [1,9] = 2.22 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 4 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 4 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V2 Prototipo sin escalamiento · Severidad: Media · TRL 5 con BRL 1 e IRL 4: prototipo calibrado con datos de un puente real, sin validación independiente ni modelo de negocio. · Estrategia de salida: Validación fuera de muestra, pruebas de sensibilidad al daño y operación continua durante un ciclo anual.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Confusión entre ajuste y predicción | Se concluye que el modelo 'refleja la condición real' del puente porque reproduce los datos usados para calibrarlo (Resumen, p. 1; Sec. 5, p. 11-12) | Sobreajuste no descartado |
| Apelación a 'tiempo real' | Se califica de 'tiempo real' un proceso de calibración por lotes con optimización evolutiva (Título; Sec. 6, p. 12-13) | El término no corresponde a lo demostrado |
| Generalización apresurada | Se afirma que la metodología es adaptable a otras infraestructuras críticas a partir de un puente (Sec. 6, p. 13) | Sin evidencia de transferibilidad |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Calibración por algoritmo genético → modelo representa la condición real del puente | Reducción de errores de frecuencia y aumento de MAC en datos de ajuste | Coherencia con prácticas de actualización de modelos | Validación independiente, unicidad de la solución, control ambiental | Condiciones de borde, masa, temperatura | 3 | Correlacional |
| Cambio de frecuencias → detección temprana de daño | Afirmación general; sin ensayos de daño | Plausibilidad | Evidencia de sensibilidad y especificidad | Variación ambiental, ruido de identificación | 1 | Hipótesis no probada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Validación independiente del modelo calibrado y pruebas de sensibilidad al daño con ruido y variación ambiental | Crítico | Media | 9 |
| Tecnológico | Actualización continua con latencia medida y operación prolongada del gemelo | Crítico | Media | 8 |
| Conocimiento | Identificabilidad de parámetros y calibración de condiciones de borde junto con rigidez | Significativo | Media | 7 |
| Mercado | Costo de instrumentación y calibración frente al valor del mantenimiento predictivo | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Puente ferroviario de armaduras de acero de tres tramos | Fotografía | Geometría y pilas de mampostería | 28,54 m; 34,72 m | Baja |
| Fig. 6 | Modelo de elementos finitos en STKO para OpenSees | Imagen | Vista 3D y esquema del modelo | 200 GPa | Media |
| Tabla 3 | Hiperparámetros del algoritmo genético en PyGAD | Tabla | Generaciones, población, genes, selección y mutación | 1000; 20; 6 | Alta |
| Tabla 4 | Módulos de elasticidad inicial y calibrado por grupo de elementos | Tabla | Arriostramientos, vías, cuerdas y montantes | 178-205 GPa | Media |
| Tabla 5 | Comparación de datos modales: puente real, modelo inicial y modelo actualizado | Tabla | Frecuencias, errores y MAC por modo | 18,51 %; 17,79 %; 2,85 % | Alta |
| Fig. 9 | Comparación del MAC del modelo inicial y del calibrado | Gráfico | Mejora de correlación modal | 0,19 a 0,93 | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Calibración bayesiana de modelos en gemelos de puentes (citada) | No especificado en documento | Academia | Actualización con inferencia bayesiana y cuantificación de incertidumbre | Incertidumbre explícita | Mayor costo de cómputo | Creciendo |
| Gemelos de SHM de puentes con medición permanente (citados, por ejemplo, Marai et al., Kaewunruen et al.) | No especificado en documento | Academia | Marcos y demostraciones con datos de campo | Datos reales | Sin calibración de parámetros por grupo | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Error de frecuencia y MAC entre modelo y mediciones
- **X:** Módulo de elasticidad por grupo de elementos (seis genes) y pesos de la función objetivo
- **Z (controles):** Número de modos usados y condiciones operativas de medición
- **Datos:** Mediciones de acelerómetros de un puente ferroviario; duración y fecha no especificadas
- **Método:** SSI y algoritmo genético con función objetivo combinada de frecuencia y MAC
- **Efecto reportado:** Reducción de errores de frecuencia de hasta 20 % a menos de 5 %; MAC de 0,19 a 0,93 como mínimo
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sensibilidad a pesos de la función objetivo; sin validación independiente

| Vacío | Tipo | Descripción |
|---|---|---|
| V-035-01 | TERR | País del puente no declarado en el texto del caso (autores de Italia); sin zonas de alta sismicidad documentada ni América Latina |
| V-035-02 | POBL | Sin usuarios, operadores ferroviarios ni impactos económicos |
| V-035-03 | TEMP | Duración de la campaña no informada; sin ciclo anual ni seguimiento de largo plazo |
| V-035-04 | MET | Calibración y evaluación con los mismos datos; parámetro único |
| V-035-05 | VAR | Faltan variables ambientales, de daño y de costo |
| V-035-06 | TEOR | Sin teoría de decisión de mantenimiento ni de resiliencia |
| V-035-07 | CAUS | Sin evidencia causal de beneficio del gemelo en detección de daño |
