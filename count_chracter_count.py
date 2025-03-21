#Ask user to input name.
fullname = input("Enter full name: ")

#remove space
fullname_no_space = fullname.replace(" ", "")

#count number of characters
characters_count = len(fullname_no_space)

#print output.
print(characters_count)