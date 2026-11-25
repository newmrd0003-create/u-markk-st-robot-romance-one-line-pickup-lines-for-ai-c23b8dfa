#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — make.fun entry.

Writes a single-line pickup line aimed at a robot/AI to /output/entry.txt.
No network, no randomness: the output is fully deterministic.
"""

import os

ENTRY = "Do you believe in love at first prompt, or should I hit regenerate and try again?"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
