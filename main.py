from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
from game import*
import game 
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

word_List = ['Code', 'Hack', 'Bug', 'Money', 'University', 'Guess', 'Time', 'Grass', 'Bless', 'Game', 'Pressure', 'Music', 'Bolt', 'Snow', 'Show', 'Canada', 'Student', 'Professor']


def getRandWord(): 
    # print(f"This is the random word: {self.word_List}\n")
    return random.choice(word_List)

randWord = getRandWord()
print(randWord)
word = Game(randWord, "Hard")




def center_window(root, width=400, height=300):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position x and y
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the geometry of the window
    root.geometry(f"{width}x{height}+{x}+{y}")

    def disable_movement():
        root.geometry(f"{width}x{height}+{x}+{y}")


# Function to update the countdown timer
def updateTime(time_left):
    if time_left > 0:
        time_label.configure(text=f"Time Left: {time_left}s")
        root.after(1000, updateTime, time_left - 1)  # Call itself after 1 sec
    else:
        game_over_window = ctk.CTkToplevel(root)
        game_over_window.title("Game Over")
        game_over_window.overrideredirect(True)
        game_over_window.attributes("-topmost", True)
        game_over_window.lift()
        game_over_window.focus_force()
        game_over_window.resizable(False, False)


        popup_width = 400
        popup_height = 200

        center_window(game_over_window, popup_width, popup_height)

        game_over_label = ctk.CTkLabel(game_over_window, text="Game Over", font=("Arial", 16), text_color="red")
        game_over_label.pack(expand=True, pady=20)
            
        def restart_game():
            game.Game("Hack", "Hard")
            game_over_window.destroy()
            print("Game restarted!")

        try_again_button = ctk.CTkButton(game_over_window, text="Try again", command=restart_game)
        try_again_button.pack(pady=10)
        
        quit_button =ctk.CTkButton(game_over_window, text = "Close", command=root.quit)
        quit_button.pack(pady=10)

        game_over_window.grab_set()

        


def get_hint():
    """Updates the hint label with a new random hint."""
    hint_label.configure(text=show_hint())


def check_answer():
    """Checks the entered answer and provides feedback."""
    answer = entry.get().lower()
    if answer == word.getWord():  
        result_label.configure(text="Correct!")
    else:
        result_label.configure(text="Incorrect. Try again.")

def shortcut(event):
    if event.keysym == "Return":
        check_answer()

def show_hint():
    "Fetches a random hint from the word's synonyms."
    synonyms = word.getSynonyms()
    if synonyms:  # Ensure there are synonyms available
        return random.choice(synonyms)  

        

# Create the main window
root = ctk.CTk()
# root.geometry("1000x500")
root.title("Word Puzzle")
center_window(root, 1100, 500)
# Difficulty and time label
difficulty_label = ctk.CTkLabel(root, text="Difficulty: easy")
difficulty_label.grid(row=0, column=0, sticky="w")

time_label = ctk.CTkLabel(root, text="Time Left: 10s")  # Timer label
time_label.grid(row=0, column=2, sticky="e")

# Puzzle text
definitionText = word.getDefinition()
printText = word.getCipherDefinition()
puzzle_text = printText
puzzle_label = ctk.CTkLabel(root, text=puzzle_text, font=("Arial", 14), wraplength=1100, justify="center", anchor="center")
puzzle_label.grid(row=1, column=0, columnspan=3, pady=20)
# for i in range(len(printText)):
    # if printText[i] != definitionText[i]  
        # puzzle_label.configure(fg="green")
    



# Input area
input_frame = ctk.CTkFrame(root)
input_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

enter_label = ctk.CTkLabel(input_frame, text="Enter word here", font=("Arial", 12), justify="center", anchor="center")
enter_label.pack(pady=10)

entry = ctk.CTkEntry(input_frame, font=("Arial", 12))
entry.bind("<KeyPress>", shortcut)
entry.pack(pady=10)

check_button = ctk.CTkButton(input_frame, text="Check", command=check_answer)
check_button.pack(pady=10)

# Hint and guesses area
hint_frame = ctk.CTkFrame(root)
hint_frame.grid(row=3, column=2, sticky="ne", padx=20, pady=10)

hint_button = ctk.CTkButton(hint_frame, text="Hint?", command=get_hint)
hint_button.pack()

# text = f"Guesses left: \n {word.getGuessNum()}"
# guess_label = ctk.CTkLabel(hint_frame, text="Guesses: \n")
# guess_label.pack()

# Result label
result_label = ctk.CTkLabel(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Hint display label
hint_label = ctk.CTkLabel(hint_frame, text="")
hint_label.pack()

# Start the countdown timer (e.g., 10 seconds)
updateTime(5)

# Closing confirmation
root.protocol("WM_DETELE_WINDOW")

def on_closing():
    if messagebox.askyesno(title = 'Quit??', message = 'Do you really want to quit?'):
        root.destroy()

# Menu bar to choose difficulty
options = ['Easy','Medium','Hard']
# menubar = ctk.CTkOptionMenu(root)
# diffMenu = ctk.CTkOptionMenu(menubar)
# diffMenu._command(label = "Easy", command = word.diff("Easy"))
# diffMenu._command(label = "Medium", command = word.diff("Medium"))
# diffMenu._command(label = "Hard", command = word.diff("Hard"))
# menubar.add_cascade(menu = diffMenu, label = "Difficulty")

root.mainloop() 
