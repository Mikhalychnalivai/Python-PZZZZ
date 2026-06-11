import tkinter as tk
from tkinter import ttk, messagebox


def submit():
    messagebox.showinfo(
        "Регистрация",
        "Данные успешно отправлены!"
    )


def cancel():
    root.destroy()


root = tk.Tk()
root.title("Sign Up")
root.geometry("600x560")
root.configure(bg="#e8e8e8")
root.resizable(False, False)

main_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="solid"
)
main_frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=520,
    height=520
)

title = tk.Label(
    main_frame,
    text="Sign Up",
    font=("Arial", 14, "bold"),
    bg="white",
    anchor="w"
)
title.pack(fill="x", padx=10, pady=(10, 5))

tk.Frame(main_frame, bg="#cccccc", height=1).pack(fill="x")


form_frame = tk.Frame(main_frame, bg="white")
form_frame.pack(pady=8, padx=20, fill="x")

label_width = 16


tk.Label(form_frame, text="First Name", bg="white", width=label_width, anchor="e").grid(
    row=0, column=0, sticky="e", pady=4
)
first_name = tk.Entry(form_frame, width=32)
first_name.insert(0, "")
first_name.grid(row=0, column=1, pady=4, padx=5)


tk.Label(form_frame, text="Last Name", bg="white", width=label_width, anchor="e").grid(
    row=1, column=0, sticky="e", pady=4
)
last_name = tk.Entry(form_frame, width=32)
last_name.insert(0, "")
last_name.grid(row=1, column=1, pady=4, padx=5)


tk.Label(form_frame, text="Screen Name", bg="white", width=label_width, anchor="e").grid(
    row=2, column=0, sticky="e", pady=4
)
screen_name = tk.Entry(form_frame, width=32)
screen_name.insert(0, "")
screen_name.grid(row=2, column=1, pady=4, padx=5)


tk.Label(form_frame, text="Date of Birth", bg="white", width=label_width, anchor="e").grid(
    row=3, column=0, sticky="e", pady=4
)
dob_frame = tk.Frame(form_frame, bg="white")
dob_frame.grid(row=3, column=1, sticky="w", pady=4, padx=5)

month = ttk.Combobox(
    dob_frame,
    values=["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"],
    width=9
)
month.set("May")
month.pack(side="left")

day = ttk.Combobox(dob_frame, values=[str(i) for i in range(1, 32)], width=4)
day.set("5")
day.pack(side="left", padx=3)

year = ttk.Combobox(dob_frame, values=[str(i) for i in range(1950, 2011)], width=6)
year.set("1985")
year.pack(side="left")


tk.Label(form_frame, text="Gender", bg="white", width=label_width, anchor="e").grid(
    row=4, column=0, sticky="e", pady=4
)
gender = tk.StringVar(value="Male")
gender_frame = tk.Frame(form_frame, bg="white")
gender_frame.grid(row=4, column=1, sticky="w", pady=4, padx=5)

tk.Radiobutton(gender_frame, text="Male", variable=gender, value="Male", bg="white").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender, value="Female", bg="white").pack(side="left")


tk.Label(form_frame, text="Country", bg="white", width=label_width, anchor="e").grid(
    row=5, column=0, sticky="e", pady=4
)
country = ttk.Combobox(
    form_frame,
    values=["USA", "Russia", "Kazakhstan", "Belarus", "Armenia", "Germany"],
    width=29
)
country.set("USA")
country.grid(row=5, column=1, pady=4, padx=5, sticky="w")


tk.Label(form_frame, text="E-mail", bg="white", width=label_width, anchor="e").grid(
    row=6, column=0, sticky="e", pady=4
)
email = tk.Entry(form_frame, width=32)
email.insert(0, "")
email.grid(row=6, column=1, pady=4, padx=5)


tk.Label(form_frame, text="Phone", bg="white", width=label_width, anchor="e").grid(
    row=7, column=0, sticky="e", pady=4
)
phone = tk.Entry(form_frame, width=32)
phone.insert(0, "")
phone.grid(row=7, column=1, pady=4, padx=5)


tk.Label(form_frame, text="Password", bg="white", width=label_width, anchor="e").grid(
    row=8, column=0, sticky="e", pady=4
)
password = tk.Entry(form_frame, width=32, show="*")
password.grid(row=8, column=1, pady=4, padx=5)


tk.Label(form_frame, text="Confirm Password", bg="white", width=label_width, anchor="e").grid(
    row=9, column=0, sticky="e", pady=4
)
confirm_password = tk.Entry(form_frame, width=32, show="*")
confirm_password.grid(row=9, column=1, pady=4, padx=5)


tk.Frame(main_frame, bg="#cccccc", height=1).pack(fill="x", pady=(4, 0))


agree = tk.IntVar()
tk.Checkbutton(
    main_frame,
    text="I agree to the Terms of Use",
    variable=agree,
    bg="white"
).pack(anchor="w", padx=80, pady=6)


tk.Frame(main_frame, bg="#cccccc", height=1).pack(fill="x")


btn_frame = tk.Frame(main_frame, bg="white")
btn_frame.pack(anchor="e", padx=10, pady=8)

tk.Button(
    btn_frame,
    text="submit",
    width=8,
    command=submit
).pack(side="left", padx=4)

tk.Button(
    btn_frame,
    text="Cancel",
    width=8,
    command=cancel
).pack(side="left", padx=4)

root.mainloop()