hunger = False
if hunger:
    print("Feed the hungry")
else:
    print("Not yet hunger")

location = "Bank"
if location == "School":
    print("Go to school!")
elif location == "Bank":
    print("No money, no honey")
else:
    print("Run run run!")


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
string = "Hello String"
string2 = "123"
dictionary = {"k1": "ab", "k2": "cd", "k3": "ef"}

for char in string:
    print(char)

for _ in string2:
    print("Whack!")

for num in list1:
    if num % 2 == 0:
        print(num, "is even")
    if num % 2 != 0:
        print(num, "is odd")

# Tuple unpacking
for (num1, num2) in list2:
    print(num1, "+", num2, "=", num1 + num2)
    if num1 % 2 == 0:
        print(num1, "is even")
    elif num1 % 2 != 0:
        print(num1, "is odd")
    if num2 % 2 == 0:
        print(num2, "is even")
    else:
        print(num2, "is odd")

for key in dictionary:
    print(key)

for key_value in dictionary.items():
    print(key_value)

for key, value in dictionary.items():
    print(key, ":", value)

for key, value in dictionary.values():
    print(key, ":", value)

for key, value in dictionary:
    print(key, ":", value)


x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print(f"x is not less than {x}")

# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all.

for num in list1:
    pass

for num in list1:
    if num % 2 == 0:
        continue
    else:
        print(f"This is {num}")

for num in range(0, 10, 2):
    print(num)


index = 0
word = "abcde"

for letter in word:
    print(f"At index {index} the letter is {index}")
    index += 1

for index, letter in enumerate(word):
    print(index, ":", letter)

for num in zip(list1, list2):
    print(num)

print("1 is found in list1:", 1 in list1)
print("ab is found in dictionary:", "ab" in dictionary.values())
print(min(list2))
print(max(list2))


from random import shuffle  # Mutates
from random import randint

print("Returns nothing:", shuffle(list1))
print("Shuffled list1", list1)
# print(randint(0, int(input("Enter a number:"))))
print([char for char in string])
print([num ** 2 for num in range(523442, 523452)])


string3 = "Sam prints only the words that start with s in this sentence"
for char in string3.split():
    if char[0].lower() == "s":
        print(char)

for num in range(0, 11, 2):
    print(num)

print([num for num in range(0, 51) if num % 2 != 0])

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print([word[0] for word in string3.split()])
