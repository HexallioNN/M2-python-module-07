from CreatureCard import CreatureCard


if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design\n")
    Fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 8)
    print("CreatureCard Info:")
    print(Fire_dragon.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable {Fire_dragon.is_playable(6)}")
    print(f"Play result: {Fire_dragon.play({})}")
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {Fire_dragon.attack_target("Goblin Warrior")}")
    print("\nTesting insufficient mana (3 available)")
    print(f"Playable {Fire_dragon.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")
