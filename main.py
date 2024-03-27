import turtle
import pandas as pd
from tkinter import messagebox

# Function to check if the user input is a valid state name
def check_input(user_input):
    if user_input.title() in all_states:
        return True
    else:
        return False

# Function to display game over message 
def game_over():
    turtle.done()
    messagebox.showinfo("Game Over", "You have run out of lives!")

# Initialize the screen for the game
screen = turtle.Screen()
screen.title("Guess the State Game")

# Read the states data from the CSV file
data = pd.read_csv("States.csv")
all_states = data["States"].tolist()
guessed_states = []  # List to store guessed states
lives = 5  # Number of lives for the game

# Add the outline map of India
screen.addshape("india-political-map.gif")
turtle.shape("india-political-map.gif")

# Main game loop
while len(guessed_states) < 32 and lives > 0:
    # Get user input for state name
    user_input = screen.textinput(title=f"{lives}/5 Lives Remaining - Guess the State", prompt="Enter the State Name: ").title()
    
    # Check if user wants to quit
    if user_input is None:
        break
    
    # Check if the input is a valid state name
    if check_input(user_input):
        # Correct guess
        screen.title("Correct!")
        guessed_states.append(user_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["States"] == user_input]
        x = int(state_data['x'].iloc[0])
        y = int(state_data['y'].iloc[0])
        t.goto(x, y)
        t.dot(5)
        t.write(user_input)
    else:
        # Incorrect guess
        screen.title("Incorrect!")
        lives -= 1
        if lives == 0:
            # Game over if lives run out
            game_over()
            break

# If all states are guessed or the user cancels the game
if len(guessed_states) == 32:
    screen.title("Congratulations! You've guessed all 30 states!")
else:
    screen.title("Game Over! You've canceled the game!")

screen.mainloop()
