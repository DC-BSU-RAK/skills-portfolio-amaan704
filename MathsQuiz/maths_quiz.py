import tkinter as tk
from tkinter import messagebox
import random

score = 0
question_count = 0
attempt = 1

num1 = 0
num2 = 0
correct_answer = 0
operation = ""

difficulty = ""

def start_quiz(level):
    global difficulty, score, question_count

    difficulty = level
    score = 0
    question_count = 0

    menu_frame.pack_forget()
    quiz_frame.pack()

    generate_question()

def randomInt():
    if difficulty == "Easy":
        return random.randint(1, 9)

    elif difficulty == "Moderate":
        return random.randint(10, 99)

    elif difficulty == "Advanced":
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(["+", "-"])

def generate_question():
    global num1, num2, correct_answer, operation, attempt

    attempt = 1

    num1 = randomInt()
    num2 = randomInt()

    operation = decideOperation()

    if operation == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    question_label.config(text=f"{num1} {operation} {num2} = ?")

    answer_entry.delete(0, tk.END)

def check_answer():
    global score, question_count, attempt

    try:
        user_answer = int(answer_entry.get())

        if user_answer == correct_answer:

            if attempt == 1:
                score += 10
            else:
                score += 5

            messagebox.showinfo("Correct", "Correct Answer!")

            question_count += 1

            if question_count == 10:
                displayResults()
            else:
                generate_question()

        else:
            if attempt == 1:
                attempt = 2
                messagebox.showwarning("Wrong", "Wrong answer! Try once more.")
            else:
                messagebox.showerror("Wrong", f"Correct answer was {correct_answer}")

                question_count += 1

                if question_count == 10:
                    displayResults()
                else:
                    generate_question()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def displayResults():

    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "D"

    replay = messagebox.askyesno(
        "Quiz Finished",
        f"Final Score: {score}/100\nGrade: {grade}\n\nPlay Again?"
    )

    if replay:
        quiz_frame.pack_forget()
        menu_frame.pack()
    else:
        root.destroy()

root = tk.Tk()
root.title("Maths Quiz")
root.geometry("500x400")
root.config(bg="#1e1e2f")

title_label = tk.Label(
    root,
    text="Maths Quiz Game",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=20)

menu_frame = tk.Frame(root, bg="#1e1e2f")
menu_frame.pack()

difficulty_label = tk.Label(
    menu_frame,
    text="Select Difficulty",
    font=("Arial", 16),
    bg="#1e1e2f",
    fg="white"
)
difficulty_label.pack(pady=10)

easy_button = tk.Button(
    menu_frame,
    text="Easy",
    width=20,
    command=lambda: start_quiz("Easy")
)
easy_button.pack(pady=5)

moderate_button = tk.Button(
    menu_frame,
    text="Moderate",
    width=20,
    command=lambda: start_quiz("Moderate")
)
moderate_button.pack(pady=5)

advanced_button = tk.Button(
    menu_frame,
    text="Advanced",
    width=20,
    command=lambda: start_quiz("Advanced")
)
advanced_button.pack(pady=5)

quiz_frame = tk.Frame(root, bg="#1e1e2f")

question_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 20),
    bg="#1e1e2f",
    fg="white"
)
question_label.pack(pady=20)

answer_entry = tk.Entry(
    quiz_frame,
    font=("Arial", 16)
)
answer_entry.pack(pady=10)

submit_button = tk.Button(
    quiz_frame,
    text="Submit Answer",
    command=check_answer,
    width=20
)
submit_button.pack(pady=10)

root.mainloop()
