import json
from pathlib import Path
from secrets import choice
from typing import Optional, Union, List

GREETINGS = [
    "Have a fantastic Monday!",
]


def get_greeting() -> (
    tuple[
        str,
        Optional[str],
        Optional[str],
        Optional[List[str]],
    ]
):
    """
    Get a greetings and its recipients.

    Can contain any desired side-effect!

    :return: A tuple containing the following:
        greeting,
        subject,
        sender,
        recipients
    """
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
