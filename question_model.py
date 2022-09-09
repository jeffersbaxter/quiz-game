class Question:
    def __init__(self, text, answer, q_type, q_options):
        self.text = text
        self.answer = answer
        self.type = q_type or "boolean"
        self.options = q_options
