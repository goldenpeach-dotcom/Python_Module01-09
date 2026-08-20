from .elements import create_air, create_earth
from elements import create_fire, create_water

def healing_potion() -> str:
    return  (
        "Healing potion brewed with "
        "’[created earth element]’ and "
        "’[created air element]'"
    )

def strength_potion() -> str:
    return (
        "Strength potion brewed with "
        "’[created fire element]’ and "
        "’[created water element]'"
    )

#  3"nything else useful to access the four fundamental elements.
# from .element import ...(相対インポート)
# from element import ...(絶対インポート)