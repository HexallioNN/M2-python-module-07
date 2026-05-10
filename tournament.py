from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    InvalidStrategyError
)


def fight(opponent1: list, opponent2: list) -> None:
    factory1, strategy1 = opponent1
    factory2, strategy2 = opponent2

    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(" * Battle *")
    print(f"{creature1.describe()}")
    print(" vs.")
    print(f"{creature2.describe()}")
    print(" now fight!")

    if not strategy1.is_valid(creature1):
        raise InvalidStrategyError(
            f"Invalid Creature '{creature1.name}' for this strategy"
        )
    strategy1.act(creature1)

    if not strategy2.is_valid(creature2):
        raise InvalidStrategyError(
            f"Invalid Creature '{creature2.name}' for this strategy"
        )
    strategy2.act(creature2)


def battle(opponents: list) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            try:
                fight(opponents[i], opponents[j])
                print()
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    print("Tournament 0 (basic)")
    tournament_0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    battle(tournament_0)

    print("Tournament 1 (error)")
    tournament_1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    battle(tournament_1)

    print("Tournament 2 (multiple)")
    tournament_2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    battle(tournament_2)


if __name__ == "__main__":
    main()
