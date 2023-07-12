import customtkinter as ctk
import tkinter
import os
from PIL import Image


main_dir = os.path.dirname(__file__)
images_dir = os.path.join(main_dir, "images")
print(images_dir)

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class Home():
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Chelsea FC Trivia")
        self.window.iconbitmap(os.path.join(images_dir, "chelsea_logo.ico"))
        self.window.geometry("600x600")



        logo = ctk.CTkImage(Image.open(os.path.join(images_dir, "chelsea_main_logo.png")), size=(473, 157))
        label = ctk.CTkLabel(master=self.window, image=logo, text="")
        label.pack(pady=30)

        chelsea_trivia = ChelseaTrivia()


        button = ctk.CTkButton(master=self.window, text="Start Trivia", 
                               text_color="white", command=chelsea_trivia.start_playing)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.window.mainloop()


class ChelseaTrivia():
    def __init__(self):
        pass

    def start_playing():
        pass
