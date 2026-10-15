# FB-L01-039 | D039 — Deep-Learning-Enabled Data Synchronization for Noninteger Time Lags in Wireless Structural Health Monitoring

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/Deep-Learning-Enabled_Data_Synchronization_for_Noninteger_Time_Lags_in_Wireless_Structural_Health_Monitoring.pdf` · 13 páginas · Relevancia para el eje del corpus: **Periférico** (Propone un método de aprendizaje profundo para estimar y corregir retardos temporales no enteros entre sensores inalámbricos de monitoreo de salud estructural (SHM) en internet de las cosas, validado con simulación y con datos del puente Jindo. Aporta calidad de datos para gemelos digitales de estructuras, pero no trata sismos, recuperación ni empresas.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-039 / D039
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, IEEE Internet of Things Journal)
- **Referencia APA 7:** Yu, X., Fu, Y., Yu, X., & Cui, S. (2026). Deep-Learning-Enabled Data Synchronization for Noninteger Time Lags in Wireless Structural Health Monitoring. *IEEE Internet of Things Journal*, *13*(10), 21328-21340. https://doi.org/10.1109/JIOT.2026.3664904
- **Autores:** Yu, Xiao (58817077400); Fu, Yuguang (57191156904); Yu, Xuewen (57212084032); Cui, Shuaiwen (57218711499)
- **Afiliaciones:** Nanyang Technological University, School of Civil and Environmental Engineering, Jurong West, 639798, Singapore
- **Fecha de publicación:** 2026
- **Fuente/contenedor:** IEEE Internet of Things Journal · vol. 13(10)
- **Identificador persistente:** DOI 10.1109/JIOT.2026.3664904 · ISSN 23274662
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105030477355&doi=10.1109%2fJIOT.2026.3664904&partnerID=40&md5=147b34716a8502745afb502f3c38bf5c
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 0

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Desarrollar un marco de sincronización de datos basado en aprendizaje que estime directamente, a partir de señales de vibración crudas, retardos temporales de valor continuo (no enteros) entre sensores inalámbricos de monitoreo estructural y que los corrija mediante remuestreo sin depender de marcas de tiempo. El estudio responde a la limitación de los protocolos de sincronización de reloj, que dejan desfases residuales de muestreo, y de los métodos en dominio de la frecuencia, que tratan los retardos como enteros y dependen de supuestos y de la experiencia del usuario. El resultado esperado es una sincronización de precisión submilisegundo, aplicable en nodos de borde con bajo costo de cómputo.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si una red neuronal convolucional con atención puede estimar retardos continuos con mayor precisión que los estimadores en el dominio de la frecuencia y que los regresores basados en características, si una estrategia de remuestreo optimizada bayesianamente corrige retardos menores que el intervalo de muestreo sin marcas de tiempo, y si el marco es suficientemente ligero para dispositivos de borde.

**Marco teórico.** El marco combina la formulación física de la respuesta de un sistema de múltiples grados de libertad, en la que un retardo temporal produce un error de fase proporcional a la frecuencia (1 ms equivale a 3,6 grados a 10 Hz y 36 grados a 100 Hz), con la distinción entre sincronización de reloj de red (protocolos TPSN, RBS y FTSP) y alineación posterior a nivel de señal. Los autores sostienen que la estimación del retardo corresponde a aprender un mapa complejo de fase y tiempo inducido por la superposición modal, por lo que el aprendizaje profundo actúa como estimador basado en datos y no sustituye el modelo vibratorio. Las contribuciones se enmarcan en la literatura de SHM inalámbrico y en métodos de dominio de la frecuencia basados en la pendiente de la fase de la densidad espectral cruzada.

**Metodología.** El marco tiene dos etapas. La primera es una red de retardo con convoluciones y atención (TLCA) que recibe pares de señales normalizadas y segmentadas, se entrena con pérdida de Huber y optimizador Adam (tasa de 1e-4, lote de 32, hasta 500 épocas con parada temprana) y estima el retardo continuo. La segunda es un remuestreo con sobremuestreo, filtro pasa-bajos y reducción, cuya frecuencia de sobremuestreo se selecciona por optimización bayesiana con una función objetivo que combina correlación de Pearson y correlación cruzada máxima. Se usaron dos conjuntos: respuestas simuladas de una estructura de cuatro grados de libertad (400 Hz, 100 s, excitación aleatoria de 20 a 150 Hz) y datos del puente Jindo (70 nodos Imote2, 1000 s a 25 Hz), a los que se inyectaron retardos conocidos mediante el Algoritmo 1 y submuestreo. La partición fue 7:1:2 y los resultados son promedios de tres ejecuciones. Los comparadores fueron un estimador de dominio de frecuencia y seis regresores (SVR, RF, GBR, XGBoost, KNN y MLP) con características construidas y búsqueda en malla con validación cruzada de cinco pliegues.

**Resultados principales.** El modelo tiene 108 mil parámetros, ocupa 0,41 MB y tarda 0,04 ms en GPU y 0,14 ms en CPU por inferencia, con 3,87 millones de operaciones de coma flotante para un par de segmentos de 2000 puntos. En el conjunto simulado, con retardos hasta 500 ms, el texto reporta un error absoluto medio de 2 ms y un error cuadrático medio de 1,4 ms, mientras los regresores de conjunto tienen errores del orden de 10 ms. En el conjunto de campo con retardos hasta 400 ms, TLCA obtuvo un error absoluto medio de 5 ms, un error cuadrático medio de 7 ms y R2 de 99,97 %, mientras los conjuntos de árboles y el MLP superan 45 ms de error y tienen R2 menor que 70 %, y el método de frecuencia, SVR y KNN no generalizan. La sensibilidad muestra errores menores que 1 ms para retardos de hasta 200 ms con segmentos de 3000 muestras en simulación, y menores de 6 ms en campo. La optimización bayesiana encontró 340 Hz como frecuencia óptima de sobremuestreo en 500 iteraciones y redujo el tiempo de cómputo cerca de un orden de magnitud respecto al remuestreo exhaustivo con exactitud comparable, según la descripción textual.

**Discusión y contribución.** Los autores atribuyen el desempeño superior a la combinación de convoluciones sensibles al retardo y atención global, que aprenden directamente de la señal sin características manuales ni supuestos de amortiguamiento lineal. Posicionan el método como complemento de los protocolos de red: estos proporcionan alineación gruesa y el método corrige los desfases residuales en el posprocesamiento. Concluyen que el marco mejora la fiabilidad de la identificación modal y de la detección de daño y, con ello, el monitoreo de infraestructura más seguro y resiliente. Reconocen un sesgo menor de amplitud por filtros FIR de longitud finita y plantean ampliar el método a muestreo no uniforme, deriva de reloj, tasas heterogéneas y dinámica no lineal, y evaluarlo en hardware de borde real.

**Limitaciones declaradas.** Declaradas: sesgo menor de amplitud por filtros FIR de longitud finita; el método no considera aún muestreo no uniforme, deriva de reloj, tasas de muestreo heterogéneas ni dinámica no lineal; falta evaluar el despliegue en hardware de borde. No declaradas: los retardos del conjunto de campo se inyectaron sobre datos que ya estaban sincronizados, de modo que no se prueba con desfases reales de una red inalámbrica; datos anómalos del puente se eliminaron antes del análisis; no se evalúa efecto sobre identificación modal con indicadores cuantitativos en el texto disponible; la afirmación de 'submilisegundo' del resumen contrasta con errores de 2 y 5 ms en las comparaciones principales; sin pruebas de generalización a otros puentes o edificios; el error cuadrático medio reportado (1,4 ms) es menor que el error absoluto medio (2 ms), lo que es matemáticamente imposible.

**Trabajo futuro.** Explícito: extender a muestreo no uniforme, deriva de reloj y tasas heterogéneas; incorporar dinámica ligeramente no lineal; optimizar el diseño de filtros; evaluar en dispositivos de borde reales. Implícito: validación con redes inalámbricas desincronizadas de forma natural y con efectos sobre detección de daño.

**Palabras clave.** Declaradas: Data synchronization; end-to-end deep learning (DL); noninteger time lag; structural health monitoring; wireless Internet of Things (IoT) | Inferidas: sincronización de datos, retardo no entero, monitoreo de salud estructural, internet de las cosas inalámbrico, red neuronal convolucional con atención, remuestreo, optimización bayesiana, puente Jindo, vibración

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un marco de aprendizaje profundo (TLCA) más remuestreo con optimización bayesiana permite estimar y corregir retardos temporales no enteros entre sensores inalámbricos de SHM directamente desde la señal de vibración, sin marcas de tiempo ni supuestos físicos restrictivos, con precisión de milisegundos o menor, robustez ante ruido y acoplamiento modal y un costo de cómputo compatible con nodos de borde, con lo que mejora la fiabilidad de la identificación modal y de la detección de daño.

**Antítesis identificada.** La evidencia de campo es menos concluyente de lo que sugiere el resumen. Los retardos se inyectaron artificialmente en datos ya sincronizados, de modo que el modelo aprende la estructura del procedimiento de síntesis y no desfases reales de una red inalámbrica. El resumen indica precisión submilisegundo, pero los resultados principales muestran errores de 2 ms en simulación y 5 ms en campo, mientras el error cuadrático medio reportado (1,4 ms) es menor que el error absoluto medio (2 ms), lo que es imposible. No hay comparación con métodos de sincronización recientes de la familia de remuestreo con marcas de tiempo ni pruebas en hardware de borde, y el beneficio sobre identificación modal y detección de daño se afirma sin indicadores cuantitativos en el texto. Los comparadores basados en características se construyeron con atributos limitados, lo que favorece al método propuesto.

**Síntesis propuesta.** La contribución sostenible es una prueba de concepto de que un estimador de retardo basado en aprendizaje con parámetros ligeros supera, en datos sintéticos y en datos de campo con retardos inyectados, a un estimador de frecuencia y a regresores con características manuales, y de que el remuestreo guiado por optimización reduce el costo de alineación. El alcance se limita a la corrección posterior de desfases residuales cuando existe una referencia sincronizada para entrenar. Para el corpus, importa porque documenta una fuente de error de datos en gemelos de infraestructura alimentados por sensores inalámbricos, pero no demuestra que la sincronización mejore decisiones ni la recuperación posterior a un sismo.

**Áreas grises detectadas.**

1. Validez de los datos de campo: los retardos de los conjuntos del puente Jindo se generaron por desplazamiento de segmentos sincronizados y submuestreo, de modo que el error reportado mide la reconstrucción de retardos sintéticos; no se prueba con registros de nodos que presenten deriva y latencias reales, ni se informa de un conjunto externo de otro puente o edificio.
2. Coherencia de las métricas: el texto reporta un error absoluto medio de 2 ms y un error cuadrático medio de 1,4 ms para el conjunto simulado (Sec. VI-F), valores incompatibles porque el segundo no puede ser menor que el primero; además, el resumen habla de precisión submilisegundo y de mejora de un orden de magnitud, mientras la comparación principal en campo muestra 5 ms y 7 ms.
3. Efecto en tareas finales: la conclusión de que la sincronización mejora la identificación modal y la detección de daño se apoya en una figura de formas modales sincronizadas, asíncronas y teóricas, sin errores modales cuantitativos ni pruebas sobre daños, lo que deja sin demostrar el beneficio para el SHM.
4. Competidores y línea base: los regresores se alimentan con pocas características (retardo por correlación cruzada, diferencias estadísticas y pendiente de fase) y se contrastan con un método de frecuencia tuneado, pero no con métodos de remuestreo recientes ni con otras redes profundas; la ventaja puede reflejar el diseño del benchmark.

**Puntos oscuros aclarados.** Llama la atención que el artículo anuncie precisión submilisegundo como logro central, mientras los resultados de comparación principal reportan errores absolutos medios de 2 ms en simulación y de 5 ms en campo, y que la tabla de comparación muestre un error cuadrático medio menor que el error absoluto medio, lo que indica un error de transcripción o de cálculo. También es notable que el método se valide en un conjunto de campo cuyos retardos fueron creados por los autores, lo cual deja abierta la pregunta de si el modelo reconocería patrones de desfase de una red real con deriva de reloj, que los autores dejan como trabajo futuro. La eliminación previa de mediciones anómalas del puente, sin criterio descrito, introduce una selección de datos no documentada. Además, el desempeño de los comparadores ML varía desde 10 ms hasta más de 45 ms entre conjuntos, sin explicar el origen de la brecha. Por último, se afirma un apoyo a infraestructura más segura y resiliente sin ninguna prueba de decisión ni de daño detectado.

**Ideas propositivas novedosas.**

1. Indicador de calidad de datos para gemelos de infraestructura: incorporar la incertidumbre del retardo estimado como atributo de cada medición que ingresa a un gemelo digital estructural, de modo que el gemelo reduzca el peso de los datos con desfase incierto durante la actualización posterior a un sismo. Se podría validar con registros de redes inalámbricas reales de un edificio en una región sísmica durante al menos seis meses de operación continua, comparando la identificación modal con y sin corrección y midiendo el cambio en el diagnóstico de daño y en el tiempo necesario para declarar una estructura apta para reocupación.
2. Prueba de robustez ante fallos de red en emergencia: repetir la validación con desfases generados por pérdida de paquetes, reinicios de nodos y reconexión tras un evento sísmico, en lugar de retardos uniformes, y reportar cuántos minutos de datos se recuperan y con qué error residual. Con ello se establecería si el método sirve en el momento en que el monitoreo es más necesario, es decir, cuando la red está degradada, y se podría estimar el costo de equipar nodos de borde con el modelo de 0,41 MB, junto con el ahorro de energía por evitar el intercambio de balizas.

**Relaciones poco exploradas.**

1. Calidad de datos de sensores (condiciona) los gemelos de infraestructura del corpus (D014, D023, D035): estos construyen gemelos de puentes y edificios con datos de sensores inalámbricos, y D039 documenta que el desfase temporal distorsiona la identificación modal que alimenta la actualización del modelo, aunque ninguno cuantifica este efecto.
2. Aprendizaje profundo en el borde (complementa) el estudio de IoT semántico para alerta temprana (D031): comparten la restricción de latencia y de recursos en nodos, pero D039 trabaja posprocesamiento de vibraciones y no alerta en tiempo real.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 4/10 — Aporta un método ligero y reproducible en principio para corregir desfases temporales en SHM inalámbrico, con comparaciones amplias en simulación y un caso de campo de un puente atirantado con retardos inyectados. Su valor para el corpus es periférico porque trata la calidad de datos en monitoreo y no sismos, empresas ni recuperación, y se reduce por la validación con retardos sintéticos, la inconsistencia de métricas y la ausencia de pruebas en hardware y de efecto sobre decisiones.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Afirmación opuesta a la evidencia presentada (El resumen declara precisión submilisegundo y un orden de magnitud de mejora, pero los resultados principales muestran 2 ms y 5 ms de error absoluto medio (Resumen, p. 1; Sec. VI-F, p. 10)); Generalización apresurada (Se concluye robustez y escalabilidad para SHM real a partir de un puente con retardos inyectados y una estructura simulada de cuatro grados de libertad (Sec. VII, p. 12)); Apelación a la tecnología (Se afirma que el marco hace el monitoreo de infraestructura 'más seguro y resiliente' sin medir efectos sobre la detección de daño ni sobre decisiones (Sec. VII, p. 12))
- **Bradford-Hill:** No aplica: es un desarrollo de método con validación predictiva sobre datos con retardos conocidos; no estima efectos causales del método sobre la calidad del diagnóstico de la estructura.
- **TRL asignado:** 4 — 'we will investigate the real-world deployment of the proposed approach on actual edge hardware' (p. 12)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (13 páginas con referencias). Las tablas I a V no son legibles en la extracción; las cifras se tomaron del texto narrativo de las secciones VI-C a VI-G. La inconsistencia RMSE 1,4 ms frente a MAE 2 ms aparece así en el texto y se reporta sin corregir.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un marco de aprendizaje profundo (TLCA) más remuestreo con optimización bayesiana permite estimar y corregir retardos temporales no enteros entre sensores inalámbricos de SHM directamente desde la señal de vibración, sin marcas de tiempo ni supuestos físicos restrictivos, con precisión de milisegundos o menor, robustez ante ruido y acoplamiento modal y un costo de cómputo compatible con nodos de borde, con lo que mejora la fiabilidad de la identificación modal y de la detección de daño.  | La evidencia de campo es menos concluyente de lo que sugiere el resumen. Los retardos se inyectaron artificialmente en datos ya sincronizados, de modo que el modelo aprende la estructura del procedimiento de síntesis y no desfases reales de una red inalámbrica. El resumen indica precisión submilisegundo, pero los resultados principales muestran errores de 2 ms en simulación y 5 ms en campo, mientras el error cuadrático medio reportado (1,4 ms) es menor que el error absoluto medio (2 ms), lo que es imposible. No hay comparación con métodos de sincronización recientes de la familia de remuestreo con marcas de tiempo ni pruebas en hardware de borde, y el beneficio sobre identificación modal y detección de daño se afirma sin indicadores cuantitativos en el texto. Los comparadores basados en características se construyeron con atributos limitados, lo que favorece al método propuesto.  | La contribución sostenible es una prueba de concepto de que un estimador de retardo basado en aprendizaje con parámetros ligeros supera, en datos sintéticos y en datos de campo con retardos inyectados, a un estimador de frecuencia y a regresores con características manuales, y de que el remuestreo guiado por optimización reduce el costo de alineación. El alcance se limita a la corrección posterior de desfases residuales cuando existe una referencia sincronizada para entrenar. Para el corpus, importa porque documenta una fuente de error de datos en gemelos de infraestructura alimentados por sensores inalámbricos, pero no demuestra que la sincronización mejore decisiones ni la recuperación posterior a un sismo.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Retardo no entero' es un desfase entre sensores menor que el intervalo de muestreo; 'sincronización' es estimar y corregir ese desfase; 'precisión submilisegundo' implica errores menores que 1 ms.
- **P2 Supuestos:** Supone que los retardos inyectados representan los desfases reales de una red inalámbrica, que el modelo entrenado con datos de un puente generaliza a otros y que corregir el desfase mejora la identificación modal.
- **P3 Evidencia:** La evidencia son dos conjuntos con retardos sintéticos, comparaciones con seis regresores y un método de frecuencia, ablación, sensibilidad y una figura de formas modales sin cifras en el texto.
- **P4 Consecuencias:** Si es cierto, los sistemas inalámbricos pueden corregir desfases residuales con modelos de 0,41 MB sin intercambio de marcas de tiempo; si es falso, pueden confiar en una corrección que falla con desfases reales.
- **P5 Contraejemplos:** No se examinan nodos con deriva real, pérdida de paquetes, otros puentes o edificios, ni el efecto en la detección de daño con indicadores cuantitativos.
- **P6 Alternativas:** Alternativas: que un protocolo de sincronización mejorado resuelva el problema en la red; que los métodos de frecuencia con ajustes finos igualen el desempeño; que el error dominante sea la calidad del sensor y no el desfase.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Parámetros entrenables del modelo TLCA | 108 | mil parámetros | Memoria 0,41 MB | Sec. VI-C, p. 9 | Texto | Alta | Modelo ligero |
| Latencia de inferencia en GPU / CPU | 0,04 / 0,14 | ms | Par de segmentos de 2000 puntos | Sec. VI-C, p. 9 | Texto | Alta | 3,87 millones de FLOPs |
| Error absoluto medio en simulación | 2 | ms | Retardos hasta 500 ms | Sec. VI-F, p. 10 | Texto | Media | Reporta RMSE de 1,4 ms, inconsistente |
| Error absoluto medio en campo (Jindo) | 5 | ms | Retardos hasta 400 ms; R2 = 99,97 % | Sec. VI-F, p. 10 | Texto | Alta | Retardos inyectados |
| Error de regresores de conjunto en simulación | 10 | ms | RF, GBR y XGBoost | Sec. VI-F, p. 9-10 | Texto | Media | Orden de magnitud |
| Error de regresores de conjunto y MLP en campo | 45 | ms | R2 inferior a 70 % | Sec. VI-F, p. 10 | Texto | Media | Valor mínimo citado como superado |
| Frecuencia óptima de sobremuestreo | 340 | Hz | Búsqueda de 100 a 600 Hz con 500 iteraciones | Sec. VI-G, p. 10 | Texto | Alta | Optimización bayesiana |
| Nodos inalámbricos del puente Jindo | 70 | nodos | Plataforma Imote2 | Sec. IV-B, p. 6 | Texto | Alta | 24 canales mostrados |
| Tiempo de entrenamiento en GPU / CPU | 4 / 12 | minutos | Aproximadamente | Sec. VI-C, p. 9 | Texto | Alta | Entrenamiento completo |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'we will investigate the real-world deployment of the proposed approach on actual edge hardware' (p. 12) | Validado en laboratorio computacional con datos sintéticos y datos de campo con retardos inyectados; sin hardware de borde ni retardos reales. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'making it well suited for IoT-based SHM applications' (p. 2) | Sin análisis de mercado, costos ni modelo de negocio. |
| IRL | 3 | Sí | 'The proposed work is positioned at the post hoc signal-level synchronization' (p. 12) | Se describe la complementariedad con protocolos de red; no se prueba la integración con una red real de nodos. |
| DRL | 3 | Sí | 'SHM imposes stringent requirements on synchronization accuracy across distributed sensor measurements' (p. 1) | Necesidad argumentada con literatura técnica; sin demanda de usuarios medida. |
| SRL | 1.33 | Sí | Componentes: Estimador de retardo TLCA (TRL 4), Remuestreo con optimización bayesiana (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 12.0; ÷9 → 1.33; nivel acotado a [1,9] = 1.33 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 4 con BRL 1 e IRL 3: método validado en datos con retardos sintéticos, sin hardware de borde, sin red real y sin análisis de costos. · Estrategia de salida: Pruebas con nodos inalámbricos reales y desfases naturales, comparación con métodos de remuestreo recientes y evaluación de efecto en identificación modal.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Afirmación opuesta a la evidencia presentada | El resumen declara precisión submilisegundo y un orden de magnitud de mejora, pero los resultados principales muestran 2 ms y 5 ms de error absoluto medio (Resumen, p. 1; Sec. VI-F, p. 10) | Resumen sobrestima los resultados |
| Generalización apresurada | Se concluye robustez y escalabilidad para SHM real a partir de un puente con retardos inyectados y una estructura simulada de cuatro grados de libertad (Sec. VII, p. 12) | Base de datos limitada |
| Apelación a la tecnología | Se afirma que el marco hace el monitoreo de infraestructura 'más seguro y resiliente' sin medir efectos sobre la detección de daño ni sobre decisiones (Sec. VII, p. 12) | Beneficio asumido |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Corrección del retardo → identificación modal más fiable y mejor detección de daño | Argumento físico (error de fase) y figura de formas modales | Plausibilidad física | Evidencia cuantitativa, comparación con daños | Calidad de sensores, ruido, método modal | 2 | Mecanismo plausible, efecto no cuantificado |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Tecnológico | Prueba con nodos reales, deriva de reloj, pérdida de paquetes y hardware de borde | Crítico | Media | 8 |
| Metodológico | Validación con retardos naturales, conjunto externo y métricas coherentes | Crítico | Media | 8 |
| Conocimiento | Efecto cuantitativo de la sincronización sobre la actualización de gemelos y el diagnóstico de daño | Significativo | Media | 7 |
| Mercado | Costo de despliegue del modelo en nodos y beneficio frente a mejorar protocolos de red | Significativo | Baja | 6 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 5 | Dominios del tiempo y de la frecuencia de la estructura de cuatro grados de libertad | Gráfico | Respuestas simuladas | 4 canales | Media |
| Fig. 6 | Distribución espacial de nodos en el puente Jindo | Esquema | Despliegue de sensores | 70 nodos | Media |
| Fig. 7 | Datos registrados por 24 sensores del puente | Gráfico | Aceleraciones | 1000 s | Media |
| Tabla I | Estudio de ablación de componentes | Tabla | CNN base, atención, correlación cruzada, LSTM y TLCA | No legible | Alta |
| Tabla V | Comparación entre modelos | Tabla | FD, SVR, RF, GBR, XGBoost, KNN, MLP y TLCA | MAE 2 ms y 5 ms | Alta |
| Fig. 9 | Convergencia de la optimización bayesiana y correlaciones frente a frecuencia | Gráfico | Frecuencia óptima | 340 Hz | Media |
| Fig. 12 | Formas modales sincronizadas, asíncronas y teóricas | Gráfico | Cuatro modos | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Dragos et al. (2024), sincronización en el dominio de la frecuencia de datos de SHM | No especificado en documento | Academia | Estimación de retardo por pendiente de fase | Método establecido | Retardos tratados como enteros y dependencia de parámetros | Estable |
| Fu et al. (2025), sincronización robusta con retardos arbitrarios | No especificado en documento | Academia | Alineación con retardos arbitrarios | Robustez | Dependencia de supuestos del modelo | Creciendo |
| Li et al. (2016) y Fu et al. (2021), sincronización por marcas de tiempo y remuestreo | No especificado en documento | Academia | Remuestreo con intercambio de balizas | Probado en campo | Consumo de energía por comunicación | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Error de estimación del retardo (MAE, RMSE y R2) en milisegundos
- **X:** Método de estimación (TLCA, FD, regresores ML) y longitud de segmento, rango de retardo y ruido
- **Z (controles):** Conjunto de datos (simulado o puente), nivel de ruido, acoplamiento modal
- **Datos:** Estructura simulada de cuatro grados de libertad (40 000 muestras por canal) y datos del puente Jindo con 1000 s a 25 Hz
- **Método:** Aprendizaje supervisado con comparación de modelos, partición 7:1:2 y tres ejecuciones
- **Efecto reportado:** MAE de 2 ms (simulación) y 5 ms (campo) frente a 10 ms y más de 45 ms de los regresores de conjunto
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Pruebas de ruido y acoplamiento modal, sensibilidad a longitud de segmento y rango de retardo; sin conjunto externo ni retardos reales

| Vacío | Tipo | Descripción |
|---|---|---|
| V-039-01 | TERR | Puente Jindo (Corea del Sur) y estructura simulada; sin otras regiones ni zonas sísmicas |
| V-039-02 | POBL | Sin usuarios ni empresas; unidad de análisis son señales de sensores |
| V-039-03 | TEMP | Registros de 100 s a 1000 s; sin monitoreo de largo plazo ni evento sísmico |
| V-039-04 | MET | Retardos inyectados, eliminación previa de datos anómalos y métrica inconsistente (RMSE menor que MAE) |
| V-039-05 | VAR | Faltan variables de deriva de reloj, pérdida de paquetes, consumo de energía medido y errores modales |
| V-039-06 | TEOR | Marco de procesamiento de señales y vibraciones; sin teoría de gemelos digitales ni de resiliencia |
| V-039-07 | CAUS | Sin evidencia causal del efecto de la corrección sobre el diagnóstico estructural |
