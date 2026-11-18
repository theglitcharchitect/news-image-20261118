"""Poster delivery program for the 18 November briefing image.

Running this module places the stored poster picture at the location
the harness asks for. The picture itself is kept alongside this file
under the name entry.jpg and measures 1024 by 683 pixels. On disk it
occupies 334294 bytes at the time of writing.

Those figures sit comfortably inside the limits set for this bounty:
a single file no larger than 1 MiB and no side longer than the
1024 by 1024 pixel ceiling.
"""

from pathlib import Path
import os


def destination_path():
    direct = os.environ.get("MAKEFUN_OUTPUT")
    if direct:
        return Path(direct)
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if folder:
        return Path(folder) / "entry.png"
    return Path("/output/entry.png")


def transfer_bytes(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    moved = 0
    with source.open("rb") as reader, target.open("wb") as writer:
        while True:
            piece = reader.read(65536)
            if not piece:
                break
            writer.write(piece)
            moved += len(piece)
    return moved


def run():
    here = Path(__file__).resolve().parent
    poster_file = here / "entry.jpg"
    if not poster_file.is_file():
        raise SystemExit(f"Missing poster file: {poster_file}")
    out_file = destination_path()
    written = transfer_bytes(poster_file, out_file)
    expected = poster_file.stat().st_size
    if written != expected:
        raise SystemExit(
            f"Short write: moved {written} of {expected} bytes"
        )
    print(f"Poster written to {out_file} ({written} bytes)")


if __name__ == "__main__":
    run()
