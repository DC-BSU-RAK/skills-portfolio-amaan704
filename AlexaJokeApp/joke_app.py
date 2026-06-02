import tkinter as tk
from tkinter import messagebox
import random

current_punchline = ""

def load_jokes():
    try:
        with open("randomJokes.txt", "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "randomJokes.txt file not found.")
        return []

def tell_joke():
    global current_punchline

    jokes = load_jokes()

    if not jokes:
        return

    joke = random.choice(jokes).strip()

    if "?" in joke:
        setup, punchline = joke.split("?", 1)
        setup_label.config(text=setup + "?")
        punchline_label.config(text="")
        current_punchline = punchline.strip()
    else:
        setup_label.config(text=joke)
        punchline_label.config(text="")
        current_punchline = ""

def show_punchline():
    if current_punchline:
        punchline_label.config(text=current_punchline)
    else:
        punchline_label.config(text="No punchline available.")

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("Alexa Joke App")
root.geometry("600x400")
root.config(bg="#1e1e2f")

title_label = tk.Label(
    root,
    text="Alexa Joke Assistant",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=20)

setup_label = tk.Label(
    root,
    text="Click the button to hear a joke!",
    font=("Arial", 15),
    wraplength=500,
    bg="#1e1e2f",
    fg="white"
)
setup_label.pack(pady=20)

punchline_label = tk.Label(
    root,
    text="",
    font=("Arial", 15, "bold"),
    wraplength=500,
    bg="#1e1e2f",
    fg="#ffd369"
)
punchline_label.pack(pady=20)

joke_button = tk.Button(
    root,
    text="Alexa tell me a Joke",
    font=("Arial", 13),
    command=tell_joke,
    width=25
)
joke_button.pack(pady=5)

punchline_button = tk.Button(
    root,
    text="Show Punchline",
    font=("Arial", 13),
    command=show_punchline,
    width=25
)
punchline_button.pack(pady=5)

next_button = tk.Button(
    root,
    text="Next Joke",
    font=("Arial", 13),
    command=tell_joke,
    width=25
)
next_button.pack(pady=5)

quit_button = tk.Button(
    root,
    text="Quit",
    font=("Arial", 13),
    command=quit_app,
    width=25
)
quit_button.pack(pady=5)

root.mainloop()
