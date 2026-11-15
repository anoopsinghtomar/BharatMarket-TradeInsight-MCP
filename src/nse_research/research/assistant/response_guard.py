UNSUPPORTED_PHRASES = ("guaranteed return", "certain to rise", "risk-free profit")


def validate_response_text(text: str) -> list[str]:
    lowered = text.lower()
    return [phrase for phrase in UNSUPPORTED_PHRASES if phrase in lowered]
