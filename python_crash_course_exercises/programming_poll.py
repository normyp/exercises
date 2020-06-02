while(True):
    reason = input("Why do you like programming? ")

    if reason == 'quit':
        break
    else:
        with open('reasons.txt', 'a') as file_object:
            file_object.write(reason + "\n")
        with open('reasons.txt') as file_object:
            lines = file_object.read()
            print(lines)
