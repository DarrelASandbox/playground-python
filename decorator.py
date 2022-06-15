def hello(name="Jose"):
    print("The hello() has been executed!")

    def greet():
        return "\t This is the greet() inside hello()."

    def welcome():
        return "\t This is the welcome() inside hello()."

    # print(greet())
    # print(welcome())
    # print("The hello() ends here.")

    return greet if name == "Jose" else welcome


func = hello()
print("\nCalling func():")
print(func())


###################################################################################################################################################


def func1():
    return "func1"


def func2(func):
    print(func())
    print("func2")


print("\nCalling func2():")
func2(func1)


###################################################################################################################################################


def new_decorator(original_func):
    def wrap_func():
        print("some extra code, BEFORE the original function")
        original_func()
        print("some extra code, AFTER the original function")

    return wrap_func


def need_decorator():
    print("Where is my decorator?!?!!")


decorated_func = new_decorator(need_decorator)
decorated_func2 = new_decorator(hello)

print("\ndecorated_func:")
decorated_func()
print("\ndecorated_func2:")
decorated_func2()


###################################################################################################################################################


@new_decorator
def below_new_decorator():
    print("I am below @new_decorator")


print("\nbelow_new_decorator():")
below_new_decorator()


###################################################################################################################################################
