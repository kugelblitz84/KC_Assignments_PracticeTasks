from project.core.entities.entity_models import current_session
from project.core.repositories.question_services import delete_question, load_knowledge
from project.features.common import selectQuestion, finishPage


def deleteQuestion():
    print("\nDelete Knowledge")
    response = load_knowledge(current_session)
    if response.success:
        selected = selectQuestion(response.data["knowledge"])
        if selected is not None:
            confirmDelete(*selected)
    else:
        print(response.message)
    finishPage()


def confirmDelete(category, position, item):
    print(f"\nID: {item['id']}\nQuestion: {item['question']}\nAnswer: {item['answer']}")
    if input("Delete this knowledge item? [y/N]: ").strip().lower() == "y":
        try:
            response = delete_question(current_session, category, position)
        except (KeyError, OSError, ValueError, TypeError) as error:
            print(f"Service unavailable: {error}")
            return
        print(response.message)
    else:
        print("Cancelled. Nothing was deleted.")
