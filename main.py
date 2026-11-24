#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Writes one job title, 60 characters at most, to /output/entry.txt.

The brief rewards a real-sounding job with one hilariously specific
twist, funny on the first read, specific enough to picture the person
doing it. Drafts considered and rejected in the revision pass:

- "Chief Apology Writer for Billionaires" — clever, but the twist is
  a client, not a job; less weird than the winner.
- "Senior Apologizer for Self-Driving Cars" — timely and specific,
  but the picture is abstract: a car cannot receive an apology.
- "Lead Penguin Counter, Antarctic Division" — a real job, funny,
  but the twist is mild; it reads as a job listing, not a joke.
- "Senior Sock Pairing Specialist" — funny and domestic, but small;
  the strangeness does not scale past the first smile.

The winner keeps the plausible job frame ("Full-Time Apologizer",
a title format any hiring page could print) and aims the twist at
the one animal everybody already knows is furious: geese. You can
picture the person at once — suited, clipboard in hand, saying
sorry to a hissing goose that does not accept. Six words, 36
characters, reads in one glance.
"""

import os
import stat

TITLE = "Full-Time Apologizer to Angry Geese"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 60


def main() -> None:
    title = TITLE.strip()
    assert title, "entry must not be empty or only whitespace"
    assert len(title) <= MAX_CHARS, (
        f"entry is {len(title)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(title)
    # The grader collects outputs as another user: leave it readable.
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(title)


if __name__ == "__main__":
    main()
