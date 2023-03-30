# PPHA 30537
# Spring 2023
# Homework 1

# YOUR CANVAS NAME HERE: YIFAN WU
# YOUR GITHUB USER NAME HEREL: genie_god

# Due date: Sunday April 2nd before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

list_1 = ["a", "b", "c", "d"]
i = 0
for el in list_1:
    print("The value at positing %i is %s" % (i, el))
    i += 1

# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

list_2 = ["radar", "A man, a plan, a canal, Panama!", "Apple", "This isn't a palindrome"]

for sen in list_2:
    sen_mod = ""
    for l in sen:
        if l.isalpha():
            sen_mod += l.lower()
    print(sen_mod == sen_mod[::-1])


# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')
while True:
    print
    if choice.lower() in available_vegetables:
        print("you can have the vegetable!")
        break
    else:
        choice = input('Please pick a vegetable I have available: ')
    


# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".
list_4 = ["radar", "A man, a plan, a canal, Panama!", "Apple", "This isn't a palindrome", "banana"]
list_4_an = [sen.lower() for sen in list_4 if sen[0].lower() in ["a", "b"]]
print(list_4_an)

# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]
end_list = [num * 2 for num in start_list[::-1]]
print(end_list)


# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']


#dict_short_long = dict(zip(short_names, long_names))
#or

new_dict = {key:val for key, val in zip(short_names, long_names)}
print(new_dict)

