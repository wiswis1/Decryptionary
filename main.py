from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
from game import *
import game 
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()
word_List = ['Code', 'Hack', 'Bug', 'Money', 'University', 'Guess', 'Time', 'Grass', 'Bless', 'Game', 'Pressure', 'Music', 'Bolt', 'Snow', 'Show', 'Canada', 'Student', 'Professor', 'Holy']
def getRandWord(): 
    # print(f"This is the random word: {self.word_List}\n")
    return random.choice(word_List)

global word, guesses, level

def initialiseGame(diff):
    randWord = getRandWord()
    randWord = game.Game(randWord, diff)
    return randWord
     
word = initialiseGame("Easy")
level = word.getDiff()
guesses = word.getGuessNum()

def updateText():    
    level = word.getDiff()
    guesses = word.getGuessNum()
    
    pass

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

def showGameOver():
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

    try_again_button = ctk.CTkButton(game_over_window, text="Try again", command=lambda: restart_game(game_over_window))        
    try_again_button.pack(pady=10)
    
    quit_button = ctk.CTkButton(game_over_window, text = "Close", command=root.quit)
    quit_button.pack(pady=10)

    game_over_window.grab_set()


# Function to update the countdown timer
def updateTime(time_left):
    # we would have to update 
    if time_left > 0:
        time_label.configure(text=f"Time Left: {time_left}s")
        root.after(1000, updateTime, time_left - 1)  # Call itself after 1 sec
    else:
        showGameOver()
        # game_over_window = ctk.CTkToplevel(root)
        # game_over_window.title("Game Over")
        # game_over_window.overrideredirect(True)
        # game_over_window.attributes("-topmost", True)
        # game_over_window.lift()
        # game_over_window.focus_force()
        # game_over_window.resizable(False, False)


        # popup_width = 400
        # popup_height = 200

        # center_window(game_over_window, popup_width, popup_height)

        # game_over_label = ctk.CTkLabel(game_over_window, text="Game Over", font=("Arial", 16), text_color="red")
        # game_over_label.pack(expand=True, pady=20)

        # try_again_button = ctk.CTkButton(game_over_window, text="Try again", command=lambda: restart_game(game_over_window))        
        # try_again_button.pack(pady=10)
        
        # quit_button = ctk.CTkButton(game_over_window, text = "Close", command=root.quit)
        # quit_button.pack(pady=10)

        # game_over_window.grab_set()

        
# Menu bar to choose difficulty
options = ['Easy','Medium','Hard']
diffMenu = ctk.CTkOptionMenu(root, values = options)

def get_selected_option():
    level = diffMenu.get()
    word.setDiff(level)

def get_hint():
    """Updates the hint label with a new random hint."""
    hint_label.configure(text=show_hint())


def check_answer():
    """Checks the entered answer and provides feedback."""
    answer = entry.get().lower()
    if answer == word.getWord():  
        result_label.configure(text="Correct!")
    else:
        guesses-=1
        if guesses == 0:
            showGameOver()
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

# root.geometry("1000x500")
root.title("Word Puzzle")
center_window(root, 1100, 500)
# Difficulty and time label
diffText = f"Difficulty: {level}"
difficulty_label = ctk.CTkLabel(root, textvariable=diffText)#error with level
difficulty_label.grid(row=0, column=0, sticky="w")

time_label = ctk.CTkLabel(root)  # Timer label removed (text = )
time_label.grid(row=0, column=2, sticky="e")



def createCipher(word, parent, color="red"):
    original_text = word.getCipherDefinition()
    originalWords = original_text.split()
    cipherWords = word.getCipher()
    
    # fullText = ""
    # for i, word in enumerate(cipherWords):
    #     # Check if the word in cipherWords matches the word in originalWords at the same position
    #     if i < len(originalWords) and word == originalWords[i]:
    #         label_color = "green"  # Correct word, show in white
    #     else:
    #         label_color = color  # Incorrect word, show in the given color (red)
        
    #     fullText += f"{word}"

    # Create and pack the label
    lbl = ctk.CTkLabel(parent, text=fullText, font=("Arial", 16), text_color=label_color)
    lbl.pack(side="left", padx=5)

puzzle_label=createCipher(word, root, color="red")


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

guessText = f"Guesses left: \n {word.getGuessNum()}"
guess_label = ctk.CTkLabel(hint_frame, textvariable= guessText)
guess_label.pack()

# Result label
result_label = ctk.CTkLabel(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Hint display label
hint_label = ctk.CTkLabel(hint_frame, text="")
hint_label.pack()

# Start the countdown timer (e.g., 10 seconds)
updateTime(5)

# Closing confirmation
def on_closing():
    if messagebox.askyesno(title = 'Quit??', message = 'Do you really want to quit?'):
        root.destroy()
root.protocol("WM_DETELE_WINDOW", on_closing)


def restart_game(game_over_window):
    word = initialiseGame(level)
    game_over_window.destroy()
    updateTime(10)
    print("Game restarted!")

updateTime(5)

root.mainloop() 
    