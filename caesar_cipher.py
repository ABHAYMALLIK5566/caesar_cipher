alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', ',', '!', '@', '#', '$', '%', '^', '&' , '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ':', ';', '|', '\\', '\"', '\'', '<', '>', '.', '/', '?']* 100

cc=True

while cc:
    security= input("What do you want to do? Type 'E' to encrypt or 'D' to decrypt\n").upper()
    user_input= input("Enter your message here:\n")
    shift= int(input("Enter shifting digit: "))


    for characters in user_input:
        position = alpha.index(characters)
        if security == 'E':
            store = position + shift
        elif security == 'D':
            store = position - shift
        comp_output= alpha[store]
        print(comp_output, end='')   

    cont = input("\nDo you want to continue? Type 'C' to continue or 'E' to exit\n").upper()

    if cont == 'E':
        cc = False
