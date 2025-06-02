# Password strength checker that checks how long it will take to crack your password
import re


def get_password():
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
        password = input('Enter your password: ')
        print(f'your chosen password is: {password}\n')
        print("Password strengthening tips:")
        valid = True
        if re.search(has_space, password):
            print('Your password is invalid because it contains space.')
            print('Try again.')
            valid = False
        else:
            if not re.search(upper, password):
                print('Your password should contain upper case letters.')
                charset -= 26
            if not re.search(lower, password):
                print('Your password should contain lower case letters.')
                charset -= 26
            if not re.search(symbol, password):
                print('Your password should contain Symbols.')
                charset -= 32
            if not re.search(num, password):
                print('Your password should contain numbers letters.')
                charset -= 10
            if len(password) < 12:
                print('Your password should be at least 12 characters long.')
            return password, charset


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


if __name__ == '__main__':

    print('Welcome to CheckMyPass')
    print('Here you can check your if password is secure.')

    password, charSet = get_password()
    estimate_brute_force_time(password, charSet)

# check if password is in a weak password list.
    with open("CommonPasswords.txt") as f:
        for n in f:
            start = n.find(" ")+1
            end = n.find("\n")
            line = n[start:end]
            if password == line:
                print("Your password is found in a week password list. BE AWARE!!!")
