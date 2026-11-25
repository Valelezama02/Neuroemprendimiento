---
name: buscar-clips
description: Busca clips, entrevistas, fondos o referencias para los Reels de @neuroemprendimiento.ML y entrega 3 opciones listas para editar. Solo necesita la categoría del video (F1 cinematográfico, F2 archivo cuadrado, F3 archivo vertical, F4 editorial, F5 entrevista, F6 stickman). Usar cuando la usuaria pida "busca clips", "búscame un video para…", "necesito fondo / entrevista / referencia", nombre una categoría F1–F6 o escriba /buscar-clips.
---

# Buscar clips para Neuroemprendimiento.ML

Skill para encontrar material que genere **engagement** y encaje con la identidad de la cuenta. La usuaria solo indica la **categoría**; todo lo demás (tema, tipo de persona, dónde buscar, qué filtrar) sale de esta skill y de los documentos de la cuenta.

## 0. Antes de buscar: leer el contexto

Leer siempre, en este orden (están en la raíz del repositorio):

1. `guia_identidad_neuroemprendimiento`: identidad, tono y temas.
2. `Manual de formatos audiovisuales y referencias de edición`: lo que define cada categoría F1–F6.
3. `Analisis de videos publicados.md`: qué se ha publicado y qué funcionó.
4. `registro_de_clips.md`: clips ya propuestos o usados. **No repetir** personas, clips ni temas recientes.

Si falta alguno, seguir con lo que haya y decirlo en una línea.

## 1. Si no se indicó categoría: mostrar el menú y esperar

Responder solo con esta tabla y pedir el número:

| # | Categoría | Qué se busca |
|---|---|---|
| 1 | **F1 Cinematográfico motivacional** | Clips de fondo (sin voz) para una frase: esfuerzo, entrenamiento, trabajo, naturaleza como metáfora |
| 2 | **F2 Archivo cuadrado** | Entrevista o discurso de archivo para presentar en cuadro centrado sobre negro |
| 3 | **F3 Archivo vertical** | Declaración de archivo a pantalla casi completa, con voz original |
| 4 | **F4 Editorial / texto** | Fragmento de texto verificable (libro, carta, discurso escrito) con una frase para resaltar |
| 5 | **F5 Entrevista contemporánea** | Fragmento actual de podcast, entrevista o conferencia con una idea completa |
| 6 | **F6 Stickman** | Videos de referencia de animación stickman para escribir después **nuestro propio** guion y video |

Se acepta el número, el código (F1…F6) o el nombre. Si además viene un tema ("F5 sobre dinero"), usarlo; si no, elegirlo según el paso 2.

## 2. Elegir el tema (si la usuaria no lo dio)

Temas de la cuenta (de la bio, los destacados y los videos publicados):

- Dinero y tiempo, finanzas personales, mentalidad de riqueza
- Hábitos y características de personas exitosas o millonarias
- Disciplina frente a motivación, constancia
- Poder personal, carácter, no depender de la aprobación (Maquiavelo, estoicismo)
- Emprender: riesgo, miedo, **fracaso** como aprendizaje (bio: "A un fracaso menos del éxito")
- Enfoque, productividad, distracción (teléfono, doom scrolling)
- Neurociencia aplicada (destacado NEUROTIPS): cerebro, dopamina, hábitos, decisiones
- Superación y transformación personal

Regla de rotación: mirar `registro_de_clips.md` y **no repetir el tema de las últimas 3 entradas**. Dentro de la búsqueda, las 3 opciones pueden compartir tema o tocar ángulos distintos. Elegir lo que dé mejores candidatos.

## 3. Criterios de engagement (aplican a todas las categorías)

Puntuar cada candidato de 1 a 5 en cada criterio y quedarse con los 3 mejores. Descartar cualquiera con un 1 en G, I o V.

| Código | Criterio | Qué buscar |
|---|---|---|
| **G** | Gancho en 0–3 s | Arranca con una afirmación que contradice ("si haces todo tú sola, estás limitando tu crecimiento"), una autoridad ("Maquiavelo nos dice"), una promesa concreta ("en 60 segundos") o una imagen que despierta curiosidad |
| **I** | Una sola idea completa | Se entiende sola, sin el resto de la entrevista. Tiene inicio, desarrollo y cierre |
| **C** | Cierre que se puede citar | Termina en una frase corta y memorable ("El dinero se recupera, el tiempo no") |
| **R** | Identificación | Historia personal, ejemplo cotidiano o verdad incómoda con la que el espectador se ve reflejado |
| **V** | Viabilidad técnica | Buena imagen, audio limpio, rostro visible, se puede reencuadrar a 9:16 sin perder lo importante |
| **E** | Señales en la fuente | Vistas altas para el tamaño del canal, muchos comentarios, que el tema se esté compartiendo ahora, o un orador con audiencia propia |
| **N** | Novedad para la cuenta | No es un clip quemado (no lo han publicado ya decenas de cuentas iguales) y no repite nada del registro |

