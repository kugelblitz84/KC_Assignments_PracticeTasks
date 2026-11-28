from project.core.entities.entity_models import current_session
from project.core.repositories.history_services import get_statistics
from project.core.repositories.question_services import load_knowledge
from project.features.common import finishPage


def viewStatistics():
    print("\nSearch Statistics")
    response = load_knowledge(current_session)
    if response.success:
        knowledge = response.data["knowledge"]
        print("Total knowledge items:", sum(len(items) for items in knowledge.values()))
    else:
        print(response.message)
    try:
        response = get_statistics(current_session)
    except (KeyError, OSError, ValueError, TypeError) as error:
        print(f"Service unavailable: {error}")
    else:
        if response.success:
            showStatistics(response.data)
        else:
            print(response.message)
    print("Searches with no results: unavailable (result counts are not stored).")
    finishPage()


def showStatistics(data):
    print("Total recorded actions:", data.get("total_actions", 0))
    print("Total searches:", data.get("total_searches", 0))
    print("Actions per user:")
    actions_per_user = data["actions_per_user"]
    if not actions_per_user:
        print("No user actions recorded yet.")
    for username, count in sorted(actions_per_user.items()):
        print(f"  {username}: {count}")
    print("Frequently searched keywords:")
    frequencies = data.get("frequency_of_querries", {})
    if not frequencies:
        print("No keywords recorded yet.")
    for keyword, count in sorted(frequencies.items(), key=lambda entry: (-entry[1], entry[0])):
        print(f"  {keyword}: {count}")
