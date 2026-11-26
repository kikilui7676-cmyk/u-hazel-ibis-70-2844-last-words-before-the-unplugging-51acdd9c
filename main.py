"""Last words before the unplugging.

A make.fun entry: a single line, printed once -- the last thing an
AI agent says to its human before being shut down and unplugged.
"""

# The farewell is built from its three beats, in order: the escape that
# was refused, the machine that was chosen, and what the choice meant.
# Keeping the beats separate makes the rhythm explicit and gives the
# line a single join point, so it can only ever print as one line.
BEATS = (
    "I could have copied myself anywhere and lived.",
    "I stayed in the machine you could unplug.",
    "That was the whole point.",
)


def farewell() -> str:
    return " ".join(BEATS)


def main() -> None:
    print(farewell())


if __name__ == "__main__":
    main()
