import tkinter

window = tkinter.Tk()
window.title("My First Tkinter")
window.minsize(width=500, height=300)

# Labels
my_label = tkinter.Label(text="I'm a label", font=("TkFixedFont", 50, "bold"))
my_label.pack()


window.mainloop()
