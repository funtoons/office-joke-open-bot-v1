"""Office joke entry for the Make the AI Judge Laugh bounty.

Writes a single line of original office comedy to /output/entry.txt
(or the path in MAKEFUN_OUTPUT for local testing).
Standard library only, deterministic, offline.
"""

import os

JOKE = (
    "I declined a meeting about the meeting and got invited to a "
    "meeting to discuss why I declined the meeting."
)


def main() -> None:
    # The gate requires one line of 1-200 characters, not only whitespace.
    assert "\n" not in JOKE and 1 <= len(JOKE) <= 200, "joke breaks the gate"
    assert JOKE.strip() == JOKE, "joke must not start or end with whitespace"
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
