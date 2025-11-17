import tkinter as tk
from tkinter import messagebox
import random

win = tk.Tk()
win.title("Rock Paper Scissors")
win.geometry("500x600")
win.config(bg="#cfe8ff")

choices = ["Rock", "Paper", "Scissor"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)

    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {comp_choice}")

    # Determine winner
    if user_choice == comp_choice:
        result = "Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissor") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissor" and comp_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"You: {user_score}   Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="")
    comp_label.config(text="")
    result_label.config(text="")
    score_label.config(text="You: 0   Computer: 0")

title = tk.Label(win, text="Rock  Paper  Scissors", font=("Arial", 26, "bold"),
                 fg="#333", bg="#f2f2f2")
title.pack(pady=20)

score_label = tk.Label(win, text="You: 0   Computer: 0", font=("Arial", 20, "bold"),
                       fg="#444", bg="#f2f2f2")
score_label.pack(pady=10)

user_label = tk.Label(win, text="", font=("Arial", 16), bg="#f2f2f2", fg="#333")
user_label.pack()

comp_label = tk.Label(win, text="", font=("Arial", 16), bg="#f2f2f2", fg="#333")
comp_label.pack()

result_label = tk.Label(win, text="", font=("Arial", 22, "bold"), bg="#f2f2f2", fg="#0057b8")
result_label.pack(pady=20)

button_frame = tk.Frame(win, bg="#f2f2f2")
button_frame.pack(pady=30)

rock_btn = tk.Button(button_frame, text="🪨", width=5, height=2, font=("Arial", 32), 
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=20)

paper_btn = tk.Button(button_frame, text="📄", width=5, height=2, font=("Arial", 32), 
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=20)

scissor_btn = tk.Button(button_frame, text="✂️", width=5, height=2, font=("Arial", 32), 
                        command=lambda: play("Scissor"))
scissor_btn.grid(row=0, column=2, padx=20)

reset_btn = tk.Button(win, text="Reset Game", font=("Arial", 15), width=15,
                      bg="#ff6666", fg="white", command=reset_game)
reset_btn.pack(pady=20)

win.mainloop()

