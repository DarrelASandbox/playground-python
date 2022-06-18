set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)
set2 = {1, 4, 5}
set3 = {7, 8, 9}

print("set1:", set1, "set2:", set2, "\n")

print("set1.difference(set2):", set1.difference(set2))
set1.add(1)
set1.add(2)
print("set1:", set1, "set2:", set2, "\n")

set1.difference_update(set2)  # returns set1 after removing elements found in set2
print("set1.difference_update(set2): set1:", set1, "set2: ", set2)
set1.discard(2)
print("discard: set1:", set1, "set2:", set2, "\n")

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
# Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)
set1.intersection_update(set2)
print("set1.intersection_update(set2): set1:", set1, "set2: ", set2, "\n")

# Return True if two sets have a null intersection.
print("set1.isdisjoint(set2):", set1.isdisjoint(set2))
print("set1.isdisjoint(set3 ):", set1.isdisjoint(set3), "\n")

print("set1:", set1, "set2:", set2, "set3:", set3)
# Return whether another set contains this set.
print("set1.issubset(set2):", set1.issubset(set2))
# Return whether this set contains another set.
print("set1.issuperset(set2):", set1.issuperset(set2))

# Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)
print("set1.symmetric_difference(set2):", set1.symmetric_difference(set2))
# Returns the union of two sets (i.e. all elements that are in either set.)
print("set1.union(set2):", set1.union(set2))
# Update a set with the union of itself and others.
set1.update(set2)
print("set1.update(set2): set1:", set1, "set2:", set2, "set3:", set3)
