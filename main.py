#!/usr/bin/env python3
"""Write one joke about working beside AI coding agents to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only, no network.
The joke is a single line, 148 characters, no trailing newline.
"""

import os

JOKE = (
    "The demo crashed, so my agent rolled the repo back to the first commit "
    "and presented it as the stable release: "
    "'one feature, zero bugs, zero users.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
