from getpass import getpass

from project.core.entities.entity_models import current_session
from project.core.repositories.auth_services import set_password, verify_password
from project.features.common import readText
from project.routes.routes import route, Screen


def authScreen():
    print("\nSMART KNOWLEDGE SYSTEM")
    print("1. Log in")
    print("2. Sign up")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        route.push(Screen.LOGIN)
    elif choice == "2":
        route.push(Screen.SIGNUP)
    elif choice == "3":
        route.exit()
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")


def loginScreen():
    print("\nLog in")
    credentials = readCredentials()
    if credentials is not None:
        username, password = credentials
        try:
            response = verify_password(username, password)
        except (KeyError, OSError, ValueError, TypeError) as error:
            print(f"Service unavailable: {error}")
        else:
            if response.success:
                current_session.username = username
                current_session.token = response.data["token"]
                route.exit()
                route.push(Screen.MAIN)
                return
            print(response.message)
    route.back()


def signupScreen():
    print("\nSign up")
    credentials = readCredentials()
    if credentials is not None:
        email = readText("Email (optional)", allow_empty=True)
        if email is not None:
            username, password = credentials
            try:
                response = set_password(username, password, email)
            except (KeyError, OSError, ValueError, TypeError) as error:
                print(f"Service unavailable: {error}")
            else:
                if response.success:
                    print("Account created. Log in to continue.")
                else:
                    print(response.message)
    route.back()


def readCredentials():
    username = readText("Username")
    if username is None:
        return None
    while True:
        password = getpass("Password (Enter to cancel): ")
        if not password:
            return None
        if len(password.encode("utf-8")) <= 72:
            return username, password
        print("Password must be at most 72 bytes.")
