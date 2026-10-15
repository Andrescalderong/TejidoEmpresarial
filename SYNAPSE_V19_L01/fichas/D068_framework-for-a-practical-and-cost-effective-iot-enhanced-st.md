# FB-L01-068 | D068 — Framework for a practical and cost-effective IoT-enhanced structural health monitoring and damage diagnostics system with digital twinning

> Corpus de origen: **SCOPUS** · Archivo: `SCOPUS_Tejido empresarial/s13349-025-00927-9.pdf` · 26 páginas · Relevancia para el eje del corpus: **Adyacente** (Presenta un marco de monitoreo de salud estructural con gemelo digital de bajo costo que une dos sensores de desplazamiento económicos (potenciómetro e infrarrojo), un microcontrolador Arduino Nano 33 IoT con nube, un modelo de elementos finitos calibrado y un programa propio (ReConTwin) que estima carga, grietas y emite alertas. Aporta una referencia concreta de costos y de precisión de un gemelo digital con IoT accesible, pertinente para pequeñas organizaciones, pero no trata sismos, recuperación productiva ni empresas, y se valida con una viga de laboratorio.)

## PARTE A — FICHA BIBLIOGRÁFICA ANALÍTICA (SYNAPSE V19.0)

### Capa 1 — Núcleo bibliográfico

- **FB_ID / DOC_ID:** FB-L01-068 / D068
- **Tipo de recurso:** Artículo científico (journal peer-reviewed, acceso abierto)
- **Referencia APA 7:** Huang, J., Broekman, A., Markou, G., & Chen, H.-P. (2025). Framework for a practical and cost-effective IoT-enhanced structural health monitoring and damage diagnostics system with digital twinning. *Journal of Civil Structural Health Monitoring*, *15*(6), 2059-2084. https://doi.org/10.1007/s13349-025-00927-9
- **Autores:** Huang, Jack (59679854600); Broekman, André (57218679015); Markou, George (29068018100); Chen, Hua-Peng (7501622980)
- **Afiliaciones:** Department of Civil Engineering, University of Pretoria, Pretoria, South Africa; Department of Civil Engineering and Geomatics, Cyprus University of Technology, Limassol, 3036, Cyprus; School of Transportation Engineering, East China Jiaotong University, Jiangxi, Nanchang, 330013, China
- **Fecha de publicación:** 2025
- **Fuente/contenedor:** Journal of Civil Structural Health Monitoring · vol. 15(6)
- **Identificador persistente:** DOI 10.1007/s13349-025-00927-9 · ISSN 21905452
- **URL de acceso:** https://www.scopus.com/inward/record.uri?eid=2-s2.0-86000488035&doi=10.1007%2fs13349-025-00927-9&partnerID=40&md5=b779bcd0c97b820559e14c77032cb300
- **Fecha de consulta:** 2026-10-15
- **Citas Scopus (a la fecha del export):** 15

### Capa 2 — Extracción metodológica

**Objetivo de la investigación.** Investigar la factibilidad de un marco de monitoreo de salud estructural (SHM) práctico y de bajo costo, potenciado por gemelos digitales (DT), para infraestructura civil, dado que muchos sistemas de DT para SHM son costosos, complejos y exigentes en recursos, lo que limita su uso en implementaciones pequeñas. El estudio explora dos sensores de desplazamiento de bajo costo, un potenciómetro de contacto y un sensor infrarrojo sin contacto, conectados a un microcontrolador con acceso remoto en la nube, y un programa de código abierto llamado ReConTwin que realiza actualización casi en tiempo real, análisis y diagnóstico de daño de una viga de concreto armado en el laboratorio.

**Pregunta de investigación.** El artículo no formula preguntas de investigación explícitas. Las preguntas implícitas son si sensores de desplazamiento de decenas de dólares alcanzan una precisión suficiente frente a un LVDT de control, si un modelo de elementos finitos calibrado con una prueba de carga puede estimar la carga aplicada y las grietas de una viga distinta, y si un programa automatizado puede emitir advertencias de daño por deflexión y ancho de fisura.

