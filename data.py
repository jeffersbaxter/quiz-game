import requests
import random
from question_model import Question

raw_data = [{"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
             "question": "The vapor produced by e-cigarettes is actually water.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "A defibrillator is used to start up a heartbeat once a heart has stopped beating.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Geography", "type": "boolean", "difficulty": "medium",
             "question": "The Southeast Asian island of Borneo is politically divided among 3 countries.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Geography", "type": "boolean", "difficulty": "medium",
             "question": "Vietnam is the only country in the world that starts with V. ",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "Time on Computers is measured via the EPOX System.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Video Games", "type": "boolean",
             "difficulty": "medium",
             "question": "David Baszucki was a co-founder of ROBLOX Corporation.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "medium",
             "question": "Pink Guy&#039;s debut album was &quot;Pink Season&quot;.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Television", "type": "boolean",
             "difficulty": "medium",
             "question": "Like his character in 'Parks and Recreation', Aziz Ansari was born in South Carolina.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Scotland voted to become an independent country during the referendum from September 2014.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "easy",
             "question": "BMW M GmbH is a subsidiary of BMW AG that focuses on car performance.",
             "correct_answer": "True", "incorrect_answers": ["False"]}]


def get_question_data():
    questions = []
    res = requests.get(format_req_url())
    if res.status_code == 200:
        for data in res.json()["results"]:
            options = [data["correct_answer"]] + data["incorrect_answers"]
            random.shuffle(options)
            options_fmt = f"({'/'.join(options)})"
            question = Question(data["question"], data["correct_answer"], data["type"], options_fmt)
            questions.append(question)
    else:
        for data in raw_data:
            options = [data["correct_answer"]] + data["incorrect_answers"]
            random.shuffle(options)
            options_fmt = f"({'/'.join(options)})"
            questions.append(Question(data["question"], data["correct_answer"], data["type"], options_fmt))

    return questions


def format_req_url():
    amount = f"amount={input('How many questions?: ') or '10'}&"

    user_difficulty = input('How hard?: (easy/medium/hard)')
    difficulty = ""
    if not user_difficulty == "":
        difficulty = f"difficulty={user_difficulty}&"

    user_type = input('What type of answers should there be?: (boolean/multiple)')
    answer_type = ""
    if not user_type == "":
        answer_type = f"type={user_type}"

    return f'https://opentdb.com/api.php?{amount}{difficulty}{answer_type}'

