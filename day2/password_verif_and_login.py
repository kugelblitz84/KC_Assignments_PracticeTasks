import sys
import bcrypt
from pathlib import Path
import json
from dataclasses import dataclass, field, asdict
from typing import Any
import jwt
from datetime import datetime, timedelta, timezone
import os

jwt_secret = os.environ["JWT_SECRET"]

@dataclass
class User:
    username: str
    password_hash: str
    email: str = ""
    token: str = ""
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
            return response_dto(success=True, data={"users": data})
    return response_dto(success=False, message="db.json not initialized. Please create a user first.", data={})

def set_password(name, password, mail = ""):
    users_response = load_users()
    if users_response.success:
        users = users_response.data["users"]
        if name in users :
            return response_dto(success=False, message="User already exists.", data={})
        has = hash_pass(password)
        file_path = Path(__file__).parent / "db.json"
        users[name] = asdict(User(username=name, password_hash=has.decode('utf-8'), email=mail))
        users[name]["studentProfile"] = {}
        with file_path.open("w") as f:
            json.dump(users, f, indent=4)
        return response_dto(success=True, message="User created successfully.", data={})
    return response_dto(success=False, message=users_response.message, data={})


def verify_password(name, password):
    users_response = load_users()
    if users_response.success:
        users = users_response.data["users"]
        if name in users:
            user = users[name]
            if bcrypt.checkpw(password.encode('utf-8'), user["password_hash"].encode('utf-8')):
                jwt_payload = {
                    "subb": user["username"],
                    "iat": datetime.now(tz=timezone.utc),
                    "exp": datetime.now(timezone.utc) + timedelta(hours=2)
                }
                user["token"] = jwt.encode(jwt_payload, jwt_secret, algorithm="HS256")
                return response_dto(success=True, message="Password verified successfully.", data={"email": user["email"], "token": user["token"]})
            else:
                return response_dto(success=False, message="Incorrect password.", data={})
        return response_dto(success=False, message="User not found.", data={})
    return users_response
    
    
def init_db():
    file_path = Path(__file__).parent / "db.json"
    if not file_path.exists():
        with file_path.open("w") as f:
            json.dump({}, f, indent=4)

def main():  
    print("Welcome to the password verification system.\n Choose an option:\n 1. Create a new user\n 2. Login\n 3. Exit")
    try:
        init_db()
        ch = input("Enter your choice (1/2/3): ")
        if ch == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            email = input("Enter an email (optional): ")
            response = set_password(username, password, email)
            print(response.message)
            
        if ch == "2":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            response = verify_password(username, password)
            print(response.message)
            if response.success:
                print(f"User's email: {response.data['email']}")

        if ch == "3":
            print("Exiting the system.")
            sys.exit(1)

    except ValueError as er:
        print(f"Error: {er}")
        sys.exit(0)

if __name__ == "__main__":
    main()
