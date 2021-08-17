# append to file
temp = open("test.txt", "a")

temp.write("ha, nerd\n")
temp.write("nice code bro\n")
temp.write("what else can I write")

temp.close()

# open file as read only
test_file = open("test.txt", "r")

# can you read the file
print(test_file.readable())
# read the whole file
print(test_file.read())
# read individual line
print(test_file.readline())
# read every line into an array
print(test_file.readlines())

test_file.close()
