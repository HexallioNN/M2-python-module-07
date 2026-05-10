from ex0.creature import CreatureFactory
from .healing import Sproutling
from .healing import Bloomelle
from .transform import Shiftling
from .transform import Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
