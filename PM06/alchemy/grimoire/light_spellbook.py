
def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    validation: str = validate_ingredients(ingredients)
    if "INVALID" in validation:
        return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"

    return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
