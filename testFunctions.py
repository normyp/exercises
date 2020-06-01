def favourite_book(title, author):
    print("One of my favourite books is ", title, " and the author is ", author)


"""favourite_book(title="Lord of the Rings", author="JRR Tolkein")
favourite_book(author="Charles Dickens", title="Oliver Twist")"""


def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and has the text '{text}' on it.")


"""make_shirt("large")
make_shirt("medium")
make_shirt("xx small", "I'm tiny")"""


def describe_city(city, country="the UK"):
    print(f"{city} is in {country}")


"""describe_city("Bristol")
describe_city("Manchester")
describe_city("Berlin", "Germany")"""


def city_country(city, country):
    city_and_country = f"{city.title()}, {country.title()}"
    return city_and_country


"""print(city_country("bristol", "uk"))
print(city_country("berlin", "germany"))
print(city_country("paris", "france"))"""


def make_album(artist_name, album_title, number_of_tracks=None):
    album = {
        "Artist": artist_name,
        "Album Title": album_title,
        "Number of Tracks": number_of_tracks
    }
    return album


""""album1 = make_album(album_title="Stadium Arcaidum", artist_name="Red Hot Chilli Peppers", number_of_tracks="12")
print(album1["Artist"])
print(album1["Album Title"])
print(album1["Number of Tracks"])
album2 = make_album(album_title="Smoke on the Water", artist_name="Deep Purple")
print(album2["Artist"])
print(album2["Album Title"])
album3 = make_album(album_title="Keep the Faith", artist_name="Bon Jovi")
print(album3["Artist"])
print(album3["Album Title"])"""
"""while True:
    artist_name = input("Enter an artist name:(q to quit) ")
    if(artist_name == 'q'):
        break
    album_title = input("Enter an album title:(q to quit) ")
    if(album_title == 'q'):
        break
    else:
        album1 = make_album(artist_name, album_title)
    print(album1["Artist"])
    print(album1["Album Title"])"""
messages = ["Hey", "how", "are", "you?"]

def show_message(msg):
    for i in msg:
        print(i, end=" ")

def send_message(msg):
    sm = []
    for i in msg:
        sm.append(i)
    return sm

"""show_message(messages)
sent_message = send_message(messages[:])
print(" ")
print(sent_message)"""

def show_sandwich(*fillings):
    for filling in fillings:
        print(filling, end = " ")

    print(" ")

"""show_sandwich("Ham")
show_sandwich("Ham", "Cheese")
show_sandwich("Bacon", "Lettuce", "Tomato")"""

import printing_functions as pf

user_profile = pf.build_profile('Paul', 'Normington', location='Hampshire', field='Programming', hair_colour = 'Black')

#print(user_profile)

def make_car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

car = make_car('Ford', 'Focus', colour='Blue', drive_type='Manual')

#print(car)





#iceCreamStand.showFlavours()

"""print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(150)
print(restaurant.number_served)"""



"""restaurant.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()"""

admin1 = Admin('Paul', 'Normington', "pw123", "black")
admin1_privileges = [
    "can add post",
    "can delete post",
    "can ban user",
]
admin1.privileges.privileges = admin1_privileges
admin1.privileges.show_privileges()


user1 = User("Paul", "Normington", "helloworld", "black")
user2 = User("Chris", "Youles", "wahwah", "ginger")
user3 = User("David", "Greedy", "boop", "brown")

"""user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()"""

#Given the triangle of consecutive odd numbers:


def sum_row(n): #Calculate the row sums
    sum = 0
    for i in range(0, len(n)):
        sum += n[i]
    return sum

n = [3, 5]
#print(sum_row(n))

def print_square(n):
    for i in range(0, n):
        for j in range(0, n):
            print('*', end = ' ')
        print(" ")

"""def print_triangle(n):
    for i in range(0, n):
        for j in range(0, n):
            if(j < j/2-1 or j > j/2+1):
                print(" ", end = ' ')
            else:
                print("*", end = ' ')"""

#print_square(2) #Should print square 2 x 2