**Marco teórico.** El marco articula el monitoreo de salud estructural, la cuarta revolución industrial y el concepto de gemelo digital como réplica virtual de un activo que se sincroniza de forma automática con sensores y apoya el mantenimiento predictivo. Los autores revisan casos de IoT en monitoreo de puentes ferroviarios, de IoT de banda estrecha con acelerómetros, de DT con aprendizaje automático y de DT para puentes de concreto presforzado, para el tablero de un puente atirantado y para estructuras patrimoniales, y señalan como obstáculos el alto costo del hardware y el software, la complejidad técnica, la falta de interpretabilidad y el exceso de mediciones. La arquitectura se divide en un sistema físico, con sensores y comunicación, y un sistema de programa con un modelo de elementos finitos que se actualiza y se diagnostica con ReConTwin.

**Metodología.** Se construyeron cinco vigas de concreto armado de 2060 mm de longitud, 150 mm de ancho y 230 mm de altura, con dos barras de 12 mm inferiores y dos de 10 mm superiores y estribos de 8 mm cada 100 mm, ensayadas en flexión de tres puntos sobre una luz de 1800 mm con un actuador MTS de 500 kN y carga controlada a 4 kN por minuto. En la etapa 1, cuatro vigas se cargaron en pasos de 4 kN, con tres minutos de mantenimiento, hasta la falla, y sirvieron para obtener la curva fuerza-desplazamiento con un LVDT y la deformación con fibra óptica distribuida, de modo que se calibró el modelo. En la etapa 2, una viga se cargó en una fase cíclica elástica (de 0 a 20 kN) y en una fase incremental hasta 56 kN, mientras el potenciómetro (84 dólares), el sensor infrarrojo (15 dólares) y el Arduino Nano 33 IoT (25 dólares) registraban el desplazamiento, con 250 muestras promediadas por medición y frecuencia efectiva de 0,39 Hz. El modelo se elaboró en FEMAP con elementos hexaédricos de 20 nodos y el modelo constitutivo de Kotsovos y Pavlovic modificado, se calibró mediante 72 análisis no lineales con variaciones del módulo del concreto de 26 a 34 GPa y del esfuerzo de fluencia del acero de 493 a 500 MPa, y ReConTwin automatizó el proceso en Python con una interfaz de cuatro ventanas, donde la ventana 4 compara la deflexión con luz/250 y el ancho de fisura con 0,3 mm.

**Resultados principales.** Los resultados indican que, en la calibración con una altura de referencia, el potenciómetro tuvo resolución de 48,4 micrómetros por dígito del convertidor, exactitud estimada de más o menos 80 micrómetros e histéresis de 0,11 %, y el sensor infrarrojo mostró una relación cuadrática con resolución de 94,1 a 285,9 micrómetros por dígito y exactitud de más o menos 363 micrómetros. En el ensayo cíclico, el error absoluto medio frente al LVDT fue de 25,2 micrómetros para el potenciómetro y de 184,8 micrómetros para el infrarrojo, y en el incremental fue de 41,2 y 176,0 micrómetros; las diferencias medias no fueron estadísticamente significativas (p de 0,621, 0,291, 0,130 y 0,359). El modelo calibrado con 72 iteraciones, de una hora de duración total, logró un error relativo medio de 4,7 % con módulo del concreto de 29 GPa y fluencia de 494 MPa. La carga estimada por el gemelo a partir de la deflexión tuvo un error absoluto medio de 2,11 kN, con una subestimación máxima de 5,18 kN a 20 kN y sobreestimación a cargas mayores a 36 kN; el espaciamiento de fisuras predicho fue de 50 mm frente a 79 mm observado, y la deformación máxima del soffit tuvo un error absoluto medio de 281 microdeformaciones y un error relativo medio de 34,3 %. Los datos llegaron a la nube de Arduino mediante Wi-Fi y se descargaron para importarlos al programa, de modo que el análisis es de casi tiempo real y no continuo.

**Discusión y contribución.** Los autores sostienen que el marco demuestra la factibilidad de un DT-SHM práctico, accesible y de bajo costo, que el potenciómetro es adecuado para mediciones precisas y el sensor infrarrojo para medición sin contacto con márgenes de error mayores, y que el modelo calibrado representa con precisión la respuesta mecánica de la viga. Afirman que la calibración iterativa automatizada es robusta y eficiente, que el programa predice daño superficial e interno y que el diseño es aplicable a estructuras reales más complejas. Reconocen que el enfoque se adecúa a geometrías, materiales y cargas simples. Como trabajo futuro proponen implementarlo en edificios y puentes de concreto a escala real, integrar análisis cíclico y dinámico del software de elementos finitos y aplicarlo a estructuras reforzadas.

