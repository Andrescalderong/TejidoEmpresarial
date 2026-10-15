# FB-L01-048 | D048 — Leveraging Digital Twins as a Common Operating Picture for Disaster Management: Case of Seismic Hazards

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/ijgi-13-00430-v2.pdf` · 20 páginas · Relevancia para el eje del corpus: **Núcleo** (Desarrolla y demuestra un gemelo digital como imagen operativa común (COP) para la respuesta a un terremoto en Kocaeli (Turquía): modelo 3D base con datos abiertos y municipales, peligro sísmico, evaluación rápida de daños, estimación de población afectada y de equipos de búsqueda y rescate, y bucle de revisión posterior. Es el segundo documento del corpus, junto con D034, que une gemelo digital, sismo y decisión; se limita a la fase de respuesta.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-048 / D048
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Korkmaz, M., Zulfikar, A. C., & Demirkesen, S. (2024). Leveraging Digital Twins as a Common Operating Picture for Disaster Management: Case of Seismic Hazards. *ISPRS International Journal of Geo-Information*, *13*(12), Article 430. https://doi.org/10.3390/ijgi13120430
- **Autores:** Korkmaz, Mustafa (57203318277); Zulfikar, A. Can (24472180100); Demirkesen, Sevilay (56331319900)
- **Afiliaciones:** Civil Engineering Department, Gebze Technical University, Kocaeli, 41400, Turkey; Disaster Management Institute, Istanbul Technical University, İstanbul, 34485, Turkey
- **Fecha de publicación:** 2024
- **Fuente/contenedor:** ISPRS International Journal of Geo-Information · vol. 13(12)
- **Identificador persistente:** DOI 10.3390/ijgi13120430 · ISSN 22209964
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85213211141&doi=10.3390%2fijgi13120430&partnerID=40&md5=43e2a0cb7f4017e26fb0e89ad163e4d6
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 18

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Explorar e ilustrar cómo la integración de gemelos digitales (DT) con una imagen operativa común (COP) puede mejorar la gestión de desastres, en particular durante la fase de respuesta a un terremoto. El estudio se propone ofrecer una comprensión detallada de DT y COP, proponer un flujo de trabajo conceptual para la respuesta, construir un modelo 3D base de Kocaeli con datos en tiempo real, modelos de información de edificios y evaluaciones de peligro sísmico, demostrar su aplicación mediante un escenario, discutir ventajas y desafíos y sugerir líneas de investigación y recomendaciones prácticas.

**Pregunta de investigación.** El artículo enuncia seis objetivos (O-1 a O-6) más que preguntas. Las preguntas implícitas son si un DT que opera como COP puede reunir datos de edificios, población, peligro y recursos para estimar daños, población afectada y necesidades de búsqueda y rescate en las primeras 72 horas, y qué desafíos de exactitud de datos, integración e interoperabilidad condicionan su uso.

**Marco teórico.** El marco articula el concepto de DT como representación virtual sincronizada con la entidad física, con sensores, analítica en tiempo real y simulación, y el de COP como pantalla compartida de información operativa que reduce la sobrecarga de datos y apoya la coordinación. El flujo conceptual de respuesta incluye recolección y evaluación de datos (estado de equipos médicos y de búsqueda y rescate, estructuras en riesgo y colapsadas), análisis de escenarios, puntos de decisión por umbrales, gestión de recursos y logística, y revisión posterior a la acción. La evaluación rápida de daños (RDA) se basa en ecuaciones de predicción de movimiento del suelo (GMPE), curvas de fragilidad y matrices de probabilidad de daño.

**Metodología.** El modelo 3D base de Kocaeli se construyó con un modelo de elevación digital de ALOS PALSAR (resolución de 12,5 m), modelos de terreno y de superficie, huellas de edificios de la Municipalidad Metropolitana de Kocaeli, ortofoto satelital, datos de vegetación, agua, calles y aceras de OpenStreetMap y datos de uso del suelo municipales. El peligro sísmico se calculó con un catálogo paramétrico de unos 1786 eventos (1900-2024) dentro de 200 km y 100 km de profundidad, con fallas de GEM y del servicio geológico MTA y Vs30 para condiciones de sitio. Los datos estructurales y de población se integraron mediante API. Una simulación de escenario basada en el terremoto de Kocaeli de 1999 (Mw 7,6) produjo intensidad (PGA), daño por categoría y estimaciones de población y de equipos de búsqueda y rescate, con Autodesk InfraWorks como plataforma principal, y un modelo matemático asignó recursos a sitios confirmados y no confirmados. No se describen la fragilidad usada, la validación ni el software de modelado con detalle.

**Resultados principales.** La intensidad del escenario varió entre 0,05 y 1,1 g de aceleración pico del suelo, con mayor vulnerabilidad en centros urbanos cercanos al hipocentro y con suelos deficientes. Cerca de 55 % de los edificios experimentaron daño moderado hasta colapso total y casi 60 % de la población requeriría refugio y protección. Las estimaciones preliminares indican unos 18 000 edificios con daño completo (alrededor de 145 000 personas) y unos 40 000 con daño extenso (alrededor de 340 000 personas). Para completar la fase de búsqueda y rescate en las 72 horas críticas, el marco estima la necesidad de 2450 equipos pesados y 380 equipos ligeros. Se muestran tableros de la COP para distribución de daños, víctimas, ocupación y taxonomía de edificios y gestión de equipos. Los autores afirman que la COP basada en DT mejora la conciencia situacional y la asignación de recursos, pero no comparan con un método sin DT ni reportan tiempos de cálculo, de actualización de los tableros ni exactitud respecto de datos observados. Se describe también un ciclo de revisión posterior a la acción en el que los informes de los equipos de búsqueda y rescate y de los equipos médicos se almacenan en la plataforma, con lo cual el sistema acumula aprendizaje para futuras respuestas.

**Discusión y contribución.** Los autores argumentan que la evaluación rápida de daños aporta una cuantificación mejor que los mapas de peligro convencionales (como ShakeMap) y que las herramientas regionales como HAZUS, CAPRA u OpenQuake, que no ofrecen el nivel de detalle ni la capacidad operativa que necesita la coordinación de búsqueda y rescate. Sostienen que su enfoque es más rápido que las técnicas de teledetección. Revisan estudios de evaluación rápida con inteligencia artificial, redes sociales y criticidad de infraestructura, y de DT en cadenas de suministro. Concluyen que el DT como COP puede mejorar la capacidad de reacción y recuperación, siempre que se resuelvan los desafíos de exactitud de datos, integración, interoperabilidad, estandarización y cooperación de las autoridades.

**Limitaciones declaradas.** Declaradas: desafíos de exactitud de datos, integración y análisis, interoperabilidad y estandarización, privacidad y cooperación de las autoridades como condiciones para el éxito. No declaradas: los resultados son de un escenario simulado sin validación contra daños observados en 1999 ni contra otros eventos; no se describen las curvas de fragilidad ni la incertidumbre; no se comparan los resultados con métodos alternativos ni con tiempos de decisión sin DT; los 'datos en tiempo real' del resumen no se muestran en la demostración; la fase de recuperación y la actividad económica no se modelan.

**Trabajo futuro.** El texto no formula una sección de trabajo futuro detallada; se plantea implícitamente resolver la exactitud, integración e interoperabilidad de datos, y se establece como objetivo O-6 sugerir áreas de investigación futura y recomendaciones para responsables de política.

**Palabras clave.** Declaradas: common operating picture; digital twin; emergency response; seismic risk | Inferidas: gemelo digital, imagen operativa común, respuesta a emergencias, riesgo sísmico, evaluación rápida de daños, búsqueda y rescate, Kocaeli, falla de Anatolia del Norte, modelo 3D, interoperabilidad

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un gemelo digital de una ciudad, organizado como imagen operativa común y alimentado con datos de edificios, población, peligro y recursos, permite estimar de forma rápida los daños, la población afectada y las necesidades de búsqueda y rescate (en Kocaeli, alrededor de 58 000 edificios con daño extenso o completo y 2450 equipos pesados en 72 horas), y mejora la conciencia situacional y la asignación de recursos frente a mapas de peligro convencionales y a herramientas regionales de pérdidas.

**Antítesis identificada.** La evidencia es una demostración de escenario sin validación. Las cifras de daño, población y equipos dependen de supuestos de fragilidad y de GMPE que no se describen, no se contrastan con los daños observados del evento de 1999 y no incluyen incertidumbre. La afirmación de que la COP mejora la conciencia situacional y la asignación de recursos no se compara con un método sin DT ni se mide en tiempos o resultados de decisión. El resumen habla de datos en tiempo real, pero el caso es un escenario simulado. La superioridad frente a ShakeMap, HAZUS, CAPRA y OpenQuake se argumenta sin comparaciones cuantitativas, y la afirmación de ser más rápido que la teledetección no tiene tiempos reportados. El estudio se limita a la respuesta y no aborda la recuperación económica.

**Síntesis propuesta.** La contribución sostenible es una arquitectura de referencia y una demostración técnica de cómo los datos geoespaciales abiertos y municipales pueden integrarse en un DT-COP para estimar daños y necesidades de respuesta en una ciudad sísmica. La utilidad operativa queda como hipótesis, pendiente de validación con eventos reales y con usuarios. Para el corpus, el valor es alto en el eslabón de integración de datos y de decisión para la respuesta, y marca el siguiente paso que falta: extender la misma arquitectura a la fase de recuperación, con datos de empresas, cadenas de suministro y servicios, que el artículo menciona solo por el perfil logístico de Kocaeli.

**Áreas grises detectadas.**

1. Validación del escenario: el modelo reproduce el terremoto de Kocaeli de 1999 (Mw 7,6) y reporta 55 % de edificios con daño moderado o mayor y cerca de 60 % de la población con necesidad de refugio; el texto no compara con los daños y víctimas observados en 1999, ni con la distribución real de edificios del momento, ni reporta incertidumbre.
2. Datos en tiempo real: el resumen declara incorporación de datos en tiempo real, pero la demostración usa datos estáticos de catastro, población, relieve y OpenStreetMap integrados por API; no se describen sensores, latencia, frecuencia de actualización ni el efecto de la falta de conectividad después del evento.
3. Estimación de recursos: las cifras de 2450 equipos pesados y 380 ligeros para cumplir las 72 horas se derivan de un modelo de asignación (ecuación 4) cuyos parámetros, supuestos de productividad por equipo y disponibilidad real de equipos en Turquía no se presentan, de modo que la cifra no puede evaluarse.
4. Alcance de la fase: el estudio se centra en la respuesta, y la recuperación productiva, la reapertura de empresas y la logística de insumos, que son relevantes en una región con concentración de empleo logístico, no se modelan.

**Puntos oscuros aclarados.** Llama la atención que el artículo contraste su evaluación rápida con ShakeMap, HAZUS, CAPRA y OpenQuake sin comparar resultados con ninguna de ellas, y que afirme mayor rapidez que la teledetección sin reportar tiempos. También es notable que las cifras de edificios y de población en daño completo y extenso sumen alrededor de 58 000 edificios y 485 000 personas sin contexto del total de la región ni validación con 1999, de modo que no se puede juzgar si son plausibles. El resumen incluye 'datos en tiempo real' y 'transformar las prácticas', pero el caso es un escenario simulado con datos estáticos. La estimación de 2450 equipos pesados se presenta como resultado del marco sin indicar la fuente de los parámetros. Por último, el artículo destaca el carácter logístico de Kocaeli como rasgo económico de la región, pero no incorpora ese rasgo en ninguna variable del modelo, lo que deja sin explorar la dimensión de continuidad empresarial.

**Ideas propositivas novedosas.**

1. Extender el DT-COP a la fase de recuperación productiva: añadir al modelo 3D de Kocaeli una capa de empresas (sector, empleo, dependencia de proveedores y de acceso logístico) y reglas de decisión que conviertan el estado de daño de cada edificio e infraestructura vial en tiempo de reapertura esperado. Se podría validar con datos de reapertura de empresas tras el evento de 1999 o de 2023 y estimar el valor de la COP como reducción de días de cierre por empresa, que hoy no se mide en ninguno de los documentos del corpus. El resultado serviría además para priorizar qué empresas y servicios de la región logística de Kocaeli requieren acceso a vías y a energía en las primeras semanas.
2. Prueba de validación retrospectiva del escenario: ejecutar el mismo flujo con los datos de edificios y población de 1999 y comparar los daños, víctimas y recursos desplegados con los registros oficiales, reportando error por distrito e incertidumbre. Con ello se establecería la confianza de las cifras de 55 % de daño y de equipos requeridos, se contrastaría la afirmación de superioridad sobre HAZUS y ShakeMap con un benchmark cuantitativo y se definiría el umbral de precisión necesario para decidir despliegues, con indicadores de error por distrito y por tipología constructiva.

**Relaciones poco exploradas.**

1. Gemelo urbano sísmico (comparte objeto con) D034: ambos modelan una ciudad con sismo y estiman daño por edificio para decisiones de rescate; D034 usa 6466 edificios de Pingluo y D048 una región con decenas de miles de edificios, y ninguno valida el daño con observaciones ni modela la recuperación.
2. Gemelo digital en gestión de desastres (se relaciona con) D019 y D042: D019 y D042 revisan tecnologías emergentes, IoT y UAV para terremotos, y D048 aporta una implementación concreta de COP con DT en la fase de respuesta.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 7/10 — Aporta una arquitectura concreta de gemelo digital como COP para respuesta sísmica, con integración de datos abiertos y municipales, evaluación rápida de daños y estimación de población y de equipos de rescate, en una región industrial y logística. Su valor para el corpus es alto por la coincidencia con gemelo, sismo y decisión; se reduce por la falta de validación del escenario, la ausencia de datos en tiempo real en la demostración, la comparación no cuantitativa con otras herramientas y la omisión de la recuperación económica.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Conclusión no respaldada por la evidencia (Se afirma que la COP mejora la conciencia situacional y la asignación de recursos y supera a otras herramientas sin comparación cuantitativa (Resumen, p. 1; Sec. 4, p. 16)); Equívoco entre simulación y operación (Se habla de datos en tiempo real y de transformación de las prácticas, pero la demostración es un escenario con datos estáticos (Resumen, p. 1; Sec. 3, p. 12-14)); Apelación a la tecnología (Se destaca el potencial del DT sin evaluar costos, capacidades institucionales ni resultados de decisión (Sec. 5, p. 17-18))
- **Bradford-Hill:** No aplica: es una demostración técnica con escenario simulado; no se estima la relación causal entre el uso de la COP y mejores resultados de respuesta.
- **TRL asignado:** 4 — 'This chapter presents the findings from a simulation of the 1999 Kocaeli earthquake, conducted to evaluate the capabilities of the proposed digital twin–common operating picture (DT–COP)' (p. 12)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (20 páginas más referencias). La extracción duplica y entrelaza líneas de dos columnas; las cifras de resultados se tomaron del texto de las secciones 3.2 y 4. Las páginas citadas siguen los marcadores del PDF (la numeración interna de la revista difiere en uno). La herramienta de modelado 3D declarada es Autodesk InfraWorks.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un gemelo digital de una ciudad, organizado como imagen operativa común y alimentado con datos de edificios, población, peligro y recursos, permite estimar de forma rápida los daños, la población afectada y las necesidades de búsqueda y rescate (en Kocaeli, alrededor de 58 000 edificios con daño extenso o completo y 2450 equipos pesados en 72 horas), y mejora la conciencia situacional y la asignación de recursos frente a mapas de peligro convencionales y a herramientas regionales de pérdidas.  | La evidencia es una demostración de escenario sin validación. Las cifras de daño, población y equipos dependen de supuestos de fragilidad y de GMPE que no se describen, no se contrastan con los daños observados del evento de 1999 y no incluyen incertidumbre. La afirmación de que la COP mejora la conciencia situacional y la asignación de recursos no se compara con un método sin DT ni se mide en tiempos o resultados de decisión. El resumen habla de datos en tiempo real, pero el caso es un escenario simulado. La superioridad frente a ShakeMap, HAZUS, CAPRA y OpenQuake se argumenta sin comparaciones cuantitativas, y la afirmación de ser más rápido que la teledetección no tiene tiempos reportados. El estudio se limita a la respuesta y no aborda la recuperación económica.  | La contribución sostenible es una arquitectura de referencia y una demostración técnica de cómo los datos geoespaciales abiertos y municipales pueden integrarse en un DT-COP para estimar daños y necesidades de respuesta en una ciudad sísmica. La utilidad operativa queda como hipótesis, pendiente de validación con eventos reales y con usuarios. Para el corpus, el valor es alto en el eslabón de integración de datos y de decisión para la respuesta, y marca el siguiente paso que falta: extender la misma arquitectura a la fase de recuperación, con datos de empresas, cadenas de suministro y servicios, que el artículo menciona solo por el perfil logístico de Kocaeli.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'COP' es la imagen operativa común compartida por los actores de respuesta; 'RDA' es la evaluación rápida de daños con GMPE y fragilidad; 'golden hours' son las 72 horas críticas para búsqueda y rescate.
- **P2 Supuestos:** Supone que las curvas de fragilidad y el catastro representan el comportamiento real del parque edificado, que los datos del municipio estarán disponibles y precisos tras el evento y que un tablero único mejora las decisiones.
- **P3 Evidencia:** La evidencia es un escenario simulado del terremoto de 1999 con tableros y cifras de daño, población y equipos, sin validación ni comparación.
- **P4 Consecuencias:** Si es cierto, los responsables pueden estimar daños y recursos en horas y coordinar con una imagen común; si es falso, pueden asignar recursos con base en cifras no verificadas.
- **P5 Contraejemplos:** No se examinan datos reales de daños de 1999, otras herramientas aplicadas al mismo escenario, fallas de conectividad ni la recuperación económica.
- **P6 Alternativas:** Alternativas: que un SIG y un mapa de daños bastaran; que la calidad del catastro limite el resultado; que la coordinación institucional sea el factor determinante.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Eventos sísmicos compilados en el catálogo | 1786 | eventos | 1900-2024, radio de 200 km y profundidad de 100 km | Sec. 3.1, p. 13 | Texto | Alta | Tipos de magnitud mb, ms, Mw, ML y MD |
| Resolución del modelo de elevación digital | 12,5 | m | ALOS PALSAR de código abierto | Sec. 3.1, p. 13 | Texto | Alta | Base del modelo 3D |
| Rango de aceleración pico del suelo (PGA) | 0,05 a 1,1 | g | Escenario del evento de Kocaeli | Sec. 3.2, p. 14 | Texto | Alta | Sin validación |
| Edificios con daño moderado a colapso total | 55 | % | Escenario simulado | Sec. 3.2, p. 14 | Texto | Alta | Sin comparación con 1999 |
| Población que requeriría refugio y protección | 60 | % | Casi 60 % según el escenario | Sec. 3.2, p. 14 | Texto | Media | Cifra aproximada |
| Edificios con daño completo / población afectada | 18 000 / 145 000 | edificios / personas | Estimación preliminar | Sec. 4, p. 16 | Texto | Media | Sin incertidumbre |
| Edificios con daño extenso / población afectada | 40 000 / 340 000 | edificios / personas | Estimación preliminar | Sec. 4, p. 16 | Texto | Media | Sin incertidumbre |
| Equipos de búsqueda y rescate para 72 horas | 2450 / 380 | equipos pesados / ligeros | Estimación del marco | Sec. 4, p. 16 | Texto | Media | Parámetros no presentados |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'This chapter presents the findings from a simulation of the 1999 Kocaeli earthquake, conducted to evaluate the capabilities of the proposed digital twin–common operating picture (DT–COP)' (p. 12) | Prueba de concepto en laboratorio computacional con datos reales de catastro y escenario simulado en Autodesk InfraWorks; sin validación ni despliegue operativo. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'a powerful tool can be created that can help save lives, reduce suffering, and minimize damage during times of crisis' (p. 18) | Beneficio afirmado sin análisis de costos, mercado ni modelo de negocio. |
| IRL | 3 | Sí | 'The structural data and population datasets were obtained from the KBB databases and integrated into the model using APIs where applicable' (p. 13) | Integración de varias fuentes por API en un modelo; sin pruebas de interoperabilidad ni de actualización posterior al evento. |
| DRL | 3 | Sí | 'Timely and well-informed decision-making is at the core of effective disaster management' (p. 1) | Necesidad argumentada con literatura; sin estudio de demanda de usuarios. |
| SRL | 1.33 | Sí | Componentes: Modelo 3D base con datos abiertos y municipales (TRL 4), Evaluación rápida de daños y asignación de recursos (TRL 4), COP con tableros (TRL 4) | SRL=Σ(TRLi×IRLij)/4 términos ordenados = 12.0; ÷9 → 1.33; nivel acotado a [1,9] = 1.33 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 3 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 3 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Alta · TRL 4 con BRL 1 e IRL 3: escenario simulado sin validación, sin datos en tiempo real demostrados, sin costos ni evaluación con usuarios. · Estrategia de salida: Validación retrospectiva con daños de 1999, prueba con datos en vivo y evaluación de decisiones con y sin COP.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Conclusión no respaldada por la evidencia | Se afirma que la COP mejora la conciencia situacional y la asignación de recursos y supera a otras herramientas sin comparación cuantitativa (Resumen, p. 1; Sec. 4, p. 16) | Superioridad argumentada, no medida |
| Equívoco entre simulación y operación | Se habla de datos en tiempo real y de transformación de las prácticas, pero la demostración es un escenario con datos estáticos (Resumen, p. 1; Sec. 3, p. 12-14) | Alcance del caso menor que el anunciado |
| Apelación a la tecnología | Se destaca el potencial del DT sin evaluar costos, capacidades institucionales ni resultados de decisión (Sec. 5, p. 17-18) | Beneficio asumido |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Uso de DT-COP → mejor asignación de recursos y menor tiempo de respuesta | Argumento de diseño y escenario | Plausibilidad | Comparación con y sin COP, datos de decisión | Calidad de datos, coordinación institucional, capacidad de los equipos | 1 | Hipótesis no probada |
| Intensidad sísmica y suelo → daño del parque edificado | GMPE, Vs30 y fragilidad en escenario | Coherencia con ingeniería sísmica | Validación con daños de 1999 | Calidad del catastro, tipología constructiva | 3 | Mecanismo establecido, magnitud sin validar |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Validación retrospectiva del escenario y análisis de incertidumbre | Crítico | Media | 9 |
| Conocimiento | Extensión a la recuperación productiva, empresas y cadenas de suministro | Crítico | Media | 9 |
| Tecnológico | Datos en tiempo real, conectividad degradada y actualización posterior al evento | Crítico | Media | 8 |
| Mercado | Costos, capacidades institucionales y adopción por autoridades locales | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Concepto y evolución de gemelos digitales | Diagrama | Tipos de DT | No aplica | Media |
| Fig. 6 | Flujo de trabajo conceptual de respuesta de emergencias con DT | Diagrama | Decisión por umbrales y revisión posterior | No aplica | Alta |
| Fig. 8 | Modelo 3D de área de interés (Çayırova y área de la bahía) | Imagen 3D | Salida del modelo base | No aplica | Media |
| Fig. 9 | Distribución de Vs30 y falla de Anatolia del Norte | Mapa | Condiciones de sitio y fallas | No aplica | Media |
| Fig. 10-11 | Ocupación y taxonomía de edificios en la COP | Capturas de tablero | Datos municipales | No aplica | Media |
| Fig. 12 | Distribución de daño y necesidad de refugio | Gráficos | 55 % de daño moderado o mayor; 60 % de población | 55 %; 60 % | Alta |
| Fig. 14-15 | Vista general de la COP y gestión de equipos de búsqueda y rescate | Capturas de tablero | Distribución de daño y equipos | No aplica | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| HAZUS | Estados Unidos | Gobierno | Estimación regional de pérdidas por peligro | Marco consolidado | Sin detalle operativo para búsqueda y rescate (según el artículo) | Estable |
| CAPRA y OpenQuake | No especificado en documento | Academia | Evaluaciones regionales de riesgo | Código abierto | Sin datos en tiempo real de alta resolución (según el artículo) | Estable |
| ShakeMap | Estados Unidos | Gobierno | Mapas de intensidad tras un evento | Rapidez y estandarización | Sin capacidades operativas de coordinación (según el artículo) | Estable |

### B.9 Variables econométricas y vacíos

- **Y:** No aplica: resultados de escenario sin variable de resultado económica
- **X:** Intensidad sísmica simulada y atributos de edificios y población
- **Z (controles):** Condiciones de sitio (Vs30), tipología estructural, ocupación
- **Datos:** Catálogo de 1786 eventos; catastro y población de Kocaeli; escenario del evento de 1999
- **Método:** GMPE, fragilidad y matrices de probabilidad de daño; modelo de asignación de recursos
- **Efecto reportado:** 55 % de edificios con daño moderado o mayor; 2450 equipos pesados y 380 ligeros
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin análisis de sensibilidad ni validación

| Vacío | Tipo | Descripción |
|---|---|---|
| V-048-01 | TERR | Kocaeli (Turquía), zona logística e industrial de la falla de Anatolia del Norte; sin otras regiones |
| V-048-02 | POBL | Población general y equipos de rescate; sin empresas ni sectores económicos |
| V-048-03 | TEMP | Primeras 72 horas de la respuesta; sin recuperación ni reconstrucción |
| V-048-04 | MET | Escenario sin validación; fragilidad y parámetros de asignación sin describir |
| V-048-05 | VAR | Faltan variables de funcionalidad, reapertura de empresas, cadena de suministro y costos |
| V-048-06 | TEOR | Gemelo digital y COP; sin teoría de recuperación económica ni de resiliencia de empresas |
| V-048-07 | CAUS | Sin evidencia causal del efecto de la COP sobre decisiones o resultados |
