# PixelCNN++ → Flux.1 Pipeline

Proyecto base para generar imágenes con PixelCNN++ y usarlas como condicionamiento en Flux.1 para crear videos. Incluye estructura, configs de ejemplo y un CLI que prepara los insumos y deja artefactos listos para ejecutar tus binarios reales.

> Este repo no incluye modelos ni pesos. El objetivo es darte un esqueleto funcional y reproducible.

## Estructura

```
.
├─ configs/
│  ├─ pixelcnn_config.json
│  └─ flux1_config.json
├─ docs/
│  └─ pixelcnn_flux1_workflow.md
├─ scripts/
│  └─ run_pipeline.sh
├─ src/
│  └─ pixelcnn_flux1_pipeline/
│     ├─ __init__.py
│     ├─ __main__.py
│     ├─ config.py
│     ├─ pipeline.py
│     └─ utils.py
└─ pyproject.toml
```

## Requisitos

- Python 3.10+
- (Opcional) tus binarios/CLI reales para PixelCNN++ y Flux.1

## Uso rápido

1) Generar imágenes (modo dummy opcional):

```bash
python -m pixelcnn_flux1_pipeline generate-images --config configs/pixelcnn_config.json
```

2) Preparar el job de Flux.1:

```bash
python -m pixelcnn_flux1_pipeline make-video --config configs/flux1_config.json
```

3) Ver artefactos generados:

- Imágenes: `outputs/pixelcnn_samples/`
- Metadata: `outputs/pixelcnn_samples/metadata.json`
- Job de video: `outputs/flux1_job.json`

## Flujo recomendado

Consulta la guía en `docs/pixelcnn_flux1_workflow.md` para entender el proceso completo y cómo ajustar parámetros.
