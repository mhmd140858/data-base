from tkinter import *
from gtts import gTTS
import os
import tkinter.messagebox as msgbox
from tkinter import font


saved_text = ""


def set_text():
    global saved_text
    saved_text = entry.get("1.0", "end-1c").strip() 
    if saved_text:
        status_label.config(text="Text saved successfully!", fg="#2E7D32") 
        play_button.config(state=NORMAL) 
    else:
        status_label.config(text="Please enter some text to save.", fg="#C62828")  
        play_button.config(state=DISABLED)  

def text_to_speech():
    global saved_text
    if saved_text:
        try:
            tts = gTTS(text=saved_text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3") 
            status_label.config(text="Playing the saved text...", fg="#2E7D32")
        except Exception as e:
            status_label.config(text=f"An error occurred: {e}", fg="#C62828")
    else:
        status_label.config(text="No text has been set. Please use 'Set' first.", fg="#C62828")


def clear_text():
    global saved_text
    saved_text = ""
    entry.delete("1.0", "end")
    status_label.config(text="Text cleared.", fg="#FF9800")
    play_button.config(state=DISABLED)  


def exit_program():
    root.quit()


def create_button(parent, text, command, bg_color, hover_color, text_color, icon=None, width=20, height=2):
    button = Button(parent, text=text, command=command, font=("Helvetica", 12, "bold"), 
                    bg=bg_color, fg=text_color, activebackground=hover_color, 
                    activeforeground="white", bd=0, relief=FLAT, width=width, height=height)
    button.grid(padx=20, pady=10, sticky="ew")  
 
    button.bind("<Enter>", lambda e: button.config(bg=hover_color))
    button.bind("<Leave>", lambda e: button.config(bg=bg_color))
    if icon:
        button.config(image=icon, compound="left")
    return button


root = Tk()
root.title("Advanced Text-to-Speech App")
root.geometry("800x600")
root.config(bg="#ECEFF1")  


title_frame = Frame(root, bg="#ECEFF1")
title_frame.pack(fill=X, pady=(10, 0))

title_label = Label(title_frame, text="Text to Speech", font=("Helvetica", 26, "bold"), bg="#ECEFF1", fg="#37474F")
title_label.pack()

separator = Frame(root, bg="#90A4AE", height=2)
separator.pack(fill=X, pady=(0, 20))


entry_frame = Frame(root, bg="#ECEFF1")
entry_frame.pack(pady=10)

entry_label = Label(entry_frame, text="Enter your text below:", font=("Helvetica", 14, "bold"), bg="#ECEFF1", fg="#455A64")
entry_label.pack(anchor="w", padx=10, pady=5)

entry = Text(entry_frame, height=7, width=60, font=("Helvetica", 12), bd=3, relief="groove", wrap=WORD, bg="#FFFFFF", fg="#212121")
entry.pack(pady=10)


button_frame = Frame(root, bg="#ECEFF1")
button_frame.pack(pady=30)


set_button = create_button(button_frame, "Set Text", set_text, "#546E7A", "#455A64", "white")
set_button.grid(row=0, column=0, padx=20, pady=10)

play_button = create_button(button_frame, "Play Text", text_to_speech, "#1E88E5", "#1565C0", "white")
play_button.grid(row=0, column=1, padx=20, pady=10)
play_button.config(state=DISABLED)  

clear_button = create_button(button_frame, "Clear Text", clear_text, "#FF9800", "#FF5722", "white")
clear_button.grid(row=1, column=0, padx=20, pady=10)

exit_button = create_button(button_frame, "Exit", exit_program, "#D32F2F", "#B71C1C", "white")
exit_button.grid(row=1, column=1, padx=20, pady=10)


status_label = Label(root, text="", font=("Helvetica", 14), fg="#37474F", bg="#ECEFF1")
status_label.pack(pady=15)

footer_frame = Frame(root, bg="#ECEFF1")
footer_frame.pack(fill=X, pady=(20, 0))

footer_label = Label(footer_frame, text="  created by Mohamed Hosam Ibrahim", font=("Helvetica", 10), bg="#ECEFF1", fg="#607D8B")
footer_label.pack(anchor="e", padx=20)


root.mainloop()
