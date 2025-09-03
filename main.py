import csv
import os
from datetime import datetime

FILENAME = "games.csv"

# Ensure the CSV file exists and has headers
if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "teams", "level", "pay"])


def valid_date(date_str):
    """Check if date is valid (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def valid_pay(pay_str):
    """Check if pay is a valid number."""
    try:
        float(pay_str)
        return True
    except ValueError:
        return False


def add_game():
    """Prompt user for game details and save to CSV."""
    while True:
        date = input("Enter game date (YYYY-MM-DD): ")
        if valid_date(date):
            break
        print("❌ Invalid date format. Try again (YYYY-MM-DD).")

    teams = input("Enter teams (e.g., Team A vs Team B): ")
    level = input("Enter game level (U12, HS, etc.): ")

    while True:
        pay = input("Enter pay amount: ")
        if valid_pay(pay):
            break
        print("❌ Invalid pay. Must be a number.")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, teams, level, pay])

    print("✅ Game added successfully!")


def view_games(return_games=False):
    """Display all logged games. Returns games if requested."""
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        games = list(reader)

    if not games:
        print("No games logged yet.")
    else:
        print("\nYour Games:")
        for i, game in enumerate(games, start=1):
            print(f"{i}. {game[0]} | {game[1]} | {game[2]} | ${game[3]}")

    if return_games:
        return games


def delete_game():
    """Delete a game by selecting its number."""
    games = view_games(return_games=True)

    if not games:
        return

    try:
        choice = int(input("Enter the number of the game to delete: "))
        if 1 <= choice <= len(games):
            removed = games.pop(choice - 1)

            # Rewrite file without the deleted game
            with open(FILENAME, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["date", "teams", "level", "pay"])
                writer.writerows(games)

            print(f"🗑️ Deleted game: {removed[0]} | {removed[1]}")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("❌ Invalid input. Must be a number.")


def summary():
    """Show total games, total pay, and average pay."""
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        games = list(reader)

    if not games:
        print("No games logged yet.")
        return

    total_games = len(games)
    total_pay = sum(float(game[3]) for game in games)
    average_pay = total_pay / total_games

    print("\n📊 Summary:")
    print(f"Total games: {total_games}")
    print(f"Total pay: ${total_pay:.2f}")
    print(f"Average per game: ${average_pay:.2f}")


def menu():
    """Main menu loop."""
    while True:
        print("\nRef Log Menu")
        print("1. Add a game")
        print("2. View games")
        print("3. View summary")
        print("4. Delete a game")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_game()
        elif choice == "2":
            view_games()
        elif choice == "3":
            summary()
        elif choice == "4":
            delete_game()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, please try again.")


if __name__ == "__main__":
    menu()

