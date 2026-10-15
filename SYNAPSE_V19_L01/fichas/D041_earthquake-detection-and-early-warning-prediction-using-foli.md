# FB-L01-041 | D041 — Earthquake detection and early warning prediction using folium and Geopandas

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/Earthquake detection and early warning prediction using folium and Geopandas.pdf` · 10 páginas · Relevancia para el eje del corpus: **Periférico** (Compara seis modelos de aprendizaje automático para predecir la magnitud de sismos en California con cuatro variables (latitud, longitud, profundidad y número de estaciones) y presenta mapas interactivos con Folium y GeoPandas. Se vincula con alerta temprana y visualización geoespacial, pero su validez predictiva es muy limitada y no trata infraestructura, empresas ni recuperación.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-041 / D041
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Y, K. B., G, V. R., R, S., S, G., Y, P., Solovev, S., Vatin, N. I., & Dabral, U. (2024). Earthquake detection and early warning prediction using folium and Geopandas. *Cogent Engineering*, *11*(1), Article 2345301. https://doi.org/10.1080/23311916.2024.2345301
- **Autores:** Y, Krishna Bhargavi (57211330396); G, Varshitha Reddy (59013357200); R, Sneha (59014015100); S, Gayatri (59013357300); Y, Pranathi (59013885800); Solovev, Sergei (24476721700); Vatin, Nikolai Ivanovich (6508103761); Dabral, Upendra (58994191000)
- **Afiliaciones:** Department of Computer Science and Engineering, Gokaraju Rangaraju Institute of Engineering and Technology, Hyderabad, India; Department of CSE, GRIET, Hyderabad, India; Institute of Digital Technologies and Economics, Kazan State Power Engineering University, Kazan, Russian Federation; Peter the Great St. Petersburg Polytechnic University, Saint Petersburg, Russian Federation; Lovely Professional University, Phagwara, India; Uttaranchal University, Dehradun, India
- **Fecha de publicación:** 2024
- **Fuente/contenedor:** Cogent Engineering · vol. 11(1)
- **Identificador persistente:** DOI 10.1080/23311916.2024.2345301 · ISSN 23311916
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85192075777&doi=10.1080%2f23311916.2024.2345301&partnerID=40&md5=32d1af566bb6d8b96eec299ada463bd1
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 2

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Predecir la magnitud de los sismos y las áreas afectadas en California mediante modelos de aprendizaje automático entrenados con datos históricos, y representar el resultado en mapas dinámicos con las bibliotecas Folium y GeoPandas. El estudio busca mejorar la exactitud y la rapidez de la localización de eventos dentro de sistemas de alerta temprana sísmica, y ofrecer una interfaz donde el usuario introduzca parámetros del sismo y obtenga una predicción y un mapa de la zona de impacto. El objetivo declarado incluye también orientar la preparación de comunidades ante desastres.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. La pregunta implícita es cuál de seis algoritmos (regresión lineal, máquinas de vectores de soporte, bosque aleatorio, XGBoost, aumento de gradiente y red neuronal) predice mejor la magnitud con las variables disponibles, y si la integración con mapas interactivos aporta valor de interpretación y de uso a los resultados de la predicción para la alerta temprana.

**Marco teórico.** El marco es la tradición de alerta temprana sísmica con sensores y datos históricos, y de aprendizaje automático supervisado para regresión. La revisión de literatura enumera una veintena de trabajos sobre detección de ondas P, redes de sensores inalámbricos, dispositivos MEMS de bajo costo y modelos como MagNet, pero sin una síntesis crítica ni una teoría que explique por qué latitud, longitud, profundidad y número de estaciones podrían predecir la magnitud. El texto describe cada algoritmo con sus ecuaciones generales y asume una arquitectura de canalización tomada de un trabajo previo de la primera autora, sin justificar la elección de variables ni de modelos con criterios sismológicos.

**Metodología.** El estudio carga un archivo CSV de sismos de California, lo divide en conjuntos de entrenamiento y prueba y entrena seis modelos de regresión con cuatro variables de entrada: latitud, longitud, profundidad y número de estaciones. El bosque aleatorio usa 100 árboles y semilla 42, la red neuronal es un perceptrón multicapa de scikit-learn con variables estandarizadas, y la máquina de vectores usa núcleo gaussiano en subconjuntos de datos. Las métricas son el coeficiente de determinación (R2), el error absoluto medio (MAE) y el error cuadrático medio (MSE). La salida incluye el cálculo del área afectada a partir de la magnitud y la profundidad, y mapas con Folium y GeoPandas. El artículo no describe la fuente de los datos, el número de registros, el período, la proporción de partición, la validación cruzada ni los hiperparámetros de la red, de modo que un lector no puede reproducir el experimento con el texto publicado.

**Resultados principales.** La red neuronal obtuvo R2 de 0,1607, MSE de 0,1615 y MAE de 0,2951. Los demás modelos mostraron valores cercanos: aumento de gradiente con R2 aproximado de 0,140 y MAE de 0,297, XGBoost con 0,138 y 0,300, y bosque aleatorio con 0,136 y 0,298. La regresión lineal obtuvo R2 de 0,0235 y MAE de 0,3227, y la máquina de vectores de soporte R2 de -2,63, MAE de 0,571 y MSE de 0,698. Los autores concluyen que la red neuronal supera a los demás algoritmos y que el sistema ofrece una solución integral para la predicción de magnitud y el mapeo de áreas afectadas. Se muestran, además, gráficos de importancia de variables, de magnitud real frente a predicha y mapas de la zona de impacto de los eventos ingresados, sin cifras de precisión de la localización ni del área afectada y sin métricas de tiempo de alerta. Tampoco se reporta la dispersión de los resultados entre ejecuciones, de modo que las diferencias entre los cuatro mejores modelos (R2 entre 0,136 y 0,161) no pueden distinguirse de la variación aleatoria del entrenamiento. La figura de magnitud real frente a predicha no se acompaña de un análisis de residuos por rango de magnitud, que es donde se esperaría el mayor error en eventos grandes.

**Discusión y contribución.** Los autores afirman que las redes neuronales superan a XGBoost, regresión lineal, bosque aleatorio, aumento de gradiente y máquinas de vectores, y que la integración con Folium y GeoPandas mejora la exactitud y la interpretabilidad de las predicciones al ofrecer mapas dinámicos. Presentan la propuesta como una solución integral para la predicción de sismos y la representación geográfica, útil para comunidades. No discuten la magnitud del error en términos físicos, la comparación con métodos de alerta temprana operativos, la diferencia entre predecir y estimar la magnitud de un evento ya ocurrido, ni las limitaciones de los datos o del uso de cuatro variables.

**Limitaciones declaradas.** Declaradas: ninguna sección de limitaciones; solo se indica que los métodos existentes necesitan más exactitud y rapidez. No declaradas: R2 de 0,16 como mejor resultado (84 % de la varianza sin explicar); las variables de entrada no contienen información de la forma de onda; la magnitud no se predice antes del evento sino que se estima sobre eventos ya registrados; diferencias entre los modelos de conjunto y la red neuronal muy pequeñas y sin intervalos de confianza ni validación cruzada; datos y partición sin describir; sin comparación con sistemas operativos de alerta (ShakeAlert); sin evaluación del tiempo de alerta ni de la precisión del área afectada; la visualización no mejora la exactitud, a diferencia de lo que afirma el texto.

**Trabajo futuro.** El texto no formula una sección de trabajo futuro explícita; implícitamente, aplicar a otras regiones y mejorar la exactitud de la predicción.

**Palabras clave.** Declaradas: Artificial Intelligence; Computer Engineering; Earthquake detection; folium; Geopandas; machine learning; Machine Learning - Design; Neural Networks; Swadesh Kumar Singh, Gokaraju Rangaraju Institute of Engineering and Technology, India; Victoria University, Australia | Inferidas: predicción de magnitud sísmica, alerta temprana, redes neuronales, regresión, XGBoost, Folium, GeoPandas, California, visualización geoespacial, aprendizaje automático

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un modelo de red neuronal entrenado con datos históricos de sismos de California predice la magnitud con mayor exactitud que XGBoost, regresión lineal, bosque aleatorio, aumento de gradiente y máquinas de vectores, y su integración con Folium y GeoPandas permite una herramienta interactiva de predicción y de visualización del área afectada que apoya la alerta temprana y la preparación de comunidades.

**Antítesis identificada.** Los resultados no sustentan la tesis. Con R2 de 0,1607, el mejor modelo explica 16 % de la varianza de la magnitud, y la diferencia con bosque aleatorio, XGBoost y aumento de gradiente es de 0,02 a 0,025 en R2, sin validación cruzada ni intervalos de confianza. Las variables de entrada (posición, profundidad y número de estaciones) no contienen información de la señal sísmica, de modo que el problema planteado no equivale a la alerta temprana, que estima la magnitud a partir de las primeras ondas P. La magnitud se predice sobre eventos ya registrados, por lo que el modelo no entrega tiempo de alerta. La visualización con mapas no mejora la exactitud del modelo, y no hay datos del origen ni del tamaño del conjunto, ni comparación con métodos de referencia.

**Síntesis propuesta.** La contribución que el texto permite sostener es una demostración técnica de integración de una canalización de regresión con una interfaz cartográfica, y la constatación de que, con esas cuatro variables, ningún algoritmo supera un R2 de 0,16 en el conjunto probado. El valor para el corpus es, por tanto, instrumental: ilustra los límites de aplicar aprendizaje automático sin información de la señal y la utilidad de mapas interactivos como capa de comunicación de resultados hacia usuarios no especialistas. No aporta evidencia de alerta temprana, de efectos sobre infraestructura ni de recuperación, y su uso en el proyecto debe restringirse a ilustrar un límite metodológico.

**Áreas grises detectadas.**

1. Descripción de los datos: el artículo no indica la fuente del archivo CSV, el número de eventos, el período, el umbral de magnitud ni el modo de partición entre entrenamiento y prueba, de modo que los resultados no son reproducibles ni interpretables.
2. Planteamiento del problema: se anuncia predicción de ubicación y de magnitud para alerta temprana, pero las entradas incluyen latitud, longitud y profundidad del evento, que solo se conocen cuando el evento ya fue localizado; el modelo estima la magnitud a partir de esos datos y no ofrece tiempo de alerta.
3. Comparación de modelos: los R2 de red neuronal, bosque aleatorio, XGBoost y aumento de gradiente están entre 0,136 y 0,161, y los errores absolutos entre 0,295 y 0,300; sin repeticiones ni intervalos no se puede afirmar superioridad.
4. Área afectada: el cálculo de áreas a partir de magnitud y profundidad se describe, pero no se explica el modelo físico ni se valida con mapas de intensidad observados, y los mapas se presentan como evidencia de impacto.

**Puntos oscuros aclarados.** Llama la atención que un estudio cuyo título y resumen prometen detección y alerta temprana de sismos presente como mejor resultado un R2 de 0,1607, un valor que indica baja capacidad predictiva, y lo califique de superior. También es notable que el artículo afirme que la integración con Folium y GeoPandas mejora la exactitud de la predicción, cuando estas bibliotecas solo visualizan resultados ya calculados. La ausencia de una descripción de los datos, de validación cruzada y de comparación con métodos operativos impide evaluar el aporte, y la revisión de literatura enumera trabajos sin análisis crítico. Además, el número de estaciones como variable de entrada podría codificar información del propio proceso de registro y no de la física del sismo. Por último, el texto presenta una interfaz de ingreso de parámetros 'en tiempo real' sin medir latencia ni uso, y señala que la integración con mapas 'transforma el sistema en una herramienta interactiva' sin ninguna evaluación con usuarios o con operadores de emergencias.

**Ideas propositivas novedosas.**

1. Evaluación operativa de la visualización: replicar el pipeline con una evaluación mínima de alerta temprana, que mida el tiempo desde la primera onda P hasta el mapa de intensidad, y que compare la zona de impacto estimada con la intensidad instrumental observada en eventos históricos de California, para determinar si la capa cartográfica aporta valor práctico para la decisión de protección de instalaciones e interrupción de procesos. Esta evaluación incluiría un conjunto de eventos con registros instrumentales abiertos y un criterio de aceptación definido antes del análisis, por ejemplo error de intensidad menor que una unidad en 80 % de los sitios.
2. Mapas de intensidad para decisiones de continuidad de empresas: adaptar el componente cartográfico para que, en lugar de magnitud, entregue una lista de activos y empresas ubicados en zonas de intensidad esperada, con tiempos de llegada y acciones sugeridas (detener líneas, proteger inventario), y probar su utilidad en un ejercicio con pymes de una región sísmica, midiendo el tiempo de reacción y las pérdidas evitadas en simulacros. El resultado sería un indicador de valor de la alerta para una empresa pequeña, como horas de producción protegidas por cada minuto de aviso, que hoy no existe en el corpus. La comparación se haría con un grupo que reciba solo una alerta genérica de la red nacional.

**Relaciones poco exploradas.**

1. Predicción con aprendizaje automático (contrasta con) los sistemas de alerta con IoT del corpus (D031): D041 usa metadatos del evento y no señales, mientras el enfoque de IoT semántico trabaja con datos del sensor; las diferencias de insumos explican el bajo R2 reportado.
2. Visualización geoespacial (complementa) los gemelos urbanos del corpus (D034): ambos presentan mapas de impacto, pero D041 no cuantifica daño por edificio ni valida el área afectada.

**Robustez argumentativa:** 1.4/10 (ponderación 30/30/25/15) — consistencia lógica 2/10; calidad de la evidencia 1/10; validez de inferencias causales 1/10; generalizabilidad 2/10.

**Valor estratégico:** 2/10 — Aporta una demostración de una canalización de regresión y de mapas interactivos con bibliotecas de código abierto para sismos de California. Su valor para el corpus es periférico y bajo: el mejor R2 es 0,1607, los datos no se describen, las entradas no contienen señal sísmica y no hay evaluación de alerta, de infraestructura ni de recuperación. Sirve como ejemplo de las limitaciones de aplicar aprendizaje automático sin información de la forma de onda.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Afirmación opuesta a la evidencia presentada (Se declara superioridad de la red neuronal y una solución integral de predicción con R2 de 0,1607 (Resumen, p. 2; Sec. 5, p. 8)); Confusión de categorías (visualizar como mejorar la predicción) (Se afirma que Folium y GeoPandas mejoran la exactitud de la predicción, cuando solo representan resultados calculados (Sec. 1, p. 3)); Apelación a la novedad / a la tecnología (Se propone una solución integral para comunidades sin evaluar tiempo de alerta ni uso (Sec. 5, p. 8))
- **Bradford-Hill:** No aplica: es un ejercicio predictivo de regresión sin diseño causal; no se estima ningún efecto sobre decisiones, daños ni víctimas.
- **TRL asignado:** 3 — 'The user interface allows for interactive input, enabling users to input earthquake parameters for real-time predictions' (p. 8)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (10 páginas). La Tabla 1 se leyó con columnas desordenadas; la asignación de valores a modelos se dedujo por la coherencia R2 = 1 - MSE/Var (varianza de magnitud aproximada de 0,19) y por la coincidencia con los valores del resumen para la red neuronal (R2 0,1607; MSE 0,1615; MAE 0,2951). El orden de los modelos intermedios (bosque aleatorio, XGBoost, aumento de gradiente) es una reconstrucción del analista.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un modelo de red neuronal entrenado con datos históricos de sismos de California predice la magnitud con mayor exactitud que XGBoost, regresión lineal, bosque aleatorio, aumento de gradiente y máquinas de vectores, y su integración con Folium y GeoPandas permite una herramienta interactiva de predicción y de visualización del área afectada que apoya la alerta temprana y la preparación de comunidades.  | Los resultados no sustentan la tesis. Con R2 de 0,1607, el mejor modelo explica 16 % de la varianza de la magnitud, y la diferencia con bosque aleatorio, XGBoost y aumento de gradiente es de 0,02 a 0,025 en R2, sin validación cruzada ni intervalos de confianza. Las variables de entrada (posición, profundidad y número de estaciones) no contienen información de la señal sísmica, de modo que el problema planteado no equivale a la alerta temprana, que estima la magnitud a partir de las primeras ondas P. La magnitud se predice sobre eventos ya registrados, por lo que el modelo no entrega tiempo de alerta. La visualización con mapas no mejora la exactitud del modelo, y no hay datos del origen ni del tamaño del conjunto, ni comparación con métodos de referencia.  | La contribución que el texto permite sostener es una demostración técnica de integración de una canalización de regresión con una interfaz cartográfica, y la constatación de que, con esas cuatro variables, ningún algoritmo supera un R2 de 0,16 en el conjunto probado. El valor para el corpus es, por tanto, instrumental: ilustra los límites de aplicar aprendizaje automático sin información de la señal y la utilidad de mapas interactivos como capa de comunicación de resultados hacia usuarios no especialistas. No aporta evidencia de alerta temprana, de efectos sobre infraestructura ni de recuperación, y su uso en el proyecto debe restringirse a ilustrar un límite metodológico.  | 1.4/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Predicción de magnitud' es estimar la magnitud con cuatro variables del evento; 'área afectada' es una región calculada con magnitud y profundidad; 'alerta temprana' implica avisar antes de la llegada de las ondas dañinas.
- **P2 Supuestos:** Supone que latitud, longitud, profundidad y número de estaciones contienen información suficiente sobre la magnitud, que un R2 de 0,16 es útil y que la visualización mejora la predicción.
- **P3 Evidencia:** La evidencia es una tabla de seis modelos con R2 entre -2,63 y 0,16, sin validación cruzada ni descripción de datos.
- **P4 Consecuencias:** Si es cierto, los usuarios podrían obtener magnitudes y mapas rápidos; si es falso, pueden confiar en estimaciones que explican 16 % de la variación y que no son alerta temprana.
- **P5 Contraejemplos:** No se examinan datos de forma de onda, tiempos de alerta, comparación con ShakeAlert u otros sistemas operativos, ni la calidad de los mapas frente a intensidades observadas.
- **P6 Alternativas:** Alternativas: que la magnitud dependa de la forma de onda y no de la posición; que la diferencia entre modelos sea ruido; que el número de estaciones refleje el registro y no el sismo.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| R2 de la red neuronal | 0,1607 | R2 | Mejor modelo comparado | Resumen, p. 2; Tabla 1, p. 7 | Tabla | Alta | 84 % de varianza sin explicar |
| MSE de la red neuronal | 0,1615 | magnitud al cuadrado | Conjunto de prueba | Resumen, p. 2 | Texto | Alta | Unidad no especificada |
| MAE de la red neuronal | 0,2951 | unidades de magnitud | Conjunto de prueba | Resumen, p. 2 | Texto | Alta | Mejor entre los seis modelos por pequeño margen |
| R2 de la regresión lineal | 0,0235 | R2 | Línea base | Tabla 1, p. 7 | Tabla | Media | Reconstruido de la tabla; orden de columnas deducido por consistencia de MSE y R2 |
| R2 de la máquina de vectores de soporte | -2,63 | R2 | Peor modelo | Tabla 1, p. 7 | Tabla | Media | MAE 0,571; MSE 0,698 |
| R2 de bosque aleatorio, XGBoost y aumento de gradiente | 0,136 a 0,140 | R2 | Modelos de conjunto | Tabla 1, p. 7 | Tabla | Media | Diferencia con la red de 0,02 |
| Variables de entrada | 4 | variables | Latitud, longitud, profundidad y número de estaciones | Sec. 3.4, p. 5 | Texto | Alta | Sin forma de onda |
| Árboles del bosque aleatorio | 100 | árboles | Semilla 42 | Sec. 3.6.1, p. 6 | Texto | Alta | Hiperparámetro único declarado |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'The user interface allows for interactive input, enabling users to input earthquake parameters for real-time predictions' (p. 8) | Prueba de concepto de software con datos históricos; sin validación operativa. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'The goal is to empower communities with timely and accurate information' (p. 3) | Objetivo declarado sin análisis de mercado, costos ni modelo de negocio. |
| IRL | 2 | Sí | 'It seamlessly integrates geospatial visualization through Folium and GeoPandas' (p. 4) | Integración de bibliotecas de software en una canalización; sin integración con redes de sensores ni con sistemas de alerta. |
| DRL | 2 | Sí | 'there is a clear demand for enhanced accuracy and expediency in the process of resolving' (p. 2) | Necesidad afirmada, no medida con usuarios. |
| SRL | 1.0 | Sí | Componentes: Modelos de regresión para magnitud (TRL 3), Visualización con Folium y GeoPandas (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 6.0; ÷9 → 0.67; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 3 con BRL 1 e IRL 2: prueba de concepto con bajo poder predictivo, sin datos descritos ni integración con sensores, sin evaluación de alerta. · Estrategia de salida: Describir y publicar el conjunto de datos, incorporar la forma de onda, validar frente a sistemas operativos y medir el tiempo de alerta.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Afirmación opuesta a la evidencia presentada | Se declara superioridad de la red neuronal y una solución integral de predicción con R2 de 0,1607 (Resumen, p. 2; Sec. 5, p. 8) | Resultado de bajo poder explicativo presentado como éxito |
| Confusión de categorías (visualizar como mejorar la predicción) | Se afirma que Folium y GeoPandas mejoran la exactitud de la predicción, cuando solo representan resultados calculados (Sec. 1, p. 3) | La visualización no altera el modelo |
| Apelación a la novedad / a la tecnología | Se propone una solución integral para comunidades sin evaluar tiempo de alerta ni uso (Sec. 5, p. 8) | Beneficio asumido |

**Recomendación:** Rechazar como evidencia (usar solo como hipótesis)

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Variables del evento → magnitud | Regresión con cuatro variables, R2 de 0,16 | Asociación débil | Mecanismo físico, forma de onda | Región, catálogo, red de estaciones | 1 | Relación débil sin mecanismo causal en la dirección predictiva |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Descripción de datos, validación cruzada, intervalos y comparación con sistemas operativos | Crítico | Media | 9 |
| Tecnológico | Uso de forma de onda y evaluación de tiempos de alerta | Crítico | Media | 8 |
| Conocimiento | Vínculo entre mapas de impacto y decisiones de empresas e instalaciones | Significativo | Media | 7 |
| Mercado | Usuarios, costos y adopción de interfaces de alerta | Moderado | Baja | 5 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Canalización de aprendizaje automático para detección y predicción | Diagrama | Flujo de datos y modelos | No aplica | Media |
| Tabla 1 | Comparación de métricas entre modelos | Tabla | R2, MAE y MSE de seis modelos | R2 de -2,63 a 0,16 | Alta |
| Fig. 2-4 | Comparación de MAE, MSE y R2 entre modelos | Gráficos de barras | Métricas por modelo | No aplica | Media |
| Fig. 5 | Importancia de variables en la red neuronal | Gráfico | Peso relativo de variables | No aplica | Media |
| Fig. 6 | Magnitud real frente a predicha | Dispersión | Ajuste del modelo | No aplica | Media |
| Fig. 7-8 | Mapas con Folium y GeoPandas | Mapas | Zonas de impacto | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Mousavi y Beroza (MagNet) | No especificado en documento | Academia | Magnitud directamente de la forma de onda con red neuronal | Usa la señal sísmica | No integrado con mapas | Creciendo |
| Kwon et al., sistema con sensores MEMS de bajo costo en Corea del Sur | Corea del Sur | Academia | Detección con sensores de bajo costo | Sistema operativo | Sin predicción de magnitud con aprendizaje | Creciendo |

### B.9 Variables econométricas y vacíos

- **Y:** Magnitud del sismo (regresión)
- **X:** Latitud, longitud, profundidad y número de estaciones
- **Z (controles):** Tipo de modelo (seis algoritmos)
- **Datos:** Catálogo de sismos de California en archivo CSV; tamaño y período no especificados
- **Método:** Comparación de modelos de regresión por R2, MAE y MSE
- **Efecto reportado:** R2 de 0,1607 para el mejor modelo; MAE de 0,2951
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin validación cruzada, intervalos ni sensibilidad

| Vacío | Tipo | Descripción |
|---|---|---|
| V-041-01 | TERR | California (Estados Unidos); sin otras regiones |
| V-041-02 | POBL | Sin población ni empresas; unidad de análisis son eventos sísmicos |
| V-041-03 | TEMP | Sin período de datos especificado ni horizonte de alerta |
| V-041-04 | MET | Datos sin describir, partición sin detallar, sin validación cruzada, entrada sin forma de onda |
| V-041-05 | VAR | Faltan forma de onda, tiempo de llegada de ondas P, intensidad observada y tiempo de alerta |
| V-041-06 | TEOR | Sin base sismológica que justifique las variables de entrada |
| V-041-07 | CAUS | Sin evidencia causal ni de efecto sobre decisiones |
