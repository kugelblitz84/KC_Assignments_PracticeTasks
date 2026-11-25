from asyncio import sleep
import sys

from day2.password_verif_and_login import load_users, response_dto, User, init_db, verify_password, set_password
from dataclasses import asdict, field, dataclass
from pathlib import Path 
import json
import os
@dataclass
class studentProfile:
    name: str | None = None
    age: str | None = None
    class_: str | None = None
    roll: str | None = None
    
@dataclass
class UserEntity:
    userEmail: str
    userName: str
    studentProfile: studentProfile = field(default_factory=studentProfile)
    
@dataclass
class session:
    isLoggedIn: bool = False
    user: UserEntity | None = None


# def updateProfile(previousProfile: studentProfile, newProfile: studentProfile):
#     return studentProfile(
#         name= (newProfile.name if newProfile.name not "" else previousProfile.name)
#     )
    

def set_student_profile(username, newstudentProfile: studentProfile):
    users_response = load_users()
    if users_response.success:
        users = users_response.data["users"]
        profile = users[username]["studentProfile"]
        changes = {
            key: value for key, value in asdict(newstudentProfile).items() if value is not None
        }
        profile.update(changes)
        # users[username]["studentProfile"] = asdict(updatedProfile)
        file_path = Path(__file__).parent.parent / "day2/db.json"
        if file_path.exists():
            with file_path.open("w") as f:
                json.dump(users, f, indent = 4)
            return response_dto(success=True, message="Student profile updated successfully.", data={})
        return response_dto(success=False, message="db.json not found.", data={})
    
    return response_dto(success=False, message=users_response.message, data={})
            
        
            

init_db() 

async def main():
    
    currentSession = session()
    while True:
        # os.system("cls" if os.name == "nt" else "clear")
        if not currentSession.isLoggedIn:
            print("Select an option:")
            print("1. Create account\n2. login\n3. Exit")
            choice = input("Enter your choice 1/2/3:")
            if choice == "1":
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                email = input("Enter an email (optional): ")
                response = set_password(username, password, email)
                if response.success:
                    print("Account created successfully, please login to set your student profile.")
                    await sleep(2)
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                print(response.message)
            elif choice == "2":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                response = verify_password(username, password)
                if response.success:
                    print("Login successful.", response.message)
                    await sleep(2)
                    os.system("cls" if os.name == "nt" else "clear")
                    currentSession.isLoggedIn = True
                    userData = load_users().data["users"][username]
                    currentSession.user = UserEntity(userEmail=userData["email"], userName=username, studentProfile=studentProfile(userData["studentProfile"]))
                    continue
                print(response.message)
            elif choice == "3":
                sys.exit(1)
        else:
            os.system("cls" if os.name == "nt" else "clear")
            user = currentSession.user
            print("User logged in. Select an option:")
            print("1. Update student profile\n2. View student profile\n3. Logout")
            choice = input("Enter your choice 1/2/3:")
            if choice == "1":
                choice = input("Enter what you want to update 1. Name\n2. Age\n3. Class\n4. Roll\n5. Back")
                if choice == "5":
                    continue
                elif choice == "1":
                    newName = input("Enter new name: ")
                    # newProfile = studentProfile(name=newName)
                    if user is None:
                        print("Error: No user is currently logged in.")
                        continue
                    response = set_student_profile(user.userName, studentProfile(name=newName))
                    print(response.message)
                elif choice == "2":
                    newAge = input("Enter new age: ")
                    if user is None:
                        print("Error: No user is currently logged in.")
                        continue
                    response = set_student_profile(user.userName, studentProfile(age=newAge))
                    print(response.message)
                elif choice == "3":
                    newClass = input("Enter new class: ")
                    if user is None:
                        print("Error: No user is currently logged in.")
                        continue
                    response = set_student_profile(user.userName, studentProfile(class_=newClass))
                    print(response.message)
                elif choice == "4":
                    newRoll = input("Enter new roll: ")
                    if user is None:
                        print("Error: No user is currently logged in.")
                        continue
                    response = set_student_profile(user.userName, studentProfile(roll=newRoll))
                    print(response.message)
                else:
                    print("Invalid choice.")
            elif choice == "2":
                if user is None:
                    print("Error: No user is currently logged in.")
                    continue
                print(f"Student Profile:\n {user}")
                choice = input("1. Exit\n2. Logout \n3. Back")
                if choice == "1":
                    sys.exit(1)
                elif choice == "2":
                    currentSession.isLoggedIn = False
                    currentSession.user = None
                    print("Logged out successfully.")
                    await sleep(2)
                elif choice == "3":
                    continue
            elif choice == "3":
                currentSession.isLoggedIn = False
                currentSession.user = None
                print("Logged out successfully.")
            else:
                print("Invalid choice.")
                continue
                

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
