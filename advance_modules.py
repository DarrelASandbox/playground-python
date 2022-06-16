# Print text header in cyan color
def print_header(string, output=""):
    print("\33[36m" + string + "\x1b[0m", output)


###################################################################################################################################################


from collections import Counter
from collections import defaultdict
from collections import namedtuple
from send2trash import send2trash

print_header("\nCounter:")
list1 = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 5]
print(Counter(list1))

sentence = "She sells sea shells by the sea shore The shells she sells are surely sea shells So if she sells shells on the sea shore Im sure she sells seashore shells"
counter = Counter(sentence.lower().split())
print(counter)
print(counter.most_common(5))
print(list(counter))


print_header("\ndefaultdict:")
dictionary = defaultdict(lambda: 0)
print("Incorrect key:", dictionary["Incorrect key"])


print_header("\nnamedtuple:")
Dog = namedtuple("Dog", ["age", "name", "breed"])
dog = Dog(age=5, name="Sammy", breed="Husky")
print(type(dog))
print(dog)
print(dog.age)


###################################################################################################################################################


import os
import shutil
import send2trash

file = open("shutil.txt", "w+")
file.write("Learning shutil module")
file.close()

print_header("\nos module:")
print("os.getcwd(): " + os.getcwd())
print("os.path.abspath(): " + os.path.abspath("./example_top_level"))
# print(os.listdir())
print(os.listdir(os.path.abspath("./example_top_level")))

shutil.move("shutil.txt", os.path.abspath("./example_top_level"))

send2trash.send2trash(os.path.abspath("./example_top_level/shutil.txt"))

print_header("\nos.walk:")
for folder, sub_folders, files in os.walk(os.path.abspath("./example_top_level")):
    print(f"\33[34mFolder Path: {folder}\n")
    print(f"\n\33[35m\tSubfolders: ")
    for sub_folder in sub_folders:
        print(f"\t  {sub_folder}")

    print(f"\n\t\33[32m\tFiles: ")
    for file in files:
        print(f"\t\t  {file}")
    print("\n\x1b[0m\t")


###################################################################################################################################################


import datetime

time = datetime.time(13, 30)
today = datetime.date.today()
age = datetime.date.today() - datetime.date(1993, 8, 6)

print_header("\ndatetime module:")
print(time)
print(today)
print(today.ctime())
print(datetime.datetime.now())
print(age)

print("Earliest  :", datetime.time.min)
print("Latest    :", datetime.time.max)
print("Resolution:", datetime.time.resolution)


###################################################################################################################################################


import math
import random

print_header("\nmath module:")
print("math.floor: ", math.floor(4.35))
print("math.ceil: ", math.ceil(4.35))
print("round: ", round(4.35), round(4.5), round(4.51), round(5.5))
print("math.pi: ", math.pi)
print("math.e: ", math.e)
print("math.inf: ", math.inf)
print("math.nan: ", math.nan)
print("math.log(math.e): ", math.log(math.e))
print("math.sin(10): ", math.sin(10))
print("math.degrees(math.pi / 2): ", math.degrees(math.pi / 2))
print("math.radians(180): ", math.radians(180))


list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Take a sample size, allowing picking elements more than once.
print_header("\nsample with replacement:")
print(random.choices(population=list1, k=10))

# Once an item has been randomly picked, it can't be picked again.
print_header("\nsample without replacement:" + "\x1b[0m")
print(random.sample(population=list1, k=10))

print_header("\nrandom.uniform(a=0, b=100):", random.uniform(a=0, b=100))
print_header("random.gauss(mu=0, sigma=1):", random.gauss(mu=0, sigma=1))

print_header("\nrandom.randint:", random.randint(0, 100))

random.seed(101)
print_header("random.seed:", random.randint(0, 100))

###################################################################################################################################################
###################################################################################################################################################
###################################################################################################################################################
###################################################################################################################################################
