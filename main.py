import csv
import os

FILENAME = "games.csv"

# Ensure the CSV file exists and has headers
if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "teams", "level", "pay"])


def add_game():
    """Prompt user for game details and save to CSV."""
    date = input("Enter game date (YYYY-MM-DD): ")
    teams = input("Enter teams (e.g., Team A vs Team B): ")
    level = input("Enter game level (U12, HS, etc.): ")
    pay = input("Enter pay amount: ")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, teams, level, pay])

    print("✅ Game added successfully!")


def view_games():
    """Display all logged games."""
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        games = list(reader)

    if not games:
        print("No games logged yet.")
    else:
        print("\nYour Games:")
        for game in games:
            print(f"- {game[0]} | {game[1]} | {game[2]} | ${game[3]}")


def menu():
    """Main menu loop."""
    while True:
        print("\nRef Log Menu")
        print("1. Add a game")
        print("2. View games")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_game()
        elif choice == "2":
            view_games()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    menu()

