from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    return (
        f"Healing potion brewed with "
        f"’{create_air()}’ and "
        f"’{create_earth()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with "
        f"’{create_fire()}’ and "
        f"’{create_water()}'"
    )

#  3"nything else useful to access the four fundamental elements.
# from .element import ...(相対インポート)
# from element import ...(絶対インポート)
