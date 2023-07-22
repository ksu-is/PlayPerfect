def display_achievements(games):
    print("Halo: The Master Chief Collection - Achievements Unlocked:")
    for game, achievements in games.items():
        print(f"{game}:")
        for achievement in achievements:
            print(f" - {achievement}")
        print()

def add_achievement(games, game, achievement):
    if game in games:
        games[game].append(achievement)
    else:
        games[game] = [achievement]
    print(f"Achievement '{achievement}' added to '{game}'.")

def remove_achievement(games, game, achievement):
    if game in games and achievement in games[game]:
        games[game].remove(achievement)
        print(f"Achievement '{achievement}' removed from '{game}'.")
    else:
        print("Achievement not found.")

def main():
    achievements = {
        "Halo: The Master Chief Collection": ["Pillar of Autumn", "Halo", "Truth and Reconciliation"],
        "Assassin's Creed Rogue": ["First Voyage", "Into the Abyss", "Tinkerer"],
        "Portal": ["Portal", "Long Jump", "Fratricide"],
    }

    
    while True:
        print("1. View Achievements")
        print("2. Add Achievement")
        print("3. Remove Achievement")
        print("4. Quit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            display_achievements(halo_achievements)
        elif choice == 2:
            game = input("Enter the Halo game name: ")
            achievement = input("Enter the achievement unlocked: ")
            add_achievement(halo_achievements, game, achievement)
        elif choice == 3:
            game = input("Enter the Halo game name: ")
            achievement = input("Enter the achievement to remove: ")
            remove_achievement(halo_achievements, game, achievement)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
