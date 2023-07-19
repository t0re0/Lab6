# i'm adding a comment. welcome to the password scramble/unscrambler!

# define encoded passwd
def encode_password(password):
    encoded_password = ""  # initialize empty string
    for digit in password:  # iterate over each digit with for loop
        # Convert the digit to an integer, raise it by 3, and wrap around if it exceeds 9
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


# add decoder fn here :)


if __name__ == '__main__':
    while True:
        # display menu with options
        print("What would you like to do?")
        print()
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Exit")
        print()

        option = int(input("Select a Menu Option: "))

        if option == 1:  # takes 8 digit int input, ensures it is 8 digits and converts it using the fn
            password = input("Enter an 8-digit integer password: ")
            if len(password) == 8:
                encoded_password = encode_password(password)
                print("Encoded password:", encoded_password)
            else:  # if not 8 dig, print error
                print("Invalid password. Please enter an 8-digit integer password.")

        elif option == 2:   # add the decoder part of the menu

        elif option == 3:  # exit program
            print("Exiting the program.")
            break

        else:  # invalid menu option
            print("Invalid option. Please select a valid menu option.")
