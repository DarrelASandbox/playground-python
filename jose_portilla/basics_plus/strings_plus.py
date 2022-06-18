string = "hello world"
print('Number of "o":', string.count("o"))
print('First "o" is at index:', string.find("o"))
print("center:", string.center(15, "x").center(17, "X"))
print('"hello world" is alpha numeric?', string.isalnum())
print('"helloworld" is alpha numeric?', "helloworld".isalnum())
print("isspace:", string.isspace())
print("istitle:", string.istitle())
print('endswith "d":', string.endswith("d"))
print('split "o":', string.split("o"))  # Every instance
print('partition "o":', string.partition("o"))  # First instance
