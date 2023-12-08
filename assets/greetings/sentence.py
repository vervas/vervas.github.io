from secrets import choice


GREETINGS = [
    "Have a fantastic Monday!",
]


def get_greeting() -> str:
    return choice(GREETINGS)