**Limitaciones declaradas.** Declaradas: el enfoque de calibración es adecuado para sistemas simples, de geometría, materiales y cargas sencillas, y el principio se demostró en un ambiente controlado; el modelo se calibró con pruebas de carga previas. No declaradas: una sola viga en la etapa 2 y carga estática de corto plazo, sin dinámica, sin temperatura ni humedad; el término de bajo costo no se respalda con el costo total del sistema (control, fibra óptica, interrogador, software de elementos finitos y programa); la frecuencia efectiva de 0,39 Hz impide capturar eventos dinámicos como un sismo; el análisis de los datos de la nube es manual por descarga; la ausencia de diferencias significativas no prueba equivalencia; el error de deformación de 34,3 % contradice la afirmación de alta precisión; el ancho de fisura se calcula multiplicando la deformación por una longitud de elemento de 150 mm sin validación con anchos medidos; la etapa 1 reporta falla a 52 kN, mientras que la descripción de método indica 56 kN; el sistema se alimenta por USB desde una computadora portátil, lo que no corresponde a un despliegue remoto; los datos solo se ofrecen a solicitud.

**Trabajo futuro.** Explícito: implementar la tecnología en edificios y puentes de concreto armado a escala real, integrar el análisis cíclico y dinámico del programa de elementos finitos para el diagnóstico con datos de carga cíclica, y extender el marco a estructuras reforzadas y rehabilitadas. Implícito: operación continua con alimentación autónoma, sensores para dinámica y pruebas de durabilidad.

**Palabras clave.** Declaradas: Damage diagnostics; Digital twin; IoT; Low-cost alternative; Sensors; Structural health monitoring | Inferidas: gemelo digital, monitoreo de salud estructural, IoT, bajo costo, Arduino, potenciómetro, sensor infrarrojo, elementos finitos, concreto armado, diagnóstico de daño

### Capa 3 — Abstracción propositiva

**Tesis central (abstraída).** Un gemelo digital de una viga de concreto armado, construido con un potenciómetro de 84 dólares o un sensor infrarrojo de 15 dólares, un microcontrolador de 25 dólares con nube gratuita y un programa de código abierto que calibra automáticamente un modelo de elementos finitos en una hora, estima la carga aplicada con un error medio de 2,11 kN y predice el patrón de grietas y las alertas de deflexión, lo que demuestra la factibilidad de un monitoreo estructural con gemelo digital accesible para infraestructura civil.

**Antítesis identificada.** La demostración se limita a una viga en carga estática de corto plazo en un laboratorio, con un único espécimen en la etapa de validación, de modo que no se prueba el desempeño ante ruido ambiental, temperatura, cargas dinámicas o estructuras reales. La afirmación de bajo costo omite el costo del software de elementos finitos, el interrogador de fibra óptica y el tiempo del especialista. El error de 34,3 % en deformación y la discrepancia de 50 frente a 79 mm en el espaciamiento de fisuras restan respaldo a la tesis de predicción precisa del daño, y el ancho de fisura estimado con un producto entre deformación y longitud de elemento no se contrasta con mediciones. Con una frecuencia de 0,39 Hz el sistema no es apto para eventos sísmicos. La falta de significancia estadística no demuestra equivalencia entre los sensores y el LVDT.

**Síntesis propuesta.** La contribución sostenible es una prueba de concepto reproducible de una cadena completa de gemelo digital con hardware económico y calibración automatizada, con costos unitarios declarados y errores de desplazamiento medidos frente a un sensor de control, que permite estimar la carga y emitir alertas simples en una viga. Para el corpus, importa como referencia de la accesibilidad del gemelo digital con IoT para organizaciones de recursos limitados, aunque su alcance es de laboratorio, estático y de elemento único. La conclusión de aplicabilidad a estructuras reales requiere ensayos con estructuras completas, comunicación autónoma y una evaluación de costo total, y debe unirse con enfoques de sismo para ser útil a la recuperación empresarial.

**Áreas grises detectadas.**

