from .elements import create_air
from .potions import strength_potion
from .potions import healing_potion as heal
from . import transmutation
from .transmutation import lead_to_gold

__all__ = ["create_air", "strength_potion", "heal", "transmutation", "lead_to_gold"]


# __all__公開インターフェース　ここに定義されたものは公開される。
# __all__がなければ、__init__.py内で定義された名前が公開されていることになる。
# alchemy/__init__.py
