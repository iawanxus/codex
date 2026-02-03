from __future__ import annotations

from datetime import datetime
from pathlib import Path

from .config import Flux1Config, PixelCNNConfig
from .utils import ensure_dir, list_images, write_json, write_ppm


def generate_pixelcnn_images(config: PixelCNNConfig) -> Path:
    ensure_dir(config.output_dir)

    if config.generate_dummy_images:
        for idx in range(config.num_samples):
            color = ((idx * 23) % 256, (idx * 47) % 256, (idx * 71) % 256)
            filename = config.output_dir / f"sample_{idx:04d}.ppm"
            write_ppm(filename, config.image_width, config.image_height, color)

    metadata = {
        "created_at": datetime.utcnow().isoformat() + "Z",
        "num_samples": config.num_samples,
        "image_width": config.image_width,
        "image_height": config.image_height,
        "generate_dummy_images": config.generate_dummy_images,
        "seed": config.seed,
    }
    write_json(config.output_dir / "metadata.json", metadata)
    return config.output_dir


def prepare_flux1_job(config: Flux1Config) -> Path:
    ensure_dir(config.output_dir)
    images = list_images(config.input_dir)
    selected = images[: config.keyframe_limit]

    payload = {
        "created_at": datetime.utcnow().isoformat() + "Z",
        "prompt": config.prompt,
        "fps": config.fps,
        "duration_seconds": config.duration_seconds,
        "image_guidance": config.image_guidance,
        "input_images": [str(path) for path in selected],
    }

    job_path = config.output_dir / "flux1_job.json"
    write_json(job_path, payload)

    summary_path = config.output_dir / "flux1_job_summary.txt"
    with summary_path.open("w", encoding="utf-8") as handle:
        handle.write("Flux.1 job preparado.\n")
        handle.write(f"Prompt: {config.prompt}\n")
        handle.write(f"Imágenes: {len(selected)}\n")
        handle.write("\n")
        handle.write("Ejecuta tu CLI de Flux.1 con el JSON anterior.\n")

    return job_path
