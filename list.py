list = ["StRiNG", 100, 23.2]
list2 = ["list2", "chickens", 123.123192734]
list3 = list + list2
list2[0] = "list2342"
list3.append("mutated")
list4 = ["a", "x", "v", "f"]
list4.sort()

print(len(list))
print(list[0])
print(list[1:])
print(list3)
print(list2)
print(list3) 
print(list4)
