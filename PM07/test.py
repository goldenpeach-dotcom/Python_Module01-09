import pytest
from ex0 import FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


# --- DefensiveStrategy ---

def test_defensive_valid_with_healer():
    creature = HealingCreatureFactory().create_base()
    assert DefensiveStrategy().is_valid(creature) is True


def test_defensive_invalid_without_heal():
    creature = FlameFactory().create_base()
    assert DefensiveStrategy().is_valid(creature) is False


def test_defensive_act_order_and_content():
    strategy = DefensiveStrategy()
    creature = HealingCreatureFactory().create_base()

    result = strategy.act(creature)

    # 別インスタンスで同じメソッドを呼び、結果を突き合わせる
    reference = HealingCreatureFactory().create_base()
    assert result == [reference.attack(), reference.heal()]


def test_defensive_act_raises_on_invalid():
    creature = FlameFactory().create_base()
    with pytest.raises(InvalidStrategyError) as exc_info:
        DefensiveStrategy().act(creature)
    assert creature.name in str(exc_info.value)


# --- AggressiveStrategy ---

def test_aggressive_valid_with_transformer():
    creature = TransformCreatureFactory().create_base()
    assert AggressiveStrategy().is_valid(creature) is True


def test_aggressive_invalid_without_transform():
    creature = FlameFactory().create_base()
    assert AggressiveStrategy().is_valid(creature) is False


def test_aggressive_act_order_transform_attack_revert():
    strategy = AggressiveStrategy()
    creature = TransformCreatureFactory().create_base()

    result = strategy.act(creature)

    assert len(result) == 3
    # Shiftlingは変身するとattack()の文言が変わる仕様なので、
    # 「変身後attackを呼んでいるか」を実際の挙動で検証する
    check_creature = TransformCreatureFactory().create_base()
    check_creature.transform()
    assert result[1] == check_creature.attack()


def test_aggressive_act_raises_on_invalid():
    creature = FlameFactory().create_base()
    with pytest.raises(InvalidStrategyError):
        AggressiveStrategy().act(creature)


# --- NormalStrategy ---

def test_normal_is_valid_always_true():
    creature = FlameFactory().create_base()
    assert NormalStrategy().is_valid(creature) is True


def test_normal_act_returns_attack_only():
    strategy = NormalStrategy()
    creature = FlameFactory().create_base()

    result = strategy.act(creature)

    reference = FlameFactory().create_base()
    assert result == [reference.attack()]