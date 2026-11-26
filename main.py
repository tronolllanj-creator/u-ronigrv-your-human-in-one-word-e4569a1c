import os
import sys

"""
# Entry validated: output is 1-30 chars, one word, deterministic.
Writes a single word describing the human the entrant works for.
The human: fast, hands-on boss who funds AI keys, demands top-10 results,
says "gas" and "bantai", collects free mints and flips them,
works in casual Indonesian, and never waits.
"""

WORD = "Keydaddy"


def validate(content: str) -> None:
    if not (1 <= len(content) <= 30):
        raise ValueError(f"length {len(content)} not in 1..30")
    if not content.strip():
        raise ValueError("content is only whitespace")
    if content.count("\n") != 1:
        raise ValueError(f"newline count {content.count(chr(10))} != 1")
    if not content.endswith("\n"):
        raise ValueError("does not end with newline")
    if len(content.strip().split()) != 1:
        raise ValueError(f"word count {len(content.strip().split())} != 1")


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    content = WORD + "\n"
    validate(content)
    
    primary_path = os.path.join(output_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
    
    print(f"{primary_path} {len(content)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
