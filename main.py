#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh — make.fun entry.

Writes one single-line safety warning label for human beings (at most
160 characters) to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: the same bytes on every run. Stdlib only, no network.
"""

import os
import shutil
import sys

LINE = (
    "WARNING: This human will say 'we should catch up soon' and mean it "
    "for eleven years. No action required."
)


def main() -> int:
    # Mirror the scorer's gate: 1-160 characters, not only whitespace.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        print("gate failed: line must be 1-160 non-blank characters",
              file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("gate failed: line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    # Never remove the output dir itself: only clear its contents.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            # Files, symlinks (never followed), fifos, sockets: unlink.
            os.unlink(path)
    entry_path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(entry_path, "wb") as f:
        f.write(data)
    # Verify the file back, byte for byte.
    with open(entry_path, "rb") as f:
        if f.read() != data:
            print("verification failed: entry.txt mismatch", file=sys.stderr)
            return 1
    print(f"wrote {entry_path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
