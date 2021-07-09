# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

substring = 'bob'
string = input("Please, enter a string: ")
index = 0
count = 0
for i in range(0,len(string)):
    if string[i] == substring[index]: # string letter matches to substring letter
        if index == len(substring)-1: # all the letters from the substring were matched to the letters from the original string
            count+=1
            index=1
        else:
            index+=1 # case for 'bobob'
    else:
        index=0

print("Number of times bob occurs is: ", count)