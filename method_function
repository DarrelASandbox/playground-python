def even_odd(num):
    return num % 2 == 0


for num in range(1, 11):
    print(num, "is even") if even_odd(num) else print(num, "is odd")


stock_prices = {"APPL": 143, "GOOG": 2_299, "MSFT": 265}

for stock, price in stock_prices.items():
    print(f"{stock}: USD {price}")

from random import shuffle

red_ball_list = ["", "Red Ball", "", "", "", ""]
shuffle(red_ball_list)


def guess():
    guess = ""

    while guess not in range(0, 6):
        guess = int(input("Pick a number from 0 to 5."))

    return guess


def check(red_ball_list, guess):
    print("Nice") if red_ball_list[guess] == "Red Ball" else print("LOSER!")


# check(red_ball_list, guess())


def calculate(*args):
    return sum(args) * 0.05


print(
    calculate(
        40, 50, 34525, 23452, 3, 423, 74, 5, 64, 34, 52, 34, 52, 2, 7, 34, 67, 3, 46, 34
    )
)


def fruit(**kwargs):
    if "fruit" in kwargs:
        print(f"The fruit is {kwargs['fruit']}")
    else:
        print("No fruit found.")


fruit(fruit="apple")


def food(*args, **kwargs):
    print(f"I would like {sum(args)} {kwargs['food']} at USD {kwargs['price']} each.")


food(10, 20, 30, food="burger", price=1)


def evenList(*args):
    return [num for num in args if num % 2 == 0]


print(evenList(1, 2, 3, 4))


def even_odd_string(string):
    string_list = []

    for index, char in enumerate(string):
        string_list.append(char.upper()) if index % 2 == 0 else string_list.append(
            char.lower()
        )
    return "".join(string_list)


def even_odd_string2(x):
    string_list = []
    for i in range(len(x)):
        string_list.append(x[i].upper()) if i % 2 == 0 else string_list.append(
            x[i].lower()
        )
    return "".join(string_list)


print(even_odd_string("hello"))

