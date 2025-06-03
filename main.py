# Password strength checker that checks how long it will take to crack your password
import re
from tkinter import *


def check_password(password):
    # RegEx for the password checks ( symbols, lower and uppercase letters, number and
    # does nor contain white spaces)
    upper = re.compile(r"[A-Z]")
    lower = re.compile(r"[a-z]")
    num = re.compile(r"\d")
    symbol = re.compile(r"\W")
    has_space = re.compile(r'\s')
    valid = False

    while not valid:
        charset = 94
        lbl.config(text=f'\nyour chosen password is: {password}\n')
        tips = Label(root, text="Password strengthening tips:", )
        tips.pack(after=lbl)
        valid = True
        # infinite loop here FIX ASAP.
        # ============================
        if re.search(has_space, password):
            tips.config(text='Your password is invalid because it contains space.\nTry again.')
            valid = False
        else:
            password_entry.destroy()
            question.destroy()
            pass_btn.config(text="Retry")
            pass_btn.place(x=147, y=170)
            if not re.search(upper, password):
                upper_case = Label(text='Your password should contain upper case letters.')
                upper_case.pack()
                charset -= 26
            if not re.search(lower, password):
                lower_case = Label(text='Your password should contain lower case letters.')
                lower_case.pack()
                charset -= 26
            if not re.search(symbol, password):
                symbols = Label(text='Your password should contain Symbols.')
                symbols.pack()
                charset -= 32
            if not re.search(num, password):
                numbers = Label(text='Your password should contain numbers letters.')
                numbers.pack()
                charset -= 10
            if len(password) < 12:
                length = Label(text='Your password should be at least 12 characters long.')
                length.pack()
            return charset


# cracking time calculation.
def estimate_brute_force_time(checking_pass, char_set):
    pass_length = len(checking_pass)
    total_combinations = char_set ** pass_length
    time_in_seconds = total_combinations / 1000000
    print('\nTime To Crack:')
    print(f'Total possible combinations: {total_combinations}')
    if time_in_seconds < 60:
        print(f"{time_in_seconds:.2f} seconds")
    elif time_in_seconds < 3600:
        print(f"{time_in_seconds / 60:.2f} minutes")
    elif time_in_seconds < 86400:
        print(f"{time_in_seconds / 3600:.2f} hours")
    elif time_in_seconds < 31536000:
        print(f"{time_in_seconds / 86400:.2f} days")
    else:
        print(f"{time_in_seconds / 31536000:.2f} years")


def pass_btn_click():
    password = password_entry.get()
    if len(password) > 0:
        charset = check_password(password)
        estimate_brute_force_time(password, charset)


def check_password_list(password):
    # check if password is in a weak password list.
    with open("CommonPasswords.txt") as f:
        for n in f:
            start = n.find(" ") + 1
            end = n.find("\n")
            line = n[start:end]
            if password == line:
                print("Your password is found in a week password list. BE AWARE!!!")


if __name__ == '__main__':
    # root window + title and size
    root = Tk()
    root.title("CheckMyPass")
    root.geometry("350x200")

    # welcome message and information
    lbl = Label(root, text="Welcome to CheckMyPass\nHere you can check if your password is secure.\n")
    lbl.pack()

    # password entry
    question = Label(root, text="Enter password: ")
    question.pack()
    password_entry = Entry(root, width=20, show='*')
    password_entry.pack(after=question)
    pass_btn = Button(root, text="Enter", padx=10, command=pass_btn_click)
    pass_btn.place(x=147, y=100)

    # password strength check

    root.mainloop()