1. Costo total: el artículo declara los precios de los sensores y del microcontrolador (84, 15 y 25 dólares) pero no suma el costo de la fibra óptica distribuida de control, el interrogador, el software de elementos finitos (FEMAP y ReConAn FEA), la computadora ni el tiempo de calibración, de modo que la afirmación de bajo costo se sostiene solo para el hardware de adquisición.
2. Frecuencia y tiempo real: las 250 muestras promediadas producen una medición cada 2,6 segundos (0,39 Hz) y los datos se descargan de la nube para importarlos al programa, de modo que el sistema puede describir procesos de carga lentos pero no vibraciones ni un sismo, aunque el texto lo presenta como casi en tiempo real.
3. Equivalencia estadística: las pruebas t pareadas con p de 0,621, 0,291, 0,130 y 0,359 se interpretan como ausencia de diferencia con el LVDT, aunque la ausencia de significancia con pocas mediciones no prueba equivalencia, y el intervalo del sensor infrarrojo (de menos 91,58 a 224,56 micrómetros) es amplio.
4. Calidad del diagnóstico de daño: la ventana de diagnóstico compara la deflexión con luz/250 y el ancho de fisura con 0,3 mm, pero el ancho se obtiene de la deformación del modelo por una longitud de elemento de 150 mm y la deformación tiene un error relativo medio de 34,3 %, de modo que la confiabilidad del umbral de alerta no se verifica con anchos de fisura medidos.

**Puntos oscuros aclarados.** Llama la atención que el artículo afirme que el sistema permite una identificación precisa de la degradación temprana, aunque no se ensayó ninguna viga dañada de forma incipiente ni se midieron anchos de fisura. También es notable que la sección de método declare que se variaron tres propiedades del material, pero el módulo del acero se mantuvo en 200 GPa y solo se combinaron 9 valores de módulo del concreto con 8 de fluencia, que suman 72 análisis. La etapa 1 se describe con carga hasta 56 kN y luego con falla a 52 kN, y la tabla de carga estimada muestra un escalón de 34 kN donde correspondería 36 kN, lo que indica errores de edición. La subestimación de 5,18 kN a 20 kN equivale a un error de 26 % de la carga, y el texto la califica como conservadora y de alta precisión. Además, el sistema se alimenta por una computadora portátil y se usa Wi-Fi de un teléfono o enrutador, condiciones que no existirían tras un sismo. Por último, la accesibilidad se sostiene con software propio de los autores, cuyo código no se publica.

**Ideas propositivas novedosas.**

1. Gemelo ligero para una nave industrial o un edificio de una pyme: instalar durante seis meses cuatro sensores de desplazamiento de bajo costo con microcontroladores de alimentación autónoma en una estructura de concreto o acero de una pequeña empresa, calibrar un modelo reducido con una prueba de carga y registrar temperatura, vibraciones y falsas alarmas. El resultado permitiría estimar el costo total de propiedad por metro cuadrado, la tasa de falsas alarmas y el esfuerzo del especialista, y definir un paquete mínimo de monitoreo asequible que indique si una empresa puede reanudar operaciones tras un evento. Se documentarían también las horas de calibración y mantenimiento.
2. Prueba de la cadena completa con un evento dinámico: sustituir el potenciómetro por acelerómetros MEMS de bajo costo y aumentar la frecuencia de muestreo a 100 Hz, aplicando impactos y sacudidas en una mesa vibratoria pequeña sobre pórticos de laboratorio con y sin daño inducido, y medir con 10 repeticiones la latencia de punta a punta, la pérdida de paquetes del Wi-Fi y el error de identificación de frecuencias. Con ello se determinaría si el marco del artículo puede ampliarse a la detección de daño posterremoto y a qué costo, lo que lo conectaría con la recuperación de operaciones.

**Relaciones poco exploradas.**

1. Gemelos de infraestructura de bajo costo (complementa) D014 y D064: D014 construye un gemelo de la Basílica María Auxiliadora y D064 una arquitectura 5G con sensores MEMS; D068 aporta costos unitarios y una calibración automatizada para elementos de concreto.
2. IoT y sostenibilidad de producción o activos (se relaciona con) D083 y D084: D083 trata IoT y sostenibilidad en sistemas de producción y D084 un SHM sincronizado de puentes colgantes; D068 ofrece un contraste de escala y de accesibilidad con sensores de decenas de dólares.

