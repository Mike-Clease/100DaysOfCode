import tkinter

window = tkinter.Tk()
window.title("My First Tkinter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Labels
my_label = tkinter.Label(text="I'm a label", font=("System", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=5, pady=5)

# Buttons


def button_click():
    input_text = input.get()
    my_label.configure(text=input_text)
    my_label.grid(column=0, row=0)
    my_label.config(padx=5, pady=5)


button = tkinter.Button(text="Click Me!", command=button_click)
button.grid(column=1, row=1)
button.config(padx=5, pady=5)

button2 = tkinter.Button(text="New Button")
button2.grid(column=2, row=0)
button2.config(padx=5, pady=5)

# Entry

input = tkinter.Entry()
input.grid(column=3, row=2)
input.config()


window.mainloop()
