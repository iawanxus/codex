#!/usr/bin/env bash
set -euo pipefail

python -m pixelcnn_flux1_pipeline generate-images --config configs/pixelcnn_config.json
python -m pixelcnn_flux1_pipeline make-video --config configs/flux1_config.json
