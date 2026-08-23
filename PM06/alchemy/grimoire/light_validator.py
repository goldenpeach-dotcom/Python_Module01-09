

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed_ingredients = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()

    for ingredient in allowed_ingredients:
        if ingredient in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"

# in を文字列同士で使うと「右側の文字列の中に、左側の文字列が部分文字列として存在するか」を調べます(リストの要素検索とは違うので注意)。