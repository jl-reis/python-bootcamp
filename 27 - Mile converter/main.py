from tkinter import *


def convert():
    """Convert the user_entry from miles to km"""
    miles_input = user_input.get()
    km_converted = float(miles_input)*1.609344
    text_km_converted.config(text=f"{km_converted}")


window = Tk()
window.title("Interface")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

text_miles = Label(text="Miles")
text_miles.grid(column=2, row=0)

text_equal = Label(text="is equal to")
text_equal.grid(column=0, row=1)

text_km = Label(text="Km")
text_km.grid(column=2, row=1)

text_km_converted = Label(text="0")
text_km_converted.grid(column=1, row=1)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()
