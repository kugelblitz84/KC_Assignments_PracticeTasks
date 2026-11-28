from project.routes.routes import route


def readText(prompt, allow_empty=False):
    while True:
        value = input(prompt + " (/back to cancel): ").strip()
        if value.lower() == "/back":
            return None
        if value or allow_empty:
            return value
        print("Please enter a value.")


def finishPage():
    input("Press Enter to go back: ")
    route.back()


def selectQuestion(knowledge):
    questions = {}
    for category, items in knowledge.items():
        for position, item in enumerate(items, start=1):
            questions[str(item["id"])] = (category, position, item)
            print(f"{item['id']}. [{category}] {item['question']}")
    if not questions:
        print("No knowledge items yet.")
        return None
    while True:
        choice = input("Enter knowledge ID (0 to go back): ").strip()
        if choice == "0":
            return None
        if choice in questions:
            return questions[choice]
        print("Invalid ID. Choose one of the displayed IDs.")
