# FB-L01-009 | D009 — Hybrid monitoring methodology: A model-data integrated digital twin framework for structural health monitoring and full-field virtual sensing

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/1-s2.0-S147403462400034X-main.pdf` · 14 páginas · Relevancia para el eje del corpus: **Adyacente** (Gemelo digital con IoT para monitoreo de salud estructural y detección de daño; menciona sismos como carga de daño súbito, pero sus pruebas usan cargas ambientales, de tráfico y térmicas en un modelo de puente, sin dimensión empresarial.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-009 / D009
- **Tipo de recurso:** Artículo científico (journal peer-reviewed)
- **Referencia APA 7:** Sun, L., Sun, H., Zhang, W., & Li, Y. (2024). Hybrid monitoring methodology: A model-data integrated digital twin framework for structural health monitoring and full-field virtual sensing. *Advanced Engineering Informatics*, *60*, Article 102386. https://doi.org/10.1016/j.aei.2024.102386
- **Autores:** Sun, Limin (7403956279); Sun, Haibin (58900700600); Zhang, Wei (59887140100); Li, Yixian (57211568199)
- **Afiliaciones:** Department of Bridge Engineering, School of Civil Engineering, Tongji University, Shanghai, China; State Key Laboratory of Disaster Reduction in Civil Engineering, Tongji University, Shanghai, China; Fujian Academy of Building Research, Fujian, Fuzhou, China; Department of Civil and Environmental Engineering, The Hong Kong Polytechnic University, Hong Kong
- **Fecha de publicación:** 2024
- **Fuente/contenedor:** Advanced Engineering Informatics · vol. 60
- **Identificador persistente:** DOI 10.1016/j.aei.2024.102386 · ISSN 14740346
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-85185705912&doi=10.1016%2fj.aei.2024.102386&partnerID=40&md5=8b8b2a6d5711821935c8b5c9af31e4f7
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 75

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Presentar un marco de sensado estructural de campo completo basado en un gemelo digital que integra modelos de elementos finitos (FEM) multiescala como gemelo mecánico, un modelo de información de puentes (BRIM) como gemelo de datos, y un sistema de Internet de las cosas (IoT) que conecta la estructura física con el entorno virtual, con el fin de convertir, ampliar y fusionar los datos monitoreados, estimar cargas y respuestas en todo el puente y gestionar de manera inteligente datos heterogéneos para el monitoreo de salud estructural, validado en un modelo de puente continuo de tres vanos.

**Pregunta de investigación.** [INFERIDA] ¿Puede un gemelo digital que combine FEM multiescala, BRIM y una red IoT, con la metodología de monitoreo híbrido modelo-datos, reconstruir las cargas y respuestas de un puente en todo su dominio a partir de sensores discretos, y gestionar y visualizar la información heterogénea de su ciclo de vida?

**Marco teórico.** El marco combina el monitoreo de salud estructural (SHM) con la teoría de gemelos digitales (concepto atribuido a Grieves, 2003, y a proyectos de la NASA) y la modelación de información de construcción (BIM), aplicada a puentes como BRIM. Se apoya en la mecánica estructural lineal y en métodos inversos: mínimos cuadrados parciales, descomposición en valores singulares truncada, regularización de Tikhonov generalizada, inferencia bayesiana de máximo a posteriori y estimadores conjuntos de entrada y estado tipo Kalman (JISE). El monitoreo híbrido se define como integración de datos y modelo para identificar características ocultas y riesgos. El paradigma es de ingeniería, con verificación experimental, y no incorpora teoría organizacional ni de resiliencia.

**Metodología.** El marco consta de tres componentes conectados por IoT: la estructura física, el gemelo mecánico (cuatro modelos FEM: modelo 1 con 110 elementos de viga para estimar carga y respuestas globales y detectar daño; modelo 2 de láminas de alta precisión; modelo 3 multiescala con láminas entre -2,7 y 2,7 m; y modelo 4 de subestructura para reconstruir deformaciones locales) y el gemelo de datos BRIM desarrollado en Revit con desarrollo secundario. La metodología de monitoreo híbrido comprende detección de respuesta cuasi estática con estimación de carga (PLSR, TSVD, regularización generalizada y MAP bayesiano), fusión de datos de video con detección de vehículos por red YOLO, efecto térmico con componentes uniforme y gradiente, monitoreo dinámico en dominio de frecuencia y filtros en el tiempo (JISE), y detección de daño con carga de daño y actualización por superficie de respuesta con algoritmo genético de ordenamiento no dominado. El caso es un modelo de puente de acero Q235 de 22 m (vanos 6+10+6 m), con sección en π de 1.200 mm de ancho y 262 mm de alto, instalado a la intemperie, con cuatro daños preestablecidos en x = -7,1, -2,1, 2,1 y 7,1 m, y un sistema de 74 sensores más estación meteorológica, báscula y cámara. Software: Matlab, Ansys, Python y Revit.

**Resultados principales.** El sistema integra el puente físico, los cuatro FEM y el BRIM, con 74 sensores (3 transductores de desplazamiento, 11 inclinómetros, 32 galgas extensométricas, 11 acelerómetros, 8 medidores de fuerza de reacción y 9 termómetros) en 21 posiciones longitudinales. El flujo de datos almacena información cada minuto, de modo que la latencia del marco es de un minuto; los tiempos por paso de cálculo son 0,002 s para la estimación de carga en Matlab, 0,2673 s para el cálculo FEM en Ansys y 1,527 s para la visualización en Revit, con un procesador Intel Core i7-7700HQ y 8 GB de memoria. Los errores de reconstrucción reportados son, en su mayoría, inferiores a 5 % de la raíz del error cuadrático medio (RMSE) frente al valor real; en la carga cuasi estática vehicular, el RMSE medio de la carga identificada es 3,80 %, el de la deflexión reconstruida 1,73 % y el error máximo de deformación 10,01 με en la sección central; en la carga dinámica de peatones corriendo, el error máximo de deflexión es 0,39 mm, y en la carga térmica de cinco días, el error máximo es 0,30 mm. La familia de daño en el BRIM registra tamaño, fecha de detección, foto y tipo, aunque la cuantificación del daño requiere esfuerzo manual. Se entrega una visualización 4D del estado estructural.

**Discusión y contribución.** Los autores sostienen que la integración de datos y modelo amplía la densidad, diversidad e integralidad de la información, y que el marco es aplicable y escalable a otras estructuras como edificios, presas y turbinas eólicas. Señalan que el BRIM supera la limitación de los sistemas BIM-IoT, que no reflejan las propiedades mecánicas, y que el sistema permite acciones de retroalimentación como cierre temporal del puente o reducción del tráfico. Reconocen limitaciones: el uso de múltiples programas implica tiempo de transmisión de datos, el marco depende de un FEM actualizado y fiable, el modelo es más sencillo que un puente real y el modelado del daño requiere trabajo manual. Proponen aplicarlo a un puente en servicio y usar enfoques basados en datos cuando no exista un modelo confiable.

**Limitaciones declaradas.** Declaradas: dependencia de varios programas con tiempos de intercambio, necesidad de un modelo FEM actualizado y fiable, simplicidad del puente de prueba frente a puentes reales y automatización insuficiente en el modelado del daño.

**Trabajo futuro.** Aplicación a un puente en servicio, incorporación de enfoques basados en datos cuando el FEM no esté disponible y mejora de la automatización del modelado de daños en el BRIM.

**Palabras clave.** Declaradas: Bridge information model; Digital twin; Full-field sensing; Heterogeneous data visualization; Hybrid monitoring; Multi-scale model | Inferidas: monitoreo híbrido, sensado de campo completo, modelo de información de puentes, estimación de carga, actualización de modelo, elementos finitos multiescala, visualización 4D, Revit, fusión de datos heterogéneos, detección de daño

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un gemelo digital que acopla FEM multiescala, BRIM e IoT mediante monitoreo híbrido de modelo y datos puede reconstruir cargas y respuestas de un puente en todo su dominio con errores del orden de 1 a 5 % y gestionar de manera integrada la información heterogénea de su ciclo de vida.

**Antítesis identificada.** Las cifras de desempeño del artículo no provienen de experimentos nuevos descritos en detalle, sino que se citan de trabajos previos de los mismos autores (referencias 54 a 64), y se muestra solo la condición cuasi estática por brevedad. El puente es un modelo de acero de 22 m instalado a la intemperie, con daños provocados artificialmente y un FEM calibrado, de modo que la facilidad de identificación no es comparable con la de un puente real con incertidumbre de modelo, deterioro difuso y datos faltantes. El marco no se probó con sismos, aunque se presenta como útil frente a daño súbito por terremotos. La latencia de un minuto, producto de intercambiar archivos de texto entre Matlab, Ansys y Revit, es incompatible con alerta temprana. La afirmación de escalabilidad a edificios, presas y turbinas no cuenta con evidencia.

**Síntesis propuesta.** El artículo demuestra la viabilidad técnica de acoplar un modelo mecánico, un modelo de información y una red de sensores, con latencia de un minuto y errores bajos en condiciones controladas, lo que define un punto de partida para gemelos de infraestructura. Su evidencia no alcanza para sostener generalización ni uso en emergencia sísmica. Para el corpus, el valor está en la arquitectura de tres gemelos (mecánico, de datos y físico) y en el requisito de un modelo calibrado, que condiciona su aplicación a edificaciones y plantas productivas de las que rara vez existe un FEM actualizado, y obliga a combinar el enfoque con modelos basados en datos.

**Áreas grises detectadas.**

1. Procedencia de las cifras de desempeño: el RMSE menor a 5 %, 3,80 %, 1,73 %, 0,39 mm y 0,30 mm se atribuyen a trabajos citados (referencias 54 a 64, 58 y 60), no a experimentos reportados con detalle aquí, por lo que el lector no puede verificar condiciones, repeticiones ni dispersión.
2. Daño y sismo: el texto menciona terremotos como causa de daño súbito, pero las cargas del caso son ambientales, de tráfico, de peatones y térmicas; la detección de daño con 'carga de daño' se explica en teoría sin presentar tasas de detección, falsos positivos ni sensibilidad al ruido.
3. Latencia y arquitectura: el sistema almacena datos cada minuto y transfiere archivos de texto entre programas; esta arquitectura por lotes no es 'tiempo real' en el sentido de monitoreo de emergencia y no se mide el retraso de extremo a extremo con carga de sensores adicional.
4. Dependencia del modelo: el marco requiere un FEM actualizado y fiable, y el propio texto admite que esto no siempre existe; no se analiza el efecto de errores del modelo (rigideces, condiciones de borde) sobre las estimaciones de carga y respuesta.

**Puntos oscuros aclarados.** La razón de la buena reconstrucción de campo completo con pocos sensores no es solo la metodología híbrida, sino que se trata de una estructura lineal, de geometría sencilla y con cargas casi conocidas por la báscula y el video, de modo que la estimación de cargas (problema mal condicionado) se regulariza con información previa casi completa. Esto explica los errores bajos y sugiere que el desempeño se degradaría si las cargas fueran desconocidas, como en un sismo, o si el modelo de elementos finitos tuviera incertidumbre. Otro punto oscuro es el uso de 'digital twin' para un esquema en que el sentido físico a digital está automatizado pero el sentido digital a físico (cierre, reducción de tráfico) es una recomendación para un operador humano, es decir, un gemelo de monitoreo más que de control. Interpretarlo así aclara el alcance real del marco y explica por qué las recomendaciones de cierre o reducción del tráfico dependen de la decisión de los gestores.

**Ideas propositivas novedosas.**

1. Gemelo sísmico de bajo costo para edificios productivos: sustituir el FEM refinado por un modelo reducido calibrado con pocos sensores de aceleración y con aprendizaje de máquina para estimar el estado de daño después de un sismo, de modo que un establecimiento pueda decidir reabrir, restringir o evacuar. Fundamento: el artículo muestra que el desempeño depende de un modelo actualizado y que los enfoques basados en datos serían la alternativa. Verificabilidad: validar con registros de edificios instrumentados antes y después de un sismo y comparar el diagnóstico con la inspección estructural. Utilidad: acorta el tiempo de reapertura y reduce inspecciones presenciales en pymes, con un costo menor que el de un modelo de elementos finitos detallado por cada edificación.
2. Prueba de robustez frente a incertidumbre de modelo y carga desconocida: repetir los experimentos con cargas no medidas por la báscula, con rigidez perturbada y con sensores fallidos, y reportar la degradación del error de reconstrucción. Fundamento: la buena precisión actual puede deberse al conocimiento casi completo de la carga. Verificabilidad: simulación de Monte Carlo sobre el modelo ya construido y comparación con mediciones. Utilidad: establece el rango de condiciones en que el gemelo puede usarse para decisiones sin intervención experta y permite definir umbrales de confianza para cada tipo de decisión.

**Relaciones poco exploradas.**

1. Densidad y ubicación de sensores (se asocia con) el condicionamiento de la estimación de carga: relación mencionada para elegir el modelo 1 de menor número de grados de libertad, pero sin análisis sistemático.
2. Calidad del FEM calibrado (condiciona) la precisión del gemelo y su transferibilidad a otras estructuras: pregunta abierta clave para llevar el marco de puentes a edificaciones productivas.

**Robustez argumentativa:** 5.3/10 (ponderación 30/30/25/15) — consistencia lógica 7/10; calidad de la evidencia 5/10; validez de inferencias causales 5/10; generalizabilidad 3/10.

**Valor estratégico:** 6/10 — Es una muestra madura de ingeniería de gemelos de infraestructura con IoT, con arquitectura clara, tiempos de cálculo y errores. Aporta al corpus la separación entre gemelo mecánico y gemelo de datos y la evidencia de que la latencia por lotes y la dependencia de un modelo calibrado son límites prácticos. Su validez para el eje sísmico y empresarial es indirecta.

**Conexiones inter-documentales.**

- (Se completan en el Análisis Relacional de la Parte final del lote.)

### Capa 4 — Control de calidad

- **Falacias detectadas:** Apelación a autoridad (autocita) (Errores de desempeño se respaldan con referencias propias [54]-[64], [58], [60] (Sec. 5.4, p. 12)); Generalización apresurada (Se afirma aplicabilidad a edificios, presas y turbinas con un solo modelo de puente (Sec. 3, p. 3)); Falsa dicotomía (Se contrapone BIM-IoT (sin propiedades mecánicas) frente a gemelo híbrido, sin considerar otros enfoques basados en datos (Sec. 1, p. 2))
- **Bradford-Hill:** Plausibilidad mecánica y coherencia con la teoría estructural; la consistencia está respaldada por trabajos previos del mismo grupo. Faltan replicación independiente, diseños con cargas desconocidas y sismo.
- **TRL asignado:** 5 — 'The proposed digital twin framework was successfully applied to a large-scale bridge model' (p. 12)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído. Tabla 1 y ecuaciones fragmentadas; se reconstruyen por el cuerpo de texto. Las cifras de desempeño remiten a trabajos previos de los autores.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un gemelo digital que acopla FEM multiescala, BRIM e IoT mediante monitoreo híbrido de modelo y datos puede reconstruir cargas y respuestas de un puente en todo su dominio con errores del orden de 1 a 5 % y gestionar de manera integrada la información heterogénea de su ciclo de vida.  | Las cifras de desempeño del artículo no provienen de experimentos nuevos descritos en detalle, sino que se citan de trabajos previos de los mismos autores (referencias 54 a 64), y se muestra solo la condición cuasi estática por brevedad. El puente es un modelo de acero de 22 m instalado a la intemperie, con daños provocados artificialmente y un FEM calibrado, de modo que la facilidad de identificación no es comparable con la de un puente real con incertidumbre de modelo, deterioro difuso y datos faltantes. El marco no se probó con sismos, aunque se presenta como útil frente a daño súbito por terremotos. La latencia de un minuto, producto de intercambiar archivos de texto entre Matlab, Ansys y Revit, es incompatible con alerta temprana. La afirmación de escalabilidad a edificios, presas y turbinas no cuenta con evidencia.  | El artículo demuestra la viabilidad técnica de acoplar un modelo mecánico, un modelo de información y una red de sensores, con latencia de un minuto y errores bajos en condiciones controladas, lo que define un punto de partida para gemelos de infraestructura. Su evidencia no alcanza para sostener generalización ni uso en emergencia sísmica. Para el corpus, el valor está en la arquitectura de tres gemelos (mecánico, de datos y físico) y en el requisito de un modelo calibrado, que condiciona su aplicación a edificaciones y plantas productivas de las que rara vez existe un FEM actualizado, y obliga a combinar el enfoque con modelos basados en datos.  | 5.3/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Monitoreo híbrido' es la integración de datos medidos y modelo FEM para identificar carga, respuesta de campo completo y daño; 'gemelo digital' es el conjunto de FEM, BRIM e IoT conectados bidireccionalmente.
- **P2 Supuestos:** Supone que un FEM calibrado representa el puente, que las cargas pueden identificarse con regularización y que la retroalimentación al puente real se realiza por decisión humana.
- **P3 Evidencia:** La evidencia procede de un modelo de 22 m con 74 sensores y de resultados que se atribuyen a trabajos previos del grupo; se muestran solo los casos cuasi estáticos.
- **P4 Consecuencias:** Si es cierto, los gestores podrían decidir cierre o reparación con información de campo completo; si es falso, un modelo desactualizado podría inducir diagnósticos erróneos.
- **P5 Contraejemplos:** Casos con incertidumbre del modelo, cargas desconocidas, sensores averiados o sismos intensos no se examinan.
- **P6 Alternativas:** Alternativas: monitoreo puramente basado en datos, inspección con UAV, o modelos reducidos con aprendizaje automático.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Longitud del puente modelo | 22 | m | Vanos 6+10+6 | Sec. 5.1, p. 8 | Texto | Alta | Modelo de acero, no puente real |
| Sensores instalados | 74 | sensores | 3 D, 11 inclinómetros, 32 galgas, 11 acelerómetros, 8 fuerza, 9 temperatura | Sec. 5.1, p. 8 | Texto | Alta | Instalación de laboratorio/campo experimental |
| Posiciones longitudinales de sensores | 21 | posiciones | Distribución a lo largo del puente | Tabla 1, p. 8 | Tabla | Alta | Tabla fragmentada en la extracción |
| Daños preestablecidos | 4 | daños | x = -7,1; -2,1; 2,1; 7,1 m, longitudes 200, 100, 50 y 20 mm | Sec. 5.1, p. 8 | Texto | Alta | Daños artificiales |
| Elementos del modelo 1 (viga) | 110 | elementos | FEM de baja complejidad | Sec. 5.2, p. 9 | Texto | Alta | Linealidad supuesta |
| Latencia del marco | 1 | min | Almacenamiento cada minuto | Sec. 5.4, p. 12 | Texto | Alta | Arquitectura por lotes |
| Tiempo de estimación de carga (Matlab) | 0.002 | s | Por paso de tiempo | Sec. 5.4, p. 12 | Texto | Alta | Hardware de portátil |
| Tiempo de cálculo FEM (Ansys) | 0.2673 | s | Por paso de tiempo | Sec. 5.4, p. 12 | Texto | Alta | Modelo pequeño |
| Tiempo de visualización (Revit) | 1.527 | s | Por paso de tiempo | Sec. 5.4, p. 12 | Texto | Alta | Procesamiento secuencial |
| Error RMSE de la carga cuasi estática identificada | 3.80 | % | Carga vehicular | Sec. 5.4, p. 12 | Texto | Media | Cifra atribuida a trabajos previos |
| Error RMSE de la deflexión reconstruida | 1.73 | % | Carga vehicular cuasi estática | Sec. 5.4, p. 12 | Texto | Media | Una condición mostrada |
| Error máximo de deformación en sección central | 10.01 | με | Carga cuasi estática | Sec. 5.4, p. 12 | Texto | Media | Sin escala relativa |
| Error máximo de deflexión dinámica | 0.39 | mm | Carga de peatones corriendo | Sec. 5.4, p. 12 | Texto | Media | Cifra de trabajo previo [60] |
| Error máximo térmico (5 días) | 0.30 | mm | Carga térmica | Sec. 5.4, p. 12 | Texto | Media | Cifra de trabajo previo [58] |
| Puentes defectuosos en EE. UU. (contexto) | 46154 | puentes | 7,5 % del total; rehabilitación de 22.700 millones USD/año | Sec. 1, p. 1 | Texto | Media | Cita de informe externo |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 5 | Sí | 'The proposed digital twin framework was successfully applied to a large-scale bridge model' (p. 12) | Marco validado en entorno relevante (puente modelo de 22 m a la intemperie) con sensores y software integrados (TRL 5). |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 1 | Sí | 'The framework should be applied to an in-service bridge for validation in the future' (p. 12) | Idea técnica sin análisis de mercado, costos ni usuarios definidos. |
| IRL | 5 | Sí | 'Switching between different software is realized by Python Language without privacy and human intervention' (p. 12) | Integración de Matlab, Ansys, Revit y sensores en entorno relevante, con latencia de un minuto. |
| DRL | N/A | No | No aplica |  |
| SRL | 2.96 | Sí | Componentes: Gemelo mecánico (FEM multiescala) (TRL 5), Gemelo de datos (BRIM) (TRL 5), Red IoT de 74 sensores (TRL 6) | SRL=Σ(TRLi×IRLij)/6 términos ordenados = 26.7; ÷9 → 2.96; nivel acotado a [1,9] = 2.96 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 4 | TRL >> BRL: tecnología sin mercado (riesgo comercial) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | N/A | N/A |
| Brecha crítica | 4 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V2 Prototipo sin escalamiento · Severidad: Media · TRL 5 con BRL 1: prototipo de laboratorio a escala sin validación en puente real ni plan de escalamiento. · Estrategia de salida: Validar en un puente en servicio, reducir latencia con arquitectura de flujo y definir modelo de servicio con operadores de infraestructura.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Apelación a autoridad (autocita) | Errores de desempeño se respaldan con referencias propias [54]-[64], [58], [60] (Sec. 5.4, p. 12) | Impide verificar la evidencia en este artículo |
| Generalización apresurada | Se afirma aplicabilidad a edificios, presas y turbinas con un solo modelo de puente (Sec. 3, p. 3) | Limita la validez externa |
| Falsa dicotomía | Se contrapone BIM-IoT (sin propiedades mecánicas) frente a gemelo híbrido, sin considerar otros enfoques basados en datos (Sec. 1, p. 2) | Presenta como única opción un diseño específico |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Información previa de carga (báscula y video) → mejor reconstrucción de respuesta | RMSE bajo en condiciones con carga conocida | Plausibilidad, coherencia | Experimento controlado de ablación | Ruido, rigidez del modelo | 5 | Causal mecánica probable |
| Daño preestablecido → carga de daño no nula | Resultado teórico y analítico | Plausibilidad | Experimento de sensibilidad, tasas de detección | Ruido de sensores | 5 | Causal (analítica) |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Conocimiento | Validación del gemelo con sismos reales o simulados y en puentes en servicio | Crítico | Media | 9 |
| Tecnológico | Arquitectura de flujo de datos de baja latencia para alerta y control | Significativo | Alta | 7 |
| Metodológico | Evaluación de robustez ante incertidumbre de modelo, cargas desconocidas y fallos de sensor | Significativo | Alta | 8 |
| Mercado | Modelo de servicio y costo del gemelo para gestores de infraestructura | Moderado | Media | 5 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Digital twin framework for bridge SHM | Diagrama | Físico, FEM y BRIM conectados por IoT | No aplica | Alta |
| Fig. 2 | Summary of hybrid monitoring | Diagrama | Detección estática, respuesta dinámica y daño | No aplica | Media |
| Fig. 4 | Procedures for model updating | Diagrama | Actualización de modelo por superficie de respuesta | No aplica | Media |
| Fig. 7 | Preset recovery damages | Esquema | Cuatro daños reversibles en el ala inferior | Longitudes 200, 100, 50 y 20 mm | Media |
| Fig. 10 | FEMs used to establish the mechanical digital twin | Esquema | Cuatro modelos FEM | 110 elementos en el modelo 1 | Alta |
| Fig. 16 | Workflow of data visualization based on hybrid monitoring | Diagrama | Flujo Matlab-Ansys-Revit con Python | Latencia 1 min | Alta |
| Fig. 17 | Dynamic 4D visualization of structural response | Gráfico | Interfaz 4D de deformación y carga | Errores 3,80 % y 1,73 % | Alta |
| Tabla 1 | Configuration of sensors | Tabla | Sensores en 21 secciones | 74 sensores | Alta |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Sistemas BIM-IoT para puentes (Adibfar y Costin; Sakr y Sadhu) | Estados Unidos / Canadá | Grupos de investigación | BrIM con datos ITS o de sensores | Gestión de información | No reflejan propiedades mecánicas | Creciendo |
| Gemelos digitales con aprendizaje profundo (Austin et al.) | Reino Unido | Grupo de investigación | Plataforma semántica de sensado urbano | Aprendizaje de datos | Menor interpretabilidad física | Creciendo |

### B.9 Variables econométricas y vacíos

- **Y:** Error de reconstrucción (RMSE) de carga, deflexión, deformación
- **X:** Número y tipo de sensores; método de estimación (PLSR, TSVD, MAP, JISE); información previa de carga
- **Z (controles):** Tipo de carga (vehicular, peatonal, térmica); modelo FEM utilizado
- **Datos:** Puente modelo de 22 m con 74 sensores (series de tiempo)
- **Método:** Problemas inversos regularizados y filtros tipo Kalman; actualización de modelo con superficie de respuesta
- **Efecto reportado:** RMSE de 1,73 % a 3,80 % según variable
- **Endogeneidad tratada:** No - no se trata sesgo de modelo; carga conocida parcialmente
- **Instrumento:** No aplica
- **Robustez reportada:** Condiciones cuasi estática, dinámica y térmica en trabajos previos; sin análisis de sensibilidad aquí

| Vacío | Tipo | Descripción |
|---|---|---|
| V-009-01 | TERR | Un solo puente modelo en China; sin casos de infraestructura de regiones sísmicas de América Latina |
| V-009-02 | POBL | No considera operadores de infraestructura ni pequeñas empresas dependientes de la ruta |
| V-009-03 | MET | No se reportan tasas de detección de daño ni análisis de incertidumbre del FEM |
| V-009-04 | VAR | Faltan variables de tiempo de reparación, costo de cierre e impacto económico |
| V-009-05 | TEOR | No se vincula con teoría de resiliencia de redes de transporte |
| V-009-06 | CAUS | No se evalúa el efecto del gemelo sobre decisiones y costos de mantenimiento |
