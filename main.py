#!/usr/bin/env python3
"""news-image-20261126 entrypoint.

Copies the front-page image (entry.png, 1024x1024) shipped in this
repository to the grader's output directory. The image was rendered
from frontpage.html (hand-written in this repo) with a headless
browser at build time; at grade time this program needs no network,
no third-party package and no font -- it only copies bytes, so both
grader runs write byte-identical output.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1048576


def _check_png(path: str) -> None:
    """Fail loudly unless path is a whole PNG, 1024x1024 or smaller, <= 1 MiB."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    width, height = struct.unpack(">II", head[16:24])
    if width > 1024 or height > 1024:
        raise SystemExit("entry.png is larger than 1024x1024")
    if os.path.getsize(path) > MAX_BYTES:
        raise SystemExit("entry.png is larger than 1 MiB")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    _check_png(src)
    if os.path.abspath(src) == os.path.abspath(dst):
        return 0
    shutil.copyfile(src, dst)
    _check_png(dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