**Robustez argumentativa:** 2.5/10 (ponderación 30/30/25/15) — consistencia lógica 3/10; calidad de la evidencia 2/10; validez de inferencias causales 2/10; generalizabilidad 3/10.

**Valor estratégico:** 5/10 — Aporta una cadena completa y replicable de gemelo digital con IoT de bajo costo, con precios unitarios (84, 15 y 25 dólares), errores de desplazamiento frente a un LVDT (25,2 a 184,8 micrómetros), error de carga de 2,11 kN y calibración automatizada de 72 iteraciones en una hora. Su valor para el corpus es moderado, porque es una viga de laboratorio, estática, con un solo espécimen de validación, de baja frecuencia, con deformación de 34,3 % de error relativo y sin costos totales ni sismo, pero sirve como referencia de accesibilidad tecnológica.

**Conexiones inter-documentales.**

- **CONFIRMA** D084 (IoT sincronizado de bajo costo para monitoreo vibracional de puentes c): relación inversa de D084 CONFIRMA D068: ambos demuestran monitoreo estructural con IoT de bajo costo solo en laboratorio (modelo a escala o viga), con TRL 4 y sin pruebas de campo [juicio del analista]
- **PRECEDE** D100 (síntesis Scopus AI): documento citado como referencia 24 de la síntesis [citación verificada]

### Capa 4 — Control de calidad

- **Falacias detectadas:** Ausencia de significancia interpretada como equivalencia (Los valores p de 0,621, 0,291, 0,130 y 0,359 se usan para afirmar que los sensores no difieren del LVDT (Sec. 5.2, p. 18-20)); Afirmación de alta precisión con un error elevado (Se califica de alta exactitud la deformación con error relativo medio de 34,3 % (Sec. 5.4, p. 22)); Generalización desde un elemento simple (Se concluye la aplicabilidad a estructuras reales con una viga de laboratorio en carga estática (Sec. 6, p. 24-25))
- **Bradford-Hill:** No aplica: es un estudio de ingeniería experimental; no se estima causalidad con datos observacionales.
- **TRL asignado:** 4 — 'The principle of such system has been demonstrated in a controlled environment' (p. 24)
- **Versión de ficha:** v1.0 | 2026-10-15 | SYNAPSE V19.0
- **Notas de proceso:** Texto completo extraído (26 páginas del PDF, 2059 a 2084 de la revista; las páginas citadas siguen los marcadores del PDF). Las tablas 1 y 2 se leyeron con orden de columnas parcialmente alterado; se usaron las cifras del texto. En la Tabla 3 el escalón de carga '34' parece corresponder a 36 kN según el texto; se cita tal como aparece. El cálculo de 9 por 8 combinaciones (72) lo verificó el analista.

---

## PARTE B — ANÁLISIS SYNAPSE DEL DOCUMENTO

### B.1 Análisis dialéctico

| TESIS | ANTÍTESIS | SÍNTESIS | ROBUSTEZ |
|---|---|---|---|
| Un gemelo digital de una viga de concreto armado, construido con un potenciómetro de 84 dólares o un sensor infrarrojo de 15 dólares, un microcontrolador de 25 dólares con nube gratuita y un programa de código abierto que calibra automáticamente un modelo de elementos finitos en una hora, estima la carga aplicada con un error medio de 2,11 kN y predice el patrón de grietas y las alertas de deflexión, lo que demuestra la factibilidad de un monitoreo estructural con gemelo digital accesible para infraestructura civil.  | La demostración se limita a una viga en carga estática de corto plazo en un laboratorio, con un único espécimen en la etapa de validación, de modo que no se prueba el desempeño ante ruido ambiental, temperatura, cargas dinámicas o estructuras reales. La afirmación de bajo costo omite el costo del software de elementos finitos, el interrogador de fibra óptica y el tiempo del especialista. El error de 34,3 % en deformación y la discrepancia de 50 frente a 79 mm en el espaciamiento de fisuras restan respaldo a la tesis de predicción precisa del daño, y el ancho de fisura estimado con un producto entre deformación y longitud de elemento no se contrasta con mediciones. Con una frecuencia de 0,39 Hz el sistema no es apto para eventos sísmicos. La falta de significancia estadística no demuestra equivalencia entre los sensores y el LVDT.  | La contribución sostenible es una prueba de concepto reproducible de una cadena completa de gemelo digital con hardware económico y calibración automatizada, con costos unitarios declarados y errores de desplazamiento medidos frente a un sensor de control, que permite estimar la carga y emitir alertas simples en una viga. Para el corpus, importa como referencia de la accesibilidad del gemelo digital con IoT para organizaciones de recursos limitados, aunque su alcance es de laboratorio, estático y de elemento único. La conclusión de aplicabilidad a estructuras reales requiere ensayos con estructuras completas, comunicación autónoma y una evaluación de costo total, y debe unirse con enfoques de sismo para ser útil a la recuperación empresarial.  | 2.5/10 |

