from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_row = {}
data_dict = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/French_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def card_flip():
    global random_row
    canvas.itemconfig(card_front_image, image = card_back)
    canvas.itemconfig(title, text="English", fill="white")
    english_word = random_row['English']
    canvas.itemconfig(word, text=f"{english_word}", fill="white")
    
def random_french_word():
    global random_row
    global flip_timer
    window.after_cancel(flip_timer)
    #random_num = random.randint(0,100)
    random_row = random.choice(data_dict)
    french_word = random_row['French']
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(card_front_image, image=card_front)
    canvas.itemconfig(word, text=f"{french_word}", fill="black")
    flip_timer = window.after(3000, card_flip)
    

def saving_progress():
    data_dict.remove(random_row)
    # print(len(data_dict))
    words_to_learn = pd.DataFrame(data_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    random_french_word()

    
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)






canvas= Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/Right.png")
wrong = PhotoImage(file="images/wrong.png")



card_front_image = canvas.create_image(410, 270, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right, highlightthickness=0, command=saving_progress)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong, highlightthickness=0, command=random_french_word)
wrong_button.grid(row=1, column=1)



random_french_word()


window.mainloop()

