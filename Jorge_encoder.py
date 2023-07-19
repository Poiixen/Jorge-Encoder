# Jorge Garcia 
def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3, Quit")


def encode(input_password):
    output = ""
    for num in str(input_password):  # turn password into string to iterate through every character
        if num == "0":  # detects 0, as int() doesn't
            num = str(3)
        else:   # any digit besides 0 
            num = str(int(num) + 3)  # must be an integer to use add operation, result must be string. Adds 3 to num
            if len(num) == 2:
                num = num[-1] # if result is 2 digits, gets the last digit. ex: 9 + 3 = 2
        output += num
    print("Your password has been encoded and stored!")
    return output


def decode(password):
    decoded_password = ''
    for num in str(password):
        if num == '0':
            num = str(7)
        elif num == '1':
            num = str(8)
        elif num == '2':
            num = str(9)
        else:
            num = str(int(num) - 3)
        decoded_password += num
    print(f"Your decoded password is {password}, and your original password is {decoded_password}")
    pass


while True:
    menu()
    option = int(input("Please enter an option:"))

    if option == 1:
        password_input = input("Please enter your password to encode:")
        print(encode(password_input))
    elif option == 2:
        decode(encode(password_input))
        pass
    elif option == 3:
        break
