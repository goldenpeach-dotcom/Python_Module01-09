from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()

    ingredients_lower = ingredients.lower()

    for ingredient in allowed_ingredients:
        if ingredient in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