### B.2 Interrogación socrática

- **P1 Definición:** 'Gemelo digital' es un modelo de elementos finitos calibrado que se actualiza con datos de sensores; 'ReConTwin' es el programa que automatiza la calibración, la estimación de carga y el diagnóstico; 'diagnóstico de daño' es la comparación de la deflexión con luz/250 y del ancho de fisura estimado con 0,3 mm; 'bajo costo' se refiere al precio de los sensores y del microcontrolador.
- **P2 Supuestos:** Supone que una viga calibrada representa una estructura real, que la ausencia de diferencia significativa equivale a exactitud, que el ancho de fisura derivado de la deformación del modelo es confiable y que una frecuencia de 0,39 Hz es suficiente.
- **P3 Evidencia:** La evidencia son ensayos de flexión de cinco vigas, comparaciones con LVDT y fibra óptica, 72 análisis de calibración y tablas de error de carga, de desplazamiento y de deformación, en un laboratorio.
- **P4 Consecuencias:** Si es cierto, organizaciones con pocos recursos podrían monitorear estructuras con gemelos digitales; si es falso, el sistema puede dar falsas seguridades en condiciones reales de ruido, temperatura, comunicación y dinámica.
- **P5 Contraejemplos:** No se examinan estructuras completas, eventos dinámicos, costos totales, falsas alarmas, alimentación autónoma ni la validación del ancho de fisura.
- **P6 Alternativas:** Alternativas: que un modelo estadístico simple baste para detectar cambios de rigidez; que los acelerómetros MEMS sean mejores que los sensores de desplazamiento para campo; que el costo dominante sea el especialista y no el hardware.

### B.3 KPIs extraídos

| KPI | VALOR | UNIDAD | CONTEXTO | UBICACIÓN | FUENTE | CONFIANZA | LIMITACIÓN |
|---|---|---|---|---|---|---|---|
| Costo del potenciómetro de contacto | 84 | USD | Sensor Variohm EuroSensor de 50 mm | Sec. 3.1, p. 6 | Texto | Alta | Solo el sensor |
| Costo del sensor infrarrojo | 15 | USD | Sensor Sharp de 30 a 300 mm | Sec. 3.1, p. 6 | Texto | Alta | Solo el sensor |
| Costo del microcontrolador Arduino Nano 33 IoT | 25 | USD | Con Wi-Fi y Bluetooth de baja energía | Sec. 3.2, p. 6 | Texto | Alta | Sin costo de nube |
| Error absoluto medio del potenciómetro frente al LVDT | 25,2 y 41,2 | μm | Ensayo cíclico e incremental | Sec. 5.2, p. 17-19 | Texto | Alta | Una viga |
| Error absoluto medio del sensor infrarrojo frente al LVDT | 184,8 y 176,0 | μm | Ensayo cíclico e incremental | Sec. 5.2, p. 18-19 | Texto | Alta | Una viga |
| Error relativo medio de calibración del gemelo | 4,7 | % | 72 iteraciones; 29 GPa y 494 MPa | Sec. 5.1, p. 16 | Texto | Alta | Fuerza-desplazamiento |
| Error absoluto medio de la carga estimada por el gemelo | 2,11 | kN | Máximo de 5,18 kN a 20 kN | Tabla 3, p. 22 | Tabla | Media | Carga de 4 a 52 kN |
| Error relativo medio de la deformación máxima del soffit | 34,3 | % | Error absoluto medio de 281 microdeformaciones | Sec. 5.4, p. 22 | Texto | Media | Base del ancho de fisura |

