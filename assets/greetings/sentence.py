from secrets import choice
from typing import Optional

GREETINGS = [
    "Have a fantastic Monday!",
]


def get_greeting() -> tuple[str, Optional[str], Optional[str], Optional[str]]:
    return choice(GREETINGS), None, None, None
