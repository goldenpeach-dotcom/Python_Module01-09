from collections.abc import Callable

Spell = Callable[[str, int], str]

def spell_combiner(spell1: Spell, spell2: Spell) -> (
    Callable[[str, int],tuple[str, str]]
):
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],spell: Spell
) -> Spell:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    def cast_all(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return cast_all

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power}HP"


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined: Callable = spell_combiner(fireball, heal)
    result: tuple[str, str] = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print()

    print("Testing power amplifier...")
    original_power: int = 10

    def power_echo(target: str, power: int) -> str:
        return str(power)

    mega_fireball: Callable = power_amplifier(power_echo, 3)
    print(f"Original: {original_power}, "
          f"Amplified: {mega_fireball('Dragon', original_power)}")
    print()

    print("Is fireball callable?", callable(fireball))

    print()
    print("Testing conditional caster...")
    strong_enough: Callable = conditional_caster(lambda t, p: p >= 20, fireball)
    print(strong_enough("Dragon", 5))
    print(strong_enough("Dragon", 25))

    print()
    print("Testing spell sequence...")
    sequence: Callable = spell_sequence([fireball, heal])
    print(sequence("Dragon", 15))