import json
from pathlib import Path
from secrets import choice
from typing import Optional, Union

GREETINGS = [
    "Have a fantastic Monday!",
]


def get_greeting() -> tuple[str, Optional[str], Optional[str], Optional[str]]:
    return choice(GREETINGS), None, None, None


def make_greeting(
    greeting: str,
    subject: Optional[str],
    sender: Optional[str],
    recipients: Optional[list[str]],
) -> dict[str, Union[str, list[str], None]]:
    payload = {
        "greeting": greeting,
        "subject": subject,
        "sender": sender,
        "recipients": recipients,
    }

    return payload


def main() -> None:
    greeting = make_greeting(*get_greeting())

    output_file = Path(__file__).parent.with_name("greeting.json")
    output_file.write_text(
        json.dumps(
            greeting,
            indent=4,
        )
    )


if __name__ == "__main__":
    main()
