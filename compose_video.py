#!/usr/bin/env python3
"""Compone un vídeo final con estructura fija: A + 10s(X) + B + 10s(Y) + C."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def run_ffmpeg(cmd: list[str]) -> None:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        if result.stderr:
            print(result.stderr.strip(), file=sys.stderr)
        raise SystemExit(result.returncode)


def make_temp_clip(
    source: Path,
    temp_dir: Path,
    label: str,
    seconds: int | None = None,
) -> Path:
    output = temp_dir / f"{label}.mp4"
    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(source),
    ]

    if seconds is not None:
        cmd.extend(["-t", str(seconds)])

    cmd.extend(
        [
            "-vf",
            "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1",
            "-r",
            "30",
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "20",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-ar",
            "48000",
            "-ac",
            "2",
            str(output),
        ]
    )
    run_ffmpeg(cmd)
    return output


def build_video(a: Path, x: Path, b: Path, y: Path, c: Path, output: Path) -> None:
    temp_dir = output.parent / f".{output.stem}_tmp"
    temp_dir.mkdir(parents=True, exist_ok=True)

    try:
        clips = [
            make_temp_clip(a, temp_dir, "01_a"),
            make_temp_clip(x, temp_dir, "02_x", seconds=10),
            make_temp_clip(b, temp_dir, "03_b"),
            make_temp_clip(y, temp_dir, "04_y", seconds=10),
            make_temp_clip(c, temp_dir, "05_c"),
        ]

        concat_file = temp_dir / "concat_list.txt"
        concat_file.write_text(
            "\n".join(f"file '{clip.resolve()}'" for clip in clips) + "\n",
            encoding="utf-8",
        )

        cmd = [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_file),
            "-c",
            "copy",
            str(output),
        ]
        run_ffmpeg(cmd)

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compone A + 10s(X) + B + 10s(Y) + C en un único mp4."
    )
    parser.add_argument("--a", required=True, type=Path, help="Vídeo fijo A (entradilla)")
    parser.add_argument("--b", required=True, type=Path, help="Vídeo fijo B (nudo)")
    parser.add_argument("--c", required=True, type=Path, help="Vídeo fijo C (cierre)")
    parser.add_argument("--x", required=True, type=Path, help="Vídeo variable X (se usan 10s)")
    parser.add_argument("--y", required=True, type=Path, help="Vídeo variable Y (se usan 10s)")
    parser.add_argument("--output", required=True, type=Path, help="Ruta del mp4 final")
    return parser.parse_args()


def validate_input(path: Path, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"No se encontró {label}: {path}")


def main() -> None:
    args = parse_args()

    if shutil.which("ffmpeg") is None:
        raise SystemExit("ffmpeg no está instalado o no está en PATH")

    validate_input(args.a, "A")
    validate_input(args.b, "B")
    validate_input(args.c, "C")
    validate_input(args.x, "X")
    validate_input(args.y, "Y")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    build_video(args.a, args.x, args.b, args.y, args.c, args.output)
    print(f"Vídeo creado: {args.output}")


if __name__ == "__main__":
    main()
