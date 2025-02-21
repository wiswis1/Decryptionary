# main game class !
import tkinter as tk
from game import game

# word_List = ['Code', 'Hack', 'Bug', 'Money', 'University', 'Guess', 'Time', 'Grass', 'Bless', 'Game', 'Pressure', 'Music',  'Bolt', 'Snow', 'Show', 'Canada', 'Student', 'Professor ']
# word = game("Code")

def check_answer():
    """Checks the entered answer and provides feedback."""
    answer = entry.get().lower()
    if answer == "money":  # Replace with the actual answer
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect. Try again.")

def shortcut(event):
    if event.keysym == "Return":
        check_answer()

def show_hint():
    """Displays a hint (replace with your actual hint logic)."""
    hint_text = "It's what you use to buy things."  # Replace with your hint
    hint_label.config(text=hint_text)  # Update the hint label

# Create the main window
root = tk.Tk()
root.title("Word Puzzle")

# Difficulty and time label
difficulty_label = tk.Label(root, text="Difficulty: easy")
difficulty_label.grid(row=0, column=0, sticky="w")
time_label = tk.Label(root, text="1:32")#waiting for logic team to implement time
time_label.grid(row=0, column=2, sticky="e")

# Puzzle text (with blank spaces represented by underscores)
puzzle_text = """a ______ medium of exchange ______ of ______ and ______ collectively."""
puzzle_label = tk.Label(root, text=puzzle_text, font=("Arial", 14))
puzzle_label.grid(row=1, column=0, columnspan=3, pady=20)

# Input area
input_frame = tk.Frame(root, borderwidth=2, relief="groove")
input_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

enter_label = tk.Label(input_frame, text="enter word here", font=("Arial", 12))
enter_label.pack(pady=10)

entry = tk.Entry(input_frame, font=("Arial", 12))
entry.bind("<KeyPress>", shortcut)
entry.pack(pady=10)

check_button = tk.Button(input_frame, text="Check", command=check_answer)
check_button.pack(ady=10)

# Hint and guesses area
hint_frame = tk.Frame(root)
hint_frame.grid(row=3, column=2, sticky="ne", padx=20, pady=10)

hint_button = tk.Button(hint_frame, text="Hint?", command=show_hint)
hint_button.pack()

guess_label = tk.Label(hint_frame, text="Guesses: ")#waiting for game logic team to create logic for the guess reduction
guess_label.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Hint display label (initially empty)
hint_label = tk.Label(hint_frame, text="")
hint_label.pack()


root.mainloop()