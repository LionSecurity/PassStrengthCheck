# Password strength checker that checks how long it will take to crack your password
import re

if __name__ == '__main__':

    # RegEx for the password checks ( symbols, lower and uppercase letters, number and
    # does nor contain white spaces)
    upper = re.compile(r"[A-Z]")
    lower = re.compile(r"[a-z]")
    num = re.compile(r"\d")
    symbol = re.compile(r"\W")
    hasSpace = re.compile(r'\s')
    valid = False

    print('Welcome to CheckMyPass')
    print('Here you can check your if password is secure.')

    while not valid:
        charSet = 94
        password = input('Enter your password: ')
        print(f'your chosen password is: {password}\n')
        print("Password strengthening tips:")
        valid = True
        if re.search(hasSpace, password):
            print('Your password is invalid because it contains space.')
            print('Try again.')
            valid = False
        else:
            if not re.search(upper, password):
                print('Your password should contain upper case letters.')
                charSet -= 26
            if not re.search(lower, password):
                print('Your password should contain lower case letters.')
                charSet -= 26
            if not re.search(symbol, password):
                print('Your password should contain Symbols.')
                charSet -= 32
            if not re.search(num, password):
                print('Your password should contain numbers letters.')
                charSet -= 10
            if len(password) < 12:
                print('Your password should be at least 12 characters long.')

# check if password is in a weak password list.
    with open("CommonPasswords.txt") as f:
        for n in f:
            start = n.find(" ")+1
            end = n.find("\n")
            line = n[start:end]
            if password == line:
                print("Your password is found in a week password list. BE AWARE!!!")

# cracking time calculation.
    passLength = len(password)
    totalCombinations = charSet ** passLength
    timeInSeconds = totalCombinations / 1000000
    print('\nTime To Crack:')
    print(f'Total possible combinations: {totalCombinations}')
    if timeInSeconds < 60:
        print(f"{timeInSeconds:.2f} seconds")
    elif timeInSeconds < 3600:
        print(f"{timeInSeconds / 60:.2f} minutes")
    elif timeInSeconds < 86400:
        print(f"{timeInSeconds / 3600:.2f} hours")
    elif timeInSeconds < 31536000:
        print(f"{timeInSeconds / 86400:.2f} days")
    else:
        print(f"{timeInSeconds / 31536000:.2f} years")
