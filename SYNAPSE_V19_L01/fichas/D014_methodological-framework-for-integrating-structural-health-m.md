# FB-L01-014 | D014 — Methodological framework for integrating structural health monitoring and digital-twin models for seismic assessment of heritage buildings: Case study of Basilica Maria Auxiliadora, Lima, Peru

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S2352012425019307-main.pdf` · 22 páginas · Relevancia para el eje del corpus: **Adyacente** (Integra monitoreo de salud estructural (SHM), gemelo digital numérico y respuesta sísmica de un edificio patrimonial, con marco de 'resiliencia circular inteligente' para gestión del riesgo de desastres; no modela recuperación productiva ni dimensión empresarial.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-014 / D014
- **Tipo de recurso:** Artículo científico (journal peer-reviewed)
- **Referencia APA 7:** Aroquipa, H., Hurtado, A., & Angel, C. (2025). Methodological framework for integrating structural health monitoring and digital-twin models for seismic assessment of heritage buildings: Case study of Basilica Maria Auxiliadora, Lima, Peru. *Structures*, *80*, Article 110115. https://doi.org/10.1016/j.istruc.2025.110115
- **Autores:** Aroquipa, Hector (57725096600); Hurtado, Alvaro (56448254200); Angel, Christiam (57210338425)
- **Afiliaciones:** Research Group on Numerical and Computational Methods, Graphic and Scientific Computing, Instituto de Investigación Científica, Universidad de Lima, Av. Javier Prado Este 4600, Santiago de Surco, 15023, Peru; Civil Engineering School, Universidad Nacional Autónoma de Tayacaja Daniel Hernández Morillo, Tayacaja, Huancavelica, Peru; School of Architecture, Urban Planning and Construction Engineering, Politecnico di Milano, Milan, Italy
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Structures · vol. 80
- **Identificador persistente:** DOI 10.1016/j.istruc.2025.110115 · ISSN 23520124
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-105015038763&doi=10.1016%2fj.istruc.2025.110115&partnerID=40&md5=5c4d6709efc2095d21642ccd5615904a
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 1

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Proponer un marco metodológico para integrar sistemas de monitoreo de salud estructural (SHM) con modelos numéricos de gemelo digital (GD) en la evaluación sísmica de estructuras patrimoniales, y aplicarlo a la Basílica de María Auxiliadora en Lima, Perú. El propósito operativo de la fase presentada es construir y calibrar el modelo virtual, caracterizar las demandas de ingeniería mediante análisis tiempo-historia con registros reales, definir la ubicación y las características de los sensores y obtener funciones de transferencia con aprendizaje profundo que conviertan señales de movimiento en esfuerzos en los muros.

**Pregunta de investigación.** El texto no formula preguntas de investigación explícitas. Las preguntas implícitas son: dónde ubicar sensores y con qué rango de operación para alimentar en tiempo real un gemelo digital de una estructura patrimonial; si un modelo de aprendizaje profundo entrenado con salidas del modelo numérico puede estimar esfuerzos en los muros a partir de aceleraciones, velocidades y desplazamientos; y si el modelo reproduce el daño histórico documentado.

**Marco teórico.** El marco combina la ingeniería sísmica basada en desempeño de edificios existentes, el monitoreo de salud estructural y el concepto de gemelo digital como acoplamiento entre un mundo físico instrumentado y un modelo virtual actualizado. Añade el concepto propio de 'resiliencia circular inteligente' (ICR), definido en tres etapas (comprender el riesgo sísmico, implementar mitigación y responder a eventos) y tres niveles (experticia institucional, gestión del riesgo de infraestructura y monitoreo en tiempo real), orientado a ciudades inteligentes y a la reducción del riesgo de desastres. El paradigma es de ingeniería computacional con orientación a la instrumentación, no de ciencias sociales ni de gestión empresarial; la seis fases de la metodología parten de la virtualización del edificio y terminan en un sistema de alerta temprana.

**Metodología.** La basílica (construida entre 1916 y 1924, con unos 2000 m2 de planta, 70 m por 30 m y torre de 56 m) se digitalizó con escáner láser y modelo BIM. Se desarrollaron dos modelos: uno lineal elástico de varios grados de libertad en SAP2000 y otro no lineal de elementos discretos en 3DEC versión 9, con aproximadamente 4500 bloques y 161.000 zonas de contacto. Las propiedades de los materiales se tomaron de archivos y estudios previos, sin ensayos destructivos por razones de conservación; la calibración con vibración ambiental queda para trabajo futuro. Se calibraron masa sísmica, periodos fundamentales y formas modales entre ambos modelos y se contrastó el daño simulado con los reportes de los sismos de 1940 y de Ica 2007. Se seleccionaron registros sísmicos a partir de un catálogo de 5745 eventos, de los cuales 75 tenían magnitud de momento de al menos 6,0 y 12 contaban con información; el texto menciona 34 registros en el resumen, una lista final de 33 y cinco análisis tiempo-historia no lineales. Los resultados se condensaron en gráficos de intensidad, duración y frecuencia (IDF) de parámetros de demanda, con cuatro regiones de interés. Para las funciones de transferencia se entrenaron 24 modelos LSTM con entrada múltiple y salida simple, con partición 70/15/15, ventanas de 4 s con traslape de 0,5 s y error cuadrático medio (RMSE) como métrica.

**Resultados principales.** El análisis modal arrojó 220 modos y periodos fundamentales de 0,39 s en la dirección X y 0,38 s en la dirección Y, con una masa sísmica cercana a 21.400 kN y una diferencia menor al 5 % entre la estimación manual y la del modelo BIM. El modelo no lineal reprodujo el patrón de agrietamiento de las bóvedas de concreto armado observado tras el sismo de Ica de 2007 (grietas de 0,01 a 4 mm y una de 7 mm), con un módulo de ruptura de 2,84 MPa, y concluyó que la mayoría de los registros no produce daño significativo, lo que concuerda con el estado de salud del edificio. Los gráficos IDF mostraron duraciones máximas sostenidas de 1,3 s, 0,5 s y 0,2 s en rangos de intensidad baja, alta y extrema. Se definieron 25 puntos de control para sensores, con desplazamientos horizontales críticos de hasta 0,40 m (en promedio 3,0 cm durante el 60 % de la duración de los registros), rango de frecuencias de 1,5 a 25 Hz, aceleraciones esperadas de unos 1,40 g y velocidades de hasta 0,80 m/s. Los modelos LSTM alcanzaron RMSE mayoritariamente inferiores a 0,1, con mejor desempeño en niveles bajos (9,38 m y 20,31 m, con valores entre 0,018 y 0,10) que en niveles altos (36,15 m y 39,65 m, hasta 0,283), y la inclusión de la componente vertical mejoró varias configuraciones. Se recomienda sensores triaxiales.

**Discusión y contribución.** Los autores sostienen que la metodología permite estandarizar la distribución de sensores a partir de la respuesta numérica, que el modelo reproduce el comportamiento histórico del edificio y que las funciones de transferencia con aprendizaje profundo son viables para convertir movimientos en esfuerzos. Reconocen que la validación actual descansa en el desempeño histórico y la consistencia analítica, que la calibración con datos de sensores es una etapa pendiente y que el artículo cubre solo dos de seis fases (virtualización y, parcialmente, obtención de datos). Plantean que la metodología se puede extender a otras estructuras civiles y que, a futuro, se integrará en un sistema de alerta temprana dentro del marco de resiliencia circular inteligente. La discusión no examina la sensibilidad a las propiedades de los materiales más allá de una mención, ni el costo de la instrumentación.

**Limitaciones declaradas.** Propiedades de materiales sin ensayos propios ni calibración con vibración ambiental; ausencia de datos reales de sensores; entrenamiento de los modelos de aprendizaje profundo con salidas del propio modelo numérico; un solo edificio; cinco análisis tiempo-historia; datos disponibles solo previa solicitud.

**Trabajo futuro.** Despliegue de sensores triaxiales en los puntos recomendados, calibración del modelo con datos experimentales de vibración, validación experimental de los puntos de control y de las funciones de transferencia, y desarrollo completo de las fases 3 a 6 (sensado, integración con el gemelo, alerta temprana y operación en la ciudad).

**Palabras clave.** Declaradas: Digital twin; FEM numerical models; Heritage buildings; Intelligent circular resilience; Seismic performance evaluation; Structural health monitoring | Inferidas: gemelo digital, monitoreo de salud estructural, edificio patrimonial, análisis tiempo-historia, ubicación de sensores, LSTM, resiliencia circular inteligente, alerta temprana, mampostería, Lima

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un modelo numérico calibrado de una estructura patrimonial, combinado con gráficos IDF de las demandas y funciones de transferencia de aprendizaje profundo, permite definir de forma sistemática dónde y con qué características instalar sensores para alimentar un gemelo digital, como primer paso de una resiliencia circular inteligente en ciudades.

**Antítesis identificada.** El gemelo digital descrito aún no existe: no hay sensores instalados, no hay datos de campo y las funciones de transferencia se entrenan con las salidas del mismo modelo que pretenden aproximar, de modo que el error reportado mide la capacidad del LSTM de reproducir un modelo numérico y no de estimar esfuerzos reales. La validación del modelo descansa en una comparación cualitativa con daño histórico y con propiedades tomadas de la literatura, sin ensayos in situ, de manera que la incertidumbre de materiales de la mampostería, que domina la respuesta, queda sin cuantificar. Los conteos de registros sísmicos (34, 33, 12 y 5) no son consistentes entre secciones, y el marco de ICR se enuncia sin indicadores ni validación. La generalización a otras estructuras y a ciudades inteligentes carece de evidencia, y el título sugiere una integración más avanzada que la reportada.

**Síntesis propuesta.** La contribución verificable es un procedimiento de diseño de instrumentación basado en simulación: modelo calibrado, registros reales, gráficos IDF y rangos de sensores justificados, útil como protocolo previo a la instalación. Debe leerse como estudio de factibilidad del componente virtual (nivel de prueba de concepto analítica) y no como gemelo digital operativo. Para el corpus, la síntesis consiste en tratar este tipo de trabajo como el eslabón físico de una cadena que debe prolongarse hacia el efecto sobre la continuidad de operaciones: asociar los estados de daño estimados por el gemelo con tiempos de inhabilitación y costos, de modo que el valor de la instrumentación se exprese en reducción esperada del tiempo de cierre y no solo en precisión de la respuesta estructural.

**Áreas grises detectadas.**

1. Circularidad de la validación: los modelos LSTM se entrenan y evalúan con salidas simuladas del modelo 3DEC, por lo que un RMSE bajo no demuestra capacidad de estimar esfuerzos reales con ruido, deriva y fallas de sensor; el texto reconoce que la calibración con datos físicos es futura.
2. Inconsistencia en el conjunto de registros sísmicos: el resumen menciona 34 registros, el texto una lista final de 33 y el análisis tiempo-historia no lineal usa cinco; no queda claro qué registros sustentan cada resultado ni cómo se escalaron.
3. Incertidumbre de materiales: las propiedades de la mampostería y del concreto provienen de archivos y de estudios previos, sin ensayos in situ ni análisis de sensibilidad completo, aunque la respuesta no lineal y el patrón de agrietamiento dependen de ellas.
4. Alcance de la resiliencia circular inteligente: el marco ICR se declara con tres etapas y tres niveles, pero no define indicadores, actores ni mecanismos de participación público-privada, y el artículo solo cubre dos de seis fases de la metodología.

**Puntos oscuros aclarados.** Llama la atención que el artículo presente como 'gemelo digital' un sistema cuyo componente físico no existe todavía y que las funciones de transferencia se evalúen mejor justamente en los niveles bajos del edificio, donde la respuesta es menos compleja y de menor interés para detectar daño en la torre y en las bóvedas. Una explicación plausible es que el RMSE normalizado favorece las señales de menor amplitud y variabilidad, y que la dificultad de predecir esfuerzos en niveles altos refleja efectos no lineales y de amplificación que el modelo de entrada con tres componentes captura mal. Esto sugiere que la ubicación de sensores recomendada por el desempeño del LSTM (priorizar niveles bajos) puede entrar en conflicto con la ubicación recomendada por la demanda de ingeniería (regiones de interés en la torre y la nave), de modo que la decisión de instrumentación necesita un criterio conjunto de información sobre daño y de costo, y no solo la minimización del error de reconstrucción. Además, la ausencia de cualquier consideración económica o de continuidad de uso indica que el marco ICR se concentra en la protección del bien y no en la recuperación de la actividad que alberga.

**Ideas propositivas novedosas.**

1. Criterio conjunto de ubicación de sensores: formular la selección de los 25 puntos de control como un problema de optimización multiobjetivo que combine la información sobre estados de daño (derivas e índices de esfuerzo de los gráficos IDF), el error de reconstrucción del LSTM y el costo de instalación y mantenimiento, y comparar el resultado con la ubicación propuesta por los autores. Fundamento: los autores observan que la fidelidad de la señal es mayor en niveles bajos, pero las regiones de interés críticas están en la torre. Verificabilidad: repetir el ejercicio con el mismo modelo 3DEC y validar con una campaña corta de vibración ambiental en la basílica. Utilidad: ofrece un método transferible para instrumentar edificios con presupuesto limitado.
2. Conversión del gemelo estructural en indicador de continuidad: asociar los estados de daño estimados por el gemelo (grietas, derivas, esfuerzos) con curvas de funcionalidad y tiempos de inhabilitación, y con el costo de interrupción de las actividades que alberga el edificio (culto, turismo, servicios), para obtener un tiempo de recuperación esperado por escenario. Fundamento: el artículo sitúa el gemelo en un marco de resiliencia circular pero no vincula daño con uso. Verificabilidad: reconstrucción retrospectiva del sismo de Ica de 2007 con registros de uso y reparación disponibles. Utilidad: permite justificar económicamente la instrumentación y vincula este eje con el tema de recuperación productiva del corpus.

**Relaciones poco exploradas.**

1. Calidad de las propiedades de los materiales (condiciona) la fiabilidad de las funciones de transferencia entrenadas con el modelo: si la rigidez y la resistencia reales difieren de las supuestas, la relación entre movimientos y esfuerzos aprendida no se traslada a la estructura física.
2. Ubicación de sensores en niveles bajos (reduce) el error de reconstrucción pero (puede limitar) la detección de daño en la torre y en las bóvedas, donde el artículo identifica las regiones de mayor demanda.

**Robustez argumentativa:** 3.9/10 (ponderación 30/30/25/15) — consistencia lógica 5/10; calidad de la evidencia 4/10; validez de inferencias causales 3/10; generalizabilidad 3/10.

**Valor estratégico:** 6/10 — Aporta un procedimiento detallado y reproducible en su lógica para definir instrumentación de un gemelo digital sísmico en estructuras de mampostería, con cifras de rango de sensores y modelos de transferencia. Su valor para el corpus es como referencia del componente físico y de datos del gemelo; se reduce porque no hay datos de campo, ni validación de la red de sensores, ni vínculo con costos o con continuidad de operaciones.

**Conexiones inter-documentales.**

- **COMPLEMENTA** D020 (IoT, SHM y resiliencia sísmica de edificios): D014 define dónde instalar sensores en un edificio patrimonial y D020 asocia componentes de IoT con resiliencia sísmica; ambos de ingeniería de edificios con IoT [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 25 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Equivocación (uso de 'gemelo digital') (El título y el resumen presentan un marco de gemelo digital cuando el componente físico y el flujo de datos reales no existen todavía (Resumen, p. 1; Sec. 5, p. 20)); Petición de principio (circularidad de la validación) (Las funciones de transferencia se entrenan con salidas del modelo numérico y su bajo RMSE se interpreta como respaldo para el uso con datos de campo (Sec. 4.6, p. 14)); Generalización apresurada (Se afirma que la metodología puede extenderse a cualquier estructura civil con ajustes, a partir de un solo edificio (Sec. 5, p. 20))
- **Bradford-Hill:** No aplica: no se estima una relación causal con datos observacionales; la relación entre ubicación de sensores y capacidad de detección de daño es una hipótesis de diseño sin contraste empírico, sin gradiente ni experimento.
- **TRL asignado:** 3 — 'tri-axial sensors are meant to be installed on-site in future research' (p. 16)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (22 páginas); el listado de referencias aparece parcial en la extracción (referencias 12 a 38) y los anexos suplementarios no estaban disponibles. Los conteos de registros sísmicos (34, 33, 12 y 5) difieren entre secciones y se reportan tal como figuran. Los valores de RMSE se leyeron de las figuras 27 y 28 transcritas por extracción de texto.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un modelo numérico calibrado de una estructura patrimonial, combinado con gráficos IDF de las demandas y funciones de transferencia de aprendizaje profundo, permite definir de forma sistemática dónde y con qué características instalar sensores para alimentar un gemelo digital, como primer paso de una resiliencia circular inteligente en ciudades.  | El gemelo digital descrito aún no existe: no hay sensores instalados, no hay datos de campo y las funciones de transferencia se entrenan con las salidas del mismo modelo que pretenden aproximar, de modo que el error reportado mide la capacidad del LSTM de reproducir un modelo numérico y no de estimar esfuerzos reales. La validación del modelo descansa en una comparación cualitativa con daño histórico y con propiedades tomadas de la literatura, sin ensayos in situ, de manera que la incertidumbre de materiales de la mampostería, que domina la respuesta, queda sin cuantificar. Los conteos de registros sísmicos (34, 33, 12 y 5) no son consistentes entre secciones, y el marco de ICR se enuncia sin indicadores ni validación. La generalización a otras estructuras y a ciudades inteligentes carece de evidencia, y el título sugiere una integración más avanzada que la reportada.  | La contribución verificable es un procedimiento de diseño de instrumentación basado en simulación: modelo calibrado, registros reales, gráficos IDF y rangos de sensores justificados, útil como protocolo previo a la instalación. Debe leerse como estudio de factibilidad del componente virtual (nivel de prueba de concepto analítica) y no como gemelo digital operativo. Para el corpus, la síntesis consiste en tratar este tipo de trabajo como el eslabón físico de una cadena que debe prolongarse hacia el efecto sobre la continuidad de operaciones: asociar los estados de daño estimados por el gemelo con tiempos de inhabilitación y costos, de modo que el valor de la instrumentación se exprese en reducción esperada del tiempo de cierre y no solo en precisión de la respuesta estructural.  | 3.9/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Gemelo digital' es un modelo virtual de la estructura acoplado a sensores que lo actualizan; 'resiliencia circular inteligente' es un marco de tres etapas y tres niveles sin indicadores definidos.
- **P2 Supuestos:** Supone que el modelo con propiedades de la literatura representa la estructura, que las salidas simuladas son un sustituto adecuado de datos reales para entrenar las funciones de transferencia y que los registros elegidos cubren la demanda esperada.
- **P3 Evidencia:** La evidencia es la comparación cualitativa con daño histórico, la coincidencia de periodos y masa entre modelos, y el RMSE de modelos LSTM entrenados con salidas simuladas; no hay datos de sensores.
- **P4 Consecuencias:** Si es cierto, instrumentar un edificio patrimonial puede planificarse antes de instalar sensores y con rangos definidos; si es falso, se podrían instalar sensores en puntos y con características no adecuadas para detectar daño real.
- **P5 Contraejemplos:** No se discuten casos de edificios patrimoniales con redes de sensores de bajo costo que hayan logrado detección de daño sin un gemelo numérico detallado, ni la comparación con ubicación óptima por métodos de teoría de la información.
- **P6 Alternativas:** Alternativas: que un modelo más simple calibrado con vibración ambiental sea suficiente; que la dispersión de materiales explique el desempeño más que la arquitectura de la red; que el valor del gemelo dependa de datos de uso y no solo de estructura.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Área aproximada del edificio | 2000 | m2 | Planta de unos 70 m por 30 m; torre de 56 m | Sec. 2-3, p. 5-7 | Texto | Media | Cifra aproximada del texto |
| Bloques en el modelo 3DEC | 4500 | bloques | Aproximadamente; 161.000 zonas de contacto | Sec. 1, p. 4 | Texto | Alta | Modelo de elementos discretos |
| Registros en el catálogo inicial | 5745 | registros | Catálogo del Instituto Geofísico del Perú | Sec. 3, p. 5 | Texto | Alta | Selección posterior por magnitud y disponibilidad |
| Registros finales y análisis no lineales | 33 / 5 | registros | Resumen indica 34; texto indica lista final de 33 y 5 análisis tiempo-historia | Resumen, p. 1; Sec. 3, p. 6; Sec. 1, p. 4 | Texto | Media | Inconsistencia de conteos |
| Periodo fundamental | 0,39 / 0,38 | s | Dirección X / dirección Y | Sec. 4.1, p. 11-12 | Texto | Alta | Calibrado entre SAP2000 y 3DEC |
| Masa sísmica | 21400 | kN | Diferencia menor al 5 % entre estimación manual y BIM | Sec. 4.1, p. 10-11 | Texto | Alta | Estimación del analista de los autores |
| Puntos de control para sensores | 25 | puntos | Definidos y validados con el modelo numérico | Sec. 5, p. 19 | Texto | Alta | Sin instalación en campo |
| Desplazamiento horizontal crítico | 0,40 | m | Promedio 3,0 cm durante el 60 % de la duración de los registros | Sec. 5, p. 19 | Texto | Alta | Resultado del modelo no lineal |
| Rango de frecuencia de sensores | 1,5 a 25 | Hz | Límite superior asociado a 80 % de participación de masa | Sec. 5, p. 20 | Texto | Alta | Derivado del análisis modal |
| Aceleración máxima esperada | 1,40 | g | Velocidades hasta 0,80 m/s | Sec. 5, p. 20 | Texto | Alta | Resultado de modelo, no de sensor |
| Modelos LSTM entrenados | 24 | modelos | Partición 70/15/15; ventanas de 4 s con traslape de 0,5 s | Sec. 4.6, p. 14 | Texto | Alta | Entrada múltiple y salida simple |
| RMSE de funciones de transferencia | 0,018 a 0,283 | adimensional | Menor en niveles de 9,38 m y 20,31 m; mayor en 36,15 m | Fig. 27-28, p. 20 | Gráfico/Texto | Media | Rango recopilado de la figura, no de una tabla |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 3 | Sí | 'tri-axial sensors are meant to be installed on-site in future research' (p. 16) | Prueba de concepto analítica del componente virtual con modelo calibrado de forma cualitativa; sin prototipo físico ni datos de sensores. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'Data will be made available on request' (p. 21) | Sin evidencia de mercado, modelo de negocio ni usuario pagador; financiado por fondos públicos de desarrollo regional. |
| IRL | 2 | Sí | 'a primer analysis of the TF uses the virtual world results due to the lack of existing recorded data' (p. 4) | Integración entre modelo y sensores solo planificada; las funciones de transferencia se entrenan con salidas simuladas. |
| DRL | 2 | Sí | 'It is worth noting that this article solely addresses two phases of the methodology' (p. 20) | Necesidad de instrumentar edificios patrimoniales argumentada a partir de literatura, sin estudio de demanda ni cliente identificado. |
| SRL | 1.0 | Sí | Componentes: Modelo numérico calibrado 3DEC/SAP2000 (TRL 4), Funciones de transferencia LSTM (TRL 3) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 7.0; ÷9 → 0.78; nivel acotado a [1,9] = 1.00 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | -1 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 3 con BRL 1 e IRL 2: prueba de concepto analítica sin sensores instalados ni modelo de negocio que sustente la instrumentación. · Estrategia de salida: Instalar una red piloto de bajo costo en la basílica, calibrar el modelo con vibración ambiental y evaluar con datos reales las funciones de transferencia, junto con un análisis de costo de instrumentación.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Equivocación (uso de 'gemelo digital') | El título y el resumen presentan un marco de gemelo digital cuando el componente físico y el flujo de datos reales no existen todavía (Resumen, p. 1; Sec. 5, p. 20) | Sobrestima el grado de integración alcanzado |
| Petición de principio (circularidad de la validación) | Las funciones de transferencia se entrenan con salidas del modelo numérico y su bajo RMSE se interpreta como respaldo para el uso con datos de campo (Sec. 4.6, p. 14) | Debilita la inferencia sobre la capacidad predictiva real |
| Generalización apresurada | Se afirma que la metodología puede extenderse a cualquier estructura civil con ajustes, a partir de un solo edificio (Sec. 5, p. 20) | Sin evidencia de transferibilidad |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Instrumentación guiada por el modelo → mejor detección de daño | Resultados simulados; sin datos de campo | Plausibilidad, coherencia con teoría estructural | Fuerza, consistencia, temporalidad, experimento | Incertidumbre de materiales, ruido de sensores | 2 | Hipótesis no probada |
| Inclusión de la componente vertical → menor error de las funciones de transferencia | Comparación de RMSE con 2 y 3 señales de entrada (Fig. 27-28) | Plausibilidad, gradiente parcial | Consistencia entre niveles, repetición | Nivel del edificio, tamaño de muestra | 4 | Correlacional |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Tecnológico | Datos reales de sensores y calibración del gemelo con vibración ambiental en edificios patrimoniales | Crítico | Media | 9 |
| Conocimiento | Cuantificación de la incertidumbre de materiales de mampostería sobre ubicación de sensores y funciones de transferencia | Significativo | Media | 8 |
| Mercado | Modelo de costo y valor de la instrumentación frente a pérdidas por interrupción de uso del edificio | Crítico | Media | 8 |
| Metodológico | Validación independiente de funciones de transferencia con datos no simulados y comparación con ubicación óptima basada en información | Significativo | Alta | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Algoritmo general del enfoque metodológico | Diagrama | Fases de la metodología desde la virtualización hasta la alerta temprana | 6 fases (según Sec. 5) | Media |
| Fig. 2 | Marco conceptual de integración del gemelo digital basado en modelación por elementos finitos | Diagrama | Vínculo entre mundo físico (sensores) y mundo virtual (modelo) | No aplica | Media |
| Tabla 1 | Resumen de propiedades mecánicas de los materiales | Tabla | Valores tomados de archivos y estudios previos | No transcritos | Media |
| Fig. 16 | Gráficos IDF de deriva, desplazamiento y aceleración de un muro longitudinal | Gráfico | Intensidad, duración y frecuencia de parámetros de demanda | No tabulados | Alta |
| Fig. 18 | Comparación de resultados de análisis con daño tras sismo de Ica 2007 | Imagen/Diagrama | Patrón de agrietamiento simulado frente al reportado | Grietas 0,01-4 mm; una de 7 mm | Media |
| Fig. 22 | Regiones de interés para mapeo de desempeño de muros | Diagrama | Cuatro regiones y niveles de la torre | 4 regiones | Media |
| Fig. 24 | Puntos recomendados para instalación de sensores | Diagrama | Distribución espacial en vistas longitudinal y transversal | 25 puntos | Alta |
| Fig. 27-28 | RMSE de funciones de transferencia para aceleración, velocidad y desplazamiento | Gráfico | Comparación de 2 y 3 señales de entrada por nivel | 0,018 a 0,283 | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Blanco et al. (SHM integrado en mampostería histórica) | España | Academia | Sistema de monitoreo de respuestas locales y globales | Instrumentación real | Sin gemelo numérico detallado | Estable |
| Gentile et al. (monitoreo de la catedral de Milán) | Italia | Academia | Monitoreo de largo plazo para mantenimiento condicionado | Datos de campo de años | Sin aprendizaje profundo | Estable |
| Alarcón et al. (SHM de bajo costo con Raspberry Shake) | Chile | Academia | Instrumentación sísmica de bajo costo en un edificio de madera | Bajo costo y datos reales | Estructura no patrimonial | Creciendo |

### B.9 Variables econométricas y vacíos

- **Y:** No aplica: no se estima una variable resultado
- **X:** Número y ubicación de sensores; señales de entrada (2 o 3 componentes)
- **Z (controles):** Nivel del edificio, tipo de registro sísmico, tipo de señal (aceleración, velocidad, desplazamiento)
- **Datos:** 5 análisis tiempo-historia no lineales sobre un edificio; 24 modelos LSTM (datos simulados)
- **Método:** Simulación numérica y aprendizaje profundo con partición 70/15/15; sin inferencia estadística
- **Efecto reportado:** No cuantificado en términos económicos; RMSE de 0,018 a 0,283
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin análisis de sensibilidad completo de materiales ni validación con datos de campo

| Vacío | Tipo | Descripción |
|---|---|---|
| V-014-01 | TERR | Un solo edificio en Lima; sin evidencia en otras regiones andinas ni en edificios no patrimoniales |
| V-014-02 | POBL | No considera usuarios, comunidades ni actividades económicas que dependen del edificio |
| V-014-03 | TEMP | Análisis de respuesta de segundos a minutos; sin horizonte de recuperación ni de degradación a largo plazo |
| V-014-04 | MET | Validación con datos reales de sensores y análisis de sensibilidad de materiales pendientes |
| V-014-05 | VAR | Faltan variables de costo, de uso del edificio y de tiempo de inhabilitación |
| V-014-06 | TEOR | El marco de resiliencia circular inteligente no se articula con teoría de recuperación o de resiliencia organizacional |
| V-014-07 | CAUS | No se estima el efecto de la instrumentación sobre la detección de daño ni sobre decisiones de intervención |
