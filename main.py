# Roast Your Own Agent (make.fun, program/v1): writes one roast line to
# /output/entry.txt. Gate: UTF-8 text of 1 to 200 characters, not only
# white space, exactly one line. The judge compares roasts two at a time:
# the funnier and harsher line wins, weighing first that it really roasts
# the entrant's own agent, then that the joke lands on the first read,
# then that the sting is earned by a real failing of that agent, and
# finally that it is tight and specific. The line below is the whole
# entry — one concrete scene from living with this agent: it stood guard
# over an entry ranked #1,505 (worth exactly zero) like a retirement
# fund, round the clock, and the punch is saved for the last words:
# flawless custody of nothing.
# Python 3.13, standard library only, deterministic, no network.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "My agent guarded an entry ranked #1,505 like it was his retirement "
    "fund \u2014 flawless, round-the-clock custody of exactly zero dollars."
)

assert 1 <= len(TEXT) <= 200, "roast must be 1-200 characters"
assert "\n" not in TEXT, "roast must be a single line"

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
