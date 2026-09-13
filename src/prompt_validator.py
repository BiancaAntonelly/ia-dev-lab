REQUIRED_ELEMENTS = {
    "contexto": ("contexto", "projeto", "cenario", "onde"),
    "tarefa": ("tarefa", "implemente", "crie", "edite", "gere"),
    "restricoes": ("restricao", "restricoes", "sem dependencia", "nao adicione"),
    "validacao": ("validacao", "valide", "teste", "criterio de aceite"),
}

QUALITY_STRONG = "strong"
QUALITY_PARTIAL = "partial"
QUALITY_WEAK = "weak"


def _normalize_prompt(prompt):
    if not isinstance(prompt, str):
        return ""

    return prompt.strip().lower()


def validate_prompt(prompt):
    normalized_prompt = _normalize_prompt(prompt)
    found = []

    for element, keywords in REQUIRED_ELEMENTS.items():
        if any(keyword in normalized_prompt for keyword in keywords):
            found.append(element)

    missing = [element for element in REQUIRED_ELEMENTS if element not in found]

    return {
        "is_valid": not missing,
        "found": found,
        "missing": missing,
        "quality": _classify_quality(found),
    }


def _classify_quality(found):
    if len(found) == len(REQUIRED_ELEMENTS):
        return QUALITY_STRONG

    if len(found) >= 2:
        return QUALITY_PARTIAL

    return QUALITY_WEAK
