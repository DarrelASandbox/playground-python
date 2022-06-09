file = open("file.txt", "w")
string = "Hello\n"
multiple_strings = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing a string to file
file.write(string)

# Writing multiple strings at a time
file.writelines(multiple_strings)

# Closing file
file.close()

# Checking if the data is written to file or not
file = open("file.txt", "r")
print(file.read())
file.close()
