from tkinter import *
from datetime import datetime

def calculate_age():
    try:
        # Get user input
        user_name = name.get()
        birth_day = int(date.get())
        birth_month = int(month.get())
        birth_year = int(year.get())

        # Create a date object for the birth date
        birth_date = datetime(birth_year, birth_month, birth_day)
        today = datetime.today()

        # Calculate age
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day

        # Adjust if birthday hasn't occurred yet this year
        if age_days < 0:
            age_months -= 1
            # Get days in previous month
            if today.month == 1:
                prev_month_days = (datetime(today.year-1, 12, 1) - datetime(today.year-1, 11, 1)).days
            else:
                prev_month_days = (datetime(today.year, today.month, 1) - datetime(today.year, today.month-1, 1)).days
            age_days += prev_month_days
        if age_months < 0:
            age_years -= 1
            age_months += 12

        result_label.config(text=f"Hello {user_name}, you are {age_years} years, {age_months} months, and {age_days} days old!")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# Tkinter GUI
root = Tk()
root.geometry("400x400")
root.title("Age Calculator")

# Labels and entries
Label(root, text="Enter your name: ").pack(pady=5)
name = Entry(root)
name.pack(pady=5)

Label(root, text="Enter the date you were born (day): ").pack(pady=5)
date = Entry(root)
date.pack(pady=5)

Label(root, text="Enter the number of the month you were born: ").pack(pady=5)
month = Entry(root)
month.pack(pady=5)

Label(root, text="Enter the year you were born: ").pack(pady=5)
year = Entry(root)
year.pack(pady=5)

# Button to calculate age
Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

# Label to show result
result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

