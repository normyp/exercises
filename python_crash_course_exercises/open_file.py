with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

"""print(pi_string)
print(len(pi_string))"""

with open('learning.python.txt') as file_object:
    lines = file_object.read()

#print(lines)

#with open('learning.python.txt') as file_object:
    #for line in file_object:
        #print(line.rstrip())

#print("")

with open('learning.python.txt') as file_object:
    lines = file_object.read()


learn_string = ""

for line in lines:
    learn_string += line

#print(learn_string.replace('Python', 'C'))

filename = 'programming.txt'

with open('programming.txt', 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


