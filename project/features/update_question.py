from project.core.entities.entity_models import current_session
from project.core.repositories.question_services import load_knowledge, update_question
from project.features.common import selectQuestion, readText, finishPage


def updateQuestion():
    print("\nUpdate Knowledge")
    response = load_knowledge(current_session)
    if response.success:
        selected = selectQuestion(response.data["knowledge"])
        if selected is not None:
            editQuestion(*selected)
    else:
        print(response.message)
    finishPage()


def editQuestion(category, position, item):
    print(f"Question: {item['question']}\nAnswer: {item['answer']}")
    question = readText("New question (Enter to keep current)", allow_empty=True)
    if question is None:
        return
    answer = readText("New answer (Enter to keep current)", allow_empty=True)
    if answer is None:
        return
    question = question or item["question"]
    answer = answer or item["answer"]
    print(f"\nQuestion: {question}\nAnswer: {answer}")
    if input("Save changes? [y/N]: ").strip().lower() == "y":
        try:
            response = update_question(current_session, category, position, question, answer)
        except (KeyError, OSError, ValueError, TypeError) as error:
            print(f"Service unavailable: {error}")
            return
        print(response.message)
    else:
        print("Cancelled. Nothing was saved.")
