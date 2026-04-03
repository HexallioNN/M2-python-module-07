from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if game_state["mana_available"] > self.cost:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
            }
        else:
            return {}

    def resolve_effect(self, targets: list) -> dict:
        if not targets:
            return {"resolved": False, "reason": "No targets provided"}

        return {
            "resolved": True,
            "effect_type": self.effect_type,
            "targets_affected": [str(t) for t in targets],
            "count": len(targets)
        }
