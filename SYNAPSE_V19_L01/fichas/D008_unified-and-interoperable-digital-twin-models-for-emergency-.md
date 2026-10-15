# FB-L01-008 | D008 — Unified and interoperable digital twin models for emergency evacuation using building simulation identity cards

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S0926580525002651-main.pdf` · 23 páginas · Relevancia para el eje del corpus: **Núcleo** (Combina gemelo digital, cosimulación estructural sísmica y evacuación de ocupantes; aunque no trata la recuperación empresarial, formaliza la interoperabilidad entre modelos que alimentarían un gemelo de continuidad operativa.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-008 / D008
- **Tipo de recurso:** Artículo científico (journal peer-reviewed)
- **Referencia APA 7:** Jahangir, M. F., Kamari, A., & Schultz, C. P. L. (2025). Unified and interoperable digital twin models for emergency evacuation using building simulation identity cards. *Automation in Construction*, *175*, Article 106225. https://doi.org/10.1016/j.autcon.2025.106225
- **Autores:** Jahangir, Muhammad Farhan (58968779900); Kamari, Aliakbar (57200725524); Schultz, Carl Peter Leslie (17435671800)
- **Afiliaciones:** DIGIT, Department of Civil and Architectural Engineering, Aarhus University, Denmark; DIGIT, Department of Software Engineering & Computing, Aarhus University, Denmark
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Automation in Construction · vol. 175
- **Identificador persistente:** DOI 10.1016/j.autcon.2025.106225 · ISSN 09265805
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105003670842&doi=10.1016%2fj.autcon.2025.106225&partnerID=40&md5=01e24ee8c8f9dcb15949703936b4a6e2
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 5

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Proponer y aplicar la Ficha de Identidad de Simulación de Edificios (Building Simulation Identity Card, BSIC), un marco para estandarizar, caracterizar e integrar las propiedades de los modelos de simulación usados en gemelos digitales de edificios, con el fin de mejorar la trazabilidad, la fiabilidad y la interoperabilidad entre modelos de dominios distintos. La aplicación se centra en una evacuación inducida por un sismo en un edificio de oficinas de varios pisos, donde la falla estructural (evento discreto) debe sincronizarse con el movimiento continuo de los ocupantes, y se busca documentar atributos que reduzcan errores de integración.

**Pregunta de investigación.** ¿Con qué eficacia un marco para unidades de simulación de edificios facilita la integración novedosa de modelos de simulación y mejora la comunicación entre ellos en un proceso de cosimulación?

**Marco teórico.** El marco combina la teoría de gemelos digitales en arquitectura, ingeniería, construcción y operación (AECO) con la cosimulación como técnica de acoplamiento de simuladores especializados y con los estándares de interoperabilidad de otras industrias: Functional Mock-up Interface (FMI), System Structure and Parameterization (SSP), Model Identity Card (MIC) de la industria automotriz y aeroespacial, Simulation Model Portability (SMP) de la Agencia Espacial Europea, MoSSEC (ISO 10303-243) y High-Level Architecture (HLA). Formaliza la interacción con el formalismo de eventos discretos (DEVS) para el simulador de eventos y con representación de estado en tiempo continuo, y plantea el algoritmo maestro de Jacobi y un motor de orquestación de cosimulación. Es un paradigma de ingeniería con validación por caso, que enfatiza factores humanos como rasgo distintivo de la industria de edificios.

**Metodología.** El estudio sigue tres fases: revisión de literatura (consulta en Web of Science sobre cosimulación en edificios, evacuación, análisis sísmico, interoperabilidad y simulación basada en BIM), desarrollo del marco BSIC con atributos organizados en siete categorías (información general, integración e interoperabilidad, configuración del edificio, comportamiento, resultados, variables internas y hardware de referencia) y caso de estudio. El caso es un edificio de oficinas de cinco pisos en Islamabad (Pakistán), terminado en 2018, con capacidad para 170 personas y estructura de concreto reforzado. El análisis estructural usa ETABS con el registro del terremoto de Loma Prieta de 1989 (base de datos PEER) y comprobaciones con el código de edificación de Pakistán (factores de reducción de 0,75 para cortante y 0,90 para flexión); la evacuación usa Pathfinder, un simulador basado en agentes, con datos de ocupación de recursos humanos, velocidades diferenciadas por categoría (hombres, mujeres, adultos mayores, personas en silla de ruedas) y siete configuraciones de salidas evaluadas con 170 y 82 ocupantes. La transferencia de datos de ETABS a Pathfinder se realizó manualmente, y se propone, como integración teórica futura, el marco INTO-CPS con FMI. No hay validación experimental ni medición de errores de integración.

**Resultados principales.** El análisis estructural indica un periodo fundamental de 0,96 s y, a los 14 s del registro sísmico, una viga sobre la puerta trasera excede su capacidad de diseño: cortante actual de 88,45 kN frente a 83,18 kN admisibles, momento de 313,68 kN·m frente a 308,36 kN·m y deflexión de 14,22 mm frente a 10,16 mm (L/240). Los excesos calculados por el analista son 6,3 % en cortante, 1,7 % en momento y 40 % en deflexión. El evento se traduce en el cierre de la puerta trasera a los 14 s en la simulación de evacuación. Con 170 ocupantes, la evacuación por las puertas principales toma 216,4 s; con salidas de emergencia y ascensor, 187,7 s; con escaleras bloqueadas a 9 m, 228,3 s; incluyendo la puerta trasera, 232,1 s, que sube a 234,9 s al cerrarla a los 14 s; solo salida de emergencia, 259,6 s; y puertas normales más ascensor, 375,9 s. Con 82 ocupantes los tiempos son 104,8; 94; 110,6; 105,5; 129,1; 110,5 y 161,2 s. Los autores informan que la cosimulación combinada de ETABS y Pathfinder tardó entre 97,4 y 118,3 s según el escenario. Concluyen que el BSIC permite alinear eventos discretos y tiempo continuo, sincronizar flujos de datos y reducir errores de integración.

**Discusión y contribución.** Los autores sostienen que el BSIC estandariza intercambios de datos, sincroniza pasos de tiempo y asegura la propagación de eventos entre modelos, con ventajas de trazabilidad y de colaboración interdisciplinaria, y que la cosimulación es escalable porque el caso se resolvió en minutos. Distinguen el sector de edificios de otros por su larga vida útil, su carga de factores humanos, la ausencia de sensores en muchos edificios y la diversidad de funciones. Reconocen limitaciones: complejidad de implementar el marco en diversas herramientas, dependencia de formatos estándar como IFC y XML, integración manual de datos en el caso, y necesidad de probar en más casos y tipos de edificio. Anticipan trabajo futuro en modelado dinámico de datos en un gemelo digital integrado con BIM, retroalimentación de componentes no estructurales y vínculos con IFC, IDS y bSDD.

**Limitaciones declaradas.** Declaradas: complejidad de implementar el BSIC en distintas herramientas, dependencia de formatos IFC y XML, integración manual de datos y necesidad de más casos de estudio para demostrar escalabilidad en distintos tipos de edificios.

**Trabajo futuro.** Extender el modelado dinámico de datos dentro de un gemelo digital integrado con BIM a edificios de gran escala, incorporar retroalimentación de componentes no estructurales, conectar el BSIC con IFC, IDS y bSDD, y estudiar el efecto en el tiempo de ejecución de dependencias cíclicas entre simuladores.

**Palabras clave.** Declaradas: BIM-based DT; Building information modelling (BIM); Co-simulation; Digital twin (DT); Model identity card (MIC) | Inferidas: gemelo digital basado en BIM, cosimulación, eventos discretos, tiempo continuo, ficha de identidad de modelo, interoperabilidad, ETABS, Pathfinder, evacuación por sismo, FMI

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Una ficha estándar de identidad de modelos de simulación (BSIC) permite sincronizar simulaciones estructurales de eventos discretos con simulaciones de evacuación en tiempo continuo, mejorando la interoperabilidad, la trazabilidad y la fiabilidad de los gemelos digitales de edificios.

**Antítesis identificada.** La eficacia del BSIC no se mide: el caso transfiere los datos a mano entre ETABS y Pathfinder, no se cuantifica ningún error de integración antes y después, y no existe comparación con un enfoque base ni con estándares como FMI aplicados al mismo problema. La 'falla' que dispara el evento a los 14 s es un exceso del 1,7 % en momento y del 6,3 % en cortante respecto de la capacidad de diseño con factores de reducción, no un colapso demostrado, de modo que el cierre de la puerta es una hipótesis del modelador. La afirmación de escalabilidad se apoya en el tiempo de cómputo de un edificio de cinco pisos con dos simuladores (97,4 a 118,3 s), cifra que no caracteriza el costo de acoplar modelos más complejos ni realimentaciones cíclicas, y que además se obtuvo en un procedimiento manual. El marco documenta atributos pero no valida su suficiencia, y la evacuación se modela con parámetros genéricos sin calibración con ejercicios reales.

**Síntesis propuesta.** El artículo ofrece una taxonomía útil de atributos para describir modelos de simulación acoplables y un ejemplo ilustrativo sísmico, pero no demuestra mejoras cuantitativas. La síntesis es adoptar el BSIC como lista de verificación de interoperabilidad y no como evidencia de reducción de errores, y exigir en trabajos posteriores medir la diferencia de resultados con integración manual y automatizada, con desenlaces de seguridad. Para el eje del corpus, el aporte es el patrón de acoplar un simulador de daño estructural con un simulador de comportamiento humano, extensible a la recuperación funcional de edificios, siempre que se añadan incertidumbre en los eventos y variables económicas de uso del espacio.

**Áreas grises detectadas.**

1. Ausencia de medición de eficacia: la afirmación del resumen de 'minimized integration errors' no se acompaña de una métrica de error, una línea base manual frente a automática ni una comparación con FMI/INTO-CPS; la integración del caso es manual por reconocimiento de los propios autores.
2. Definición del evento de falla: se toma como falla de viga el exceso de la capacidad de diseño (con factor de reducción de 0,75 y 0,90) por 6,3 % en cortante y 1,7 % en momento, y se asume cierre inmediato de la puerta a los 14 s; no se discute la incertidumbre del modelo ni la diferencia entre exceder la capacidad de diseño y colapsar.
3. Escalabilidad inferida de un solo caso: 'between 97.4 s and 118.3 s' se presenta como evidencia de que la cosimulación escala, pero depende de dos simuladores y un edificio de cinco pisos; el propio texto reconoce que los ciclos de realimentación entre simuladores no se evaluaron.
4. Consistencia de normativas: el análisis aplica el Código de Edificación de Pakistán con el registro de Loma Prieta (California) sin justificar la compatibilidad del movimiento con el peligro local, lo que afecta la interpretación de los tiempos de falla.

**Puntos oscuros aclarados.** Resulta llamativo que el cierre de la puerta trasera a los 14 s aumente en solo 2,8 s el tiempo de evacuación con 170 personas (232,1 a 234,9 s) pero en 23,6 s con 82 personas (105,5 a 129,1 s). La explicación probable es que, con ocupación alta, la salida trasera es poco usada o está saturada, de modo que el cierre redistribuye poco flujo, mientras que con ocupación baja la distribución espacial de los ocupantes concentra a más personas cerca de la puerta cerrada. Esto sugiere que el resultado depende de la distribución inicial de ocupantes y no solo del número, un factor que el artículo no analiza. De igual modo, que los escenarios con ascensor sean los más largos (375,9 s) indica que se modeló la espera en ascensor como evacuación ordinaria; en sismos reales el ascensor se excluye, de modo que ese escenario no aporta información útil y conviene descartarlo del análisis comparativo.

**Ideas propositivas novedosas.**

1. Cosimulación de recuperación funcional: añadir al BSIC un atributo de 'función económica del espacio' y acoplar un tercer simulador que, a partir del estado de daño estructural y de servicios, estime el tiempo de reocupación y la interrupción de actividades de las empresas alojadas. Fundamento: el artículo ya acopla daño estructural y comportamiento humano mediante atributos de eventos; agregar un simulador de continuidad operativa reutiliza el mismo mecanismo. Verificabilidad: aplicar el marco a un edificio con inquilinos conocidos y comparar el tiempo de reocupación simulado con el observado tras un sismo. Utilidad: conecta la ingeniería de edificios con la recuperación productiva y permite priorizar reforzamientos.
2. Disparadores estocásticos de eventos discretos: reemplazar el umbral determinista de falla por funciones de fragilidad y muestrear el instante y la ubicación de la falla, ejecutando miles de cosimulaciones para obtener la distribución del tiempo de evacuación y la probabilidad de bloqueo de salidas. Fundamento: la falla del caso es un exceso marginal de capacidad, por lo que la decisión de bloquear la puerta es incierta. Verificabilidad: simulación de Monte Carlo con los mismos modelos y comparación de la distribución con el escenario determinista. Utilidad: ofrece planes de evacuación robustos y cuantifica el riesgo residual.

**Relaciones poco exploradas.**

1. Distribución espacial inicial de los ocupantes (modula) el costo en tiempo de cerrar una salida: el efecto de 2,8 s con 170 personas frente a 23,6 s con 82 sugiere interacción entre ocupación y geometría que merece experimentos paramétricos.
2. Dependencias cíclicas entre simuladores (aumentan) el tiempo de ejecución y exigen pausas y reconfiguraciones: el artículo lo señala como tema futuro y es clave para escalar a edificios con carga de ocupantes que afecte a la estructura.

**Robustez argumentativa:** 4.2/10 (ponderación 30/30/25/15) — consistencia lógica 6/10; calidad de la evidencia 4/10; validez de inferencias causales 3/10; generalizabilidad 3/10.

**Valor estratégico:** 6/10 — Aporta una estructura reutilizable para documentar modelos y sincronizar eventos discretos con procesos continuos, directamente aplicable a gemelos digitales de edificios en zonas sísmicas, y proporciona datos numéricos transparentes de un caso. Su valor estratégico se limita por la falta de validación cuantitativa de la mejora, pero sirve como base para diseñar gemelos que incluyan continuidad operativa.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Petición de principio (Se concluye que el BSIC 'minimiza errores de integración' sin medir errores y con integración manual (Resumen y Sec. 6)); Generalización apresurada (Escalabilidad inferida de un edificio de cinco pisos y dos simuladores (Sec. 6.2.4, p. 18)); Equivocación (falla de código frente a colapso) (Exceso de 1,7 % y 6,3 % sobre capacidad de diseño se trata como falla que cierra la puerta (Sec. 5.1, p. 10))
- **Bradford-Hill:** La relación daño estructural → bloqueo de puerta → mayor tiempo de evacuación es plausible y coherente en el modelo, pero no hay evidencia experimental ni replicación; la causalidad es de simulación.
- **TRL asignado:** 4 — 'This case study demonstrates manual co-simulation process, future adoption of INTO-CPS will enable automated synchronization' (p. 13)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído; las ecuaciones aparecen fragmentadas, pero tablas y resultados numéricos son legibles. Apéndices A y B referenciados no están completos en el PDF extraído (tiempos detallados se toman del texto principal).

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Una ficha estándar de identidad de modelos de simulación (BSIC) permite sincronizar simulaciones estructurales de eventos discretos con simulaciones de evacuación en tiempo continuo, mejorando la interoperabilidad, la trazabilidad y la fiabilidad de los gemelos digitales de edificios.  | La eficacia del BSIC no se mide: el caso transfiere los datos a mano entre ETABS y Pathfinder, no se cuantifica ningún error de integración antes y después, y no existe comparación con un enfoque base ni con estándares como FMI aplicados al mismo problema. La 'falla' que dispara el evento a los 14 s es un exceso del 1,7 % en momento y del 6,3 % en cortante respecto de la capacidad de diseño con factores de reducción, no un colapso demostrado, de modo que el cierre de la puerta es una hipótesis del modelador. La afirmación de escalabilidad se apoya en el tiempo de cómputo de un edificio de cinco pisos con dos simuladores (97,4 a 118,3 s), cifra que no caracteriza el costo de acoplar modelos más complejos ni realimentaciones cíclicas, y que además se obtuvo en un procedimiento manual. El marco documenta atributos pero no valida su suficiencia, y la evacuación se modela con parámetros genéricos sin calibración con ejercicios reales.  | El artículo ofrece una taxonomía útil de atributos para describir modelos de simulación acoplables y un ejemplo ilustrativo sísmico, pero no demuestra mejoras cuantitativas. La síntesis es adoptar el BSIC como lista de verificación de interoperabilidad y no como evidencia de reducción de errores, y exigir en trabajos posteriores medir la diferencia de resultados con integración manual y automatizada, con desenlaces de seguridad. Para el eje del corpus, el aporte es el patrón de acoplar un simulador de daño estructural con un simulador de comportamiento humano, extensible a la recuperación funcional de edificios, siempre que se añadan incertidumbre en los eventos y variables económicas de uso del espacio.  | 4.2/10 |

### B.2 Interrogación socrática

- **P1 Definición:** BSIC es una ficha estándar con atributos de un modelo de simulación; 'cosimulación' es la ejecución coordinada de simuladores separados; 'falla' es el exceso de capacidad de diseño de una viga.
- **P2 Supuestos:** Supone que la documentación de atributos reduce errores de integración, que el exceso marginal de capacidad equivale a cierre de puerta y que un solo edificio ilustra la escalabilidad.
- **P3 Evidencia:** La evidencia es numérica y de un solo caso: tablas de verificación de la viga y tiempos de evacuación; no hay medida de errores de integración ni validación empírica.
- **P4 Consecuencias:** Si es cierto, las organizaciones pueden construir gemelos de edificios con modelos intercambiables; si es falso, el marco aumentaría la carga documental sin mejorar la fiabilidad.
- **P5 Contraejemplos:** Casos con realimentación entre ocupantes y estructura, edificios con sistemas no estructurales críticos, o evacuaciones en las que el comportamiento real difiera del modelo, no se examinan.
- **P6 Alternativas:** Alternativas: aplicar FMI y SSP sin una ficha específica; usar herramientas integradas de simulación sísmica y de evacuación; validar con ejercicios de evacuación.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Edificio del caso | 5 | pisos | Oficinas en Islamabad, Pakistán | Sec. 5, p. 10 | Texto | Alta | Un solo edificio |
| Capacidad de ocupantes | 170 | personas | Plena ocupación | Sec. 5, p. 10 | Texto | Alta | Datos del área de recursos humanos |
| Ocupación en días festivos | 82 | personas | Escenario parcial | Sec. 5.2, p. 13 | Texto | Alta | Sin calibración con ejercicios reales |
| Periodo fundamental | 0.96 | s | Análisis estructural en ETABS | Sec. 5.1, p. 10 | Texto | Alta | Modelo sin validación |
| Instante de falla de la viga | 14 | s | Registro de Loma Prieta 1989 | Sec. 5.1, p. 10 | Texto | Alta | Exceso marginal sobre capacidad de diseño |
| Cortante actual frente a admisible | 88.45 / 83.18 | kN | Viga sobre la puerta trasera | Tabla 2, p. 12 | Tabla | Alta | Exceso de 6,3 % (cálculo del analista) |
| Momento actual frente a admisible | 313.68 / 308.36 | kN·m | Viga sobre la puerta trasera | Tabla 2, p. 12 | Tabla | Alta | Exceso de 1,7 % (cálculo del analista) |
| Deflexión actual frente a admisible | 14.22 / 10.16 | mm | Criterio L/240 | Tabla 2, p. 12 | Tabla | Alta | Exceso de 40 % (cálculo del analista) |
| Tiempo de evacuación normal (170 personas) | 216.4 | s | Puertas principales | Sec. 5.2, p. 13 | Texto | Alta | Una sola corrida determinista |
| Tiempo con salidas de emergencia y ascensor (170) | 187.7 | s | Mejor escenario con 170 personas | Sec. 5.2, p. 13 | Texto | Media | Incluye ascensor, inapropiado en sismo |
| Tiempo con puerta trasera cerrada a los 14 s (170) | 234.9 | s | Evento del caso | Sec. 5.2, p. 13 | Texto | Alta | Aumento de 2,8 s frente a 232,1 s (cálculo del analista) |
| Tiempo con puerta trasera cerrada a los 14 s (82) | 129.1 | s | Evento del caso | Sec. 5.2, p. 13 | Texto | Alta | Aumento de 23,6 s frente a 105,5 s (cálculo del analista) |
| Mayor tiempo de evacuación (170) | 375.9 | s | Puertas normales más ascensor | Sec. 5.2, p. 13 | Texto | Media | Escenario no realista en sismo |
| Tiempo de cosimulación ETABS-Pathfinder | 97.4-118.3 | s | Según escenario, evidencia de escalabilidad | Sec. 6.2.4, p. 18 | Texto | Media | Dos simuladores y un edificio; integración manual |
| Categorías de atributos BSIC | 7 | categorías | Información general, integración, configuración, comportamiento, resultados, variables internas, hardware | Fig. 16, p. 16 | Figura | Alta | Suficiencia no validada |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'This case study demonstrates manual co-simulation process, future adoption of INTO-CPS will enable automated synchronization' (p. 13) | Marco validado en laboratorio computacional con un caso y transferencia manual de datos (TRL 4). |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'One limitation of this work is the complexity involved in implementing the BSIC framework across diverse tools' (p. 19) | Idea conceptual sin análisis de mercado, usuarios ni modelo de negocio. |
| IRL | 3 | Sí | 'BSIC's dependence on manual data integration, as evidenced in case studies, limits its effectiveness' (p. 19) | Compatibilidad entre simuladores establecida conceptualmente con atributos, pero sin integración automática; interfaces manuales. |
| DRL | N/A | No | No aplica |  |
| SRL | 2.11 | Sí | Componentes: ETABS (análisis estructural) (TRL 9), Pathfinder (evacuación) (TRL 9), Marco BSIC (TRL 4) | SRL=Σ(TRLi×IRLij)/6 términos ordenados = 19.0; ÷9 → 2.11; nivel acotado a [1,9] = 2.11 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | N/A | N/A |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V4 Componentes sin integración · Severidad: Media · Componentes comerciales maduros (ETABS, Pathfinder) con IRL bajo por integración manual: riesgo de falla en el ensamblaje automatizado. · Estrategia de salida: Implementar la integración automática con FMI/INTO-CPS, medir errores frente a la integración manual y validar con ejercicios de evacuación reales.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Petición de principio | Se concluye que el BSIC 'minimiza errores de integración' sin medir errores y con integración manual (Resumen y Sec. 6) | La eficacia no se demuestra |
| Generalización apresurada | Escalabilidad inferida de un edificio de cinco pisos y dos simuladores (Sec. 6.2.4, p. 18) | Limita la validez externa |
| Equivocación (falla de código frente a colapso) | Exceso de 1,7 % y 6,3 % sobre capacidad de diseño se trata como falla que cierra la puerta (Sec. 5.1, p. 10) | Sobreestima la gravedad y el efecto en la evacuación |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Cierre de puerta trasera → mayor tiempo de evacuación | Aumentos de 2,8 s (170) y 23,6 s (82) en Pathfinder | Plausibilidad, temporalidad, coherencia | Experimento real, consistencia entre ocupaciones | Distribución de ocupantes, geometría de salidas | 5 | Causal (simulada) |
| Uso del BSIC → menor error de integración | Afirmación sin medición | Ninguno demostrado | Fuerza, temporalidad, experimento, consistencia | Integración manual, selección de caso | 2 | Hipótesis no probada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Medición de errores de integración con y sin BSIC y con FMI/INTO-CPS en el mismo caso | Crítico | Alta | 9 |
| Tecnológico | Automatización de la cosimulación entre simuladores estructurales y de evacuación | Significativo | Media | 7 |
| Conocimiento | Incertidumbre de los disparadores de falla y su efecto en la evacuación | Significativo | Alta | 8 |
| Mercado | Adopción del BSIC por firmas de ingeniería y su costo de implementación | Moderado | Baja | 4 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Overview of research structure | Diagrama | Fases de revisión, desarrollo y caso | No aplica | Baja |
| Fig. 2 | Integration of physical building and digital model with BSIC | Diagrama | Sensores, modelo digital y coordinador de simulaciones | No aplica | Media |
| Fig. 3 | System architecture of DT development in buildings | Diagrama | Capas de adquisición, transmisión, modelado, integración y servicio | Cinco capas | Media |
| Fig. 5 | Sequence diagram for co-simulation process | Diagrama | Interacciones COE-FMU en la evacuación | Hito t = 14 s | Alta |
| Fig. 10 | ETABS structural model (3D) | Esquema | Modelo estructural del edificio | No aplica | Media |
| Fig. 14 | Contours representing the time required to exit the building | Gráfico | Tiempos de salida de 50 a 450 s | Rango 50-450 s | Media |
| Fig. 16 | Attributes of BSIC | Diagrama | Siete categorías de atributos | 7 categorías | Alta |
| Tabla 2 | Comparison of allowable and actual shear, moment and deflection | Tabla | Capacidad frente a demanda en la viga | 83,18 vs 88,45 kN; 308,36 vs 313,68 kN·m; 10,16 vs 14,22 mm | Alta |
| Tabla 3 | Evacuation characteristics of building occupants | Tabla | Categorías, edades, velocidades (0,48 a 1,5 m/s) | 170 ocupantes | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| FMI / INTO-CPS | Europa | Estándar / proyecto | Intercambio de modelos y cosimulación | Estándar abierto y maduro | Difícil sincronización de eventos con relojes distintos | Creciendo |
| HLA (High-Level Architecture) | Estados Unidos | Estándar | Simulación distribuida con RTI | Sincronización de pasos de tiempo | Complejidad de integración | Estable |
| SSP y MIC | Europa | Estándar | Estructura de sistemas y tarjeta de modelos | Modularidad y trazabilidad | Madurez y consenso de vocabulario | Creciendo |
| Pathfinder, ETABS (herramientas comerciales) | Estados Unidos | Empresa | Evacuación basada en agentes; análisis estructural | Uso extendido | Cajas negras y formatos propietarios | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** Tiempo de evacuación (s) y estado de la viga (cumple/no cumple)
- **X:** Escenario de salidas (puertas principales, emergencia, ascensor, puerta trasera cerrada); número de ocupantes
- **Z (controles):** Parámetros de velocidad y respuesta por categoría; propiedades estructurales
- **Datos:** Simulación de un edificio con registro de Loma Prieta 1989
- **Método:** Cosimulación manual ETABS-Pathfinder; análisis de capacidad según código
- **Efecto reportado:** Cierre de puerta aumenta la evacuación en 2,8 s (170) y 23,6 s (82)
- **Endogeneidad tratada:** No - no se trata variabilidad ni incertidumbre del evento
- **Instrumento:** No aplica
- **Robustez reportada:** Dos niveles de ocupación; sin análisis de sensibilidad ni Monte Carlo

| Vacío | Tipo | Descripción |
|---|---|---|
| V-008-01 | TERR | Un solo edificio en Pakistán; sin casos en América Latina ni validación local |
| V-008-02 | POBL | Se omiten comportamientos de pánico, grupos vulnerables en trauma y personal de empresas en turnos |
| V-008-03 | MET | No se compara integración manual y automática ni se aplican disparadores probabilistas |
| V-008-04 | VAR | No se incluyen variables económicas, tiempo de reocupación ni interrupción de actividades |
| V-008-05 | TEOR | Falta vincular con teorías de resiliencia funcional y de comportamiento humano en desastres |
| V-008-06 | CAUS | No hay evidencia causal empírica entre daño estructural y resultados de evacuación |
