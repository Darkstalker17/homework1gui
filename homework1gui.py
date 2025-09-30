from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Interest Calculator")

def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda e: clear_placeholder(entry, placeholder))
    entry.bind("<FocusOut>", lambda e: restore_placeholder(entry, placeholder))

def clear_placeholder(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, END)

def restore_placeholder(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)

entry1 = Entry(root, width=20)
entry1.pack(pady=10)
add_placeholder(entry1, "Enter the rate : ")

entry2 = Entry(root, width=20)
entry2.pack(pady=10)
add_placeholder(entry2, "Enter the principle : ")

entry3 = Entry(root, width=20)
entry3.pack(pady=10)
add_placeholder(entry3, "Enter the time : ")

label = Label(root, text="")
label.pack(pady=10)

def get_number(entry, placeholder):
    try:
        value = float(entry.get())
        return value
    except ValueError:
        return None

def compound_interest_calculator():
    rate = get_number(entry1, "Enter the rate : ")
    principle = get_number(entry2, "Enter the principle : ")
    time = get_number(entry3, "Enter the time : ")
    if rate is None or principle is None or time is None:
        label.config(text="Please enter valid numbers!")
        return
    interest = principle * ((1 + rate / 100) ** time)
    label.config(text=f"Compound Interest = {interest}")

def simple_interest_calculator():
    rate = get_number(entry1, "Enter the rate : ")
    principle = get_number(entry2, "Enter the principle : ")
    time = get_number(entry3, "Enter the time : ")
    if rate is None or principle is None or time is None:
        label.config(text="Please enter valid numbers!")
        return
    interest = principle * rate * time / 100
    label.config(text=f"Simple Interest = {interest}")

button1 = Button(root, text="Calculate Simple Interest", command=simple_interest_calculator)
button1.pack(pady=5)

button2 = Button(root, text="Calculate Compound Interest", command=compound_interest_calculator)
button2.pack(pady=5)

root.mainloop()




