from project.routes.routes import route, Screen
from project.core.entities.entity_models import current_session


def homeScreen():
    print("\n================================")
    print("SMART KNOWLEDGE SYSTEM")
    print("================================")
    print("1. Add Knowledge")
    print("2. Search Knowledge")
    print("3. View All Knowledge")
    print("4. Update Knowledge")
    print("5. Delete Knowledge")
    print("6. View Search History")
    print("7. View Statistics")
    print("8. Exit")
    print("9. Log out")
    options = {
        "1": Screen.ADD_KNOWLEDGE,
        "2": Screen.SEARCH,
        "3": Screen.VIEW_ALL,
        "4": Screen.UPDATE,
        "5": Screen.DELETE,
        "6": Screen.HISTORY,
        "7": Screen.STATISTICS,
    }
    choice = input("Enter your choice: ").strip()
    if choice == "8":
        route.exit()
        print("Goodbye!")
    elif choice == "9":
        current_session.clear()
        route.exit()
        route.push(Screen.AUTH)
    elif choice in options:
        route.push(options[choice])
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
