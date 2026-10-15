# FB-L01-043 | D043 — Federated Unlearning Framework for Digital Twin–Based Aviation Health Monitoring Under Sensor Drift and Data Corruption

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/electronics-14-02968-v2.pdf` · 35 páginas · Relevancia para el eje del corpus: **Periférico** (Propone un marco de gemelos digitales por subsistema, aprendizaje federado y 'desaprendizaje' federado (eliminación a posteriori de contribuciones corruptas) para el monitoreo de salud de aeronaves, validado solo por simulación. Aporta una idea transferible sobre integridad de datos y corrección de modelos en gemelos alimentados por sensores, pero su dominio es aviación y no trata sismos, infraestructura ni empresas.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-043 / D043
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Kabashkin, I. (2025). Federated Unlearning Framework for Digital Twin–Based Aviation Health Monitoring Under Sensor Drift and Data Corruption. *Electronics (Switzerland)*, *14*(15), Article 2968. https://doi.org/10.3390/electronics14152968
- **Autores:** Kabashkin, Igor (6602318373)
- **Afiliaciones:** Engineering Faculty, Transport and Telecommunication Institute, Lauvas 2, Riga, LV-1019, Latvia
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Electronics (Switzerland) · vol. 14(15)
- **Identificador persistente:** DOI 10.3390/electronics14152968 · ISSN 20799292
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105013332039&doi=10.3390%2felectronics14152968&partnerID=40&md5=c3be19eeed473bd3de07ea857b719b69
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 7

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Proponer un marco que combine gemelos digitales de subsistemas de aeronaves, aprendizaje federado (FL) para entrenamiento colaborativo sin compartir datos crudos y desaprendizaje federado (FU) para eliminar a posteriori la influencia de contribuciones de clientes con datos corruptos o adversarios, en el monitoreo de salud de aeronaves (AHM). El estudio pretende restaurar la exactitud de los modelos degradados por deriva de sensores, errores de etiquetas y actualizaciones adversarias, reducir los falsos negativos en la detección temprana de fallas y asegurar trazabilidad auditable de las correcciones, en línea con requisitos regulatorios de aviación.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son cuánto se degrada un modelo federado de detección de fallas cuando 20 % de los clientes aporta datos corruptos, si tres métodos de desaprendizaje (resta de gradientes, reagregación exacta y reentrenamiento restringido) restauran el desempeño y a qué costo computacional, y si el registro criptográfico de eventos de desaprendizaje es compatible con la auditoría de aviación.

**Marco teórico.** El marco integra tres componentes. Primero, gemelos digitales por subsistema (hidráulica, motores, superficies de control y ambiente) que reciben telemetría sincronizada y entrenan localmente. Segundo, el promedio federado (FedAvg) con un coordinador central que agrega actualizaciones de modelos. Tercero, mecanismos de desaprendizaje federado que retiran la contribución de un cliente comprometido. Se añade una capa de gobernanza con registro criptográfico, puntuación de confianza y participación, y se plantean métricas de recuperación (deriva del modelo en norma euclidiana y tasa de recuperación basada en F1). La motivación proviene de la inseguridad de datos en dominios críticos para la seguridad y del derecho al borrado de datos en privacidad.

**Metodología.** La simulación replica una flota de 30 gemelos digitales cliente con series de tiempo de presión hidráulica, vibración y temperatura de gases de escape de motores, actuadores y variables ambientales. Los datos son sintéticos y 'semirrealistas', generados con modelos estadísticos basados en distribuciones reales, con degradación periódica, dinámica de fases de vuelo y ruido, y con fallas etiquetadas según cronologías de mantenimiento. Cada cliente entrena una red LSTM con pérdida de entropía cruzada binaria. El entrenamiento federado dura 100 rondas con 80 % de participación. A partir de la ronda 10, seis de 30 clientes (20 %) reciben corrupción: deriva de sensores (por ejemplo, +20 % de presión base), inversión de etiquetas, ruido gaussiano o sesgo adversario. Se aplican tres métodos de desaprendizaje sobre instantáneas idénticas del modelo en la ronda 60. Las métricas son exactitud, precisión, exhaustividad, F1, AUC, latencia y similitud coseno. Se agrega un estudio de caso de un cliente con deriva del +15 % en presión desde la ronda 21.

**Resultados principales.** El modelo base federado alcanzó exactitud de 92,8 %, precisión de 91,2 %, exhaustividad de 90,4 %, F1 de 90,8 %, AUC de 0,96 y latencia de 23,5 ms, frente a 93,1 % de exactitud del modelo centralizado. Con 20 % de clientes corruptos, a la ronda 60 la exactitud cayó a 84,1 %, la precisión a 80,2 %, la exhaustividad a 75,5 %, el F1 a 77,8 % y el AUC a 0,88, con aumento de falsos negativos y similitud coseno de gradientes de clientes corruptos de 0,42. Tras el desaprendizaje, la exactitud fue de 88,2 % con resta de gradientes, 90,7 % con reagregación exacta y 92,5 % con reentrenamiento restringido, y el F1 llegó a 90,5 % con este último. La similitud coseno con el modelo base subió de 0,76 a 0,91 y 0,97 con los dos primeros métodos. El resumen declara una restauración de 'hasta 95 %' de la exactitud degradada. El reentrenamiento restringido tuvo el mayor costo computacional y la resta de gradientes el menor. El estudio de caso hidráulico con un cliente con deriva de +15 % desde la ronda 21 muestra una caída de sensibilidad hacia la ronda 40 para fallas incipientes, que se corrige al retirar la contribución del cliente. Se reporta además que la participación de los clientes limpios se reanudó sin rechazo y que cada evento de desaprendizaje quedó registrado en la pista de auditoría con los clientes afectados, el método, la hora y el resultado de validación.

**Discusión y contribución.** El artículo sostiene que el desaprendizaje federado es un habilitador de inteligencia artificial resiliente, corregible y confiable para el monitoreo de salud de aeronaves, porque permite revertir los efectos de clientes comprometidos sin reentrenar desde cero, mantiene la participación de los clientes limpios y deja un registro auditable. Plantea una guía de selección de método según el compromiso entre precisión, eficiencia, trazabilidad y escalabilidad, la integración con puntuación de confianza y la necesidad de acoplar la detección de anomalías en el gemelo con la calibración de confianza del modelo federado. Reconoce que los resultados son de simulación y propone pilotos con datos reales.

**Limitaciones declaradas.** Declaradas: resultados con datos sintéticos y semirrealistas en un entorno federado simulado; ausencia de condiciones reales como actualizaciones asíncronas, heterogeneidad de hardware y retrasos de comunicación; granularidad gruesa del desaprendizaje; falta de integración con flujos de certificación regulatoria. No declaradas: la corrupción se inyecta con parámetros fijados por la autoría del estudio (20 % de clientes, +20 % de deriva) y los clientes corruptos se conocen de antemano para aplicar el desaprendizaje, sin un detector; un solo conjunto de ejecución sin repeticiones ni intervalos; comparaciones con otras defensas (agregación robusta, filtrado por confianza) no se realizan; el resumen reporta 'hasta 95 %' mientras la tabla permite calcular recuperaciones distintas según la métrica; texto que califica de 'mejora' la caída de exactitud, precisión y exhaustividad.

**Trabajo futuro.** Explícito: pilotos con datos reales de aeronaves, desaprendizaje de granularidad fina, orquestación multiobjetivo de estrategias de desaprendizaje, acoplamiento bidireccional entre detección de anomalías del gemelo y confianza del modelo federado, e integración con flujos de certificación. Implícito: comparación con defensas robustas y pruebas con comunicación asíncrona.

**Palabras clave.** Declaradas: aviation health monitoring; data corruption; digital twin; federated learning; federated unlearning; sensor drift | Inferidas: monitoreo de salud de aeronaves, gemelo digital, aprendizaje federado, desaprendizaje federado, deriva de sensores, corrupción de datos, envenenamiento de datos, integridad, auditoría criptográfica, LSTM

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Los marcos de gemelos digitales con aprendizaje federado necesitan un mecanismo de desaprendizaje para eliminar la influencia de datos corruptos o adversarios una vez integrados al modelo global; en simulación con 30 gemelos de aeronave y 20 % de clientes corruptos, el desaprendizaje restaura el desempeño perdido (exactitud de 84,1 % a 88,2 %, 90,7 % y 92,5 %, según el método), reduce los falsos negativos y deja registros auditables, por lo que constituye un componente esencial de sistemas de monitoreo confiables en dominios críticos.

**Antítesis identificada.** El resultado depende del diseño de la simulación. Los datos son sintéticos, la corrupción se genera con parámetros elegidos por la autoría del estudio y los seis clientes dañados se identifican de antemano, de modo que el estudio no mide la parte difícil del problema, que es detectar qué cliente está comprometido y cuándo. Se compara solo contra el modelo sin desaprendizaje y no contra defensas de agregación robusta o de filtrado por confianza que evitan el problema en origen. No se reportan repeticiones ni intervalos, y el texto describe como 'mejora' la caída de las métricas con corrupción. La cifra 'hasta 95 %' del resumen no se corresponde de forma directa con la tabla, y la afirmación de alineación con la regulación aeronáutica se apoya en el diseño de registros y no en una evaluación con una autoridad.

**Síntesis propuesta.** La contribución sostenible es una prueba de concepto de que, bajo corrupción conocida de una fracción de clientes, retirar sus contribuciones restaura gran parte del desempeño de un detector de fallas federado, con compromisos claros entre fidelidad y costo entre tres métodos. La transferencia al corpus es conceptual: cualquier gemelo digital alimentado por sensores de múltiples activos (puentes, plantas, flotas) puede sufrir deriva y datos corruptos, y requiere trazabilidad y capacidad de corrección. No hay evidencia en infraestructura sísmica, ni de detección automática de clientes corruptos, ni de costos, de modo que su uso en el proyecto se limita a especificar requisitos de trazabilidad y de corrección para gemelos con múltiples fuentes de datos.

**Áreas grises detectadas.**

1. Naturaleza de los datos: los conjuntos son sintéticos 'basados en distribuciones reales' y se declara su carácter semirrealista, pero no se describen las distribuciones, los parámetros de generación ni su verificación con telemetría real, de modo que las métricas de 92,8 % de exactitud base reflejan el generador.
2. Detección de clientes corruptos: el desaprendizaje se aplica a seis clientes 'previamente identificados', y la identificación depende de un mecanismo (puntuación de confianza o similitud de gradientes) que no se evalúa; la parte más difícil de la práctica, saber cuándo y a quién desaprender, queda fuera de los resultados.
3. Consistencia numérica: el texto indica que las métricas 'mejoraron' en 8,7 %, 11,0 %, 14,9 % y 13,0 % tras la corrupción, cuando son caídas, y el resumen cita 'hasta 95 %' de recuperación mientras el cálculo por F1 (90,5 frente a 77,8 y 90,8) da cerca de 98 % para el reentrenamiento restringido.
4. Aplicabilidad regulatoria: se afirma alineación con normas de aviación por el registro criptográfico de eventos, pero no hay evaluación con un regulador ni mapeo a requisitos específicos de certificación, y el propio texto reconoce falta de integración con flujos de certificación.

**Puntos oscuros aclarados.** Llama la atención que el resumen presente el desaprendizaje como habilitador de sistemas confiables cuando el experimento parte de un conjunto conocido de seis clientes dañados, de modo que no se mide la capacidad de detectar la corrupción. También es notable que el texto describa como mejoras las caídas de exactitud, precisión, exhaustividad y F1 del escenario corrupto, lo que revela descuido en la redacción de resultados. La ausencia de repeticiones, de intervalos de confianza y de comparación con técnicas de agregación robusta limita la inferencia sobre la ventaja del desaprendizaje. Además, el estudio de caso hidráulico se presenta como demostración de aplicabilidad real, aunque corresponde a un cliente simulado con deriva programada de +15 %. Por último, el artículo extiende más de 30 páginas con numerosos diagramas conceptuales y solo una tabla de resultados cuantitativos, lo que sugiere un mayor peso del diseño que de la evidencia, y que la audiencia a la que se dirigen las conclusiones (reguladores, operadores y fabricantes) no participó en ninguna validación del marco.

**Ideas propositivas novedosas.**

1. Gemelo de infraestructura con trazabilidad de datos: adaptar el esquema de confianza y desaprendizaje a una red de gemelos de puentes o edificios que comparten un modelo de daño entre propietarios, de modo que un sensor con deriva detectado después de un sismo pueda retirarse del modelo global sin reentrenar y con registro auditable. Se podría probar con los datos de redes inalámbricas de monitoreo estructural, inyectando deriva en un nodo y midiendo la degradación del diagnóstico de daño y la recuperación tras el desaprendizaje, así como el tiempo entre la aparición de la deriva y su retiro del modelo, que es el indicador que decide si la técnica sirve durante la ventana de decisión posterior a un sismo.
2. Detector de corrupción como componente evaluado: construir un banco de pruebas donde el detector de clientes comprometidos (similitud de gradientes, puntuación de confianza) deba identificar la corrupción sin conocimiento previo, y reportar sensibilidad, especificidad y retraso de detección, además de la recuperación posterior. Un resultado en un entorno de múltiples pymes con sensores de bajo costo mostraría qué fracción de errores de deriva se corrige antes de que afecte decisiones de reanudación de producción, con cuántas horas de retraso y a qué costo de cómputo por corrección en dispositivos de borde de bajo costo.

**Relaciones poco exploradas.**

1. Calidad de datos de sensores (comparte problema con) D039: ambos tratan errores de los sensores en sistemas de monitoreo con IoT (retardos temporales en D039, deriva y corrupción en D043), con soluciones de aprendizaje y validación en simulación o con datos de campo alterados.
2. Gemelo digital con múltiples activos (contrasta con) D018: D018 aplica inteligencia artificial agéntica y gemelos en redes eléctricas, y D043 formaliza la corrección de modelos cuando los datos de algunos activos se degradan; ninguno evalúa pérdida económica.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 3/10 — Ofrece una arquitectura y una prueba de concepto de corrección a posteriori de modelos federados alimentados por gemelos digitales, con tres métodos comparados y trazabilidad. Su valor para el corpus es periférico: el dominio es aviación, los datos son sintéticos, la detección de clientes corruptos no se evalúa y no hay vínculo con sismos, infraestructura o empresas. Sirve como referencia conceptual sobre integridad y auditabilidad de datos en gemelos digitales.

**Conexiones inter-documentales.**

- **CONFIRMA** D065 (Asignación de recursos en cómputo en el borde con subastas y sistemas ): validación únicamente simulada de marcos descentralizados con tecnologías de borde y aprendizaje federado [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 93 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Petición de principio (resultado condicionado por el diseño) (El desaprendizaje se aplica a seis clientes ya identificados y se concluye que habilita sistemas confiables (Sec. 3.3, p. 21-22; Sec. 5, p. 33)); Generalización apresurada (Se concluye aplicabilidad real a partir de datos sintéticos y un cliente simulado con deriva programada (Sec. 3.4, p. 23-24)); Afirmación opuesta a la evidencia presentada (Se califican de 'mejora' las caídas de exactitud, precisión, exhaustividad y F1 con corrupción (Sec. 3.2, p. 20))
- **Bradford-Hill:** No aplica: es una simulación con intervención diseñada por la autoría del estudio; no se estima causalidad con datos observados, aunque la relación entre corrupción y degradación del modelo es consistente dentro del experimento.
- **TRL asignado:** 3 — 'The experimental results presented in this study were generated using a simulated federated environment with synthetic and semi-realistic data' (p. 32)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (35 páginas con referencias). Las figuras conceptuales no son legibles; las cifras de la Tabla 1 se reconstruyeron del texto con orden de columnas consistente con las cifras del texto (exactitud base 92,8 %; con corrupción 84,1 %). El cálculo de recuperación cercano a 98 % por F1 es del analista (90,5 - 77,8) / (90,8 - 77,8).

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Los marcos de gemelos digitales con aprendizaje federado necesitan un mecanismo de desaprendizaje para eliminar la influencia de datos corruptos o adversarios una vez integrados al modelo global; en simulación con 30 gemelos de aeronave y 20 % de clientes corruptos, el desaprendizaje restaura el desempeño perdido (exactitud de 84,1 % a 88,2 %, 90,7 % y 92,5 %, según el método), reduce los falsos negativos y deja registros auditables, por lo que constituye un componente esencial de sistemas de monitoreo confiables en dominios críticos.  | El resultado depende del diseño de la simulación. Los datos son sintéticos, la corrupción se genera con parámetros elegidos por la autoría del estudio y los seis clientes dañados se identifican de antemano, de modo que el estudio no mide la parte difícil del problema, que es detectar qué cliente está comprometido y cuándo. Se compara solo contra el modelo sin desaprendizaje y no contra defensas de agregación robusta o de filtrado por confianza que evitan el problema en origen. No se reportan repeticiones ni intervalos, y el texto describe como 'mejora' la caída de las métricas con corrupción. La cifra 'hasta 95 %' del resumen no se corresponde de forma directa con la tabla, y la afirmación de alineación con la regulación aeronáutica se apoya en el diseño de registros y no en una evaluación con una autoridad.  | La contribución sostenible es una prueba de concepto de que, bajo corrupción conocida de una fracción de clientes, retirar sus contribuciones restaura gran parte del desempeño de un detector de fallas federado, con compromisos claros entre fidelidad y costo entre tres métodos. La transferencia al corpus es conceptual: cualquier gemelo digital alimentado por sensores de múltiples activos (puentes, plantas, flotas) puede sufrir deriva y datos corruptos, y requiere trazabilidad y capacidad de corrección. No hay evidencia en infraestructura sísmica, ni de detección automática de clientes corruptos, ni de costos, de modo que su uso en el proyecto se limita a especificar requisitos de trazabilidad y de corrección para gemelos con múltiples fuentes de datos.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Desaprendizaje federado' es retirar de un modelo global la influencia de un cliente; 'deriva del sensor' es un desplazamiento gradual de la medición; 'tasa de recuperación' es la fracción de F1 perdida que se restaura.
- **P2 Supuestos:** Supone que los clientes corruptos pueden identificarse, que la corrupción simulada representa fallas reales y que la restauración en simulación se mantiene con datos reales y asíncronos.
- **P3 Evidencia:** La evidencia es una simulación con 30 clientes, 100 rondas, 6 clientes corruptos y una tabla con cinco condiciones, sin repeticiones ni datos reales.
- **P4 Consecuencias:** Si es cierto, las flotas pueden corregir modelos sin reentrenar y con auditoría; si es falso, pueden confiar en una corrección que depende de conocer de antemano a los clientes dañados.
- **P5 Contraejemplos:** No se examinan defensas robustas, detección automática de corrupción, datos reales, comunicación asíncrona ni costos.
- **P6 Alternativas:** Alternativas: que el filtrado de actualizaciones evite la corrupción en origen; que el reentrenamiento completo sea suficiente por su sencillez; que el entorno de certificación impida el uso de modelos federados.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Exactitud del modelo federado base | 92,8 | % | 30 clientes, 100 rondas, 80 % de participación | Sec. 3.1, p. 20 | Texto | Alta | Centralizado 93,1 % |
| Exactitud con 20 % de clientes corruptos | 84,1 | % | Ronda 60; caída de 8,7 puntos | Sec. 3.2, p. 20 | Texto | Alta | El texto lo describe como 'mejora' |
| Exhaustividad con corrupción | 75,5 | % | Frente a 90,4 % base | Sec. 3.2, p. 20 | Texto | Alta | Mayor caída; más falsos negativos |
| Exactitud tras resta de gradientes / reagregación / reentrenamiento | 88,2 / 90,7 / 92,5 | % | Tabla 1 | Tabla 1, p. 22 | Tabla | Alta | Datos sintéticos |
| F1 tras reentrenamiento restringido | 90,5 | % | Frente a 77,8 % con corrupción y 90,8 % base | Tabla 1, p. 22 | Tabla | Alta | Recuperación cercana a 98 % (cálculo del analista) |
| Similitud coseno con el modelo base tras desaprendizaje | 0,91 / 0,97 | coseno | Resta de gradientes y reagregación; 0,76 tras la corrupción | Sec. 3.3, p. 21-22 | Texto | Alta | Parámetros del modelo |
| Clientes del gemelo en la simulación / corruptos | 30 / 6 | clientes | 20 % de corrupción desde la ronda 10 | Sec. 3.2, p. 20 | Texto | Alta | Corrupción asignada por la autoría del estudio |
| Latencia de inferencia | 23,5 | ms | Por muestra en entorno de borde simulado | Sec. 3.1, p. 20 | Texto | Media | Simulada |
| Restauración declarada en el resumen | hasta 95 | % | De la exactitud degradada | Resumen, p. 1 | Texto | Media | No coincide con el cálculo directo de la Tabla 1 |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'The experimental results presented in this study were generated using a simulated federated environment with synthetic and semi-realistic data' (p. 32) | Prueba de concepto en simulación; sin datos reales ni hardware. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'aligning with aviation regulatory standards' (p. 1) | Alineación regulatoria afirmada; sin análisis de mercado, costos ni modelo de negocio. |
| IRL | 3 | Sí | 'real-world federated deployments introduce challenges such as non-synchronous updates, hardware heterogeneity, communication delays' (p. 32) | Integración de gemelos, aprendizaje federado y desaprendizaje en simulación; sin pruebas de integración con sistemas de aeronave. |
| DRL | 3 | Sí | 'In safety-critical domains, like aviation, the inability to remove the influence of these "damaged" datasets from trained models presents a serious challenge' (p. 2) | Necesidad argumentada con literatura de seguridad y regulación; sin demanda de usuarios medida. |
| SRL | 1.0 | Sí | Componentes: Gemelo digital por subsistema y aprendizaje federado (TRL 3), Desaprendizaje federado y auditoría (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 9.0; ÷9 → 1.00; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 3 con BRL 1 e IRL 3: simulación con corrupción conocida, sin datos reales, sin detección automática evaluada y sin análisis de costos. · Estrategia de salida: Pilotos con telemetría real, evaluación de detectores de corrupción y comparación con agregación robusta.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Petición de principio (resultado condicionado por el diseño) | El desaprendizaje se aplica a seis clientes ya identificados y se concluye que habilita sistemas confiables (Sec. 3.3, p. 21-22; Sec. 5, p. 33) | No se mide la detección de la corrupción |
| Generalización apresurada | Se concluye aplicabilidad real a partir de datos sintéticos y un cliente simulado con deriva programada (Sec. 3.4, p. 23-24) | El estudio de caso es una simulación |
| Afirmación opuesta a la evidencia presentada | Se califican de 'mejora' las caídas de exactitud, precisión, exhaustividad y F1 con corrupción (Sec. 3.2, p. 20) | Error de interpretación en el texto |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Clientes con datos corruptos → degradación del modelo federado → más falsos negativos | Resultado de simulación con corrupción inyectada | Experimento controlado (simulado) | Datos reales, repeticiones | Tipo y fracción de corrupción, heterogeneidad | 3 | Efecto establecido dentro de la simulación, sin validación externa |
| Desaprendizaje → recuperación del desempeño | Comparación de tres métodos sobre instantáneas idénticas | Experimento controlado (simulado) | Detección real, repeticiones, comparadores robustos | Momento de aplicación, número de clientes retirados | 3 | Efecto condicionado a identificación previa |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Evaluación del detector de corrupción y repeticiones con intervalos de confianza | Crítico | Media | 8 |
| Tecnológico | Pruebas con telemetría real, comunicación asíncrona y hardware heterogéneo | Crítico | Media | 8 |
| Conocimiento | Aplicación a gemelos de infraestructura civil y a entornos de desastre | Significativo | Media | 7 |
| Mercado | Costos y marco regulatorio de implementación | Moderado | Baja | 5 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 5 | Entorno federado simulado con coordinador y gemelos por subsistema | Diagrama | 30 clientes | 30 clientes | Media |
| Fig. 6 | Convergencia del modelo federado en 100 rondas | Gráfico | Exactitud, precisión, exhaustividad y F1 | 92,8 % final | Media |
| Fig. 7 | Matriz de confusión con 20 % de clientes corruptos | Matriz | Aumento de falsos negativos | No aplica | Media |
| Tabla 1 | Desempeño base, tras corrupción y tras tres métodos de desaprendizaje | Tabla | Exactitud, precisión, exhaustividad, F1 y AUC | 84,1 a 92,5 % | Alta |
| Fig. 8 | Curvas ROC en cinco escenarios | Gráfico | AUC por condición | AUC 0,88 a 0,96 | Media |
| Fig. 9 | Desempeño comparado de los cinco escenarios | Gráfico de barras | Base, corrupto y tres recuperaciones | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Marcos de aprendizaje federado robusto con normas de gradiente (Byzantine-resilient FL) | No especificado en documento | Academia | Agregación resistente a clientes maliciosos | Evitan el problema en origen | No retiran contribuciones ya agregadas | Creciendo |
| Marcos de aprendizaje federado para mantenimiento predictivo en aviación | No especificado en documento | Academia | Entrenamiento colaborativo sin compartir datos | Privacidad | Sin mecanismo de corrección posterior | Creciendo |

### B.9 Variables econométricas y vacíos

- **Y:** Exactitud, precisión, exhaustividad, F1 y AUC del detector de fallas; tasa de recuperación
- **X:** Fracción de clientes corruptos (20 %), tipo de corrupción y método de desaprendizaje
- **Z (controles):** Número de rondas, participación (80 %), subsistema
- **Datos:** 30 clientes simulados con telemetría sintética y semirrealista
- **Método:** Simulación federada con FedAvg y comparación de tres métodos de desaprendizaje
- **Efecto reportado:** Caída de exactitud de 92,8 % a 84,1 % y recuperación a 88,2 %, 90,7 % y 92,5 %
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin repeticiones ni intervalos; sin comparación con defensas robustas

| Vacío | Tipo | Descripción |
|---|---|---|
| V-043-01 | TERR | Sin territorio; dominio de aviación, institución de Letonia |
| V-043-02 | POBL | Flota simulada de 30 gemelos; sin operadores, empresas ni usuarios |
| V-043-03 | TEMP | 100 rondas de comunicación; sin horizonte operativo ni evolución del hardware |
| V-043-04 | MET | Datos sintéticos, corrupción asignada, detección no evaluada, sin repeticiones |
| V-043-05 | VAR | Faltan costos, tasas reales de falla de sensores y tiempo de detección de corrupción |
| V-043-06 | TEOR | Aprendizaje federado y desaprendizaje; sin teoría de resiliencia organizacional ni de gemelos de infraestructura |
| V-043-07 | CAUS | Efecto causal solo dentro de la simulación |
