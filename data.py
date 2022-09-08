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
    for data in raw_data:
        questions.append(Question(data["question"], data["correct_answer"]))
    return questions
