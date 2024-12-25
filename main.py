print("Welcome to the Patent Tracker!")
# Patent Tracker Tool

# Sample data structure to store patents
patents = []

def add_patent():
    """Add a new patent."""
    title = input("Enter the patent title: ")
    application_number = input("Enter the application number: ")
    deadline = input("Enter the deadline (YYYY-MM-DD): ")
    patent = {
        "title": title,
        "application_number": application_number,
        "deadline": deadline
    }
    patents.append(patent)
    print("\nPatent added successfully!\n")

def view_patents():
    """View all patents."""
    if not patents:
        print("\nNo patents to display.\n")
        return
    print("\nPatents:")
    for idx, patent in enumerate(patents, start=1):
        print(f"{idx}. Title: {patent['title']}, Application Number: {patent['application_number']}, Deadline: {patent['deadline']}")
    print()

def main_menu():
    """Display the main menu."""
    while True:
        print("Patent Tracker")
        print("1. Add Patent")
        print("2. View Patents")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_patent()
        elif choice == "2":
            view_patents()
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

# Entry point
if __name__ == "__main__":
    main_menu()
