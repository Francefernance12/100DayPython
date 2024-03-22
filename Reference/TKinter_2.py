from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Labels
label = Label(text="This is old text", font=("Arial", 20, "bold"))
label.config(text="This is new text")
label.grid(column=0, row=0)
label.config(padx=10, pady=10)


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=1, row=2)

# new button
button_2 = Button(text="Click Me again", command=action)
button_2.grid(column=2, row=0)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(column=3, row=3)

window.mainloop()
