from project.core.entities.entity_models import current_session
from project.core.repositories.question_services import retrieve_best_answer
from project.features.common import readText, finishPage
from project.routes.routes import route


def askQuestion():
    print("\nSearch Knowledge")
    query = readText("Enter your question")
    if query is None:
        route.back()
        return
    showSearchResults(query)
    finishPage()


def showSearchResults(query):
    try:
        response = retrieve_best_answer(current_session, query)
    except (KeyError, OSError, ValueError, TypeError) as error:
        print(f"Service unavailable: {error}")
        return
    if not response.success:
        print(response.message)
        return
    answer = response.data["answer"]
    if answer:
        print(f"Answer: {answer}")
    else:
        print("No matching answers found. Try rephrasing your question.")
