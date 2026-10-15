# FB-L01-015 | D015 — A bayesian ordinal structural equation modeling framework for evaluating the seismic resilience of IoT-enabled buildings under uncertainty

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S2352012426005990-main.pdf` · 17 páginas · Relevancia para el eje del corpus: **Adyacente** (Modela con ecuaciones estructurales bayesianas ordinales la resiliencia sísmica de edificios con IoT y alerta temprana (calidad de sensado, analítica en tiempo real, control adaptativo, integración normativa); trata continuidad operativa y costo de falsas alarmas, pero no recuperación productiva ni empresas.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-015 / D015
- **Tipo de recurso:** Artículo científico (journal peer-reviewed)
- **Referencia APA 7:** Li, Z., Yan, G., Zandi, Y., Gholizadeh, M., Chen, Y., Khairy, Y., & Escorcia-Gutierrez, J. (2026). A bayesian ordinal structural equation modeling framework for evaluating the seismic resilience of IoT-enabled buildings under uncertainty. *Structures*, *88*, Article 111650. https://doi.org/10.1016/j.istruc.2026.111650
- **Autores:** Li, Zhonghong (57353303300); Yan, Gongxing (36705499200); Zandi, Yousef (54783788000); Gholizadeh, Morteza (57223289796); Chen, Yang (58897337000); Khairy, Yasmin (55823472700); Escorcia-Gutierrez, José (57191268293)
- **Afiliaciones:** School of architectural engineering, Chongqing Chemical Industry Vocational College, Chongqing, 401228, China; School of Intelligent Construction, Luzhou vocational and technical college, Sichuan, Luzhou, 646000, China; Luzhou Key Laboratory of Intelligent Construction and Low carbon Technology, Sichuan, Luzhou, 646000, China; Department of Civil Engineering, Tabriz Branch, Islamic Azad University, Tabriz, Iran; School of civil engineering, Chongqing Vocational Institute of Engineering, Chongqing, 402260, China; Central Labs, King Khalid University, AlQura’a, P.O. Box 960, Abha, Saudi Arabia; Department of Computational Science and Electronics, Universidad de la Costa, CUC, Barranquilla, 080002, Colombia
- **Fecha de publicación:** 2026
- **Fuente/contenedor:** Structures · vol. 88
- **Identificador persistente:** DOI 10.1016/j.istruc.2026.111650 · ISSN 23520124
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105034741784&doi=10.1016%2fj.istruc.2026.111650&partnerID=40&md5=7f58d2d52ee6aac6f6de76fb9c2efe6f
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 1

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Desarrollar un marco unificado y consistente con la incertidumbre para evaluar y mejorar la resiliencia sísmica de edificios con IoT en términos de desempeño relevante para la normativa. El marco, denominado BOSEM (modelo de ecuaciones estructurales ordinal bayesiano), integra la evaluación estructural en tiempo real mediante IoT con la modelación de variables latentes de resiliencia a partir de encuestas e inspecciones, y propaga la incertidumbre del sensado y de la alerta temprana hasta la probabilidad de cumplir límites de desempeño.

**Pregunta de investigación.** El texto no formula preguntas de investigación. Las preguntas implícitas son: cuáles mecanismos latentes (calidad de analítica en tiempo real, confiabilidad de la alerta temprana, capacidad adaptativa, integración de sensado y comunicación) explican el desempeño de resiliencia sísmica, con qué intensidad, y cómo se propaga la incertidumbre de los sensores y de la alerta hacia el cumplimiento normativo.

**Marco teórico.** El marco combina la ingeniería sísmica basada en desempeño (PBEE), que define el cumplimiento mediante límites de deriva de entrepiso y aceleración de piso, con el modelado de ecuaciones estructurales para constructos latentes y la inferencia bayesiana con verificaciones predictivas posteriores. Define cinco constructos latentes (calidad de analítica en tiempo real RTAQ, confiabilidad de la alerta temprana EWR, efectividad del control adaptativo ACE, integración de sensado y comunicación CSI y desempeño de resiliencia sísmica SRP), una capa ordinal por umbrales (probit o logit ordenado) y una capa de decisión con selección multinomial del modo de control. Es un enfoque cuantitativo, positivista y de ingeniería de sistemas.

**Metodología.** El modelo tiene cuatro capas: indicadores ordinales de encuesta e inspección con umbrales ordenados y cargas factoriales con una carga fijada en 1 por constructo; un sistema estructural latente (η = Bη + Γx + ζ); un modelo de incertidumbre de intensidad de alerta (I verdadera = I alerta + δ) y una capa de decisión y cumplimiento con probabilidad de excedencia r = Pr(D mayor que D límite). Las entradas incluyen ruido, datos faltantes, latencia, pérdida de paquetes, tiempo de anticipación, intensidad predicha, límites de incertidumbre y atributos del edificio. La inferencia se realiza por Monte Carlo con cadenas de Markov (muestreador sin vuelta en U) o por inferencia variacional, con diagnósticos de tamaño efectivo de muestra y R-sombrero, verificaciones predictivas posteriores, comparación de modelos por PSIS-LOOIC, WAIC y pesos de apilamiento y diagnósticos de endogeneidad con un instrumento. Los resultados se reportan para 162 casos; el texto no describe quién respondió, cómo se muestreó, qué edificios se inspeccionaron ni los indicadores de cada constructo.

**Resultados principales.** Las cargas posteriores promedio fueron de 0,70 a 0,80; la confiabilidad compuesta, de 0,83 (EWR) a 0,92 (SRP), y la varianza media extraída, de 0,51 a 0,65. Las razones HTMT de validez discriminante tuvieron medias de 0,53 a 0,63 con límites superiores de credibilidad menores o iguales a 0,72. La verificación predictiva posterior arrojó probabilidad de cola de 0,46, RMSE de residuos policóricos de 0,07, residuo máximo por ítem de 0,12 y proporción de indicadores con residuo mayor que 0,10 de 0,14. Los efectos estructurales estandarizados sobre SRP fueron 0,38 para RTAQ (IC 0,23-0,53), 0,31 para ACE, 0,21 para EWR y 0,19 para CSI, con Pr(β mayor que 0) de 0,971 a 0,999. El modelo completo, con estilo de respuesta y cargas cruzadas, tuvo PSIS-LOOIC de 4121,6, WAIC de 4124,0 y peso de apilamiento de 0,75, frente a 4215,3 del modelo nulo. Las correlaciones predictor-error estructural fueron cercanas a cero (0,04; 0,02; menos 0,05; 0,06) y el R2 condicional del instrumento fue de 0,16 para RTAQ y de 0,12 para CSI. Los efectos de la latencia, de la pérdida de paquetes y de la varianza de intensidad sobre la probabilidad de excedencia y la elección del modo de control se presentan como implicaciones del modelo, no como estimaciones empíricas, según los propios autores.

**Discusión y contribución.** Los autores concluyen que la mejora de resiliencia depende más de convertir las señales de sensado y alerta en inferencia confiable y control ejecutable dentro del margen de tiempo, que de la mera existencia de alerta temprana. Establecen una priorización para inversión en despliegue y modernización: primero la calidad de la analítica en tiempo real y la preparación del control adaptativo, luego la confiabilidad de la alerta y la integración de sensado. Comparan el marco con trabajos sobre alerta temprana, control semiactivo y modelos ordinales, y afirman que ninguno integra la cadena completa de sensado a cumplimiento. Incluyen una sección de factibilidad económica que sugiere umbrales de activación por costo esperado de falsos positivos y negativos, sin cuantificación.

**Limitaciones declaradas.** No se declaran limitaciones en una sección propia. Quedan implícitas: muestra de 162 casos sin descripción de origen; ausencia de datos reales de sensores, latencia o alertas; resultados de propagación de incertidumbre sin estimación empírica; instrumento no identificado; sin validación externa ni contraste con un caso real de edificio.

**Trabajo futuro.** Extensión a riesgos múltiples (incendio posterior al sismo), integración de optimización con aprendizaje automático (máquina de aprendizaje extremo con optimizador de lobo gris), mejora de descriptores de salud de sensores y cuantificación numérica de escenarios por modo de control.

**Palabras clave.** Declaradas: Adaptive structural control; Bayesian ordinal structural equation modeling; Compliance exceedance probability; Earthquake early warning; IoT sensing quality; Performance-based earthquake engineering | Inferidas: IoT, alerta temprana sísmica, ecuaciones estructurales bayesianas, indicadores ordinales, control adaptativo, ingeniería sísmica basada en desempeño, probabilidad de excedencia, calidad de sensado, resiliencia sísmica, incertidumbre

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** La resiliencia sísmica de edificios con IoT puede modelarse de forma conjunta mediante un modelo bayesiano ordinal que propaga la incertidumbre del sensado y de la alerta hasta el cumplimiento normativo, y los datos muestran que la calidad de la analítica en tiempo real y la preparación del control adaptativo son los factores con mayor efecto sobre el desempeño de resiliencia.

**Antítesis identificada.** El artículo no describe la muestra de 162 casos, los ítems de los constructos ni el instrumento usado para el diagnóstico de endogeneidad, lo que impide evaluar la validez y la reproducibilidad. Los constructos RTAQ, ACE y SRP se miden con percepciones de encuesta e inspección, de modo que el efecto estructural puede reflejar varianza de método común y no un efecto causal sobre desempeño estructural medido. El modelo de propagación de incertidumbre (ecuaciones 12 a 16) no se alimenta con datos de latencia, alertas ni respuesta de edificios: los autores afirman que esos resultados son implicaciones del modelo, de modo que la sección de incertidumbre y control carece de evidencia empírica. La literatura citada (unas 117 referencias) incluye estudios de túneles, vehículos conectados, tuberías y explosiones de gas sin relación directa con el argumento, lo que sugiere acumulación de citas y no fundamentación. La lectura causal de efectos estandarizados con R2 condicional del instrumento de 0,12 a 0,16 es débil.

**Síntesis propuesta.** El aporte defendible es una especificación de modelo y una lista de constructos y variables de entrada para un análisis de resiliencia con IoT, junto con evidencia de asociación entre percepciones de capacidad de analítica y de control y desempeño autorreportado. Debe leerse como propuesta metodológica con una demostración empírica de alcance limitado y no como evidencia de eficacia causal de los sistemas IoT o de alerta temprana. Para el corpus, la síntesis es aprovechar la estructura del modelo (calidad de datos, latencia, margen de anticipación y factibilidad de ejecución) para evaluar la viabilidad de tecnologías de alerta y monitoreo antes de invertir, y combinarla con datos observados de desempeño y de tiempo de cierre de empresas, de modo que los efectos se midan sobre continuidad productiva y no sobre percepciones.

**Áreas grises detectadas.**

1. Procedencia de los datos: los 162 casos se describen como encuestas e inspecciones, pero no se informa población, muestreo, país, tipo de edificio, instrumentos de medida, ítems por constructo ni tasa de respuesta, de modo que no se puede evaluar sesgo de selección ni validez de contenido.
2. Identificación causal: el diagnóstico de endogeneidad se apoya en un instrumento no descrito, con R2 condicional de 0,12 a 0,16 y correlaciones predictor-error cercanas a cero; no se justifican relevancia ni exclusión del instrumento, por lo que la afirmación de efectos causales no tiene respaldo suficiente.
3. Resultados de propagación de incertidumbre: las secciones sobre latencia, pérdida de paquetes, varianza de intensidad y modo de control describen direcciones esperadas y reconocen que no son estimaciones empíricas; no se reportan simulaciones ni valores de r, ni probabilidades por modo.
4. Relevancia de las referencias: una parte sustancial de las unas 117 referencias trata temas ajenos (túneles, tuberías, explosiones de gas, vehículos conectados, aguas residuales), por lo que no queda claro qué parte de la literatura sustenta cada decisión de modelado.

**Puntos oscuros aclarados.** Resulta llamativo que un modelo cuyo objeto es la propagación de incertidumbre de sensado y alerta hasta el cumplimiento normativo no use ningún dato de sensores, de alertas ni de desempeño estructural observado, y que los resultados cuantitativos se limiten a validez de medida y efectos entre constructos de percepción. Una explicación plausible es que obtener datos de latencia, alertas y respuesta de edificios con control activo es costoso y poco frecuente, de modo que los autores recurren a encuestas e inspecciones, las cuales sí pueden recolectarse en un número moderado de casos. Esta elección convierte el modelo en una medición de percepción de preparación, y el efecto de 0,38 de la calidad de analítica sobre el desempeño puede reflejar que los encuestados que valoran bien la analítica también valoran bien el desempeño. La falta de descripción de la muestra, la presencia de un estilo de respuesta que mejora el ajuste y la ausencia de una variable de desempeño medido sugieren varianza de método común. Por tanto, el hallazgo útil para decisión sería comprobar si estos constructos predicen resultados observados, como tiempos de inhabilitación o reapertura, y no su asociación entre sí.

**Ideas propositivas novedosas.**

1. Anclaje del constructo SRP a resultados observados: reemplazar o complementar el desempeño autorreportado con medidas observadas por edificio (tiempo de inhabilitación, costo de reparación, días de interrupción de actividades) tras eventos reales, y estimar con el mismo marco bayesiano ordinal si RTAQ y ACE predicen esos resultados. Fundamento: el artículo reconoce que los efectos de propagación no son empíricos y que SRP es latente. Verificabilidad: aplicación a edificios con registros de eventos recientes y comparación de la capacidad predictiva con un modelo de percepciones. Utilidad: separa el efecto de la capacidad de analítica del sesgo de percepción y ofrece un indicador para priorizar inversión en monitoreo.
2. Valor de la información de alerta ajustado por costo: acoplar la probabilidad de excedencia r con una función de costo de falsa alarma, de interrupción de actividades y de pérdida evitada, y estimar el punto de equilibrio de latencia y de confiabilidad de alerta que justifica el control adaptativo o el apagado preventivo de procesos. Fundamento: la sección 3.6 plantea el criterio de costo esperado sin cuantificarlo. Verificabilidad: simulación con parámetros de sistemas de alerta publicados y datos de costos de interrupción de industrias de una zona sísmica. Utilidad: ofrece a empresas y administradores de infraestructura una regla de decisión sobre cuándo actuar ante alertas inciertas.

**Relaciones poco exploradas.**

1. Margen de anticipación de la alerta temprana (condiciona) la factibilidad del control adaptativo: si la suma de latencia y tiempo de inferencia se acerca al tiempo de anticipación, la ventaja del control se anula, según la restricción de factibilidad planteada, aunque este vínculo no se estima con datos.
2. Calidad de sensado y comunicación (aumenta o reduce) la incertidumbre posterior de la probabilidad de excedencia, y esa incertidumbre (influye en) el cumplimiento de umbrales de desempeño; la relación se deriva de ecuaciones y no de observaciones.

**Robustez argumentativa:** 3.0/10 (ponderación 30/30/25/15) — consistencia lógica 4/10; calidad de la evidencia 3/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Ofrece una especificación probabilística explícita que une calidad de sensado, latencia, alerta, control y cumplimiento normativo, útil como lista de variables y de restricciones de factibilidad para evaluar tecnologías de monitoreo y alerta. Su valor para el corpus es metodológico y para el diseño de evaluación; es limitado como evidencia porque la muestra no se describe, las percepciones sustituyen el desempeño observado y la propagación de incertidumbre no se estima con datos.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Correlación y causalidad (Los efectos estandarizados entre constructos de percepción se interpretan como 'causal drivers' y 'mecanismo' (Sec. 3.2, p. 10; Sec. 3.5, p. 14)); Apelación a la cantidad (acumulación de citas) (Unas 117 referencias, muchas ajenas al tema, se invocan para 'justificar' el modelo (Sec. 1, pp. 3-4)); Petición de principio (Se concluye que la propagación de incertidumbre reduce la exceedencia con control adaptativo a partir de las propias ecuaciones, reconocidas como implicaciones del modelo (Sec. 3.3-3.5, pp. 11-12))
- **Bradford-Hill:** No se cumplen los criterios: la fuerza de asociación (0,19 a 0,38) proviene de percepciones transversales; faltan temporalidad, gradiente y experimento; la consistencia y la plausibilidad se invocan por teoría, no por replicación.
- **TRL asignado:** 3 — 'The framework is demonstrated on 162 cases' (p. 1)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (15 páginas más referencias). Las ecuaciones aparecen desordenadas en la extracción; las cifras de tablas se leyeron del texto y se contrastaron con el resumen y las conclusiones. La descripción de la muestra de 162 casos no aparece en el texto.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| La resiliencia sísmica de edificios con IoT puede modelarse de forma conjunta mediante un modelo bayesiano ordinal que propaga la incertidumbre del sensado y de la alerta hasta el cumplimiento normativo, y los datos muestran que la calidad de la analítica en tiempo real y la preparación del control adaptativo son los factores con mayor efecto sobre el desempeño de resiliencia.  | El artículo no describe la muestra de 162 casos, los ítems de los constructos ni el instrumento usado para el diagnóstico de endogeneidad, lo que impide evaluar la validez y la reproducibilidad. Los constructos RTAQ, ACE y SRP se miden con percepciones de encuesta e inspección, de modo que el efecto estructural puede reflejar varianza de método común y no un efecto causal sobre desempeño estructural medido. El modelo de propagación de incertidumbre (ecuaciones 12 a 16) no se alimenta con datos de latencia, alertas ni respuesta de edificios: los autores afirman que esos resultados son implicaciones del modelo, de modo que la sección de incertidumbre y control carece de evidencia empírica. La literatura citada (unas 117 referencias) incluye estudios de túneles, vehículos conectados, tuberías y explosiones de gas sin relación directa con el argumento, lo que sugiere acumulación de citas y no fundamentación. La lectura causal de efectos estandarizados con R2 condicional del instrumento de 0,12 a 0,16 es débil.  | El aporte defendible es una especificación de modelo y una lista de constructos y variables de entrada para un análisis de resiliencia con IoT, junto con evidencia de asociación entre percepciones de capacidad de analítica y de control y desempeño autorreportado. Debe leerse como propuesta metodológica con una demostración empírica de alcance limitado y no como evidencia de eficacia causal de los sistemas IoT o de alerta temprana. Para el corpus, la síntesis es aprovechar la estructura del modelo (calidad de datos, latencia, margen de anticipación y factibilidad de ejecución) para evaluar la viabilidad de tecnologías de alerta y monitoreo antes de invertir, y combinarla con datos observados de desempeño y de tiempo de cierre de empresas, de modo que los efectos se midan sobre continuidad productiva y no sobre percepciones.  | 3.0/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Resiliencia sísmica de edificios con IoT' se mide con cinco constructos latentes de percepción e inspección; 'cumplimiento relevante para la normativa' es la probabilidad de que la demanda supere un límite de desempeño.
- **P2 Supuestos:** Supone que las respuestas ordinales reflejan constructos latentes unidimensionales, que el instrumento usado para endogeneidad es válido y que las relaciones entre percepciones equivalen a efectos sobre desempeño real.
- **P3 Evidencia:** La evidencia son estimaciones bayesianas de 162 casos con buenos índices de medida y efectos de 0,19 a 0,38; la propagación de incertidumbre se deriva por ecuaciones.
- **P4 Consecuencias:** Si es cierto, conviene invertir primero en analítica en tiempo real y preparación del control antes que en más alertas; si es falso, se priorizaría una dimensión cuya asociación puede deberse a percepciones compartidas.
- **P5 Contraejemplos:** No se examinan casos en que edificios con alerta y analítica robusta no mejoraron su desempeño, ni modelos sin control activo con igual resiliencia, ni datos de falsas alarmas reales.
- **P6 Alternativas:** Alternativas: que la varianza de método común explique las asociaciones; que el tamaño del edificio o el presupuesto expliquen tanto la analítica como el desempeño; que la factibilidad temporal, no la calidad, sea la restricción dominante.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Tamaño de muestra | 162 | casos | Encuesta e inspección; sin descripción de origen | Tabla 1, p. 5 | Tabla | Media | Procedencia no especificada |
| Carga posterior promedio por constructo | 0,70 a 0,80 | adimensional | EWR 0,70; SRP 0,80 | Tabla 1, p. 5 | Tabla | Alta | Escala estandarizada |
| Confiabilidad compuesta | 0,83 a 0,92 | adimensional | Mínima en EWR, máxima en SRP | Tabla 1, p. 5 | Tabla | Alta | Intervalos de credibilidad de 95 % |
| Varianza media extraída | 0,51 a 0,65 | adimensional | Todas mayores que 0,50 | Tabla 1, p. 5 | Tabla | Alta | Validez convergente |
| HTMT posterior | 0,53 a 0,63 | adimensional | Límites superiores no mayores que 0,72 | Tabla 2, p. 6 | Tabla | Alta | Validez discriminante |
| Efecto RTAQ sobre SRP | 0,38 | efecto estandarizado | IC 95 % 0,23-0,53; Pr(β>0)=0,998 | Tabla 3, p. 6 | Tabla | Alta | Mayor efecto directo |
| Efecto ACE sobre SRP | 0,31 | efecto estandarizado | IC 95 % 0,18-0,45; Pr(β>0)=0,999 | Tabla 3, p. 6 | Tabla | Alta | Segundo efecto |
| Efectos EWR y CSI sobre SRP | 0,21 / 0,19 | efecto estandarizado | Pr(β>0)=0,982 y 0,971 | Tabla 3, p. 6 | Tabla | Alta | Efectos menores |
| PSIS-LOOIC del modelo completo | 4121,6 | índice | Modelo nulo 4215,3; peso de apilamiento 0,75 | Tabla 5, p. 11 | Tabla | Alta | Modelo con estilo de respuesta y cargas cruzadas |
| Probabilidad de cola predictiva posterior | 0,46 | probabilidad | RMSE de residuos policóricos 0,07 | Tabla 4, p. 9 | Tabla | Alta | Ajuste de la capa ordinal |
| R2 condicional del instrumento | 0,16 / 0,12 | adimensional | Sobre RTAQ y CSI | Tabla 6, p. 11 | Tabla | Media | Instrumento no descrito |
| Mercado de IoT en construcción | 16 | miles de millones USD | Proyectado a 2024 con CAGR de 26,0 % | Sec. 1, p. 2 | Texto | Baja | Cita externa sin fuente primaria en el texto |
| Reducción de costos de construcción atribuida a IoT | 20 a 25 | % | Proyección citada | Sec. 1, p. 2 | Texto | Baja | Cita externa |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'The framework is demonstrated on 162 cases' (p. 1) | Marco analítico con demostración estadística sobre datos de percepción; sin prototipo físico ni datos de campo de sensores o alertas. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'The proposed framework offers a decision grade basis for prioritizing interventions' (p. 15) | Sin evidencia de mercado, usuario pagador ni modelo de negocio; solo discusión cualitativa de costo de falsas alarmas. |
| IRL | 2 | Sí | 'This statement is a theoretical implication of the specified channels... rather than a separate empirical estimate' (p. 11) | La integración entre sensado, alerta y control se plantea en ecuaciones; sin implementación ni datos reales de integración. |
| DRL | 2 | Sí | 'the effects of IoT based sensing and warning systems on building performance have not been thoroughly validated' (p. 2) | Necesidad argumentada con literatura y cifras de mercado externas; sin estudio de demanda propio. |
| SRL | 1.0 | Sí | Componentes: Modelo estructural latente BOSEM (TRL 3), Capa de decisión y cumplimiento (control adaptativo) (TRL 2) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 5.0; ÷9 → 0.56; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 3 con BRL 1 e IRL 2: especificación estadística sin datos operativos de sensores ni modelo de negocio. · Estrategia de salida: Aplicar el modelo a edificios con datos reales de latencia, alertas y respuesta, y cuantificar el costo y beneficio por modo de control.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Correlación y causalidad | Los efectos estandarizados entre constructos de percepción se interpretan como 'causal drivers' y 'mecanismo' (Sec. 3.2, p. 10; Sec. 3.5, p. 14) | Afirmación causal sin diseño ni identificación suficientes |
| Apelación a la cantidad (acumulación de citas) | Unas 117 referencias, muchas ajenas al tema, se invocan para 'justificar' el modelo (Sec. 1, pp. 3-4) | Sustituye la fundamentación específica por volumen |
| Petición de principio | Se concluye que la propagación de incertidumbre reduce la exceedencia con control adaptativo a partir de las propias ecuaciones, reconocidas como implicaciones del modelo (Sec. 3.3-3.5, pp. 11-12) | Los resultados repiten los supuestos de especificación |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Calidad de analítica en tiempo real → desempeño de resiliencia sísmica | Efecto estandarizado 0,38 (IC 0,23-0,53) sobre 162 casos | Fuerza de asociación, plausibilidad | Temporalidad, experimento, consistencia con datos observados | Varianza de método común, tamaño del edificio, presupuesto | 3 | Correlacional |
| Latencia y pérdida de paquetes → incertidumbre del cumplimiento normativo | Derivación por ecuaciones; sin estimación empírica | Plausibilidad teórica | Todos los demás criterios | Tiempo de anticipación, tipo de edificio | 1 | Hipótesis no probada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Descripción, representatividad y reproducibilidad de la muestra de 162 casos y de los instrumentos | Crítico | Alta | 9 |
| Tecnológico | Datos reales de latencia, alertas y respuesta de edificios con control adaptativo para alimentar la propagación de incertidumbre | Crítico | Media | 8 |
| Conocimiento | Relación entre constructos de preparación y resultados observados (tiempos de inhabilitación, costos) | Significativo | Media | 8 |
| Mercado | Cuantificación del costo de falsas alarmas y del valor de la información de alerta por tipo de ocupación | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Marco de modelación ordinal bayesiano de resiliencia con entradas IoT | Diagrama | Entradas IoT y de alerta, constructos latentes y salidas de decisión | 5 constructos | Alta |
| Fig. 2 | Cargas posteriores, confiabilidad compuesta y AVE por constructo | Gráfico | Calidad de medida de RTAQ, EWR, ACE, CSI y SRP | 0,70-0,80; 0,83-0,92; 0,51-0,65 | Alta |
| Fig. 3 | Probabilidades posteriores por categoría ordinal para EWR, ACE y CSI | Gráfico | Perfiles de respuesta por categoría | No tabulados | Media |
| Fig. 4 | Resumen posterior de coeficientes de los predictores de SRP | Gráfico | Medias, desviaciones y Pr(β>0) | 0,38; 0,31; 0,21; 0,19 | Alta |
| Fig. 5 | Comparación de modelos por PSIS-LOOIC y WAIC | Gráfico | Modelo completo con menor criterio | 4121,6; 4124,0 | Alta |
| Fig. 6 | Correlaciones del error estructural y R2 condicional del instrumento | Gráfico | Diagnóstico de endogeneidad | 0,04; 0,02; -0,05; 0,06 | Media |
| Tabla 5 | Comparación bayesiana de modelos | Tabla | Nulo, estilo de respuesta, cargas cruzadas y completo | 4215,3; 4158,7; 4121,6 | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Abdalzaher et al. (aprendizaje automático e IoT para alerta temprana en ciudades inteligentes) | No especificado en documento | Academia | Revisión de arquitectura y algoritmos de EEW con IoT | Síntesis de tuberías de alerta | Sin modelo latente ni cumplimiento normativo | Creciendo |
| Allen et al. (detección global con Android) | No especificado en documento | Industria/Academia | Alerta sísmica a gran escala con teléfonos inteligentes | Cobertura global y años de operación | Sin control en edificios | Creciendo |
| Cheng et al. (alerta temprana aplicada a edificios) | No especificado en documento | Academia | Aplicación de alerta temprana a edificios | Vínculo alerta-edificio | Antigüedad (2014); sin modelo ordinal | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Desempeño de resiliencia sísmica (SRP), constructo latente ordinal
- **X:** Calidad de analítica en tiempo real (RTAQ), efectividad del control adaptativo (ACE), confiabilidad de la alerta (EWR), integración de sensado y comunicación (CSI)
- **Z (controles):** Tipología, altura y periodo del edificio, sistema de aislamiento, ocupación e importancia (descritos, sin valores)
- **Datos:** 162 casos de encuesta e inspección; origen y periodo no especificados
- **Método:** Ecuaciones estructurales bayesianas ordinales; Monte Carlo con cadenas de Markov; verificaciones predictivas posteriores; PSIS-LOOIC y WAIC
- **Efecto reportado:** Efectos estandarizados de 0,19 a 0,38 con Pr(β>0) de 0,971 a 0,999
- **Endogeneidad tratada:** Sí - se discute con correlaciones predictor-error cercanas a cero
- **Instrumento:** Instrumento no identificado; R2 condicional de 0,16 (RTAQ) y 0,12 (CSI)
- **Robustez reportada:** Comparación de cuatro especificaciones; sin pruebas de sensibilidad a priors ni validación externa

| Vacío | Tipo | Descripción |
|---|---|---|
| V-015-01 | TERR | País, región y tipo de edificio de la muestra no especificados; sin evidencia en América Latina andina |
| V-015-02 | POBL | Población de encuestados e inspectores no descrita; sin empresas ni usuarios del edificio |
| V-015-03 | TEMP | Sin dimensión temporal de eventos, de recuperación ni de degradación; análisis transversal |
| V-015-04 | MET | Ítems, instrumento de endogeneidad y muestreo no descritos; sin validación externa |
| V-015-05 | VAR | Faltan variables observadas de desempeño (tiempo de inhabilitación, costos) y datos reales de latencia y alertas |
| V-015-06 | TEOR | No se vincula con teoría de resiliencia organizacional ni de recuperación económica |
| V-015-07 | CAUS | Efectos entre percepciones interpretados como causales sin diseño de identificación convincente |
