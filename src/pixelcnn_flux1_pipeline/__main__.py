from __future__ import annotations

import argparse
from pathlib import Path

from .config import load_flux1_config, load_pixelcnn_config
from .pipeline import generate_pixelcnn_images, prepare_flux1_job


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PixelCNN++ → Flux.1 pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    images_parser = subparsers.add_parser("generate-images", help="Generar imágenes con PixelCNN++")
    images_parser.add_argument("--config", type=Path, required=True, help="Ruta a config JSON")

    video_parser = subparsers.add_parser("make-video", help="Preparar job de Flux.1")
    video_parser.add_argument("--config", type=Path, required=True, help="Ruta a config JSON")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "generate-images":
        config = load_pixelcnn_config(args.config)
        output_dir = generate_pixelcnn_images(config)
        print(f"Imágenes preparadas en: {output_dir}")
        return

    if args.command == "make-video":
        config = load_flux1_config(args.config)
        job_path = prepare_flux1_job(config)
        print(f"Job de Flux.1 listo en: {job_path}")
        return


if __name__ == "__main__":
    main()
