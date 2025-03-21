#Ask user to input statement.
statement = input("Enter a complete statement: ")

#separate words in the statement
words = statement.split()

#count number of words
word_count = len(words)

#print output
print("Word count:", word_count)
