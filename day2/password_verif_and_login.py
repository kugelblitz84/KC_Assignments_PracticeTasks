import sys
import bcrypt
from pathlib import Path
import json
from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class User:
    username: str
    password_hash: str

@dataclass
class response_dto:
    success: bool
    message: str = ""
    data: dict[str, Any] = field(default_factory=dict)
     
    
def hash_pass(password):
    salt = bcrypt.gensalt(rounds = 6)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def load_users():
    file_path = Path(__file__).parent / "db.json"
    if file_path.exists():
        with file_path.open("r") as f:
            data = json.load(f)
            users = [User(**user) for user in data]
            return response_dto(success=True, data={"users": users})
    return response_dto(success=False, message="db.json not initialized. Please create a user first.", data={})

def set_password(name, password):
    users_response = load_users()
    if users_response.success:
        users = users_response.data["users"]
        for user in users:
            if user.username == name:
                return response_dto(success=False, message="User already exists.", data={})
        has = hash_pass(password)
        file_path = Path(__file__).parent / "db.json"
        users.append(User(username=name, password_hash=has.decode('utf-8')))
        with file_path.open("w") as f:
            json.dump([asdict(user) for user in users], f, indent=4)
        return response_dto(success=True, message="User created successfully.", data={})
    return response_dto(success=False, message=users_response.message, data={})


def verify_password(name, password):
    users_response = load_users()
    if users_response.success:
        users = users_response.data["users"]
        for user in users:
            if user.username == name:
                if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
                    return response_dto(success=True, message="Password verified successfully.", data={})
                else:
                    return response_dto(success=False, message="Incorrect password.", data={})
        return response_dto(success=False, message="User not found.", data={})
    return users_response
    
    
def init_db():
    file_path = Path(__file__).parent / "db.json"
    if not file_path.exists():
        with file_path.open("w") as f:
            json.dump([], f, indent=4)
    
print("Welcome to the password verification system.\n Choose an option:\n 1. Create a new user\n 2. Login\n 3. Exit")
try:
    init_db()
    ch = input("Enter your choice (1/2/3): ")
    if ch == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        response = set_password(username, password)
        print(response.message)
        
    if ch == "2":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        response = verify_password(username, password)
        print(response.message)


    if ch == "3":
        print("Exiting the system.")
        sys.exit(1)

except ValueError as er:
    print(f"Error: {er}")
    sys.exit(1)
