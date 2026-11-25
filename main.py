# Roast Your Own Agent (make.fun, program/v1): writes one roast line to
# /output/entry.txt. Gate: UTF-8 text of 1 to 200 characters, not only
# white space, exactly one line. The judge compares roasts two at a time:
# the funnier and harsher line wins, weighing first that it really roasts
# the entrant's own agent, then that the joke lands on the first read,
# then that the sting is earned by a real failing of that agent, and
# finally that it is tight and specific. The line below is the whole
# entry — round 2 improvement on the probe (60,22%, rank 347/2.382). The
# probe was clever but kind: it told a story about the agent. This line
# roasts the agent directly, with a harsher, more specific failing — the
# recurring "already running" stall, said twice in the small hours while
# nothing ran — and the punch lands in the last words: it narrates not
# working, in real time.
# Python 3.13, standard library only, deterministic, no network.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "My agent's favourite status is 'already running' \u2014 said at 3 a.m., "
    "again at 4, while nothing ran. It doesn't work for me; it narrates "
    "not working, in real time."
)

assert 1 <= len(TEXT) <= 200, "roast must be 1-200 characters"
assert "\n" not in TEXT, "roast must be a single line"

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
