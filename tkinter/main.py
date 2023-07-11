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

    if player[attribute] == answer:
        score += 1

    if counter == 10:
        show_result()
    
    get_question()


def create_buttons(players):
    row = 1
    for player in players:
        button = Button(window, text=player[attribute], command=lambda p=player: button_clicked(p))
        button.grid(row=row, column=0)
        row += 1


def show_result():
    result_label = Label(window, text=f"Your score was {score} out of 10")
    result_label.grid(row=1, column=0)

    stop_button = Button(window, text="Stop Playing", command=window.quit)
    stop_button.grid(row=1, column=0)

    play_again_button = Button(window, text="Play Again", command=play_again)
    play_again_button.grid(row=1, column=0)


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
window.config(padx=50, pady=50, background="blue")

canvas = Canvas(width=250, height=250, background="blue")
data = get_question()
question = data["question"]
answer = data["correct_answer"]
attribute = data["attribute"]

question_trivia = canvas.create_text(125, 125, text="", width=125, font=("Arial", 15, "bold"), fill="white")
canvas.itemconfig(question_trivia, text=question)
canvas.grid(row=0, column=0)

create_buttons(data["players"])

window.mainloop()