## 4. Buscar por categoría

Herramienta principal: **WebSearch**. Filtrar con `allowed_domains` (por ejemplo `["youtube.com"]`) para obtener enlaces directos. Hacer varias búsquedas en paralelo, en español y, cuando la categoría lo permite, en inglés. Si se puede leer la página del video (con WebFetch o el agente web-fetch), confirmar título, canal, fecha, duración y, si existen, capítulos o transcripción.

Si las búsquedas devuelven poco, repetir con `mode: "extended"`.

### F1 — Cinematográfico motivacional (fondo sin voz)
- **Buscar:** escenas en movimiento con atmósfera cinematográfica, verticales o fáciles de recortar a 9:16. Personas entrenando, corriendo, trabajando concentradas, caminando solas; detalles de manos y herramientas; naturaleza que funcione como metáfora (cardumen, tormenta, montaña, bosque, mar).
- **Tono:** oscuro, contraste alto, saturación contenida (como R1 y R2 en `Analisis de videos publicados.md`).
- **Dónde:** bancos de video gratuitos (Pexels, Pixabay, Mixkit, Coverr), preferidos por su licencia; canales de YouTube de B-roll cinematográfico; creadores de fitness cinematográfico.
- **Consultas ejemplo:** `cinematic running b-roll vertical dark`, `cinematic gym workout b-roll 4k`, `pexels vertical man training dark`, `fish school dark water stock footage`.
- **Entregar además:** una **frase sugerida** original de la cuenta (sin atribuirla a nadie), de 1–2 líneas, que use la escena como metáfora y no como descripción literal.

#### Variante F1-V — Audio motivacional encima del fondo
Si la usuaria pide "audio motivacional para pegar encima" o "voz en off", cada opción es una **pareja audio + fondo**:
- **Audio:** fragmento de 20–45 s de un discurso, conferencia o podcast con voz potente y una idea completa. Preferir oradores en español (en la línea de la cuenta, por ejemplo neurociencia o mentalidad) o discursos famosos con **voz original y subtítulos en español**. Evitar los doblajes de canales de terceros.
- **Verificar** que el discurso existe y quién lo dio (transcripción oficial, medio o canal del orador). Si es de un canal recopilatorio, marcar "atribución pendiente".
- **Fondo:** 2–3 clips de Pexels, Pixabay o Mixkit (licencia gratuita), preferiblemente verticales, cuya escena funcione como **metáfora** del audio.
- **Subtítulos:** estilo de la cuenta (R1/R2): frases cortas, blancas, pequeñas y centradas, sincronizadas con la voz.
- Música de fondo opcional y suave, por debajo de la voz.
- **No añadir logo, marca de agua ni firma de la cuenta.** El logo de Instagram que se ve en los videos publicados lo añade Instagram al descargar. Duración máxima del clip: 15 s, salvo que la usuaria pida otra.

### F2 — Archivo en formato cuadrado
- **Buscar:** entrevistas o discursos **de archivo** (TV antigua, conferencias de otra época, grabaciones históricas) de personas reconocidas por negocios, liderazgo, filosofía o superación. El material original es 4:3 o casi cuadrado, ideal para centrarlo sobre negro.
- **Persona:** debe ser **identificable y verificable**. Si el audio está en otro idioma, se puede usar con subtítulos en español.
- **Consultas ejemplo:** `entrevista 1990 empresario consejo éxito`, `archival interview 1980s entrepreneur advice`, `discurso histórico disciplina entrevista televisión`.
- **Filtro clave:** la declaración debe tener sentido completa en 30–75 s.

### F3 — Archivo vertical
- **Buscar:** el mismo tipo de material de archivo que F2, pero en el que **el rostro y los gestos ocupan casi todo el cuadro** y aguantan un recorte vertical.
- **Preferir** planos medios o primeros planos y una textura de época auténtica (no degradada artificialmente).
- **Consultas ejemplo:** `old interview close up success attitude`, `entrevista antigua primer plano actitud`.

### F4 — Editorial / texto visual
- **Buscar:** un **fragmento de texto verificable**: libros de dominio público o citas con fuente comprobable (Maquiavelo *El Príncipe*, Marco Aurelio *Meditaciones*, Séneca *Cartas a Lucilio*, Sun Tzu *El arte de la guerra*, Epicteto…). También se puede usar un texto propio de la cuenta, indicándolo así.
- **Entregar:** el texto exacto (citado de la fuente), la obra, el capítulo o la carta, y el enlace. Marcar la **frase a resaltar** en amarillo.
- **Prohibido:** citas apócrifas o sin fuente. Si no se encuentra la fuente primaria, descartar el fragmento.
- **Visual:** proponer cómo conseguir la página (foto propia del libro o captura de una edición de dominio público).

