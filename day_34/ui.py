from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizGameUi:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # window
        self.window = Tk()
        self.window.title("Quiz Brain")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.minsize(height=500, width=300)
        # scoreboard
        self.score = 0
        self.scoreboard = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.scoreboard.grid(row=0, column=1, pady=20, padx=20)
        # canvas
        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 120, text="questions", fill="black", font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # true button
        true_image = PhotoImage(file="./images/true.png")
        self.true = Button(image=true_image, command=self.true_pressed, bg=THEME_COLOR, highlightthickness=0)
        self.true.grid(row=2, column=0, pady=20, padx=20)
        # False button
        false_image = PhotoImage(file="./images/false.png")
        self.false = Button(image=false_image, command=self.false_pressed, bg=THEME_COLOR, highlightthickness=0)
        self.false.grid(row=2, column=1, pady=20, padx=20)
        # next question
        self.get_next_question()

        # exit loop
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score += 1
            self.scoreboard.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
