#list of numbers from 0 - 9
#space is the indication that we are doing separate parts in comprehension/blocks
import numbers


x = [i for i in range(10)]
print(x)

#adding an expression - square of each number
squares = [i**2 for i in range(10)]
print(squares)

#mult each element by 3
list1 = [3,4,5]
mult = [num*3 for num in list1]
print(mult)

#word manipulation --> indexing first letter of each word
listOfWords = ["this", "is", "a", "list", "of", "words"]
new_words = [word[0] for word in listOfWords]
print(new_words)

#list to lowercase
list1 = ['A', 'B', 'C']

lower = [letter.lower() for letter in list1]
print(lower)

upper = [letter.upper() for letter in list1]
print(upper)

# adding in an IF condition square of numbers 
# divisible by 2 with no remainder (evens)

new_range = [i * i for i in range(5) if i%2 == 0]
print(new_range)

# only words and only numbers
string = "Hello 12345 World"
number = [x for x in string if x.isdigit()]
letters = [x for x in string if x.isalpha()]
print(number)
print(letters)

# using a file : expression | iteration | condition
myfile = open('test.txt', 'r')
result = [i.rstrip("\n") for i in myfile if "line 3" in i]
print(result)

#using functions
def double(x):
    return x*2

print(double(10))

mynumbers = [double(x) for x in range(10)]
print(mynumbers)

#for even numbers only
mynumbers = [double(x) for x in range(10) if x%2 == 0]
print(mynumbers)

# You can add more than one argument
result = [x+y for x in [10,30,50] for y in [20,40,60]]
print(result)
