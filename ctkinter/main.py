import customtkinter as ctk
from PIL import Image
import os, random, requests


main_dir = os.path.dirname(__file__)
images_dir = os.path.join(main_dir, "images")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class Home():
    """
    Handles the home window of the GUI.
    """
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

        button = ctk.CTkButton(master=self.window, text="Start Trivia" , text_color="#887642", 
                               border_color="#887642", border_width=1, fg_color="#13487B", 
                               font=("Arial", 13, "bold"), command=self.start_playing)
        button.pack(pady=5)

        rules_button = ctk.CTkButton(master=self.window, text="Rules", text_color="#13487B", 
                                     border_color="#13487B", border_width=1, fg_color="#BFA251", 
                                     hover_color="#887643", font=("Arial", 13, "bold"), command=self.show_rules)
        rules_button.pack(pady=5)

        self.window.mainloop()
    
    def start_playing(self):
        """
        Helper function that works as a button command to start the trivia.
        """
        self.window.destroy()
        trivia = ChelseaTrivia()


    def show_rules(self):
        """
        Helper function that works as a button command to show the game rules.
        """
        rules = Rules()


class ChelseaTrivia():
    """
    Handles the trivia window of the GUI.
    """
    def __init__(self):
        self.endpoints = ["players", "nationality", "position", "top_appearances", 
                          "top_goalscorer", "most_goals", "most_appearances"]
        self.repeat_endpoints = ["players", "nationality", "position", "most_goals", "most_appearances"]
        self.do_not_repeat_endpoints = ["top_appearances", "top_goalscorer"]
        self.endpoint_track = []
        self.score = 0
        self.counter = 0
        self.value = 0
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("550x500")
        self.window.resizable(width=False, height=False)

        logo = ctk.CTkImage(Image.open(os.path.join(images_dir, "chelsea_trivia_logo.png")), size=(125, 125))
        logo_label = ctk.CTkLabel(master=self.window, image=logo, text="")
        logo_label.place(anchor="nw")

        self.canvas = ctk.CTkCanvas(width=275, height=250, bg="#13487B", highlightbackground="#887642")
        self.canvas.pack(pady=45)

        self.canvas_question = self.canvas.create_text(137, 125, text="", width=250, 
                                                       font=("Arial", 15, "bold"), fill="#887642")
        
        self.button1 = ctk.CTkButton(master=self.window, text="", text_color="#887642", border_color="#887642", 
                                     border_width=1, width=270, fg_color="#13487B", font=("Arial", 13, "bold"))
        self.button1.pack(pady=5)

        self.button2 = ctk.CTkButton(master=self.window, text="", text_color="#887642", border_color="#887642", 
                                     border_width=1, width=270, fg_color="#13487B", font=("Arial", 13, "bold"))
        self.button2.pack(pady=5)

        self.button3 = ctk.CTkButton(master=self.window, text="", text_color="#887642", border_color="#887642", 
                                     border_width=1, width=270, fg_color="#13487B", font=("Arial", 13, "bold"))
        self.button3.pack(pady=5)

        self.label = ctk.CTkLabel(master=self.window, text=f"Score: 0/10", font=("Arial", 20, "bold"), 
                                  text_color="#887642")
        self.label.place(relx=0.01, rely=1, anchor="sw")

        self.progess_bar = ctk.CTkProgressBar(master=self.window, mode="determinate", width=275, height=15, 
                                              fg_color="#887642", progress_color="#13487B")
        self.progess_bar.set(value=self.value)
        self.progess_bar.place(rely=0.99, relx=0.5, anchor="s")

        self.get_questions()
        self.window.mainloop()

    def get_questions(self):
        """
        Helper function that works as the logic of the trivia, by getting a json object from the api.
        With that json assigns to the canvas and buttons the respective question and options.
        """
        random_endpoint = random.choice(self.endpoints)
        self.endpoint_track.append(random_endpoint)
        if random_endpoint in self.endpoint_track and random_endpoint in self.do_not_repeat_endpoints:
            random_endpoint = random.choice(self.repeat_endpoints)
        response = requests.get(f"http://localhost:8000/{random_endpoint}")
        self.output = response.json()
        self.canvas.itemconfig(self.canvas_question, text=self.output["question"])
        options_array = [player[self.output["attribute"]] for player in self.output["players"]]
        self.button1.configure(text=options_array[0], 
                               command=lambda ans=options_array[0]: self.check_question(ans))
        self.button2.configure(text=options_array[1], 
                               command=lambda ans=options_array[1]: self.check_question(ans))
        self.button3.configure(text=options_array[2], 
                               command=lambda ans=options_array[2]: self.check_question(ans))
        

    def check_question(self, answer):
        """
        Helper function that works as a button command to check if the option that was selected by the user is correct.
        Also tracks the amount of questions to be asked, so when the trivia is finished it shows the score window.
        """
        self.label.configure(text=f"Score: {self.score}/10")
        self.value += 0.1
        self.progess_bar.set(value=self.value)
        if self.output["correct_answer"] == answer:
            self.score += 1


        self.counter += 1
        if self.counter < 10:
            self.get_questions()
        else:
            self.window.destroy()
            score = ShowScore(self.score)            


