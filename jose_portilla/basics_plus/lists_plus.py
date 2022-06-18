def flatten(x):
    if isinstance(x, list):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


list1 = [1, 2, 3]
list1.append(4)

print(list1)
print("list1.count(10):", list1.count(10))
print("list1.count(2):", list1.count(2), "\n")

list1.extend([5, 6])  # extends list by appending elements from the iterable:
print("extend:", list1)

list1.append([6, 7])  # appends whole object at end
print("append:", list1)

list1.insert(6, "inserted")  # This method places the object at the index supplied.
print("insert:", list1, "\n")

inserted = list1.pop(6)
print("pop:", inserted, "list1:", list1)

# Removes the first occurrence of a value.
removed = list1.remove(6)
print("remove returns:", removed, "list1:", list1, "\n")

list1.insert(1, 10)
list1 = flatten(list1)
print("flatten:", list1)
list1.sort()
print("sort:", list1)
list1.sort(reverse=True)
print("sort reverse:", list1)
list1.reverse()
print("reverse:", list1, "\n")

