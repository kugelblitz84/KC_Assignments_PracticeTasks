from project.routes.routes import route, Screen
from project.features.home import homeScreen
from project.features.auth_screens import authScreen, loginScreen, signupScreen
from project.core.entities.entity_models import current_session
from project.core.repositories.token_services import verify_token
from project.features.add_knowledge import addKnowledge
from project.features.search import askQuestion
from project.features.view_questions import viewQuestions
from project.features.update_question import updateQuestion
from project.features.delete_question import deleteQuestion
from project.features.history import viewHistory
from project.features.statistics import viewStatistics
from project.core.repositories.auth_services import init_db


auth_screens = {Screen.AUTH, Screen.LOGIN, Screen.SIGNUP}

screens = {
    Screen.AUTH: authScreen,
    Screen.LOGIN: loginScreen,
    Screen.SIGNUP: signupScreen,
    Screen.MAIN: homeScreen,
    Screen.ADD_KNOWLEDGE: addKnowledge,
    Screen.SEARCH: askQuestion,
    Screen.VIEW_ALL: viewQuestions,
    Screen.UPDATE: updateQuestion,
    Screen.DELETE: deleteQuestion,
    Screen.HISTORY: viewHistory,
    Screen.STATISTICS: viewStatistics,
}


def main():
    init_db()
    route.exit()
    current_session.clear()
    route.push(Screen.AUTH)
    try:
        while route.stack:
            screen = route.stack[-1]
            if screen not in auth_screens and not verify_token(current_session):
                print("Session expired. Please log in again.")
                current_session.clear()
                route.exit()
                route.push(Screen.AUTH)
                continue
            screens[screen]()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
    finally:
        current_session.clear()
        route.exit()


if __name__ == "__main__":
    main()
