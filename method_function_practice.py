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
