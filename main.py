import tkinter as tk
import game 
import random

word_List = ['Code', 'Hack', 'Bug', 'Money', 'University', 'Guess', 'Time', 'Grass', 'Bless', 'Game', 'Pressure', 'Music', 'Bolt', 'Snow', 'Show', 'Canada', 'Student', 'Professor']
word = game.Game('Code')

printText = word.getCipherDefinition()

# Function to update the countdown timer
def updateScore(time_left):
    if time_left > 0:
        time_label.config(text=f"Time Left: {time_left}s")
        root.after(1000, updateScore, time_left - 1)  # Call itself after 1 sec
    elif (time_left == 0):
        win = tk.Tk()    
        win.geometry("250x250")
        win.Label(win,text = 'GAME OVER').pack
    else:
        time_label.config(text="Game Over")  # Display game over message
        game.time.sleep(5)
        root.destroy()

def check_answer():
    """Checks the entered answer and provides feedback."""
    answer = entry.get().lower()
    if answer == word.getWord():  
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect. Try again.")

def shortcut(event):
    if event.keysym == "Return":
        check_answer()

def show_hint():
    """Displays a hint (replace with your actual hint logic)."""
    hint_text = "It's what you use to buy things."  
    hint_label.config(text=hint_text)  

# Create the main window
root = tk.Tk()
root.geometry("1100x500")
root.title("Word Puzzle")

# Difficulty and time label
difficulty_label = tk.Label(root, text="Difficulty: easy")
difficulty_label.grid(row=0, column=0, sticky="w")

time_label = tk.Label(root, text="Time Left: 10s")  # Timer label
time_label.grid(row=0, column=2, sticky="e")

# Puzzle text
puzzle_text = printText
puzzle_label = tk.Label(root, text=puzzle_text, font=("Arial", 14), wraplength=1000, justify="center", anchor="center")
puzzle_label.grid(row=1, column=0, columnspan=3, pady=20)

# Input area
input_frame = tk.Frame(root, borderwidth=2, relief="groove")
input_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

enter_label = tk.Label(input_frame, text="Enter word here", font=("Arial", 12), justify="center", anchor="center")
enter_label.pack(pady=10)

entry = tk.Entry(input_frame, font=("Arial", 12))
entry.bind("<KeyPress>", shortcut)
entry.pack(pady=10)

check_button = tk.Button(input_frame, text="Check", command=check_answer)
check_button.pack(pady=10)

# Hint and guesses area
hint_frame = tk.Frame(root)
hint_frame.grid(row=3, column=2, sticky="ne", padx=20, pady=10)

hint_button = tk.Button(hint_frame, text="Hint?", command=show_hint)
hint_button.pack()

guess_label = tk.Label(hint_frame, text="Guesses: ")
guess_label.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Hint display label
hint_label = tk.Label(hint_frame, text="")
hint_label.pack()

# Start the countdown timer (e.g., 10 seconds)
updateScore(10)

root.mainloop()
