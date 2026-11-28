from pathlib import Path
from datetime import datetime
import json
from project.core.services.text_tokenizer import tokenize_text
from project.core.entities.entity_models import Session, response_dto
from project.core.repositories.token_services import verify_token

def write_history(session: Session, action, querry=None):
        if not verify_token(session):
            return response_dto(False, "Invalid token. Please log in again.")
        file_path_history = Path(__file__).resolve().parents[2] / "history.json"
        if file_path_history.exists():
            with open(file_path_history, "r") as f:
                history_data = json.loads(f.read() or "{}")
                f.close()
                time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                tokenized_querry = sorted(tokenize_text(querry or ""))
                history_data[time_stamp] = {
                    "username": session.username,
                    "action": action,
                    "querry": tokenized_querry
                }
            with open(file_path_history, "w") as f:
                json.dump(history_data, f, indent=4)
                f.close()
                return response_dto(success=True, message="History written successfully.", data={})
        else: 
            with open(file_path_history, "w") as f:
                history_data = {}
                time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                history_data[time_stamp] = {
                    "username": session.username,
                    "action": action,
                    "querry": sorted(tokenize_text(querry or ""))
                }
                json.dump(history_data, f, indent=4)
                f.close()
                return response_dto(success=True, message="History storage file was created and history written successfully.", data={})
                
def read_history(session: Session):
    if not verify_token(session):
        return response_dto(False, "Invalid token. Please log in again.")
    file_path_history = Path(__file__).resolve().parents[2] / "history.json"
    if file_path_history.exists():
        with open(file_path_history, "r") as f:
            history_data = json.loads(f.read() or "{}")
            f.close()
            return response_dto(success=True, message="History read successfully.", data={"history": history_data})
    else:
        with open(file_path_history, "w") as f:
            history_data = {}
            json.dump(history_data, f, indent=4)
            f.close()
        return response_dto(success=True, message="History storage file does not exist and has been created", data={})
    
    
def get_statistics(session: Session):
    if not verify_token(session):
        return response_dto(False, "Invalid token. Please log in again.")
    file_path_history = Path(__file__).resolve().parents[2] / "history.json"
    if file_path_history.exists():
        with open(file_path_history, "r") as f:
            history_data = json.loads(f.read() or "{}")
            f.close()
            total_actions = len(history_data)
            total_searches = 0
            actions_per_user = {}
            frequency_of_querries = {}
            for entry in history_data.values():
                action = entry.get("action")
                if isinstance(action, str) and action.startswith((
                    "Retrieved best answer for question:",
                )):
                    total_searches += 1
                username = entry["username"]
                actions_per_user[username] = actions_per_user.get(username, 0) + 1
                queryTokens = entry.get("querry", [])
                for query in queryTokens:
                    frequency_of_querries[query] = frequency_of_querries.get(query, 0) + 1
            data = {
                "total_actions": total_actions,
                "total_searches": total_searches,
                "actions_per_user": actions_per_user,
                "frequency_of_querries": frequency_of_querries
            }    
            return response_dto(success=True, message="Statistics generated successfully.", data=data)
    else:
        return response_dto(success=False, message="History storage file does not exist.", data={})
