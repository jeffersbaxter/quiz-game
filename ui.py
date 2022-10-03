from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 21, "italic")


class QuizInterface:

    def __init__(self, quiz_brain):
        self.window = Tk()
        self.window.title("Quiz Show")
        self.window.config(padx=20, pady=20, height=500, bg=THEME_COLOR)

        self.quiz_brain = quiz_brain

        self.score_label = Label(text=f"Score: {self.quiz_brain.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Here is the question...",
            fill=THEME_COLOR,
            font=FONT,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.answer_as_true)
        self.true_btn.grid(row=2, column=0)
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.answer_as_false)
        self.false_btn.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.change_canvas_bg("white")
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfigure(self.question_text, text=self.quiz_brain.format_question())
        else:
            self.true_btn["state"] = "disabled"
            self.false_btn["state"] = "disabled"
            self.canvas.itemconfigure(self.question_text, text=f"Your final score is {self.quiz_brain.score}/10!")

    def answer_as_true(self):
        is_right = self.quiz_brain.answer_matches("True")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        self.give_feedback(is_right)

    def answer_as_false(self):
        is_right = self.quiz_brain.answer_matches("False")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.change_canvas_bg("green")
        else:
            self.change_canvas_bg("red")
        self.window.after(1000, func=self.next_question)

    def change_canvas_bg(self, color):
        self.canvas.config(bg=color)


