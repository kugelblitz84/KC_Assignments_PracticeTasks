from pathlib import Path
import json
from tempfile import NamedTemporaryFile
from project.core.entities.entity_models import Session, response_dto
from project.core.repositories.token_services import verify_token
from project.core.services.match_scorer import calculate_match_score
from project.core.repositories.history_services import write_history
# from project.core.services.text_tokenizer import tokenize_text
# def fetch_questions(category_name):
#     file_path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
#     if file_path.exists():
#         with open(file_path, "r") as f:
#             data = json.load(f)
#             if category_name in data:
#                 questions = list(f"{i + 1}. {data[category_name][i]['question']}" for i in range(len(data[category_name])))
#                 return response_dto(success=True, message="Questions fetched successfully.", data={"questions": questions})
#             else:
#                 return response_dto(success=False, message="Category not found.", data={})
#     else:
#         return response_dto(success=False, message="knowledge_base.json not initialized.", data={})
    
    
def load_knowledge(session: Session):
    if not verify_token(session):
        return response_dto(False, "Invalid token. Please log in again.")
    path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
    knowledge = {}
    try:
        if path.exists():
            with path.open(encoding="utf-8") as file:
                knowledge = json.loads(file.read().strip() or "{}")
    except (OSError, ValueError) as error:
        return response_dto(False, f"Service unavailable: {error}")
    return response_dto(True, data={"knowledge": knowledge})


def add_knowledge(session: Session, category, question, answer):
    response = load_knowledge(session)
    if not response.success:
        return response
    category, question, answer = category.strip(), question.strip(), answer.strip()
    if not all((category, question, answer)):
        return response_dto(False, "Category, question and answer are required.")

    knowledge = response.data["knowledge"]
    next_id = max((item["id"] for items in knowledge.values() for item in items), default=0) + 1
    # Older empty categories were stored as {}.
    if knowledge.get(category) == {}:
        knowledge[category] = []
    item = {"id": next_id, "question": question, "answer": answer}
    knowledge.setdefault(category, []).append(item)

    path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
    temp = NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False)
    temp_path = Path(temp.name)
    try:
        with temp:
            json.dump(knowledge, temp, indent=4)
        temp_path.replace(path)
    finally:
        temp_path.unlink(missing_ok=True)
    return response_dto(True, "Knowledge added successfully.", {"id": next_id})


def update_question(session: Session, category_name, question_number, new_question, new_answer):
    if not verify_token(session):
        return response_dto(False, "Invalid token. Please log in again.")
    file_path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
    if file_path.exists():
        with open(file_path, "r") as f:
            data = json.load(f)
            if category_name in data:
                if 0 < question_number <= len(data[category_name]):
                    data[category_name][question_number - 1]["question"] = new_question
                    data[category_name][question_number - 1]["answer"] = new_answer
                    with open(file_path, "w") as f_write:
                        json.dump(data, f_write, indent=4)
                    return response_dto(success=True, message="Question updated successfully.", data={})
                else:
                    return response_dto(success=False, message="Invalid question number.", data={})
            else:
                return response_dto(success=False, message="Category not found.", data={})
    else:
        return response_dto(success=False, message="knowledge_base.json not initialized.", data={})
    
def delete_question(session: Session, category_name, question_number):
    if not verify_token(session):
        return response_dto(False, "Invalid token. Please log in again.")
    file_path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
    if file_path.exists():
        with open(file_path, "r") as f:
            data = json.load(f)
            if category_name in data:
                if 0 < question_number <= len(data[category_name]):
                    del data[category_name][question_number - 1]
                    with open(file_path, "w") as f_write:
                        json.dump(data, f_write, indent=4)
                    return response_dto(success=True, message="Question deleted successfully.", data={})
                else:
                    return response_dto(success=False, message="Invalid question number.", data={})
            else:
                return response_dto(success=False, message="Category not found.", data={})
    else:
        return response_dto(success=False, message="knowledge_base.json not initialized.", data={})
    
    
    
def retrieve_best_answer(session: Session, users_question):
    if not verify_token(session):
        return response_dto(False, "Invalid token. Please log in again.")
    file_path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
    if file_path.exists():
        with open(file_path, "r") as f:
            data = json.load(f)
            best_answer = ""
            current_score = 0.0
            for category in data:
                for question_set in data[category]:
                    question = question_set["question"]
                    answer = question_set["answer"]
                    question_score = calculate_match_score(users_question, question)
                    answer_score = calculate_match_score(users_question, answer)
                    score = (question_score * 0.7) + (answer_score * 0.3)
                    if score > current_score:
                        current_score = score
                        best_answer = answer
            f.close()
            write_history(session, f"Retrieved best answer for question: {users_question}", users_question)
            return response_dto(success=True, message="Best answer retrieved successfully.", data={"answer": best_answer})
    else:
        return response_dto(success=False, message="knowledge_base.json not initialized.", data={})
# def submit_answer(category_name, question_number, ):
#     file_path = Path(__file__).resolve().parents[2] / "knowldge_base.json"
#     if file_path.exists():
#         with open(file_path, "r") as f:
#             data = json.load(f)
#             if category_name in data:
#                 if 0 < question_number <= len(data[category_name]):
#                     answer = data[category_name][question_number - 1]["answer"]
#                     return response_dto(success=True, message="Answer fetched successfully.", data={"answer": answer})
#                 else:
#                     return response_dto(success=False, message="Invalid question number.", data={})
#             else:
#                 return response_dto(success=False, message="Category not found.", data={})
#     else:
#         return response_dto(success=False, message="knowledge_base.json not initialized.", data={})