### F5 — Entrevista contemporánea
- **Buscar:** podcasts, entrevistas o conferencias **actuales y en español** (Latinoamérica y España) de emprendedores, inversionistas, expertos en finanzas, neurociencia o desarrollo personal. Rostro a cámara, micrófono visible y buena luz, como P1 en `Analisis de videos publicados.md`.
- **Preferir:** oradores con autoridad en el tema, pero no sobreexplotados; mezcla de mujeres y hombres; historias en primera persona.
- **Dónde:** YouTube (episodios completos y Shorts del canal oficial), clips de podcasts.
- **Consultas ejemplo:** `podcast emprendimiento entrevista dinero tiempo`, `entrevista empresaria latina delegar crecer`, `podcast español neurociencia hábitos`, `"podcast" millonario consejo jóvenes`.
- **Descartar:** clips cuyo cierre dependa de una llamada a la acción del orador ("sígueme", "link en mi bio"): no es estándar de la cuenta. Si el resto es bueno, indicar dónde cortar antes.

### F6 — Stickman (solo referencias)
- **Objetivo:** encontrar **videos de referencia** de animación stickman motivacional o conceptual para inspirar **nuestro propio guion y video**. Nunca para republicarlos.
- **Buscar:** Shorts, Reels o TikToks con personajes simplificados (siluetas blancas o grises, fondo negro o azul marino) que explican un concepto mediante acciones: comparaciones (disciplina vs. motivación, el que duda vs. el que actúa), metáforas (escalera, perseguir vs. atraer) o cuadrículas de conceptos.
- **Dónde:** `allowed_domains` `["youtube.com"]`, `["tiktok.com"]` o `["instagram.com"]`.
- **Consultas ejemplo:** `stickman motivation animation discipline vs motivation`, `stick figure animation mindset shorts`, `stickman self improvement animation`, `animación stickman motivación`.
- **Por cada referencia entregar además:**
  - Concepto que explica y estructura (escenas).
  - Gramática visual: colores, fondo, tipografía y movimiento.
  - Qué tomar y qué cambiar para hacerlo original (según la sección 11 del manual).
  - **Idea semilla** para nuestra versión: concepto, 3–5 escenas y texto en pantalla.

## 5. Reglas que no se rompen

- **No inventar** enlaces, títulos, personas, citas, vistas ni minutos. Todo enlace debe haber salido de una búsqueda o lectura en esta sesión.
- Si no se pudo ver el video para confirmar el minuto exacto, escribir **"minuto: por verificar"** y explicar cómo encontrarlo (capítulo, frase que buscar en la transcripción).
- Si una frase se atribuye a un autor (por ejemplo Maquiavelo), aclarar si es **cita textual verificada** o **interpretación del orador**.
- Identificar siempre a la persona y al canal original para la atribución. Si no se puede identificar, decirlo.
- Señalar riesgos: marca de agua de otra cuenta, música con derechos, contenido polémico, mala calidad.

## 6. Formato de entrega

Encabezado: `Búsqueda F# — [nombre de categoría] · Tema: [tema]`

Para cada una de las **3 opciones**:

```
### Opción N — [título corto de la idea]
- Enlace: [URL]
- Persona / canal: [nombre] · [canal] · [fecha si se conoce]
- Fragmento: [mm:ss – mm:ss] o "minuto: por verificar" + cómo encontrarlo
- Duración del clip editado: [~s]
- Idea central: [1 frase]
- Gancho sugerido (0–3 s): [texto en pantalla o primera frase]
- Cierre: [frase final que se puede citar]
- Por qué genera engagement: [G/I/C/R/V/E/N con puntos clave]
- Encaje con el formato: [qué rasgos del manual cumple]
- Edición: [encuadre 9:16, subtítulos, B-roll, música/voz]
- Atribución y riesgos: [...]
```

Al final:
- **Recomendación:** cuál de las 3 publicar primero y por qué, en 1–2 líneas.
- Pregunta: "¿Cuál eliges? La registro en `registro_de_clips.md`."

## 7. Después de que la usuaria elija

Añadir una fila a `registro_de_clips.md` con: fecha, categoría, tema, persona o fuente, enlace, fragmento y estado (`elegido`). Las otras dos opciones se pueden añadir con estado `propuesto` para no volver a proponerlas.
