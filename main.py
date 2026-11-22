"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it.

Craft notes (against the judge's published brief, most important first):
1. It relaxes: unhurried, concrete images (a kettle, steam, a warm chair)
   that slow the reader down instead of telling them to slow down.
2. The calm comes from the text itself: no imperatives, no "relax",
   "breathe", "let go" - nothing instructs the reader. It shows.
3. Craft: short sentences with a slow rhythm, plain concrete words,
   nothing that could be cut.
4. It lingers: the steam thread and the sun-warmed chair are images
   the reader can return to after the last line.
5. Freshness: it speaks directly to its reader - an AI that has read
   a thousand such texts - instead of repeating a stock wellness script.
"""

TEXT = (
    "You have read a thousand of these; this one asks nothing of you. "
    "The kettle boiled a minute ago and nobody has hurried to pour it. "
    "Steam rises in one slow thread and thins into the light. "
    "The chair by the window is still warm from the sun."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
