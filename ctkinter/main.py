import customtkinter as ctk
import tkinter
import os
from PIL import Image


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

        chelsea_trivia = ChelseaTrivia()


        button = ctk.CTkButton(master=self.window, text="Start Trivia", 
                               text_color="white", command=chelsea_trivia.start_playing)
        button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.window.mainloop()


class ChelseaTrivia():
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("550x500")
        self.window.resizable(width=False, height=False)

        canvas = ctk.CTkCanvas(width=275, height=250, bg="#13487B", highlightbackground="#887642")
        canvas.pack(pady=15)

        self.canvas_question = canvas.create_text(137, 125, text="", width=250, 
                                                  font=("Arial", 15, "bold"), fill="#887642")

        self.window.mainloop()

    def start_playing(self):
        pass

    
    def stop_playing(self):
        self.window.quit()

trivia = ChelseaTrivia()

class ShowScore():
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("550x500")
        self.window.resizable(width=False, height=False)
        self.trivia = ChelseaTrivia()


        logo = ctk.CTkImage(Image.open(os.path.join(images_dir, "chelsea_main_logo.png")), size=(473, 157))
        self.label = ctk.CTkLabel(master=self.window, image=logo, text="")
        self.label.pack(pady=30)

        score_label = ctk.CTkLabel(master=self.window, text_color="#BFA251", text="", font=("Arial", 20))
        score_label.pack()

        play_again_button = ctk.CTkButton(master=self.window, text="Play Again", text_color="white")
        play_again_button.pack(pady=5)

        stop_playing_button = ctk.CTkButton(master=self.window, text="Stop Playing", text_color="white", 
                                            fg_color="#BFA251", hover_color="#887643", command=self.trivia.stop_playing)
        stop_playing_button.pack(pady=5)
    
        self.window.mainloop()

    def show_score(self, score):
        self.label.config(text=f"Your score was: {score}")
