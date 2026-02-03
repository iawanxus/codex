from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def list_images(path: Path, extensions: Iterable[str] = (".png", ".jpg", ".jpeg", ".ppm")) -> list[Path]:
    images: list[Path] = []
    for ext in extensions:
        images.extend(sorted(path.glob(f"*{ext}")))
    return sorted(images)


def write_ppm(path: Path, width: int, height: int, color: tuple[int, int, int]) -> None:
    header = f"P3\n{width} {height}\n255\n"
    pixel = f"{color[0]} {color[1]} {color[2]}\n"
    with path.open("w", encoding="utf-8") as handle:
        handle.write(header)
        for _ in range(width * height):
            handle.write(pixel)
