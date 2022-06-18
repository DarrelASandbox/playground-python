# Dictionaries: Objects retrieved by key name.
# - Unordered and cannot be sorted.
# Lists: Objects retrieved by location.
# - Ordered sequence can be indexed or slice.

fruits = {"apple": 12.50, "orange": 4.6}
ugly = {"u1": [0, 1, 2], "u2": {"omg": "why"}}
ugly["u3"] = "appended"
ugly["u3"] = "overwrite appended"

print(fruits["apple"])
print(ugly["u1"][2])
print(ugly["u2"]["omg"].upper())
print(ugly)
print(ugly.keys())
print(ugly.values())
print(ugly.items())

