from project.core.entities.entity_models import current_session
from project.core.repositories.question_services import load_knowledge
from project.features.common import selectQuestion, finishPage


def viewQuestions():
    print("\nView All Knowledge")
    response = load_knowledge(current_session)
    if response.success:
        knowledge = response.data["knowledge"]
        while True:
            selected = selectQuestion(knowledge)
            if selected is None:
                break
            showQuestion(selected[0], selected[2])
    else:
        print(response.message)
    finishPage()


def showQuestion(category, question):
    print(f"\nID: {question['id']}\nCategory: {category}")
    print(f"Question: {question['question']}")
    print(f"Answer: {question['answer']}")
    input("Press Enter to return to the list: ")
