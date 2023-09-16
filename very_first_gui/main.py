from tkinter import Tk, Label, Entry, Button, END

# Set up a window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# Labels
miles = Label(text="Miles")
miles.grid(row=1, column=3)

equal = Label(text="is equal to")
equal.grid(row=2, column=1)

km = Label(text="Km")
km.grid(row=2, column=3)

conversion = Label(text="0")
conversion.grid(row=2, column=2)


# Entry
entry = Entry(width=8)
entry.insert(END, string="0")
entry.grid(row=1, column=2)


# Convert Function
def convert_function():
    # Take miles_num and convert to km_num
    # Print in km
    miles_num = entry.get()

    km_num = round(float(miles_num) * 1.60934, 2)
    conversion["text"] = km_num



# Button
button = Button(text="Calculate", command=convert_function)
button.grid(row=3, column=2)


window.mainloop()