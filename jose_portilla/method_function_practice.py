def lesser_of_two_evens(num1, num2):
    return min(num1, num2) if num1 % 2 == 0 and num2 % 2 == 0 else max(num1, num2)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))


def animal_crackers(text):
    return text.split()[0][0] == text.split()[1][0]


print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))


def makes_twenty(num1, num2):
    return sum((num1, num2)) == 20 or num1 == 20 or num2 == 20


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


def old_macdonald(name):
    return (
        name[:3].upper() + name[3:].upper() if len(name) > 3 else "Name is too short!"
    )


def old_macdonald2(name):
    string_list = []
    for i in range(len(name)):
        string_list.append(name[i].upper()) if i == 0 or i == 3 else string_list.append(
            name[i].lower()
        )
    return "".join(string_list)


print(old_macdonald2("macdonald"))


def master_yoda(text):
    return " ".join(text.split()[::-1])


def master_yoda2(text):
    reverse = text.split()
    reverse.reverse()
    return " ".join(reverse)


print(master_yoda("I am home"))
print(master_yoda("We are ready"))


def almost_there(n):
    return n >= 90 and n <= 110 or n >= 190 and n <= 210


print("almost_there 90:", almost_there(90))
print("almost_there 104:", almost_there(104))
print("almost_there 150:", almost_there(150))
print("almost_there 209:", almost_there(209))


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


def has_33_2(nums):
    for i in range(0, len(nums) - 1):
        if nums[i : i + 2] == [3, 3]:
            return True
    return False


print("has_33:", has_33([1, 3, 3]))
print("has_33:", has_33([1, 3, 1, 3]))
print("has_33:", has_33([3, 1, 3]))


def paper_doll(text):
    result = ""
    for char in text:
        result += char * 3
    return result


def paper_doll2(text):
    string_list = []
    for _, char in enumerate(text):
        string_list.append(3 * char)
    return "".join(string_list)


print(paper_doll("Hello"))
print(paper_doll("Mississippi"))


def blackjack(num1, num2, num3):

    if sum((num1, num2, num3)) <= 21:
        return sum((num1, num2, num3))
    elif sum((num1, num2, num3)) <= 31 and 11 in (num1, num2, num3):
        return sum((num1, num2, num3)) - 10
    else:
        return "BUST"


def blackjack2(num1, num2, num3):
    sum_three_nums = num1 + num2 + num3
    if (sum_three_nums) <= 21:
        return sum_three_nums
    else:
        if num1 == 11 or num2 == 11 or num3 == 11:
            sum_three_nums -= 10
    return "BURST" if (sum_three_nums > 21) else sum_three_nums


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print("summer_69:", summer_69([1, 3, 5]))
print("summer_69:", summer_69([4, 5, 6, 7, 8, 9]))
print("summer_69:", summer_69([2, 1, 6, 9, 11]))


def spy_game(nums):
    string_list = []
    for num in nums:
        if num == 0 or num == 7:
            string_list.append(num)

    string_list = map(str, string_list)
    contains = "".join(string_list).find("007")
    return False if contains == -1 else True


def spy_game2(nums):
    code = [0, 0, 7, "x"]
    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works
    return len(code) == 1


print(spy_game2([1, 2, 4, 0, 0, 7, 5]))
print(spy_game2([1, 0, 2, 4, 0, 5, 7]))
print(spy_game2([1, 7, 2, 0, 4, 5, 0]))


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3, x, 2):  # test all odd factors up to x-1
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)


def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)


print(count_primes(100))


def print_big(letter):
    patterns = {
        1: "  *  ",
        2: " * * ",
        3: "*   *",
        4: "*****",
        5: "**** ",
        6: "   * ",
        7: " *   ",
        8: "*   * ",
        9: "*    ",
    }
    alphabet = {
        "A": [1, 2, 4, 3, 3],
        "B": [5, 3, 5, 3, 5],
        "C": [4, 9, 9, 9, 4],
        "D": [5, 3, 3, 3, 5],
        "E": [4, 9, 4, 9, 4],
    }
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big("d")  # Up to letter "E"

###################################################################################################################################################

from functools import reduce
import math
import string
import numpy


def vol(rad):
    return 4 / 3 * math.pi * (rad ** 3)


def ran_check(num, low, high):
    if num >= low and num <= high:
        return f"{num} is in the range between {low} and {high}"


def ran_bool(num, low, high):
    return num >= low and num <= high


def up_low(s):
    upper_char = 0
    lower_char = 0

    for char in s:
        if char.isupper():
            upper_char += 1
        elif char.islower():
            lower_char += 1
        else:
            pass

    return f"No. of Upper case characters : {upper_char} \n No. of Upper case characters : {lower_char}"


def unique_list(a_list):
    return set(a_list)


def multiply(numbers):
    return reduce(lambda num1, num2: num1 * num2, numbers)


def multiply2(numbers):
    return numpy.prod(numpy.array(numbers))


def palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]


def ispangram(str1, alphabet=string.ascii_lowercase):
    return len(alphabet) == len("".join(set(str1.lower().replace(" ", ""))))


print(f"{vol(2):.5f}")
print(ran_check(5, 2, 7))
print(ran_bool(3, 1, 10))
print(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))
print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
print(multiply([1, 2, 3, -4]))
print(multiply2([1, 2, 3, -4]))
print("palindrome:", palindrome("helleh"))
print("palindrome:", palindrome("nurses run"))
print("palindrome:", palindrome("abcba"))
print("ispangram:", ispangram("The quick brown fox jumps over the lazy dog"))