### B.4 Evaluación multinivel de madurez

| Dimensión | Score | Aplica | Evidencia | Justificación |
|---|---|---|---|---|
| TRL | 4 | Sí | 'The principle of such system has been demonstrated in a controlled environment' (p. 24) | Validación de componentes y del sistema integrado en laboratorio con una viga; sin entorno relevante ni estructuras a escala real. |
| MRL | N/A | No | No aplica | Sin manufactura. |
| BRL | 2 | Sí | 'The proposed framework offers a roadmap towards a simpler, affordable, and accessible alternative for infrastructure asset monitoring' (p. 24) | Se plantea el atractivo de costo; no hay modelo de negocio, costo total ni clientes identificados. |
| IRL | 4 | Sí | 'The seamless integration of the Arduino with the DTSHM framework streamlined the data transmission process, automating the flow of information from the physical structure to the digital model' (p. 20) | Integración de sensores, microcontrolador, nube, modelo de elementos finitos y programa probada en laboratorio; el flujo incluye descarga manual de datos. |
| DRL | 2 | Sí | 'Future work foresees the implementation of the proposed technology in real-scale structures such as important buildings and RC bridges' (p. 25) | Se identifica una necesidad técnica de monitoreo accesible; sin estudio de demanda ni usuarios. |
| SRL | 1.33 | Sí | Componentes: Sensores de desplazamiento y microcontrolador IoT (TRL 4), Modelo de elementos finitos calibrado y programa ReConTwin (TRL 4) | SRL=Σ(TRLi×IRLij)/2 términos ordenados = 12.0; ÷9 → 1.33; nivel acotado a [1,9] = 1.33 |

**Análisis de brechas**

| Brecha | Valor | Interpretación |
|---|---|---|
| Gap TRL-BRL | 2 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap TRL-MRL | N/A | N/A |
| Gap TRL-IRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Gap BRL-DRL | 0 | Desarrollo relativamente balanceado (|brecha|<3) |
| Brecha crítica | 2 | Valle de la Muerte Comercial (TRL-BRL) |

**Valle de la muerte:** V1 Investigación sin aplicación · Severidad: Media · TRL 4 con BRL 2 e IRL 4: prueba de concepto de laboratorio sin estructura real, sin costo total y con descarga manual de datos. · Estrategia de salida: Piloto en una estructura real con alimentación autónoma, costo total de propiedad, falsas alarmas y validación de ancho de fisura.

### B.5 Robustez argumentativa y causalidad

| Falacia | Evidencia | Impacto |
|---|---|---|
| Ausencia de significancia interpretada como equivalencia | Los valores p de 0,621, 0,291, 0,130 y 0,359 se usan para afirmar que los sensores no difieren del LVDT (Sec. 5.2, p. 18-20) | Con pocas mediciones no se prueba equivalencia |
| Afirmación de alta precisión con un error elevado | Se califica de alta exactitud la deformación con error relativo medio de 34,3 % (Sec. 5.4, p. 22) | Contradice las cifras presentadas |
| Generalización desde un elemento simple | Se concluye la aplicabilidad a estructuras reales con una viga de laboratorio en carga estática (Sec. 6, p. 24-25) | Los autores reconocen que la calibración es adecuada para sistemas simples |

**Recomendación:** Aceptar con reservas

| Relación propuesta | Evidencia correlacional | Criterios cumplidos | Criterios no cumplidos | Confusores | Score | Veredicto |
|---|---|---|---|---|---|---|
| Calibración del modelo con una prueba de carga → estimación de la carga a partir de la deflexión | Tabla 3 con error medio de 2,11 kN | Mecanismo mecánico directo | Estructuras reales con cargas variables | Temperatura, fluencia, adherencia | 3 | Efecto plausible en laboratorio |
| Deformación estimada por el modelo → ancho de fisura y alerta | Deformación con error relativo medio de 34,3 % | Relación calculada con una longitud de elemento | Anchos de fisura medidos | Tamaño de malla, espaciamiento de fisuras | 2 | Relación no validada |

### B.6 Gaps identificados

