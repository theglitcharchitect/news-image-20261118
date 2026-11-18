#!/usr/bin/env python3
"""Entry program for the make.fun bounty news-image-20261118.

The repository carries the entry image beside this file as ``entry.jpg``:
one briefing poster that sums up the world news of Wednesday
18 November 2026. This program's only job is to place those bytes,
untouched, at the output path it is pointed at, so every run writes
exactly the same file.

The picture is a whole JPEG of 1024 by 683 pixels and 347,493 bytes,
inside the bounty's image gate of at most 1 MiB and at most 1024 by
1024 pixels. The output
keeps the name ``entry.png`` whatever the bytes are; the format reads
from the JPEG magic at the start of the file, not from the name.

Where the copy lands, first match wins:

* ``$MAKEFUN_OUTPUT`` when it names a full file path,
* ``$MAKEFUN_OUTPUT_DIR/entry.png`` when that variable is set,
* ``/output/entry.png`` otherwise.

Python 3.13, standard library only, no network.
"""

import os
import shutil
from pathlib import Path


def pick_destination() -> Path:
    named_file = os.environ.get("MAKEFUN_OUTPUT")
    if named_file:
        return Path(named_file)
    named_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if named_dir:
        return Path(named_dir) / "entry.png"
    return Path("/output/entry.png")


def main() -> None:
    poster = Path(__file__).resolve().parent / "entry.jpg"
    destination = pick_destination()
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(poster, destination)


if __name__ == "__main__":
    main()