class ShowScore():
    """
    Handles the score windows of the GUI.
    """
    def __init__(self, score):
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("550x500")
        self.window.resizable(width=False, height=False)


        logo = ctk.CTkImage(Image.open(os.path.join(images_dir, "chelsea_main_logo.png")), size=(473, 157))
        self.label = ctk.CTkLabel(master=self.window, image=logo, text="")
        self.label.pack(pady=45)

        score_label = ctk.CTkLabel(master=self.window, text_color="#BFA251", 
                                   text=f"Your final score is: {score}", font=("Arial", 20))
        score_label.pack(pady=10)

        play_again_button = ctk.CTkButton(master=self.window, text="Play Again", text_color="#887642", 
                                          border_color="#887642", border_width=1, fg_color="#13487B", 
                                          font=("Arial", 13, "bold"), command=self.play_again)
        play_again_button.pack(pady=5)

        stop_playing_button = ctk.CTkButton(master=self.window, text="Stop Playing", text_color="#13487B", 
                                            border_color="#13487B", border_width=1, fg_color="#BFA251", 
                                            hover_color="#887643", font=("Arial", 13, "bold"), 
                                            command=self.stop_playing)
        stop_playing_button.pack(pady=5)

        self.window.mainloop()

    def stop_playing(self):
        """
        Helper function that works as a button command to quit playing.
        """
        self.window.destroy()
        self.window.quit()
    

    def play_again(self):
        """
        Helper function that works as a button command to play again the trivia.
        """
        self.window.destroy()
        trivia = ChelseaTrivia()


class Rules():
    def __init__(self):
        self.window = ctk.CTkToplevel()
        self.window.title("Rules")
        self.window.geometry("550x225")
        self.window.resizable(width=False, height=False)
        self.window.grab_set()
        self.rules = '''Welcome to Chelsea FC Trivia!
        \nThis game will test your knowledge of Chelsea FC.
        \nWith 10 random questions about players, stats, nationalities, and positions.
        \nEach question will have a time limit of 15 seconds.
        \nGet ready to have some fun and enjoy the game!"'''
    
        label = ctk.CTkLabel(master=self.window, text=self.rules, justify="center", 
                             text_color="#BFA251", font=("Arial", 13, "bold"))
        label.pack(padx=(10,10), pady=(15,0))

        button = ctk.CTkButton(master=self.window, text="Close", width=80, text_color="#887642", 
                               border_color="#887642", border_width=1, fg_color="#13487B", 
                               font=("Arial", 13, "bold"), command=lambda: self.window.destroy())
        button.pack(pady=10)

trivia = Home()


# TODO maybe find a way to not repeat the same question, like most_goals or most_appearances more than 2 times.
# TODO add a timer of 15/20 seconds and if there is no answer pass to the next one.
# TODO how to pack a python gui to execute in windows