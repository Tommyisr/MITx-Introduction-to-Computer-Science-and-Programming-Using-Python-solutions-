# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

substring = 'bob'
string = input("Please, enter a string: ")
index = 0
count = 0
it = 0
i = 0
match = 0
for it in range(len(string)):
    for i in range(len(substring)):
        if it+i < len(string) and string[it+i] == substring[index]:
            match += 1
        index += 1

    if match == len(substring):
        count +=1
    it += 1
    match = 0
    index = 0


print("Number of times bob occurs is: ", count)