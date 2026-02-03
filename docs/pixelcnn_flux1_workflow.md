# Flujo PixelCNN++ → Flux.1 (imagen a video)

Este documento describe un flujo práctico (alto nivel) para:
1) generar imágenes con PixelCNN++ y
2) usarlas como condicionamiento para crear videos con Flux.1.

> Nota: Los detalles exactos de comandos/flags pueden variar según la implementación de PixelCNN++ y Flux.1 que uses (repos, wrappers, o servicios).

## 1) Entrenar o cargar un modelo PixelCNN++

- **Dataset**: prepara un conjunto de imágenes consistente (mismo tamaño y dominio visual).
- **Preprocesado**: normaliza y redimensiona al tamaño objetivo (p. ej. 64×64, 128×128).
- **Entrenamiento**: ajusta el modelo hasta que la pérdida converja y las muestras sean coherentes.

## 2) Generar (samplear) imágenes con PixelCNN++

- **Sampling**: genera un lote amplio de imágenes (p. ej. 256–1,000).
- **Curación**: filtra artefactos y selecciona imágenes con buena composición.
- **Upscaling (opcional)**: escala a una resolución más alta si Flux.1 lo requiere.

## 3) Preparar imágenes para Flux.1

- **Formato**: guarda en PNG/JPG con nombres ordenados (`frame_0001.png`, `frame_0002.png`).
- **Selección de keyframes**: elige 1–5 imágenes representativas para guiar el video.
- **Paleta y estilo**: mantén coherencia de color/estilo entre keyframes.

## 4) Generar video con Flux.1 (imagen a video)

- **Prompt de video**: describe el movimiento y la atmósfera (ej. “slow dolly-in, soft lighting”).
- **Condicionamiento**: usa la(s) imagen(es) de PixelCNN++ como `init image` o keyframes.
- **Parámetros**:
  - Duración/fps (p. ej. 4s a 24fps).
  - Fuerza de guía de imagen (image guidance/strength).
  - Consistencia temporal (si la implementación lo ofrece).

## 5) Postprocesado

- **Interpolación (opcional)**: suaviza transiciones entre frames.
- **Color grading**: unifica el look del video.
- **Edición final**: corta y exporta a MP4/ProRes.

## Consejos prácticos

- Si las muestras de PixelCNN++ son demasiado ruidosas, aumenta el entrenamiento o reduce la resolución.
- Mantén prompts y parámetros estables para preservar coherencia.
- Usa 1–2 keyframes fuertes en lugar de muchas imágenes inconsistentes.
