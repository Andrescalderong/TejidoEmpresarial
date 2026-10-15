# FB-L01-021 | D021 — Multi-domain data integration and management for enhancing service-oriented digital twin for infrastructure operation and maintenance

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S266616592400156X-main.pdf` · 21 páginas · Relevancia para el eje del corpus: **Adyacente** (Propone un marco de gemelo digital orientado a servicios para operación y mantenimiento de infraestructura (SoDT-IOM) con integración de datos de múltiples dominios (BIM, sistemas de gestión de activos, sensores IoT) y lo evalúa con dos casos y entrevistas a expertos; aporta la capa de datos y servicios de un gemelo, pero no trata sismos ni recuperación posdesastre.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-021 / D021
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Liu, L., Zeng, N., Liu, Y., Han, D., & König, M. (2024). Multi-domain data integration and management for enhancing service-oriented digital twin for infrastructure operation and maintenance. *Developments in the Built Environment*, *18*, Article 100475. https://doi.org/10.1016/j.dibe.2024.100475
- **Autores:** Liu, Liu (57388815500); Zeng, Ningshuang (56367393300); Liu, Yan (56368702300); Han, Daguang (57212621350); König, Markus (8883542500)
- **Afiliaciones:** Computing in Engineering, Department of Civil and Environmental Engineering, Ruhr-Universität Bochum, Bochum, 44801, Germany; School of Civil Engineering, Southeast University, No.2, Southeast University Road, Nanjing, 211189, China; School of Management and Engineering, Nanjing University, Jiangsu, Nanjing, 210093, China
- **Fecha de publicación:** 2024
- **Fuente/contenedor:** Developments in the Built Environment · vol. 18
- **Identificador persistente:** DOI 10.1016/j.dibe.2024.100475 · ISSN 26661659
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85195018599&doi=10.1016%2fj.dibe.2024.100475&partnerID=40&md5=66f9cdbdb7b4cb565534dc0329c86965
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 31

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Desarrollar y evaluar un marco de gemelo digital orientado a servicios para operación y mantenimiento de infraestructura (SoDT-IOM) que supere la heterogeneidad, fragmentación e interoperabilidad de los datos entre sistemas de distintas autoridades de activos. El estudio busca diseñar los componentes del gemelo y el mecanismo de integración de datos de múltiples dominios, definir un repositorio de datos individual-múltiple para servicios y valorar su funcionalidad y eficacia con casos de uso y entrevistas con profesionales de la industria, y derivar requisitos de diseño y recomendaciones de implementación técnicos y de gestión.

**Pregunta de investigación.** Las preguntas de investigación declaradas son dos: cómo diseñar un gemelo digital orientado a servicios para mejorar la operación y el mantenimiento de infraestructura, y cómo diseñar un mecanismo de integración e intercambio de datos que permita realizar el SoDT-IOM.

**Marco teórico.** El marco combina la evolución de BIM (modelo estático) al gemelo digital (representación dinámica centrada en datos), el concepto de gemelo digital orientado a servicios, tomado de la manufactura, y la gestión de activos bajo las normas ISO 55000 y la serie ISO 19650 sobre entorno común de datos (CDE), con tecnologías de web semántica y contenedores de información para la integración. Adopta la ciencia del diseño (DSR) de Peffers y Hevner como paradigma metodológico: identificar el problema, definir objetivos, diseñar el artefacto, demostrarlo y evaluarlo. Los componentes del gemelo se organizan en entorno físico, conexiones físico-virtuales, entorno virtual (servicios de visualización, de gemelo y de gestión de datos) y repositorio de datos.

**Metodología.** El estudio sigue las etapas de la DSR. El problema se identificó mediante una revisión sistemática de la literatura y actividades con la industria (observaciones y entrevistas). Los requisitos se obtuvieron con cinco entrevistas semiestructuradas a expertos (R1 a R5: ingeniería civil de autoridad vial, consultoría, desarrollo de software y transferencia de ingeniería), con experiencias de 3 a 29 años. El marco se diseñó de forma iterativa y se desarrolló un prototipo, probado en una demostración técnica con dos casos de proyectos reales: el mantenimiento de un tramo de pavimento de 460 m en renovación durante siete meses y el monitoreo de corrosión de ocho tendones de un puente de autopista con sensores que miden una vez al mes. La evaluación se hizo en dos pasos: contraste con criterios publicados de funcionalidad y una entrevista estructurada con cinco expertos (E1 a E5) sobre ventajas, desventajas, intención de uso y mejoras, además de la evaluación de la metodología con las directrices de Hevner y Chatterjee. No se aplican métricas cuantitativas de desempeño.

**Resultados principales.** Los expertos describieron problemas de gestión de datos (habilidades desiguales, documentación en papel, nivel de detalle inconsistente y responsabilidades poco claras) y de tecnología (sistemas aislados de puentes y pavimentos, silos de datos y ausencia de intercambio estandarizado). A partir de ellos se definió el marco SoDT-IOM con un repositorio híbrido (centralizado, alineado con el entorno común de datos, e individual alojado por cada actor), un mecanismo de mapeo para vincular datos heterogéneos y servicios de gemelo con ciclos de proceso por tipo de actividad. El primer caso mostró entrega, verificación automática y actualización de protocolos de conformidad de asfalto contra requisitos legibles por máquina. El segundo mostró un servicio de monitoreo que integra datos del puente, sensores de resistencia eléctrica de los tendones y un algoritmo de evaluación, con notificación automática cuando el valor excede el rango admisible. Los expertos reconocieron como ventajas la digitalización, la actualización oportuna, la precisión, la vinculación de datos heterogéneos, la visión de las actividades, el apoyo a decisiones y la colaboración, y como desventajas la seguridad de datos, el procesamiento en profundidad, el costo, la dificultad de automatización, la complejidad de las actividades y el esfuerzo de adopción. Los autores concluyen que el marco mejora la interoperabilidad, la colaboración y la automatización de procesos, y que el mapeo y el flujo de datos requieren desarrollo y validación adicionales.

**Discusión y contribución.** Los autores sostienen que el marco ofrece una solución general para varios activos, a diferencia de los gemelos de infraestructura centrados en un solo activo y en el monitoreo estructural, y que reduce la necesidad de desarrollar soluciones aisladas basadas solo en modelos BIM. Destacan que los datos deben organizarse con estándares BIM y web semántica, que la precisión depende de definir requisitos y responsabilidades de entrega de información y que los presupuestos limitados y la carga de trabajo retrasan la adopción en el sector. Recomiendan a los profesionales seleccionar de forma estratégica el servicio por implementar según la capacidad del sistema de gestión de activos existente, los beneficios de la tecnología y los recursos, y adoptar formatos abiertos. Reconocen que el marco no crea nuevos modelos de información ni resuelve la comunicación entre personas, y proponen incorporar pronóstico con aprendizaje automático.

**Limitaciones declaradas.** Declaradas: el marco se centra en integrar fuentes existentes y no en crear nuevos modelos de activos; la comunicación persona a persona queda limitada; el mapeo y el flujo de datos requieren desarrollo y validación. No declaradas: muestra de cinco expertos por etapa y sin cuantificación; evaluación cualitativa sin comparación con una alternativa; casos de un país y dos tipos de activos; sin métricas de rendimiento, costo ni seguridad.

**Trabajo futuro.** Desarrollar el SoDT-IOM completo, validar el enfoque de mapeo y el flujo de procesamiento de datos, explorar funciones de pronóstico en tiempo real con aprendizaje automático y profundo, ampliar la comunicación con terceros (por ejemplo, residentes), integrar tecnologías inmersivas para capacitación e integrar teoría y práctica.

**Palabras clave.** Declaradas: Digital twin; Infrastructure; Multi-domain data integration; Operation and maintenance; Service-oriented design | Inferidas: gemelo digital, integración de datos multidominio, diseño orientado a servicios, operación y mantenimiento de infraestructura, BIM, tecnologías de web semántica, entorno común de datos, gestión de activos, IoT, entrevistas con expertos

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un gemelo digital orientado a servicios, con un repositorio híbrido de datos basado en estándares BIM y web semántica y con servicios definidos por tipo de actividad, permite integrar datos heterogéneos de varios sistemas de gestión de activos y de sensores IoT, mejorar la oportunidad y precisión de la información y automatizar tareas de operación y mantenimiento de infraestructura.

**Antítesis identificada.** La evidencia se reduce a un prototipo demostrado en dos casos y a opiniones de cinco expertos, sin métricas de tiempo, costo, errores, calidad de datos o seguridad, y sin comparación con una alternativa (por ejemplo, un tablero o un sistema de gestión de activos integrado). Los expertos que definieron los requisitos y los que evaluaron el marco son profesionales de ingeniería civil y de gestión de infraestructura, y el texto no indica criterios de selección ni país, lo que permite un sesgo hacia la aceptación; el artículo reconoce costos, seguridad, complejidad y esfuerzo de adopción como desventajas, pero no las cuantifica. El mecanismo de mapeo, que es la contribución técnica central de integración de datos, se declara pendiente de desarrollo y validación. El segundo caso emplea mediciones mensuales de ocho tendones, lejos de las condiciones de tiempo real o de alta frecuencia que justificarían un gemelo digital, y el caso de pavimento es principalmente gestión documental.

**Síntesis propuesta.** La contribución sostenible es una arquitectura de datos y servicios para gemelos de infraestructura, con lista de requisitos de gestión y tecnología obtenidos de usuarios, y con la distinción entre un repositorio central y repositorios individuales por actor. Debe leerse como diseño conceptual con demostración de factibilidad y no como evidencia de beneficio. Para el corpus, la síntesis consiste en aprovechar esta arquitectura para la capa de datos de un gemelo de recuperación posdesastre, donde múltiples actores (autoridades, empresas, aseguradoras, proveedores) mantienen sistemas separados, y evaluar con un caso retrospectivo si la integración de datos reduce el tiempo de decisión, estimando costos de integración y riesgos de seguridad por actor.

**Áreas grises detectadas.**

1. Alcance de la evaluación: la evaluación se basa en cinco expertos y se resume en una tabla de ventajas y desventajas sin frecuencia de menciones, sin escala de intención de uso y sin indicación de si los expertos de evaluación coinciden con los de requisitos, por lo que no se puede juzgar el sesgo de confirmación ni la magnitud del apoyo.
2. Mecanismo de mapeo no validado: el enfoque de mapeo para vincular datos heterogéneos y el flujo de procesamiento para garantizar calidad y coherencia entre repositorios se declaran sin desarrollo completo ni validación, aunque son la contribución técnica principal de la integración de datos.
3. Representatividad de los casos: los dos casos (pavimento de 460 m y puente con ocho tendones medidos una vez al mes) son de un solo contexto y de baja frecuencia de datos, lo que no demuestra la capacidad de integración de datos multidominio en tiempo real ni su escalabilidad a redes de infraestructura.
4. Costos y seguridad sin cuantificar: los expertos señalan costo, seguridad de datos y esfuerzo de adopción como desventajas, pero el artículo no estima costos de instalación, mantenimiento ni riesgo de seguridad al agregar datos de distintos actores, por lo que la viabilidad económica queda abierta.

**Puntos oscuros aclarados.** Llama la atención que los expertos consideren el gemelo digital principalmente como método de automatización de procesos y no como herramienta de simulación o de predicción, y que el segundo caso de uso emplee mediciones mensuales, lejos del 'tiempo real' que se invoca en el marco. Una explicación plausible es que, en la práctica de operación y mantenimiento de infraestructura, el valor inmediato proviene de integrar documentos y registros dispersos y de reducir trabajo manual, y no de modelos dinámicos de alta frecuencia, cuyos datos y capacidades de análisis aún no existen en las organizaciones. Esto indica que la brecha principal para los gemelos de infraestructura es la gobernanza de datos (responsabilidades, formatos, accesos) más que la sofisticación de la simulación, y que un gemelo de recuperación tendría que empezar por esa capa. Además, que la adopción dependa de presupuestos y capacidades que varían mucho entre municipios y niveles nacionales sugiere que el diseño debe poder implementarse de forma gradual y con costo acotado por actor.

**Ideas propositivas novedosas.**

1. Gemelo de gobernanza de datos para recuperación posdesastre: aplicar el repositorio híbrido (central más individual por actor) a un escenario de recuperación posterior a un sismo, con servicios por tipo de actividad (inspección de daño, permisos, reabastecimiento, reapertura de empresas), y medir la reducción del tiempo de decisión y de errores de transferencia de información frente a los procesos manuales. Fundamento: el artículo reconoce que los datos están en silos de actores distintos y propone la integración como solución en operación y mantenimiento. Verificabilidad: simulacro o reconstrucción retrospectiva con actores reales y medición del tiempo entre solicitud y decisión. Utilidad: ofrece un diseño de coordinación de datos antes de invertir en modelos físicos complejos.
2. Evaluación cuantitativa de adopción de servicios de gemelo por nivel de capacidad organizacional: construir una escala de madurez de datos y de capacidad de las organizaciones (municipal, regional, nacional) y asociarla con los servicios que cada una podría adoptar, estimando costos de implementación y soporte, y validar la escala con una muestra mayor de profesionales. Fundamento: el artículo señala que la capacidad varía mucho entre niveles y que el presupuesto es limitante, sin medirlo. Verificabilidad: encuesta de muestra amplia y contraste con adopciones reales. Utilidad: permite seleccionar servicios viables por tipo de organización y reduce el riesgo de diseños inalcanzables.

**Relaciones poco exploradas.**

1. Calidad y formato estandarizado de los datos de origen (condicionan) la utilidad del gemelo orientado a servicios: los expertos señalan que la información heterogénea y los silos impiden entregar datos completos a las actividades de operación y mantenimiento.
2. Capacidad y presupuesto de las organizaciones (limitan) la adopción del gemelo: los autores reconocen que las capacidades varían entre municipal y nacional y que la nueva tecnología exige personal calificado y financiamiento, aunque no los miden.

**Robustez argumentativa:** 3.4/10 (ponderación 30/30/25/15) — consistencia lógica 4/10; calidad de la evidencia 3/10; validez de inferencias causales 3/10; generalizabilidad 4/10.

**Valor estratégico:** 6/10 — Aporta una arquitectura de gemelo digital centrada en datos y servicios, con requisitos obtenidos de profesionales, un mecanismo de repositorio híbrido y casos reales, útil como patrón de diseño para la capa de integración de información de un gemelo de recuperación. Su valor se reduce por la evaluación cualitativa con cinco expertos, la ausencia de métricas, el mapeo sin validar y el dominio de infraestructura vial sin sismos.

**Conexiones inter-documentales.**

- **COMPLEMENTA** D025 (Gemelo digital de puentes: interoperabilidad BIM-IoT): D021 integra datos heterogéneos con repositorio BIM y web semántica para gestión de activos; D025 sincroniza BIM, inspecciones y sensores con identificadores persistentes alineados con IFC 4.3 [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 47 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Apelación a la autoridad (selección de expertos) (La validez del marco se apoya en la opinión de cinco profesionales del mismo entorno, sin criterios de selección ni contraste (Sec. 7, p. 17)); Generalización apresurada (Se afirma que el marco es genérico para múltiples activos a partir de dos casos de un contexto (Sec. 7.3, p. 18)); Petición de principio (Se presenta la rigurosidad de la metodología DSR como garantía de la utilidad del artefacto, evaluada por los propios autores (Tabla 8, p. 18))
- **Bradford-Hill:** No aplica: es un diseño con evaluación cualitativa; las mejoras atribuidas al marco (oportunidad, precisión, colaboración) provienen de opiniones y no de medición con temporalidad, gradiente o experimento.
- **TRL asignado:** 5 — 'The prototype was developed and tested in a technical demonstration using two use cases from road and bridge projects' (p. 5)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (19 páginas más referencias). Las tablas 2, 3 y 4 se extrajeron con el orden desordenado; los perfiles de los expertos se leyeron de forma parcial. Las figuras de arquitectura no son legibles en la extracción de texto; la descripción se basa en el texto de las secciones 5 y 6.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un gemelo digital orientado a servicios, con un repositorio híbrido de datos basado en estándares BIM y web semántica y con servicios definidos por tipo de actividad, permite integrar datos heterogéneos de varios sistemas de gestión de activos y de sensores IoT, mejorar la oportunidad y precisión de la información y automatizar tareas de operación y mantenimiento de infraestructura.  | La evidencia se reduce a un prototipo demostrado en dos casos y a opiniones de cinco expertos, sin métricas de tiempo, costo, errores, calidad de datos o seguridad, y sin comparación con una alternativa (por ejemplo, un tablero o un sistema de gestión de activos integrado). Los expertos que definieron los requisitos y los que evaluaron el marco son profesionales de ingeniería civil y de gestión de infraestructura, y el texto no indica criterios de selección ni país, lo que permite un sesgo hacia la aceptación; el artículo reconoce costos, seguridad, complejidad y esfuerzo de adopción como desventajas, pero no las cuantifica. El mecanismo de mapeo, que es la contribución técnica central de integración de datos, se declara pendiente de desarrollo y validación. El segundo caso emplea mediciones mensuales de ocho tendones, lejos de las condiciones de tiempo real o de alta frecuencia que justificarían un gemelo digital, y el caso de pavimento es principalmente gestión documental.  | La contribución sostenible es una arquitectura de datos y servicios para gemelos de infraestructura, con lista de requisitos de gestión y tecnología obtenidos de usuarios, y con la distinción entre un repositorio central y repositorios individuales por actor. Debe leerse como diseño conceptual con demostración de factibilidad y no como evidencia de beneficio. Para el corpus, la síntesis consiste en aprovechar esta arquitectura para la capa de datos de un gemelo de recuperación posdesastre, donde múltiples actores (autoridades, empresas, aseguradoras, proveedores) mantienen sistemas separados, y evaluar con un caso retrospectivo si la integración de datos reduce el tiempo de decisión, estimando costos de integración y riesgos de seguridad por actor.  | 3.4/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Gemelo digital orientado a servicios' es un gemelo que ofrece funciones específicas a usuarios y se apoya en integración de datos; 'integración de datos multidominio' es vincular datos de sistemas, formatos y actores distintos.
- **P2 Supuestos:** Supone que los silos de datos son el obstáculo principal, que estándares BIM y web semántica son el camino y que la opinión de cinco expertos valida el marco.
- **P3 Evidencia:** La evidencia son entrevistas, un prototipo y dos casos de uso; no hay métricas de desempeño ni comparación.
- **P4 Consecuencias:** Si es cierto, las autoridades de activos deberían priorizar la gobernanza y la integración de datos antes de invertir en modelos de simulación; si es falso, se podría invertir en arquitectura que no reduce el esfuerzo de adopción.
- **P5 Contraejemplos:** No se examinan casos en que sistemas integrados de gestión de activos sin gemelo lograran resultados equivalentes, ni fallas de integración.
- **P6 Alternativas:** Alternativas: que la mejora provenga de la digitalización de procesos y no del gemelo; que el costo de adopción supere el beneficio en organizaciones pequeñas; que la seguridad de datos impida compartir entre actores.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Expertos entrevistados para requisitos | 5 | personas | R1 a R5; experiencia de 3 a 29 años | Sec. 4.2, p. 5-6 | Texto/Tabla | Alta | Tabla 3 |
| Expertos que evaluaron el marco | 5 | personas | E1 a E5; entrevista estructurada | Sec. 7.1, p. 17 | Texto/Tabla | Alta | Tabla 4 |
| Casos de uso de demostración | 2 | casos | Pavimento y monitoreo de puente | Sec. 6, p. 14 | Texto | Alta | Contexto de proyectos reales |
| Longitud del tramo de pavimento | 460 | m | Tres capas bituminosas a renovar en 7 meses | Sec. 6.1, p. 15 | Texto | Alta | Un solo carril habilitado |
| Tendones monitoreados | 8 | tendones | Sensores de resistencia eléctrica; una medición mensual | Sec. 6.2, p. 16 | Texto | Alta | Frecuencia baja |
| Componentes primarios del gemelo | 4 | componentes | Entorno físico, conexiones, entorno virtual y repositorio de datos | Sec. 4.1, p. 5 | Texto | Alta | Subdivididos en Tabla 5 |
| Ventajas identificadas | 7 | categorías | Digitalización, actualización, precisión, vinculación, visión, decisión y colaboración | Tabla 7, p. 17 | Tabla | Media | Sin frecuencias |
| Desventajas identificadas | 6 | categorías | Seguridad, procesamiento, costo, automatización, complejidad y adopción | Tabla 7, p. 17 | Tabla | Media | Sin cuantificación |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 5 | Sí | 'The prototype was developed and tested in a technical demonstration using two use cases from road and bridge projects' (p. 5) | Prototipo validado en demostración técnica con casos de proyectos reales; sin operación sostenida. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'The limited budgets and intensive workloads are well-known reasons for the delayed adoption of novel digital technologies' (p. 19) | Costos de adopción y de instalación reconocidos como barrera; sin modelo de negocio, precios ni pagador identificado. |
| IRL | 4 | Sí | 'future studies are required to fully develop the mapping approach and implement and validate the introduced data processing workflow' (p. 18) | Integración demostrada en un prototipo con fuentes existentes; mapeo y flujo de datos sin validación completa. |
| DRL | 4 | Sí | 'increasing optimization and automation of IOM activities' (p. 7) | Necesidad de integración y automatización confirmada por cinco expertos y por la revisión de la literatura; sin estudio de mercado ni intención de pago. |
| SRL | 2.0 | Sí | Componentes: Prototipo SoDT-IOM (servicios del gemelo) (TRL 5), Repositorio híbrido y mapeo de datos (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 18.0; ÷9 → 2.00; nivel acotado a [1,9] = 2.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V2 Prototipo sin escalamiento · Severidad: Media · TRL 5 con BRL 2 e IRL 4: prototipo validado en casos reales con modelo de negocio sin definir y mecanismo de integración sin validar, en un sector con presupuestos limitados. · Estrategia de salida: Piloto con al menos una autoridad de activos, costos de implementación medidos y validación del mapeo de datos.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Apelación a la autoridad (selección de expertos) | La validez del marco se apoya en la opinión de cinco profesionales del mismo entorno, sin criterios de selección ni contraste (Sec. 7, p. 17) | Sesgo de confirmación posible |
| Generalización apresurada | Se afirma que el marco es genérico para múltiples activos a partir de dos casos de un contexto (Sec. 7.3, p. 18) | Sin evidencia de transferibilidad |
| Petición de principio | Se presenta la rigurosidad de la metodología DSR como garantía de la utilidad del artefacto, evaluada por los propios autores (Tabla 8, p. 18) | Autoevaluación |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Integración de datos multidominio → decisiones más rápidas y precisas | Opinión de cinco expertos; sin métrica | Plausibilidad, coherencia con la literatura | Fuerza, consistencia, temporalidad, experimento | Capacidad organizacional, calidad de datos de origen | 2 | Hipótesis no probada |
| Servicios de gemelo con IoT → automatización de actividades | Dos casos de uso; sin medición de ahorro | Plausibilidad | Medición de esfuerzo y tiempos | Complejidad de la actividad, costo de sensores | 2 | Hipótesis no probada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Evaluación cuantitativa con métricas de tiempo, costo, calidad de datos y seguridad frente a alternativas | Crítico | Media | 9 |
| Tecnológico | Validación del mecanismo de mapeo y del flujo de datos entre repositorios centrales e individuales | Crítico | Media | 8 |
| Mercado | Costos de implementación, modelo de negocio y capacidad de adopción de organizaciones de distinto tamaño | Significativo | Media | 8 |
| Conocimiento | Extensión del marco a emergencias y recuperación posdesastre con múltiples actores | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Metodología para el desarrollo del SoDT-IOM | Diagrama | Etapas de la DSR | 5 etapas | Media |
| Tabla 1 | Ejemplos de sistemas de gestión de activos por país | Tabla | Soluciones de Alemania, Estados Unidos y Reino Unido | 5 sistemas | Baja |
| Tabla 2 | Estudios actuales de gemelos digitales de infraestructura | Tabla | Marcos y casos de puentes, túneles y carreteras | 10 estudios | Media |
| Tabla 5 | Componentes del SoDT-IOM | Tabla | Subdivisión de componentes del gemelo | 4 componentes primarios | Media |
| Fig. 2 | Marco SoDT-IOM con especificación según las entrevistas | Diagrama | Arquitectura de componentes | No aplica | Alta |
| Fig. 8 | Interfaz del caso de mantenimiento de pavimento | Captura de interfaz | Información de proyecto y documentación | 460 m | Baja |
| Fig. 9 | Monitoreo de corrosión de tendones de un puente | Captura de interfaz | Servicio de monitoreo con datos del puente y sensores | 8 tendones | Baja |
| Tabla 7 | Resultado de la evaluación del SoDT-IOM | Tabla | Ventajas y desventajas en integración de datos y servicios | 7 ventajas; 6 desventajas | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Hakimi et al. (marco conceptual de gemelo con fusión de datos y BIM abierto) | No especificado en documento | Academia | Marco de gestión de infraestructura a lo largo del ciclo de vida | Fusión de datos y BIM abierto | Nivel conceptual | Estable |
| Kaewunruen et al. (gemelo con BIM para inspección de puentes basada en riesgo) | No especificado en documento | Academia | Aplicación para tres tipos de riesgo | Caso de inspección | Un solo activo | Estable |
| Sistemas de gestión de activos: SIB-Bauwerke, AASHTOWare, HAPMS | Alemania/Estados Unidos/Reino Unido | Institucional | Gestión de inventario, inspección y mantenimiento | Implantación consolidada | Segmentados por tipo de activo y base relacional | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** No aplica: no se estima una variable resultado
- **X:** No aplica
- **Z (controles):** Tipo de actividad de operación y mantenimiento y tipo de activo
- **Datos:** Cinco entrevistas de requisitos, cinco de evaluación y dos casos de uso
- **Método:** Ciencia del diseño; análisis cualitativo de entrevistas; prototipo
- **Efecto reportado:** No cuantificado
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin triangulación cuantitativa; evaluación metodológica por directrices de Hevner y Chatterjee

| Vacío | Tipo | Descripción |
|---|---|---|
| V-021-01 | TERR | País de los casos no especificado en el texto extraído (los sistemas de ejemplo son de Alemania, Estados Unidos y Reino Unido); sin evidencia en zonas sísmicas ni en América Latina |
| V-021-02 | POBL | Solo profesionales de ingeniería civil; sin usuarios finales, residentes ni empresas afectadas |
| V-021-03 | TEMP | Datos mensuales en el caso del puente; sin dinámica de eventos extremos ni de recuperación |
| V-021-04 | MET | Muestra de cinco expertos y evaluación cualitativa sin comparación |
| V-021-05 | VAR | Faltan variables de costo, tiempo, calidad de datos y seguridad |
| V-021-06 | TEOR | Sin teoría de adopción de tecnología ni de resiliencia de infraestructura |
| V-021-07 | CAUS | Sin evidencia causal de efecto del gemelo sobre decisiones o costos |