| Tipo | Descripción | Magnitud | Viabilidad | Prioridad |
|---|---|---|---|---|
| Metodológico | Validación en estructuras reales con ruido, temperatura y carga variable, y con anchos de fisura medidos | Crítico | Media | 9 |
| Tecnológico | Muestreo dinámico, alimentación autónoma y comunicación robusta tras un evento extremo | Crítico | Media | 8 |
| Mercado | Costo total de propiedad y esfuerzo de especialista para pequeñas organizaciones | Crítico | Media | 8 |
| Conocimiento | Conexión del diagnóstico con la decisión de reocupación o de continuidad de operaciones | Significativo | Media | 7 |

### B.7 Figuras y tablas clave

| N.º | Título | Tipo | Descripción | Datos extraídos | Relevancia |
|---|---|---|---|---|---|
| Fig. 1 | Arquitectura del marco de SHM con gemelo digital | Diagrama | Sistema físico y sistema de programa | No aplica | Media |
| Fig. 7 | Descripción general del sistema de hardware | Diagrama | Sensores, Arduino y nube | 84 USD; 15 USD; 25 USD | Media |
| Fig. 21 | Curvas fuerza-desplazamiento de las 72 iteraciones y del gemelo calibrado | Gráfico | Error relativo de 4,7 % de la iteración elegida | 4,7 % | Alta |
| Tabla 3 | Carga experimental y carga estimada por el gemelo | Tabla | Error medio de 2,11 kN | 2,11 kN | Alta |
| Fig. 27 | Grietas predichas y observadas en el soffit | Imagen | Espaciamiento predicho de 50 mm frente a 79 mm observado | 50 mm; 79 mm | Media |

### B.8 Competidores / actores / alternativas tecnológicas

| Nombre | País | Tipo | Tecnología núcleo | Ventaja | Desventaja | Tendencia |
|---|---|---|---|---|---|---|
| Sistemas de DT para SHM de alto costo con software avanzado | No especificado en documento | Empresa | Monitoreo continuo de infraestructura | Funcionalidades avanzadas | Costo y complejidad según los autores | Estable |
| IoT de banda estrecha con acelerómetros MEMS de Di Nuzzo et al. | No especificado en documento | Academia | Monitoreo continuo de largo alcance y bajo consumo | Conectividad de bajo consumo | Detalle de costos no reportado | Creciente |
| Monitoreo de puente ferroviario con IoT y DT de Armijo y Zamora-Sánchez | No especificado en documento | Academia | Nube y aprendizaje automático para mantenimiento | Caso en campo | Costo no reportado | Creciente |

### B.9 Variables econométricas y vacíos

- **Y:** Error de desplazamiento (μm), error de carga estimada (kN), error de calibración (%), error de deformación (%)
- **X:** Tipo de sensor (potenciómetro o infrarrojo) y uso del gemelo calibrado
- **Z (controles):** Nivel de carga, distancia de detección del infrarrojo, reflectividad de la superficie, propiedades del material
- **Datos:** Ensayos de flexión de cinco vigas de concreto armado en laboratorio, con LVDT y fibra óptica como control
- **Método:** Prueba experimental con calibración por búsqueda exhaustiva de 72 combinaciones y pruebas t pareadas
- **Efecto reportado:** Error medio de desplazamiento de 25,2 a 41,2 μm (potenciómetro) y de 176,0 a 184,8 μm (infrarrojo); error de carga de 2,11 kN
- **Endogeneidad tratada:** No - no se discute
- **Instrumento:** No aplica
- **Robustez reportada:** Sin réplicas de la etapa 2, sin ruido ambiental y con valores p interpretados como equivalencia

| Vacío | Tipo | Descripción |
|---|---|---|
| V-068-01 | TERR | Laboratorio de la Universidad de Pretoria (Sudáfrica); sin estructura en campo |
| V-068-02 | POBL | Cinco vigas de concreto armado; sin edificios, puentes ni empresas |
| V-068-03 | TEMP | Ensayos de minutos de carga estática; sin monitoreo de largo plazo |
| V-068-04 | MET | Una sola viga de validación, sin dinámica y con descarga manual de datos |
| V-068-05 | VAR | Faltan costo total, temperatura, ruido, falsas alarmas y anchos de fisura medidos |
| V-068-06 | TEOR | Gemelo digital y SHM; sin teoría de continuidad ni de recuperación económica |
| V-068-07 | CAUS | Efecto de las alertas sobre decisiones de mantenimiento sin evidencia |
