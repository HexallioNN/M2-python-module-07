from Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        base_info = super().get_card_info()
        base_info["type"] = "Creature"
        base_info["attack"] = self.attack
        base_info["health"] = self.health
        return base_info

    def play(self, game_state: dict) -> dict:
        if game_state["mana_available"] > self.cost:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
        else:
            return {}

    def attack_target(self, target) -> dict:
        if self.playability:
            return {
                "attacker": self.name,
                "target": target,
                "damage_dealt": self.attack,
                "combat_resolved": self.playability
            }
        else:
            return {}
