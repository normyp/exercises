while(True):
    guest_name = input("Enter your name: ")
    if guest_name == 'quit':
        break
    else:
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(guest_name + "\n")
        print("Hello,", guest_name,"and welcome")
