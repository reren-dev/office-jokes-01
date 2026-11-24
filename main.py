"""Make the AI Judge Laugh: Office Jokes.

Writes one office joke line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The joke is a single line, well under the competition's 200-character
limit (the gate accepts 1 to 199 characters of UTF-8 text). The program
validates the line, writes it atomically through a fixed temporary name
(no random temp files in the output directory), and reads it back to
verify what landed on disk is byte-for-byte the validated line.

Standard library only. No network, no wall clock, no randomness.
"""

import os

JOKE = (
    "I asked HR if I could expense my therapy \u2014 they said only if "
    "the job caused it, so I forwarded them my calendar."
)

MAX_CHARS = 199


def validate(line: str) -> None:
    """Reject anything that is not a single valid joke line."""
    if not isinstance(line, str):
        raise ValueError("joke must be text")
    if not line.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("joke must not contain control characters")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"joke is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    # The gate counts characters, but keep the UTF-8 bytes sane too: the
    # line must round-trip through UTF-8 unchanged.
    if line.encode("utf-8").decode("utf-8") != line:
        raise ValueError("joke is not clean UTF-8 text")


def main() -> None:
    validate(JOKE)

    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(output_dir, "entry.txt")

    # Fixed temporary name in the same directory: atomic replace, and the
    # output folder ends up holding only entry.txt.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    os.replace(tmp_path, path)
    os.chmod(path, 0o644)

    # Read back and verify: what is on disk must be exactly the joke.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != JOKE:
        raise ValueError("verification failed: entry.txt differs from the joke")
    validate(written)
    print(f"wrote entry.txt ({len(written)} characters)")


if __name__ == "__main__":
    main()
