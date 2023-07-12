import customtkinter as ctk
from PIL import Image
import tkinter, os, random, requests


main_dir = os.path.dirname(__file__)
images_dir = os.path.join(main_dir, "images")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class Home():
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("550x500")
        self.window.resizable(width=False, height=False)


        logo = ctk.CTkImage(Image.open(os.path.join(images_dir, "chelsea_main_logo.png")), size=(473, 157))
        label = ctk.CTkLabel(master=self.window, image=logo, text="")
        label.pack(pady=30)

        paragraph_label = ctk.CTkLabel(master=self.window, text_color="#BFA251", 
                                       text="Unleash your Chelsea FC knowledge!", font=("Arial", 20))
        paragraph_label.pack(pady=5)

        button = ctk.CTkButton(master=self.window, text="Start Trivia", text_color="white", command=self.start_playing)
        button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.window.mainloop()
    
    def start_playing(self):
        self.window.destroy()
        trivia = ChelseaTrivia()


class ChelseaTrivia():
    def __init__(self):
        self.endpoints = ["players", "nationality", "position", "top_appearances", 
                          "top_goalscorer", "most_goals", "most_appearances"]
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("550x500")
        self.window.resizable(width=False, height=False)

        self.canvas = ctk.CTkCanvas(width=275, height=250, bg="#13487B", highlightbackground="#887642")
        self.canvas.pack(pady=15)

        self.canvas_question = self.canvas.create_text(137, 125, text="", width=250, 
                                                       font=("Arial", 15, "bold"), fill="#887642")

        self.window.mainloop()


class ShowScore():
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("550x500")
        self.window.resizable(width=False, height=False)


        logo = ctk.CTkImage(Image.open(os.path.join(images_dir, "chelsea_main_logo.png")), size=(473, 157))
        self.label = ctk.CTkLabel(master=self.window, image=logo, text="")
        self.label.pack(pady=30)

        score_label = ctk.CTkLabel(master=self.window, text_color="#BFA251", text="", font=("Arial", 20))
        score_label.pack()

        play_again_button = ctk.CTkButton(master=self.window, text="Play Again", 
                                          text_color="white", command=self.play_again)
        play_again_button.pack(pady=5)

        stop_playing_button = ctk.CTkButton(master=self.window, text="Stop Playing", text_color="white", 
                                            fg_color="#BFA251", hover_color="#887643", command=self.stop_playing)
        stop_playing_button.pack(pady=5)
    
        self.window.mainloop()

    def show_score(self, score):
        self.label.config(text=f"Your score was: {score}")


    def stop_playing(self):
        self.window.quit()
    

    def play_again(self):
        self.window.destroy()
        trivia = ChelseaTrivia()

score = ShowScore()

# TODO Start to work in the logic of the game
# TODO buttons, question, and how so make the loop until 10 iterations
# TODO The logic should work when the user press any of the 3 buttons(options) no matter if the answer is correct
# TODO track the score