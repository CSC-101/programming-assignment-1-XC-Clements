import data

# Write your functions for each part in the space below.

# Part 1
print("Part 1")
#creates a set of all of the vowels that we can check off of
vowels = {"A","E","I","O","U","a","e","i","o","u"}

#creates a function that takes an input string, and outputs a count of the number of vowels in it
def vowel_count(input_string:str) -> int:
    #creates a temporary count variable to keep track of
    count = 0
    #converts the input into a list of each character, and iterates through each character
    for n in list(input_string):
        #checks if the current character is in the vowel set, and if it is, increases the count
        if n in vowels:
            count += 1
    #finally returns the total value after iterating through the whole prompt
    return count

print(vowel_count("asdflgl;.kjkl"))

# Part 2
print("Part 2")
#this is just what we're testing -- i could take input but it would be too tedious for the rest
temp_lists = [[12, 16], [4], [72, 90, 98], [14, 155]]
#creates a function short_lists that takes an input of a list of lists of ints, and returns a list
def short_lists(input_list:list[list[int]]) -> list:
    #creates a temp output variable list
    output = []
    #iterates through the list of lists
    for n in input_list:
        #if the length of each sub-list is 2, then adds the sublist to the output
        if len(n) == 2:
            output.append(n)
    #returns the resulting list
    return output

print(short_lists(temp_lists))


# Part 3


# Part 4


# Part 5


# Part 6


# Part 7


# Part 8


