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

        button = ctk.CTkButton(master=self.window, text="Start Trivia" , text_color="#887642", 
                               fg_color="#13487B", font=("Arial", 13, "bold"), command=self.start_playing)
        button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.window.mainloop()
    
    def start_playing(self):
        self.window.destroy()
        trivia = ChelseaTrivia()


class ChelseaTrivia():
    def __init__(self):
        self.endpoints = ["players", "nationality", "position", "top_appearances", 
                          "top_goalscorer", "most_goals", "most_appearances"]
        self.score = 0
        self.counter = 0
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("550x500")
        self.window.resizable(width=False, height=False)

        self.canvas = ctk.CTkCanvas(width=275, height=250, bg="#13487B", highlightbackground="#887642")
        self.canvas.pack(pady=30)

        self.canvas_question = self.canvas.create_text(137, 125, text="", width=250, 
                                                       font=("Arial", 15, "bold"), fill="#887642")
        
        self.button1 = ctk.CTkButton(master=self.window, text="", text_color="#887642", 
                                    width=270, fg_color="#13487B", font=("Arial", 13, "bold"))
        self.button1.pack(pady=5)

        self.button2 = ctk.CTkButton(master=self.window, text="", text_color="#887642", 
                                    width=270, fg_color="#13487B", font=("Arial", 13, "bold"))
        self.button2.pack(pady=5)

        self.button3 = ctk.CTkButton(master=self.window, text="", text_color="#887642", 
                                    width=270, fg_color="#13487B", font=("Arial", 13, "bold"))
        self.button3.pack(pady=5)

        self.get_questions()
        self.window.mainloop()

    def get_questions(self):
        random_endpoint = random.choice(self.endpoints)
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
        if self.output["correct_answer"] == answer:
            self.score += 1
            self.label = ctk.CTkLabel(master=self.window, text=f"Score: {self.score}/10", font=("Arial", 15, "bold"), 
                                      text_color="#887642")
            self.label.place(relx=0.01, rely=1, anchor="sw")

        self.counter += 1
        if self.counter < 10:
            self.get_questions()
        else:
            self.window.destroy()
            score = ShowScore(self.score)
            


class ShowScore():
    def __init__(self, score):
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("550x500")
        self.window.resizable(width=False, height=False)


        logo = ctk.CTkImage(Image.open(os.path.join(images_dir, "chelsea_main_logo.png")), size=(473, 157))
        self.label = ctk.CTkLabel(master=self.window, image=logo, text=f"Your score was: {score}")
        self.label.pack(pady=30)

        score_label = ctk.CTkLabel(master=self.window, text_color="#BFA251", text="", font=("Arial", 20))
        score_label.pack()

        play_again_button = ctk.CTkButton(master=self.window, text="Play Again", text_color="#887642", 
                                          fg_color="#13487B", font=("Arial", 13, "bold"), command=self.play_again)
        play_again_button.pack(pady=5)

        stop_playing_button = ctk.CTkButton(master=self.window, text="Stop Playing", text_color="white", 
                                            fg_color="#BFA251", hover_color="#887643", font=("Arial", 13, "bold"), 
                                            command=self.stop_playing)
        stop_playing_button.pack(pady=5)

        self.window.mainloop()

    def stop_playing(self):
        self.window.quit()
    

    def play_again(self):
        self.window.destroy()
        trivia = ChelseaTrivia()

score = Home()

# TODO Fix the repetition of top_goalscorer, top_appearances
# TODO Fix the question itself, have x has
# TODO Improve the way that you know if it is correct or not
