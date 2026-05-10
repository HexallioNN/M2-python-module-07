from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature):
        pass

    @abstractmethod
    def act(self, creature):
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature):
        return True

    def act(self, creature):
        print(creature.attack())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature):
        return hasattr(creature, "heal")

    def act(self, creature):
        print(creature.attack())
        print(creature.heal())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature):
        return hasattr(creature, "transform") and hasattr(creature, "revert")

    def act(self, creature):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class InvalidStrategyError(Exception):
    pass
