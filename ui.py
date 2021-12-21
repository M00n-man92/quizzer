THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class Extriemist:
    def __init__(self,quiz:QuizBrain) :
        self.quizzer=quiz
        self.flightmanypeople=""
        self.window=Tk()
        self.window.title("Quize")
        self.window.config(padx=100,pady=200)
        self.label=Label(text=f"Score: ",font=("ariel",12,"bold"),padx=10,pady=20)
        self.label.grid(column=1,row=0)
        self.canvas_one=Canvas(width=300,height=250,bg="#375362")
        self.fuilledinfuiel=self.canvas_one.create_text(160,100,width=300,text="an amazing bit thier priefernces are the beaset in the world",fill="white",font=("ariel",18,"bold"))
        self.canvas_one.grid(column=0,row=1,columnspan=2)

        image_one=PhotoImage(file="./quiz/images/false.png")
        image_two=PhotoImage(file="./quiz/images/true.png")

        self.button_one=Button(width=100,height=90,image=image_two,command=self.maybetheyknew)
        self.button_one.grid(column=0,row=2)
        self.button_two=Button(width=100,height=90,image=image_one,command=self.thatstheonewhichgotshot)
        self.button_two.grid(column=1,row=2)
        self.kindov()
        self.window.mainloop()
    def kindov(self):
 
        self.canvas_one.itemconfig(self.fuilledinfuiel,text=f"{self.quizzer.next_question()}")
        # self.quizzer.check_answer(self.button_one,self.button_two)

    def maybetheyknew(self):
        # couldntly=True
        self.quizzer.check_answer("True")
        self.label.config(text=f"Score: {self.quizzer.score}")
        self.kindov()
    def thatstheonewhichgotshot(self):
        self.quizzer.check_answer("false")
        self.label.config(text=f"Score: {self.quizzer.score}")
        self.kindov()