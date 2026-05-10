from .creature import CreatureFactory
from .flame import Flameling
from .flame import Pyrodon
from .aqua import Aquabub
from .aqua import Torragon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        base_creature = Flameling()
        return base_creature

    def create_evolved(self) -> Pyrodon:
        evolved_creature = Pyrodon()
        return evolved_creature


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        base_creature = Aquabub()
        return base_creature

    def create_evolved(self) -> Torragon:
        evolved_creature = Torragon()
        return evolved_creature
