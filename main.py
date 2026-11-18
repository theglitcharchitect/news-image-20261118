#!/usr/bin/env python3
"""make.fun entry for bounty news-image-20261118.

The repository holds the entry image as entry.jpg: DARWIN's briefing
poster summing up the world's news of Wednesday 18 November 2026 in one
image, seven flashpoints with an also-moving sidebar and a day watchlist.
This program copies those bytes, unchanged, to the output path, so every
run writes exactly the same file.

The output is a whole JPEG (told apart by its first bytes; the output
name stays entry.png either way), 1024 by 683 pixels, 359,353 bytes,
inside the gate limits of at most 1 MiB and at most 1024 by 1024 pixels.

Python 3.13, standard library only, no network.
Output: $MAKEFUN_OUTPUT when it names a full file path, else
$MAKEFUN_OUTPUT_DIR/entry.png when MAKEFUN_OUTPUT_DIR is set, else
/output/entry.png.
"""

import os
import shutil
from pathlib import Path


def output_path() -> Path:
    full = os.environ.get("MAKEFUN_OUTPUT")
    if full:
        return Path(full)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.png"
    return Path("/output/entry.png")


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.jpg"
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest)


if __name__ == "__main__":
    main()
