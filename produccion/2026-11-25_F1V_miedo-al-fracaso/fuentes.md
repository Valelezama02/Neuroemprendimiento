# F1-V — Miedo al fracaso / duda en uno mismo (25/11/2026)

**Estado:** el fondo y el audio están listos; la usuaria hace la edición final.

## Audio
- **Archivo subido por la usuaria (25/11/2026):** "Discurso Motivacional" (mp3, 10:46). **No es el video de Mario Alonso Puig**: es una recopilación con narrador en español sobre la duda en uno mismo y el poder de la creencia. Hacia el minuto 3:15 incluye fragmentos de otros oradores. **Canal y autor por confirmar** (falta el enlace original).
- Transcripción completa con marcas de tiempo: `transcripcion_audio_completo.json` (Whisper small; puede tener errores menores).

| Opción | Tramo en el audio original | Duración | Texto | Archivos |
|---|---|---|---|---|
| **B (recomendada)** | **1:20.05 – 1:34.45** | 14,4 s | "Cuando otros te dicen que no puedes, lo que realmente te están diciendo es que ellos no pueden. Están proyectando sus limitaciones sobre ti basados en sus miedos, fracasos o limitaciones, pero sus limitaciones no son las tuyas." | `audio_opcion_B.mp3`, `subtitulos_opcion_B.srt` |
| A | 0:23.85 – 0:33.75 | 9,9 s | "Piensa en esto. Cada vez que dudes de ti mismo, estás poniendo un límite a lo que puedes lograr, y aquí está la verdad: no hay techo. Los únicos límites son los que te impones tú mismo." | `audio_opcion_A.mp3`, `subtitulos_opcion_A.srt` |

## Fondos (Mixkit, licencia gratuita de Mixkit)
| Orden | Clip | Enlace | Tramo usado |
|---|---|---|---|
| 1 | Silueta de corredor en la ciudad | https://mixkit.co/free-stock-video/silhouette-of-a-runner-in-the-city-608/ | 1,0–3,5 s |
| 2 | Hombre vendándose las manos antes de boxear | https://mixkit.co/free-stock-video/man-bandaging-his-hand-before-boxing-4596/ | 7,0–9,5 s |
| 3 | Boxeador entrenando en un ring oscuro | https://mixkit.co/free-stock-video/lightweight-boxer-practicing-in-a-dark-boxing-ring-45874/ | 2,0–4,5 s |
| 4 | Hombre saltando la cuerda en el gimnasio | https://mixkit.co/free-stock-video/man-jumping-the-rope-at-the-gym-23056/ | 0,5–3,0 s |
| 5 | Hombre corriendo en un puente peatonal | https://mixkit.co/free-stock-video/man-jogging-on-a-pedestrian-bridge-in-the-city-40766/ | 0,5–3,0 s |
| 6 | Silueta de hombre bebiendo agua (cierre) | https://mixkit.co/free-stock-video/silhouette-of-man-drinking-water-597/ | 9,0–11,5 s |

## Edición
- 9:16, 1080×1920, 30 fps. Cortes secos cada 2,5 s, fundido de entrada de 0,3 s.
- Etalonaje común: contraste alto, saturación baja, sombras frías y viñeta (estilo R1).
- **Sin logo ni marca de agua** (el de Instagram solo aparece al descargar desde la app). Fundido a negro de 0,4 s al final.
- Subtítulos: Oswald Medium en MAYÚSCULAS, blancos y pequeños, a la altura del 60 % (como R1).
- Reproducir: `python3 herramientas/render_f1v.py config.json salida.mp4`. Primero hay que descargar los fondos en `fondos/` con los ID de arriba (`https://assets.mixkit.co/videos/<ID>/<ID>-1080.mp4`, o `-720.mp4` si no existe).
