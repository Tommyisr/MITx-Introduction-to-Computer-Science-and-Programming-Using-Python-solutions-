#Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc

current_index = 0
result_index = -1
max_length = 0
length = 1

string = input("Please, enter a string: ")
for i in range(0,len(string)):
    if i>0 and string[i] >= string[i-1]:
        length+=1

    else:
        current_index = i
        length = 1

    if length > max_length:
        result_index = current_index
        max_length = length



print("Longest substring in alphabetical order is: ",string[result_index:result_index+max_length])
