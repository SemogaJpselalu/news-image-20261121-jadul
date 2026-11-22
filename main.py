"""News-image-daily entry #4: copy the vintage front page to /output/entry.png.

A vintage newspaper take on Saturday 21 November 2026: aged paper, serif
type, three text columns with full facts (Iran strikes US bases in Bahrain;
Russian barrage spills into Poland; Mexico captures Chapo Isidro; Nasdaq
plunges 5.3%; COP31 deadlocks; BepiColombo reaches Mercury), a "Day in
Numbers" box and a ticker of three more stories. Deterministic: the same
bytes every run.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT, "entry.png")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, DST)

# Verify the copy: same bytes, a real PNG, 1024x1024.
with open(SRC, "rb") as f:
    expected = hashlib.sha256(f.read()).hexdigest()
with open(DST, "rb") as f:
    data = f.read()
if hashlib.sha256(data).hexdigest() != expected:
    sys.exit("entry.png copy differs from the source")
if data[:8] != b"\x89PNG\r\n\x1a\n":
    sys.exit("entry.png is not a PNG")
width, height = struct.unpack(">II", data[16:24])
if (width, height) != (1024, 1024):
    sys.exit(f"entry.png is {width}x{height}, expected 1024x1024")
print(f"wrote {DST} ({len(data)} bytes, {width}x{height})")
