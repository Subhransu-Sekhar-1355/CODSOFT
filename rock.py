import tkinter as tk
import random

# Game logic
choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

user_score = 0
comp_score = 0
target_score = 5

def get_winner(user, comp):
    if user == comp:
        return "It's a Tie!"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

def play(user_choice):
    global user_score, comp_score

    if user_score >= target_score or comp_score >= target_score:
        return

    comp_choice = random.choice(choices)
    result = get_winner(user_choice, comp_choice)

    if result == "You Win!":
        user_score += 1
    elif result == "You Lose!":
        comp_score += 1

    result_label.config(
        text=f"You: {emojis[user_choice]} ({user_choice})\n"
             f"Computer: {emojis[comp_choice]} ({comp_choice})\n\n{result}")
    score_label.config(
        text=f"🎯 Your Score: {user_score} | Computer Score: {comp_score}")

    if user_score == target_score:
        result_label.config(text="🏆 Congratulations! You won the match!")
    elif comp_score == target_score:
        result_label.config(text="💻 Computer won! Better luck next time.")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="🎯 Your Score: 0 | Computer Score: 0")

def random_move():
    play(random.choice(choices))

# UI Setup
root = tk.Tk()
root.title("🪨📄✂️ Rock Paper Scissors Game")
root.geometry("420x500")
root.configure(bg="#222")

# Fonts and styling
font_title = ("Arial", 20, "bold")
font_normal = ("Arial", 13)

tk.Label(root, text="Rock-Paper-Scissors", font=font_title, fg="white", bg="#222").pack(pady=20)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14), justify="center", fg="lightgreen", bg="#222")
result_label.pack(pady=20)

score_label = tk.Label(root, text="🎯 Your Score: 0 | Computer Score: 0", font=("Arial", 12), fg="lightblue", bg="#222")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#222")
button_frame.pack(pady=10)

# Game buttons
tk.Button(button_frame, text="🪨 Rock", width=12, font=font_normal, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="📄 Paper", width=12, font=font_normal, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="✂️ Scissors", width=12, font=font_normal, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Extra buttons
tk.Button(root, text="🔁 Reset Game", font=font_normal, command=reset_game).pack(pady=15)
tk.Button(root, text="🎲 Random Move", font=font_normal, command=random_move).pack()

root.mainloop()
