file = open("test.txt", "r")
data = file.read()
occurrences = data.count("Python")
print('Number of occurrences of the word :', occurrences)
