from project.core.entities.entity_models import current_session
from project.core.repositories.history_services import read_history
from project.features.common import finishPage


def viewHistory():
    print("\nSearch History")
    try:
        response = read_history(current_session)
    except (KeyError, OSError, ValueError, TypeError) as error:
        print(f"Service unavailable: {error}")
    else:
        if response.success:
            showHistory(response.data.get("history", {}))
        else:
            print(response.message)
    finishPage()


def showHistory(history):
    if not history:
        print("No history yet.")
        return
    print("Existing history records actions; result counts are not recorded.")
    for timestamp, entry in sorted(history.items(), reverse=True):
        print(f"\n{timestamp} | {entry.get('username', '')}")
        print(entry.get("action", ""))
        if entry.get("querry"):
            print("Keywords: " + ", ".join(entry["querry"]))
