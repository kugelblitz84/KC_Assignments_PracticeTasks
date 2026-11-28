from dataclasses import asdict
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path

import bcrypt
import jwt

from project.core.entities.entity_models import User, response_dto


DB_PATH = Path(__file__).resolve().parents[2] / "db.json"


def hash_pass(password):
    salt = bcrypt.gensalt(rounds=6)
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def load_users():
    if DB_PATH.exists():
        with DB_PATH.open(encoding="utf-8") as file:
            return response_dto(True, data={"users": json.load(file)})
    return response_dto(False, "db.json not initialized. Please create a user first.")


def set_password(name, password, mail=""):
    
    users_response = load_users()
    if not users_response.success:
        return users_response

    users = users_response.data["users"]
    if name in users:
        return response_dto(False, "User already exists.")

    user = User(username=name, password_hash=hash_pass(password).decode("utf-8"), email=mail)
    users[name] = asdict(user)
    with DB_PATH.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)
    return response_dto(True, "User created successfully.")


def verify_password(name, password):
    users_response = load_users()
    if not users_response.success:
        return users_response

    record = users_response.data["users"].get(name)
    if record is None:
        return response_dto(False, "User not found.")
    user = User(record["username"], record["password_hash"], record.get("email", ""))
    if not bcrypt.checkpw(password.encode("utf-8"), user.password_hash.encode("utf-8")):
        return response_dto(False, "Incorrect password.")

    secret = os.environ.get("JWT_SECRET")
    if not secret:
        return response_dto(False, "Set JWT_SECRET before logging in.")
    now = datetime.now(timezone.utc)
    payload = {"sub": user.username, "iat": now, "exp": now + timedelta(hours=2)}
    user.token = jwt.encode(payload, secret, algorithm="HS256")
    return response_dto(True, "Password verified successfully.", {"email": user.email, "token": user.token})


def init_db():
    if not DB_PATH.exists() or DB_PATH.stat().st_size == 0:
        with DB_PATH.open("w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)
