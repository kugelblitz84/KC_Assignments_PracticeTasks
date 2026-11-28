from project.core.entities.entity_models import current_session
from project.core.repositories.question_services import add_knowledge
from project.features.common import readText, finishPage
from project.routes.routes import route


def addKnowledge():
    print("\nAdd Knowledge")
    values = []
    for prompt in ("Category", "Question", "Answer"):
        value = readText(prompt)
        if value is None:
            route.back()
            return
        values.append(value)
    confirmKnowledge(*values)
    finishPage()


def confirmKnowledge(category, question, answer):
    print(f"\nCategory: {category}\nQuestion: {question}\nAnswer: {answer}")
    if input("Save this knowledge? [y/N]: ").strip().lower() == "y":
        try:
            response = add_knowledge(current_session, category, question, answer)
        except (KeyError, OSError, ValueError, TypeError) as error:
            print(f"Service unavailable: {error}")
            return
        print(response.message)
    else:
        print("Cancelled. Nothing was saved.")
