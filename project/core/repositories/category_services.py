from pathlib import Path
import json

from project.core.entities.entity_models import Session, response_dto
from project.core.repositories.token_services import verify_token
from project.core.repositories.history_services import write_history
def load_categories(session: Session):
    if verify_token(session):
        # userName = tokenResponse["username"]
        write_history(session, "Viewed FAQ categories")

        file_path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
        if file_path.exists():
            with open(file_path, "r") as f:
                data = json.load(f)
                keys = list(data.keys())
                return response_dto(success=True, message="Categories loaded successfully.", data={"categories": keys})
        else :
            return response_dto(success=False, message="knowledge_base.json not initialized.", data={})
        
            # return response_dto(success=True, message="Categories loaded successfully.", data={"categories": keys})
    else:
        return response_dto(success=False, message="Invalid token.", data={})
    

def add_category(session: Session):
    if verify_token(session):
        category_name = input("Enter the name of the new FAQ category: ")
        file_path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
        if file_path.exists():
            with open(file_path, "r") as f:
                data = json.load(f)
                if category_name in data:
                    return response_dto(success=False, message="Category already exists.", data={})
                else:
                    data[category_name] = []
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            write_history(session, f"Added FAQ category: {category_name}")
            return response_dto(success=True, message="Category added successfully.", data={})
        else:
            return response_dto(success=False, message="knowledge_base.json not initialized.", data={})
    else:
        return response_dto(success=False, message="Invalid token.", data={})
    
def update_category(session: Session):
    if verify_token(session):
        category_name = input("Enter the name of the FAQ category to update: ")
        file_path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
        if file_path.exists():
            with open(file_path, "r") as f:
                data = json.load(f)
                if category_name in data:
                    question_number = int(input("Enter the question number to update: "))
                    if 0 < question_number <= len(data[category_name]):
                        new_question = input("Enter the new question: ")
                        new_answer = input("Enter the new answer: ")
                        data[category_name][question_number - 1]["question"] = new_question
                        data[category_name][question_number - 1]["answer"] = new_answer
                        with open(file_path, "w") as f:
                            json.dump(data, f, indent=4)
                        write_history(session, f"Updated FAQ category: {category_name}, Question number: {question_number}")
                        return response_dto(success=True, message="Question updated successfully.", data={})
                    else:
                        return response_dto(success=False, message="Invalid question number.", data={})
                else:
                    return response_dto(success=False, message="Category not found.", data={})
        else:
            return response_dto(success=False, message="knowledge_base.json not initialized.", data={})
    else:
        return response_dto(success=False, message="Invalid token.", data={})
    
    
def delete_category(session: Session):
    if verify_token(session):
        category_name = input("Enter the name of the FAQ category to delete: ")
        file_path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
        if file_path.exists():
            with open(file_path, "r") as f:
                data = json.load(f)
                if category_name in data:
                    del data[category_name]
                    with open(file_path, "w") as f:
                        json.dump(data, f, indent=4)
                    write_history(session, f"Deleted FAQ category: {category_name}")
                    return response_dto(success=True, message="Category deleted successfully.", data={})
                else:
                    return response_dto(success=False, message="Category not found.", data={})
        else:
            return response_dto(success=False, message="knowledge_base.json not initialized.", data={})
    else:
        return response_dto(success=False, message="Invalid token.", data={})