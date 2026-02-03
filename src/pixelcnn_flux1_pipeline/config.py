from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict


@dataclass
class PixelCNNConfig:
    output_dir: Path
    num_samples: int
    image_width: int
    image_height: int
    generate_dummy_images: bool
    seed: int | None = None


@dataclass
class Flux1Config:
    input_dir: Path
    output_dir: Path
    prompt: str
    fps: int
    duration_seconds: int
    image_guidance: float
    keyframe_limit: int


def _load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_pixelcnn_config(path: Path) -> PixelCNNConfig:
    data = _load_json(path)
    return PixelCNNConfig(
        output_dir=Path(data["output_dir"]),
        num_samples=int(data.get("num_samples", 16)),
        image_width=int(data.get("image_width", 64)),
        image_height=int(data.get("image_height", 64)),
        generate_dummy_images=bool(data.get("generate_dummy_images", False)),
        seed=data.get("seed"),
    )


def load_flux1_config(path: Path) -> Flux1Config:
    data = _load_json(path)
    return Flux1Config(
        input_dir=Path(data["input_dir"]),
        output_dir=Path(data["output_dir"]),
        prompt=str(data["prompt"]),
        fps=int(data.get("fps", 24)),
        duration_seconds=int(data.get("duration_seconds", 4)),
        image_guidance=float(data.get("image_guidance", 0.6)),
        keyframe_limit=int(data.get("keyframe_limit", 5)),
    )
