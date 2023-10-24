import tkinter


def calculate():
    km = float(input_miles.get())
    miles = km * 1.609
    km_output.configure(text=miles)
    km_output.grid(column=1, row=1)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

input_miles = tkinter.Entry(width=7)
input_miles.grid(column=1, row=0)

miles_text = tkinter.Label(text="Miles")
miles_text.grid(column=2, row=0)

equals_text = tkinter.Label(text="is equal to")
equals_text.grid(column=0, row=1)

km_text = tkinter.Label(text="Km")
km_text.grid(column=2, row=1)

km_output = tkinter.Label(text="0")
km_output.grid(column=1, row=1)

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()