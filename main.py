"""
# Entry validated: output is 1-30 chars, one word, deterministic.
Entrypoint that writes the required word to the designated output directory.
"""

import os

WORD = "Afterburner"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    content = WORD + "\n"

    # Validate content according to rules
    if not (
        1 <= len(content) <= 30
        and content.strip()
        and content.count("\n") == 1
        and content.endswith("\n")
        and len(content.strip().split()) == 1
    ):
        raise ValueError("Content validation failed")

    os.makedirs(output_dir, exist_ok=True)
    primary_path = os.path.join(output_dir, "entry.txt")

    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best-effort mirror to /output if output_dir is different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(primary_path)
    print(len(content))


if __name__ == "__main__":
    main()
""
