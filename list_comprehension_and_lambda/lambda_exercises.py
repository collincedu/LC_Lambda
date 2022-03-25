''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
from unittest import result

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers from said list:")
even_list = list(filter(lambda num: num%2 == 0, original_list))
print(even_list)
print("Odd numbers from said list:")
odd_list = list(filter(lambda num: num%2 == 1, original_list))
print(odd_list)

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print("Days of the week with 6 characters")
six_char = list(filter(lambda day: len(day) == 6, weekdays))
print(six_char)







''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
def remove_words(list1, remove_words):
    result = list(filter(lambda word: word not in remove_words, list1))
    return result
        
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_colors = ['orange','black']
print("Original list:")
print(colors)
print("\nRemove words:")
print(remove_colors)
print("\nAfter removing the specified words from the said list:")
print(remove_words(colors, remove_colors))




''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

def remove_elements(list1,list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result 

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

print("Original lists:")
print(list1)
print(list2)
print("\nRemoved all elements from list1 present in list2")
print(remove_elements(list1,list2))



''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
def search_substr(str, sub_str):
    result = list(filter(lambda i: sub_str in i, str))
    return result






''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''







''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
