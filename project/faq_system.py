from day2.password_verif_and_login import load_users, response_dto, User, init_db, verify_password, set_password
from day3.update_student_profile import session
from dataclasses import asdict, field, dataclass
from pathlib import Path 
import json


def verify_token(username, token):
    # Placeholder for token verification logic
    return True

def load_categories(username, token):
    if verify_token(username, token):
        file_path = Path(__file__).parent / "knowledge_base.json"
        with open(file_path, "r") as f:
            data = json.load(f)
            keys = list(data.keys())
            return response_dto(success=True, message="Categories loaded successfully.", data={"categories": keys})
    else:
        return response_dto(success=False, message="Invalid token.", data={})

async def Faqsystem(username, token):
    while True:
        print("Welcome to the FAQ system.")
        print("1. View FAQ categories\n2. Add FAQ category\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            categories = load_categories(username, token)
            if not categories.success:
                print(categories.message)
                continue
            print("FAQ Categories:", categories.data)
        elif choice == "2":
            pass
            
                
        
    
    
    
    
async def main():
    
    while True:
        print("Welcome to the FAQ system.")
        print("Users must log in to access the system.")
        print("1. Login\n2. Create new user\n3.Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            response = verify_password(username, password)
            if response.success:
                print("Login successful.")
                if not await Faqsystem(response.data["username"], response.data["token"]):
                    break
                # Proceed to FAQ system functionality
            else:
                print(response.message)
        
        



