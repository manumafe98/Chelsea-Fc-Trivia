from tkinter import *
import requests
import random


ENDPOINTS = ["players", "nationality", "position", "top_appearances", 
             "top_goalscorer", "most_goals", "most_appearances"]
NOT_REPEAT = ["top_goalscorer", "top_appearances"]

used_endpoint = []
counter = 0
score = 0


def button_clicked(player):
    global counter, score
    counter += 1
    print(f"Selected player: {player}")

    if player == "Correct Answer":
        score += 1

    if counter == 10:
        show_result()


def create_buttons(players):
    for player in players:
        button = Button(window, text=player[attribute], command=lambda p=player: button_clicked(p))
        button.pack()


def show_result():
    result_label = Label(window, text=f"Your score was {score} out of 10")
    result_label.pack()

    stop_button = Button(window, text="Stop Playing", command=window.quit)
    stop_button.pack()

    play_again_button = Button(window, text="Play Again", command=play_again)
    play_again_button.pack()        


def play_again():
    global counter, score
    counter = 0
    score = 0

    # Clear the previous buttons and result
    for widget in window.winfo_children():
        widget.destroy()


def get_question():
    random_endpoint = random.choice(ENDPOINTS)
    used_endpoint.append(random_endpoint)

    if random_endpoint in NOT_REPEAT and random_endpoint in used_endpoint:
        get_question()
    response = requests.get(f"http://localhost:8000/{random_endpoint}")
    output = response.json()

    return output


window = Tk()
window.title("Chelsea Fc Trivia")
window.config(padx=50, pady=50)

data = get_question()
question = data["question"]
answer = data["correct_answer"]
attribute = data["attribute"]

create_buttons(data["players"])


window.mainloop()