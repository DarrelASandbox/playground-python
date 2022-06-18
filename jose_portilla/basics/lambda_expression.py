def splicer(string):
    return "Even" if len(string) % 2 == 0 else string[0]


def check_even(num):
    return num % 2 == 0


names = ["Andy", "Eve", "Thomas"]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


print(list(map(splicer, names)))
print(list(filter(check_even, nums)))

print(list(map(lambda num: num ** 2, nums)))
print(list(filter(lambda num: num % 2 == 0, nums)))
