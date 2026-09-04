DEFAULT_NAME = "IA"
DEFAULT_LANGUAGE = "pt-BR"

GREETINGS = {
    "pt-BR": {
        "manha": "Bom dia",
        "tarde": "Boa tarde",
        "noite": "Boa noite",
        "neutral": "Ola",
    },
    "en": {
        "manha": "Good morning",
        "tarde": "Good afternoon",
        "noite": "Good evening",
        "neutral": "Hello",
    },
}


def _clean_text(value, default=""):
    if not isinstance(value, str):
        return default

    cleaned_value = value.strip()
    return cleaned_value or default


def build_configurable_greeting(name=DEFAULT_NAME, language=DEFAULT_LANGUAGE, period="neutral"):
    display_name = _clean_text(name, DEFAULT_NAME)
    selected_language = _clean_text(language, DEFAULT_LANGUAGE)
    selected_period = _clean_text(period, "neutral")

    if selected_language not in GREETINGS:
        selected_language = DEFAULT_LANGUAGE

    language_greetings = GREETINGS[selected_language]
    greeting = language_greetings.get(selected_period, language_greetings["neutral"])

    return f"{greeting}, {display_name}!"


def build_greeting(name="IA"):
    display_name = _clean_text(name, DEFAULT_NAME)
    return f"Ola, {display_name}! Ambiente de IA para desenvolvimento configurado e testado."


def main():
    print(build_greeting())


if __name__ == "__main__":
    main()
