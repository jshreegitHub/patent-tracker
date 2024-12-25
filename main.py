import json
import os
from datetime import datetime

# File to store patent data
DATA_FILE = "patents.json"

# Load existing patents from the file
def load_patents():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save patents to the file
def save_patents(patents):
    with open(DATA_FILE, "w") as file:
        json.dump(patents, file, indent=4)

# Add a new patent
def add_patent(patents):
    title = input("Enter the patent title: ")
    application_number = input("Enter the application number: ")
    deadline = input("Enter the deadline (YYYY-MM-DD): ")
    try:
        # Validate the date format
        datetime.strptime(deadline, "%Y-%m-%d")
        patent = {
            "title": title,
            "application_number": application_number,
            "deadline": deadline
        }
        patents.append(patent)
        save_patents(patents)
        print("\nPatent added successfully!\n")
    except ValueError:
        print("\nInvalid date format. Please use YYYY-MM-DD.\n")

# View all patents
def view_patents(patents):
    if not patents:
        print("\nNo patents to display.\n")
        return
    print("\nPatents:")
    for idx, patent in enumerate(patents, start=1):
        print(f"{idx}. Title: {patent['title']}, Application Number: {patent['application_number']}, Deadline: {patent['deadline']}")
    print()

# Search for a patent by title or application number
def search_patent(patents):
    query = input("Enter the title or application number to search: ").lower()
    results = [p for p in patents if query in p["title"].lower() or query in p["application_number"].lower()]
    if results:
        print("\nSearch Results:")
        for patent in results:
            print(f"Title: {patent['title']}, Application Number: {patent['application_number']}, Deadline: {patent['deadline']}")
    else:
        print("\nNo matching patents found.\n")

# Check for upcoming deadlines
def check_deadlines(patents):
    if not patents:
        print("\nNo patents to check.\n")
        return
    print("\nUpcoming Deadlines:")
    today = datetime.today()
    upcoming = [p for p in patents if datetime.strptime(p["deadline"], "%Y-%m-%d") > today]
    if upcoming:
        for patent in upcoming:
            print(f"Title: {patent['title']}, Deadline: {patent['deadline']}")
    else:
        print("No upcoming deadlines.\n")

# Main menu
def main_menu():
    patents = load_patents()
    while True:
        print("\nPatent Tracker")
        print("1. Add Patent")
        print("2. View Patents")
        print("3. Search Patent")
        print("4. Check Deadlines")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_patent(patents)
        elif choice == "2":
            view_patents(patents)
        elif choice == "3":
            search_patent(patents)
        elif choice == "4":
            check_deadlines(patents)
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

# Entry point
if __name__ == "__main__":
    main_menu()

