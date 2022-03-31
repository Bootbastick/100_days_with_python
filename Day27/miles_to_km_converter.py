from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=330, height=200)


def button_clicked():
    new_text = int(input.get()) * 1.60934
    label1.config(text=new_text)


# Labels
label1 = Label(text="0", font=("Arial", 24, "bold"))
label1.grid(column=1, row=1)

label2 = Label(text="is equal to", font=("Arial", 24, "bold"))
label2.grid(column=1, row=0)

label3 = Label(text="Km", font=("Arial", 24, "bold"))
label3.grid(column=1, row=2)

label4 = Label(text="Miles", font=("Arial", 24, "bold"))
label4.grid(column=0, row=2)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=1)


# Entry
input = Entry(width=10)
input.grid(column=0, row=1)


window.mainloop()
