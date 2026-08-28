def build_greeting(name="IA"):
    cleaned_name = name.strip() if isinstance(name, str) else ""
    display_name = cleaned_name or "IA"
    return f"Ola, {display_name}! Ambiente de IA para desenvolvimento configurado e testado."


def main():
    print(build_greeting())


if __name__ == "__main__":
    main()
