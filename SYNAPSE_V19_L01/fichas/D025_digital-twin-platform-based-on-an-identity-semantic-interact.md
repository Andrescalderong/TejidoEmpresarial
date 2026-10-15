# FB-L01-025 | D025 — Digital twin platform based on an identity-semantic-interaction framework to improve bridge management workflows

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S2950550X26000245-main.pdf` · 14 páginas · Relevancia para el eje del corpus: **Adyacente** (Propone una plataforma de gemelo digital para puentes basada en identificadores persistentes, protocolo semántico IFC 4.3 y servicio de integración con datos IoT, demostrada en un puente en servicio; aporta la capa de interoperabilidad y de sincronización de un gemelo con IoT, pero no trata sismos ni recuperación posdesastre ni empresas.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-025 / D025
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Rico Thirion, M. A., Moghtadernejad, S., Xu, Y., Lounis, Z., & Chen, Q. (2026). Digital twin platform based on an identity-semantic-interaction framework to improve bridge management workflows. *Digital Engineering*, *11*, Article 100111. https://doi.org/10.1016/j.dte.2026.100111
- **Autores:** Rico Thirion, M.A. (58528835300); Moghtadernejad, S. (56703141100); Xu, Y. (60597345400); Lounis, Z. (6603924464); Chen, Q. (60596973300)
- **Afiliaciones:** Founder & Consultant, K&M BIM Design and Simulation, Guelph, ON, Canada; Construction Research Centre, National Research Council, Ottawa, ON, Canada; Student; School of Engineering, University of British Columbia, Okanagan, BC, Canada; Principal Research Officer, Construction Research Centre, National Research Council, Ottawa, ON, Canada; School of Engineering, University of British Columbia, Okanagan, BC, Canada
- **Fecha de publicación:** 2026
- **Fuente/contenedor:** Digital Engineering · vol. 11
- **Identificador persistente:** DOI 10.1016/j.dte.2026.100111 · ISSN 2950550X
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105036651598&doi=10.1016%2fj.dte.2026.100111&partnerID=40&md5=d66e0e17755b9254fe07398c87b5666f
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 1

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Evaluar si un marco de identidad, semántica e interacción puede mejorar de forma medible la consistencia de datos, la interoperabilidad y el desempeño de sincronización de flujos de trabajo de gemelo digital de puentes, en comparación con el intercambio convencional de datos basado en BIM, como prueba de concepto. El estudio desarrolla una plataforma que integra el modelado de información de puentes (BrIM) con datos de IoT y protocolos semánticos mediante un sistema unificado de propiedades e identificadores, con el fin de reducir la conciliación manual y facilitar la adopción de gemelos digitales en proyectos de puentes.

**Pregunta de investigación.** La pregunta rectora es si un marco que combina identificadores persistentes de componentes, un protocolo semántico basado en IFC 4.3, un protocolo de intercambio y un servicio de integración mejora la persistencia de identidad, la coherencia semántica, la latencia de sincronización y la eficiencia de automatización frente a los flujos convencionales de BIM.

**Marco teórico.** El marco combina el modelado de información de construcción (BIM) y el estándar abierto IFC, el concepto de gemelo digital con niveles de madurez (pre-gemelo, gemelo, gemelo adaptativo y gemelo inteligente según Tao y colaboradores) y principios de interoperabilidad semántica y de entornos comunes de datos (ISO 19650). Se define un marco de tres ejes: identidad persistente (identificador de componente PCID construido con la descomposición espacial y de producto), invariancia semántica (plantillas JSON que mapean propiedades entre BIM, IFC y bases de datos) y protocolos de intercambio por eventos (formato, método, destino, disparador, carga y respuesta). La orientación es de ingeniería de software y de gestión de activos, sin teoría de adopción tecnológica ni de recuperación.

**Metodología.** El marco incluye cuatro mecanismos: identificador persistente de componente, protocolo semántico basado en IFC 4.3, protocolo de intercambio de datos y servicio de integración con una tubería de seis etapas (detección de eventos, instantánea de datos, mapeo semántico, diferencia semántica, mapeo de cambio-acción y envío de acciones). El caso de estudio es un puente de hormigón de tres vanos con vigas pretensadas prefabricadas, en servicio y anonimizado por confidencialidad, con 1067 componentes y una red de sensores de ocho tipos (temperatura, deformación, desplazamiento, potencial de corrosión, aceleración, humedad y vibración) en 112 componentes monitoreados. Se implementó el servicio en Python 3.12 alojado en Google Cloud con Cloud SQL (PostgreSQL) y BigQuery, y se usaron BlenderBIM, Autodesk Docs y Tandem y Power BI. La validación se basó en cuatro escenarios (revisión del modelo BIM, actualización de sensores, flujo de inspección IFC y coordinación BCF) y seis criterios (persistencia de identificadores, consistencia semántica, latencia de sincronización, completitud de datos, eficiencia de automatización y robustez), evaluados con registros del sistema y verificaciones automatizadas dentro del propio equipo del proyecto.

**Resultados principales.** En una prueba de robustez con 1067 registros de componentes en cuatro dominios de datos (BlenderBIM, IFC, Tandem y Power BI) y actualizaciones aleatorias (renombrado, regeneración de IFC y recarga de inspecciones), el identificador persistente se conservó en 100 % de los casos. Un escenario de monitoreo de deformación con umbral de 60 microdeformaciones activó una alerta visible en los tableros de Tandem y Power BI en 4,2 s, con un correo al ingeniero de mantenimiento. Los autores informan consistencia semántica sin discrepancias observadas, completitud de datos sin valores faltantes, sincronización 'casi en tiempo real' y eliminación de pasos manuales respecto de los flujos convencionales, sin reportar el número de pasos antes y después, la distribución de latencias ni los tamaños de muestra por escenario. Tampoco se presentan resultados de pruebas de carga, de actualización concurrente por varios usuarios ni de manejo de datos faltantes o erróneos de los sensores, de modo que los valores reportados describen el funcionamiento esperado del sistema en condiciones controladas y no su comportamiento bajo carga real, con varios usuarios o ante fallas. La discusión de limitaciones señala escalabilidad limitada en proyectos grandes y multiorganizacionales, dependencia de configuración manual de plantillas, ausencia de una capa transaccional para actualizaciones concurrentes y falta de razonamiento ontológico.

**Discusión y contribución.** Los autores sostienen que el marco es modular, replicable y de bajo costo, apto para proyectos de puentes de escala pequeña y mediana, y que reduce la barrera técnica de adopción de gemelos digitales al eliminar intercambios manuales de IFC, mantener identidades estables y reutilizar plantillas semánticas. Lo posicionan como una capa intermedia (middleware) que complementa a plataformas comerciales como Tandem o iTwin, que ofrecen más visualización e inteligencia pero menos transparencia. Recomiendan una estrategia incremental de despliegue (empezar por la integración de datos de inspección), y proponen como trabajo futuro una arquitectura de microservicios, mayor gobernanza de datos (versionado, control de acceso y auditoría) y motores de reglas hacia gemelos cognitivos con aprendizaje adaptativo.

**Limitaciones declaradas.** Declaradas: validación interna del equipo del proyecto, escalabilidad limitada, configuración manual de plantillas JSON, ausencia de capa transaccional para concurrencia, sin razonamiento ontológico, demostración sobre una plataforma comercial (Tandem). No declaradas: puente anónimo y un solo caso; sin comparación cuantitativa con un flujo convencional; una sola alerta temporizada; sin costos ni esfuerzo de adopción medidos.

**Trabajo futuro.** Arquitectura de microservicios con intermediarios de mensajes para coordinación distribuida, gobernanza de datos con versionado, control de acceso y auditoría, motores de reglas y capacidades cognitivas, validación externa con propietarios de infraestructura y expertos, y una plataforma independiente de gemelo digital integrada con el servicio de integración.

**Palabras clave.** Declaradas: BIM/IFC interoperability; Bridge information modeling (BrIM); Digital twin; IoT-enabled lifecycle monitoring; Persistent component identification; Semantic data integration | Inferidas: gemelo digital, modelado de información de puentes, interoperabilidad BIM e IFC, IoT, identificador persistente de componente, protocolo semántico, integración de datos, gestión de puentes, servicio de integración, Autodesk Tandem

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un identificador persistente de componente, plantillas semánticas alineadas con IFC 4.3 y un servicio de integración por eventos permiten sincronizar de forma automática y consistente los modelos BIM, los registros de inspección y los datos de sensores de un puente en servicio, reducir el trabajo manual y bajar la barrera de adopción de gemelos digitales en proyectos de tamaño mediano.

**Antítesis identificada.** La evidencia se produce dentro del equipo del proyecto, en un puente anónimo, sin comparación cuantitativa con un flujo convencional y sin informar tamaños de muestra, distribución de latencias, número de pasos manuales eliminados, costos ni tiempo de configuración de plantillas; el resultado de '100 % de persistencia' mide una propiedad que el propio diseño garantiza (el identificador se incrusta como propiedad compartida) y no la robustez ante escenarios adversos. La alerta de 4,2 s corresponde a un evento aislado, y los umbrales son inconsistentes (50 microdeformaciones en la tabla de ejemplo, 60 en el escenario, 45,7 en la carga de ejemplo). El texto califica el marco de 'confiable y escalable' al tiempo que reconoce escalabilidad limitada y configuración manual. La dependencia de Tandem y Power BI para la demostración limita la neutralidad del protocolo, y la integración de IoT se describe a nivel de mensajes, no de manejo de fallas o pérdida de datos.

**Síntesis propuesta.** El aporte defendible es un patrón de interoperabilidad de bajo costo (identificador estable, plantillas de mapeo y servicio por eventos) que resuelve un problema práctico real de los gemelos de infraestructura: mantener la correspondencia entre el elemento físico y sus datos a lo largo de herramientas y fases. Debe leerse como prueba de concepto de ingeniería de software y no como evidencia de mejora medida de gestión. Para el corpus, la síntesis consiste en aprovechar este patrón para la capa de identidad y datos de un gemelo de recuperación (inspección posterior a un sismo, estado de componentes, sensores), y exigir su evaluación con métricas explícitas: tiempo de sincronización, tasa de errores de mapeo, horas de trabajo manual evitadas y costo de implementación frente a un flujo documental convencional.

**Áreas grises detectadas.**

1. Validación interna y sin línea base: la implementación fue validada internamente por el equipo del proyecto, no se declara una medición con flujo convencional ni tamaño de muestra por escenario, y los criterios de eficiencia de automatización y de robustez se afirman sin números.
2. Interpretación del 100 % de persistencia: la retención total de identificadores se logra porque el identificador es una propiedad incrustada en el modelo y replicada en bases y API, y la prueba aleatoria de renombrado, regeneración y recarga mide una propiedad por diseño, no la resistencia a errores humanos, cambios de proveedor o corrupción de datos.
3. Inconsistencia de umbrales y de eventos: el ejemplo de protocolo usa un umbral de 50 microdeformaciones (con carga de 45,7), el escenario de alerta usa 60, y la latencia de 4,2 s proviene de una sola prueba; no se informa la distribución de latencias ni el desempeño bajo volumen de datos de 112 componentes con sensores continuos.
4. Alcance y neutralidad: la demostración usa Autodesk Docs, Tandem y Power BI, y la afirmación de que el protocolo es independiente de herramientas no se prueba con otra plataforma; el puente es anónimo por confidencialidad, lo que impide verificar contexto, tamaño y condiciones del caso.

**Puntos oscuros aclarados.** Resulta llamativo que un estudio que pretende mejorar la gestión de puentes con gemelos digitales declare como resultado principal la conservación de un identificador y la ausencia de pasos manuales, y que no presente ningún análisis de decisión de mantenimiento, riesgo o costo. Una explicación plausible es que el problema que el trabajo resuelve es de infraestructura de datos y que su validación natural son pruebas de software (consistencia, latencia, completitud), que no requieren años de datos operativos ni eventos de daño; la evaluación de beneficios de gestión exigiría otro tipo de estudio. Esto indica que el nivel de madurez demostrado es de integración técnica, y que el valor para el gestor de activos depende de condiciones no evaluadas: capacidad para mantener plantillas, calidad de los datos de origen y gobernanza. Además, que los autores definan el trabajo como middleware que complementa plataformas comerciales sugiere que la innovación está en el estándar de identidad y mapeo, y que su adopción requeriría acuerdos entre propietarios, contratistas y proveedores, no solo código.

**Ideas propositivas novedosas.**

1. Identidad persistente como requisito de un gemelo de recuperación: adoptar un esquema de identificadores estables de edificios, componentes críticos, activos de empresas y sensores para que inspecciones posteriores a un sismo, registros de daño y de reparación y datos de operación se vinculen sin conciliación manual, y medir el tiempo y los errores evitados en un simulacro de inspección posterior a un sismo. Fundamento: el artículo muestra que el identificador persistente elimina conciliaciones en el ciclo de vida de un puente. Verificabilidad: simulacro con un conjunto de edificios, comparando el flujo documental con el flujo con identificadores. Utilidad: reduce el tiempo de consolidación de información de daño y facilita decisiones de reapertura.
2. Medición comparativa de esfuerzo de adopción de un gemelo de bajo costo: registrar horas de configuración de plantillas, número de plantillas por tipo de activo, costo de nube y mantenimiento, y tiempo de respuesta en un conjunto de proyectos de puentes de tamaños diferentes, para contrastar la afirmación de bajo costo y de aptitud para proyectos medianos. Fundamento: la discusión sostiene que el enfoque es de bajo costo sin cifras. Verificabilidad: registro de esfuerzo en dos o más proyectos y comparación con una plataforma comercial. Utilidad: permite fijar un presupuesto realista y decidir si el modelo se justifica para organizaciones con recursos limitados.

**Relaciones poco exploradas.**

1. Identificador estable por componente (condiciona) la posibilidad de vincular inspecciones, sensores y modelos: sin una clave común, los datos de distintos sistemas no se asocian al elemento físico y se requiere conciliación manual.
2. Plantillas de mapeo configuradas manualmente (limitan) la escalabilidad del marco: los autores reconocen que la configuración manual aumenta el mantenimiento y restringe la adaptación en tiempo real a muchos puentes.

**Robustez argumentativa:** 3.3/10 (ponderación 30/30/25/15) — consistencia lógica 4/10; calidad de la evidencia 3/10; validez de inferencias causales 3/10; generalizabilidad 3/10.

**Valor estratégico:** 6/10 — Aporta un diseño concreto y reproducible de identificadores persistentes, plantillas semánticas y servicio de integración por eventos para vincular modelos, inspecciones y sensores de un puente, con una demostración en un activo real. Su valor para el corpus es de patrón de interoperabilidad de datos de un gemelo con IoT. Se reduce porque la validación es interna y sin línea base, el caso es único y anónimo, no se miden costos ni beneficios de gestión y el dominio no incluye sismos.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Petición de principio (Se concluye que el marco 'provides measurable improvements' sin mostrar las medidas comparativas, y se evalúa con criterios definidos y verificados por el mismo equipo (Sec. 3.5, p. 8; Sec. 5, p. 13)); Tautología en la medición (La persistencia de 100 % de identificadores se obtiene de un mecanismo diseñado para conservarlos (Sec. 4.1, p. 10-12)); Contradicción interna / generalización (Se califica el marco de 'fiable y escalable' mientras se reconoce escalabilidad limitada y configuración manual (Sec. 5, p. 12-13))
- **Bradford-Hill:** No aplica: es una demostración de ingeniería de software; las mejoras atribuidas (automatización, reducción de conciliación) no se contrastan con una condición de comparación ni con datos de decisión o costos.
- **TRL asignado:** 5 — 'The implementation was internally validated within the project team' (p. 8)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (14 páginas más referencias). Las tablas 1 y 2 se extrajeron con el orden desordenado; los campos y ejemplos se leyeron del texto. El texto enumera ocho tipos de sensores pero nombra siete magnitudes; se reporta tal como figura. Los hallazgos del servicio provienen de validación interna del propio equipo.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un identificador persistente de componente, plantillas semánticas alineadas con IFC 4.3 y un servicio de integración por eventos permiten sincronizar de forma automática y consistente los modelos BIM, los registros de inspección y los datos de sensores de un puente en servicio, reducir el trabajo manual y bajar la barrera de adopción de gemelos digitales en proyectos de tamaño mediano.  | La evidencia se produce dentro del equipo del proyecto, en un puente anónimo, sin comparación cuantitativa con un flujo convencional y sin informar tamaños de muestra, distribución de latencias, número de pasos manuales eliminados, costos ni tiempo de configuración de plantillas; el resultado de '100 % de persistencia' mide una propiedad que el propio diseño garantiza (el identificador se incrusta como propiedad compartida) y no la robustez ante escenarios adversos. La alerta de 4,2 s corresponde a un evento aislado, y los umbrales son inconsistentes (50 microdeformaciones en la tabla de ejemplo, 60 en el escenario, 45,7 en la carga de ejemplo). El texto califica el marco de 'confiable y escalable' al tiempo que reconoce escalabilidad limitada y configuración manual. La dependencia de Tandem y Power BI para la demostración limita la neutralidad del protocolo, y la integración de IoT se describe a nivel de mensajes, no de manejo de fallas o pérdida de datos.  | El aporte defendible es un patrón de interoperabilidad de bajo costo (identificador estable, plantillas de mapeo y servicio por eventos) que resuelve un problema práctico real de los gemelos de infraestructura: mantener la correspondencia entre el elemento físico y sus datos a lo largo de herramientas y fases. Debe leerse como prueba de concepto de ingeniería de software y no como evidencia de mejora medida de gestión. Para el corpus, la síntesis consiste en aprovechar este patrón para la capa de identidad y datos de un gemelo de recuperación (inspección posterior a un sismo, estado de componentes, sensores), y exigir su evaluación con métricas explícitas: tiempo de sincronización, tasa de errores de mapeo, horas de trabajo manual evitadas y costo de implementación frente a un flujo documental convencional.  | 3.3/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Gemelo digital' es aquí una plataforma que sincroniza modelo BIM, inspecciones y sensores mediante identificadores y eventos; 'interoperabilidad semántica' es conservar el mismo significado de una propiedad entre sistemas.
- **P2 Supuestos:** Supone que el problema principal es la fragmentación de datos, que la persistencia de identificadores garantiza consistencia y que la validación interna es suficiente para una prueba de concepto.
- **P3 Evidencia:** La evidencia son un caso con 1067 componentes, pruebas aleatorias de identificadores y una alerta de 4,2 s; no hay comparación con un flujo convencional.
- **P4 Consecuencias:** Si es cierto, los propietarios de puentes pueden adoptar un gemelo con herramientas abiertas y bajo costo; si es falso, podrían asumir una carga de configuración y mantenimiento mayor a la esperada.
- **P5 Contraejemplos:** No se examinan fallas de sincronización, datos erróneos ni conflictos de actualización concurrente, ni la comparación con plataformas comerciales integradas.
- **P6 Alternativas:** Alternativas: que el beneficio provenga de la digitalización de inspecciones y no del gemelo; que la capacidad del personal para mantener plantillas sea el factor limitante; que la dependencia de proveedores comerciales anule la ventaja de bajo costo.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Componentes del puente | 1067 | componentes | Superestructura y subestructura | Sec. 4, p. 8 | Texto | Alta | Puente anónimo de tres vanos |
| Componentes monitoreados con sensores | 112 | componentes | Ocho tipos de sensores | Sec. 4, p. 8 | Texto | Alta | El texto enumera siete tipos de magnitud |
| Persistencia del identificador | 100 | % | 1067 registros en cuatro dominios con actualizaciones aleatorias | Sec. 4.1, p. 10-12 | Texto | Media | Propiedad garantizada por diseño |
| Latencia de alerta de deformación | 4,2 | s | Umbral de 60 microdeformaciones; evento único | Sec. 4.1, p. 12 | Texto | Media | Sin distribución de latencias |
| Etapas de la tubería del servicio de integración | 6 | etapas | Detección, instantánea, mapeo, diferencia, mapeo cambio-acción y envío | Sec. 3.4, p. 6-7 | Texto | Alta | Servicio en Python 3.12 |
| Criterios de validación | 6 | criterios | Persistencia, consistencia, latencia, completitud, automatización y robustez | Tabla 3, p. 8 | Tabla | Alta | Sin umbrales de aceptación |
| Escenarios de aplicación | 4 | escenarios | Revisión BIM, sensores, inspección IFC y BCF | Sec. 4.1, p. 8 | Texto | Alta | Evaluados internamente |
| Umbral del ejemplo de protocolo | 50 | microdeformaciones | Ejemplo de la Tabla 2; carga de ejemplo de 45,7 | Tabla 2, p. 6 | Tabla | Media | Difiere del umbral de 60 del escenario |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 5 | Sí | 'The implementation was internally validated within the project team' (p. 8) | Prototipo validado en un puente en servicio mediante pruebas internas; sin validación externa ni operación prolongada. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'significantly lowers the technical barrier to digital twin adoption in bridge projects' (p. 1) | Se alega bajo costo y adopción incremental, sin cifras de costo, mercado ni modelo de negocio. |
| IRL | 5 | Sí | 'The Integration Service acted as the operational backbone of this framework, coordinating event-driven synchronization' (p. 12) | Integración operativa entre modelo, nube, sensores y paneles en un caso real; sin pruebas de carga, concurrencia ni fallas. |
| DRL | 3 | Sí | 'the lack of standardized modeling processes, and limited interoperability among heterogeneous systems' (p. 2) | Necesidad argumentada por la literatura; sin estudio de demanda de propietarios ni disposición a pagar. |
| SRL | 2.78 | Sí | Componentes: Identificador persistente y protocolo semántico (TRL 5), Servicio de integración por eventos con IoT (TRL 5) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 25.0; ÷9 → 2.78; nivel acotado a [1,9] = 2.78 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V2 Prototipo sin escalamiento · Severidad: Media · TRL 5 con BRL 2 e IRL 5: prototipo integrado y probado internamente, sin modelo de negocio, validación externa ni evidencia de beneficios de gestión. · Estrategia de salida: Validación externa con propietarios de puentes, medición de costos y esfuerzo y pilotos en más de un activo.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Petición de principio | Se concluye que el marco 'provides measurable improvements' sin mostrar las medidas comparativas, y se evalúa con criterios definidos y verificados por el mismo equipo (Sec. 3.5, p. 8; Sec. 5, p. 13) | Autoevaluación sin línea base |
| Tautología en la medición | La persistencia de 100 % de identificadores se obtiene de un mecanismo diseñado para conservarlos (Sec. 4.1, p. 10-12) | El resultado no prueba robustez |
| Contradicción interna / generalización | Se califica el marco de 'fiable y escalable' mientras se reconoce escalabilidad limitada y configuración manual (Sec. 5, p. 12-13) | Conclusión más fuerte que la evidencia |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Identificador persistente → menor conciliación manual de datos | Retención de 100 % de identificadores; sin medición del esfuerzo evitado | Plausibilidad, mecanismo claro | Cuantificación, línea base, replicación | Calidad de los datos de origen, capacidad del personal | 3 | Hipótesis no probada |
| Servicio por eventos → decisiones más oportunas de mantenimiento | Una alerta de 4,2 s | Plausibilidad | Medición del efecto en decisiones y costos | Procesos organizacionales | 2 | Hipótesis no probada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Validación externa con línea base cuantitativa, tamaños de muestra y métricas de esfuerzo y costo | Crítico | Media | 9 |
| Tecnológico | Escalabilidad, concurrencia, gobernanza de datos y manejo de fallas y pérdida de datos de sensores | Crítico | Media | 8 |
| Mercado | Modelo de costos y capacidades necesarias para pequeñas organizaciones propietarias de puentes | Significativo | Media | 7 |
| Conocimiento | Extensión del patrón de identidad y semántica a gemelos de recuperación posdesastre | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Ejemplo de protocolo semántico | Diagrama | Mapeo de un componente entre modelo, IFC y Tandem | No aplica | Media |
| Tabla 1 | Definición de campos de la plantilla de mapeo semántico | Tabla | Campos de plantilla y de propiedad | No aplica | Media |
| Fig. 2 | Ejemplo de protocolo de intercambio | Diagrama | Formato, método, destino, disparador, carga y respuesta | 50 microdeformaciones; 45,7 | Media |
| Fig. 3 | Tubería del servicio de integración | Diagrama | Seis etapas | 6 etapas | Alta |
| Tabla 3 | Marco de validación y criterios de evaluación | Tabla | Seis criterios y métodos de evaluación | 6 criterios | Alta |
| Fig. 4 | Vistas del puente de ejemplo | Imagen | Puente de tres vanos de hormigón | 1067 componentes | Baja |
| Fig. 5-8 | Procesos de revisión BIM, actualización de sensores, inspección IFC y BCF | Diagrama | Cuatro flujos de trabajo | 4 escenarios | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Autodesk Tandem | No especificado en documento | Industria | Plataforma comercial de gemelo digital usada como entorno de demostración | Visualización y análisis integrados | Dependencia de proveedor | Creciendo |
| Bentley iTwin | No especificado en documento | Industria | Plataforma comercial de gemelos de infraestructura | Simulación y análisis predictivo | Menor transparencia | Creciendo |
| Lin et al., Ma et al. y Yang et al. (modelos FEM, nubes de puntos y sustitutos, citados) | No especificado en documento | Academia | Representaciones de gemelo basadas en física o geometría | Análisis estructural | Sin identidad semántica persistente | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** No aplica: no se estima una variable resultado
- **X:** No aplica
- **Z (controles):** Tipo de evento (modelo, sensor, inspección, incidencia)
- **Datos:** Un puente con 1067 componentes y 112 monitoreados; escenarios controlados
- **Método:** Prueba de concepto con registros de sistema y verificaciones automáticas
- **Efecto reportado:** No cuantificado en términos de costo o decisión
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Pruebas aleatorias de actualización; sin análisis de sensibilidad ni validación externa

| Vacío | Tipo | Descripción |
|---|---|---|
| V-025-01 | TERR | Puente anonimizado por confidencialidad; el texto no declara el contexto geográfico (el identificador de ejemplo incluye la sigla PEI); sin zona sísmica |
| V-025-02 | POBL | Sin análisis de usuarios, personal de mantenimiento ni propietarios de infraestructura |
| V-025-03 | TEMP | Prueba de integración sin horizonte de operación prolongada |
| V-025-04 | MET | Validación interna sin línea base ni tamaños de muestra |
| V-025-05 | VAR | Faltan variables de costo, esfuerzo, calidad de datos y fallas |
| V-025-06 | TEOR | Sin teoría de adopción tecnológica ni de gobernanza de datos |
| V-025-07 | CAUS | Sin evidencia causal de beneficio de gestión |
