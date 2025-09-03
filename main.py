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

    print("Game added successfully!")


if __name__ == "__main__":
    # For now, just test adding one game
    add_game()

