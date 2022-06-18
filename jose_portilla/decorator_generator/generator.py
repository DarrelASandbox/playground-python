import random


def create_cubes(nums):
    result = map(lambda num: num ** 3, list(range(nums)))
    return list(result)


print(create_cubes(10))


def genfib(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for num in genfib(10):
    print(num)


s = "hello"

# Iterate over string
for let in s:
    print(let)

# next(s)

s_iter = iter(s)
next(s_iter)
next(s_iter)


###################################################################################################################################################


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)
print("\n")


my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)


###################################################################################################################################################
