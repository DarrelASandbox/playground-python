name = "global greet"  # Global


def greet():
    name = "enclosing greet"  #  Enclosing

    def greet_in_greet():
        name = "local greet"  # Local
        print("Greet in " + name)

    greet_in_greet()


greet()

x = 10


def global_x():
    global x
    print(f"x is {x}")
    x = 15
    print(f"x is now {x}")
    x = 20


global_x()
print(f"Printing x without using global_x function, x is {x}")


# Use this method instead of global keyword 
def reassign_x():
    return 30


x = reassign_x()

print(x)

