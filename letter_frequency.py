""" Letter frequency

Analysing the frequency of letters in a string using loops and lists.

You are required to use the trinket IDE below to create a program that determines the frequency of specific letters in a string.
This is a coding exercise that is often given during coding interviews, and so a very useful one to master..
Frequency analysis is the study of the frequency of letters or combination of letters in encrypted text.
Frequency analysis is based on the fact that in a particular language, certain letters, and groups of letters, appear with essentially the same frequency in almost all text.
For example 'A' is a relatively common letter in the English language while 'Z' is less common.
For this challenge, create a program that determines the number of occurrences of each letter in the quote
"You can have data without information, but you cannot have information without data.", and output a list with each letter and its frequency.
For this task, you will also need to remember what you’ve learned about lists, as well as some additional understanding of a concept not previously discussed in this trial: for loops.
Remember that a list is an ordered sequence of elements that can be modified or changed.
Each element inside of a list is called an item.
Lists enable you to keep similar data together, condense your code, and perform the same methods and operations on multiple values at once.
In Python, lists are created by placing items, separated by commas, between square brackets[].
Lists work similarly to strings
you use square brackets[] to access data and the first element has an index of 0.
The values or items in a list can be strings, integers, floats, other lists or a mix of different types.
Create a variable to store the given string "You can have data without information, but you cannot have information without data."
Convert the given string to lowercase
Create a list containing every lowercase letter of the English alphabet

For every letter in the alphabet list:
    Create a variable to store the frequency of each letter in the string and assign it an initial value of zero
    for every letter in the given string:
        if the letter in the string is the same as the letter in the alphabet list
            increase the value of the frequency variable by one.
    if the value of the frequency variable does not equal zero:
        print the letter in the alphabet list followed by a colon and the value of the frequency variable


 """


# Built-in module, needs to be placed at the top. This function split the specified string into words using str.
import string
# Create a variable to store the string
theSentence = "You can have data without information, but you cannot have information without data."

# Convert the given string to lowercase
theSentence = theSentence.lower()
print(theSentence)

# populate list with the alphabet using the string module - no need to create a list with the entire alphabet
# The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.
myList = list(string.ascii_lowercase)
print(myList)

# declare a dictionary to store the frequency of each letter
frequencyDict = dict()

# initialize the dictionary with zeros
# Create a list containing every lowercase letter of the English alphabet with an initila value = 0
for x in range(len(myList)):
    frequencyDict[myList[x]] = 0

# parse mySentence, one letter at a time - the Parse function enables the user to parse the data in one field in the source file and write the "parts" of the data to a field or fields in the target file.
for char in theSentence:
    # increment the frequency if the letter matches
    if char in myList:
        frequencyDict[char] += 1  # increment

# print the results
for letter in myList:
    # only show letters that were used
    if frequencyDict[letter] != 0:
        print(letter + ":" + str(frequencyDict[letter]))
