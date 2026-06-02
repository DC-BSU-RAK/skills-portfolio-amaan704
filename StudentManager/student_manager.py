import tkinter as tk
from tkinter import messagebox

FILE_NAME = "studentMarks.txt"

def calculate_percentage(student):
    coursework = student["mark1"] + student["mark2"] + student["mark3"]
    total = coursework + student["exam"]
    return (total / 160) * 100

def calculate_grade(percentage):
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()[1:]

            for line in lines:
                data = line.strip().split(",")

                student = {
                    "code": data[0],
                    "name": data[1],
                    "mark1": int(data[2]),
                    "mark2": int(data[3]),
                    "mark3": int(data[4]),
                    "exam": int(data[5])
                }

                students.append(student)

    except FileNotFoundError:
        messagebox.showerror("Error", "studentMarks.txt file not found.")

    return students

def format_student(student):
    coursework = student["mark1"] + student["mark2"] + student["mark3"]
    percentage = calculate_percentage(student)
    grade = calculate_grade(percentage)

    return (
        f"Student Name: {student['name']}\n"
        f"Student Number: {student['code']}\n"
        f"Total Coursework Mark: {coursework}/60\n"
        f"Exam Mark: {student['exam']}/100\n"
        f"Overall Percentage: {percentage:.2f}%\n"
        f"Grade: {grade}\n"
        "-----------------------------\n"
    )

def view_all_students():
    students = load_students()

    output_box.delete("1.0", tk.END)

    if not students:
        return

    total_percentage = 0

    for student in students:
        output_box.insert(tk.END, format_student(student))
        total_percentage += calculate_percentage(student)

    average = total_percentage / len(students)

    output_box.insert(
        tk.END,
        f"\nNumber of Students: {len(students)}\n"
        f"Average Percentage: {average:.2f}%"
    )

def view_individual_student():
    students = load_students()
    search_value = search_entry.get().lower()

    output_box.delete("1.0", tk.END)

    for student in students:
        if search_value == student["code"] or search_value in student["name"].lower():
            output_box.insert(tk.END, format_student(student))
            return

    messagebox.showerror("Not Found", "Student not found.")

def show_highest_student():
    students = load_students()

    if students:
        highest = max(students, key=calculate_percentage)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Student With Highest Overall Mark\n\n")
        output_box.insert(tk.END, format_student(highest))

def show_lowest_student():
    students = load_students()

    if students:
        lowest = min(students, key=calculate_percentage)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Student With Lowest Overall Mark\n\n")
        output_box.insert(tk.END, format_student(lowest))

root = tk.Tk()
root.title("Student Manager")
root.geometry("750x600")
root.config(bg="#1e1e2f")

title_label = tk.Label(
    root,
    text="Student Manager",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=10)

search_entry = tk.Entry(root, font=("Arial", 14), width=30)
search_entry.pack(pady=5)
search_entry.insert(0, "Enter student name or code")

button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=10)

tk.Button(button_frame, text="View All Students", width=25, command=view_all_students).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="View Individual Student", width=25, command=view_individual_student).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Highest Score", width=25, command=show_highest_student).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Lowest Score", width=25, command=show_lowest_student).grid(row=1, column=1, padx=5, pady=5)

output_box = tk.Text(root, width=85, height=22, font=("Arial", 11))
output_box.pack(pady=10)

root.mainloop()
