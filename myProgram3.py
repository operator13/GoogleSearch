

print("Hello World!")
print("I am now a Python Language Coder!")
print("This is my second simple program!")
print("I love the simplicity of Python")
print("I will display whatever is here in quotes such as owyhen2589gdbnzo82")

num1=4
num2=5
sum=num1+num2
print(sum)


# The output should be 54

num1 = 43
num2 = 11

sum = num1 + num2

print(sum)

num1 = 101
num2 = 66
sum = num1 + num2
print(sum)

num1 = 9
num2 = 19
sum = num1 + num2
print(sum)

_scri=75
sc_r=9
sscr2=13
Scr=18

str='Going Deep!'
print (str)                     #Prints a complete string
print (str[0])                  #Prints first character of the string
print (str[3:6])                #Prints characters starting from the fourth to seventh
print (str[3:])                 #Prints string starting from the fourth character
print (str*3)                   #Prints string three times
print (str + "I love Python")   #Prints concatenated string
str='I think I am now a Programmer.'
print(str)                      #Prints a complete string
print(str[1:5])                 #Prints characters of the string from the second character to the sixth
print (str*2)                   #Print statment 2 times
print (str + ' of Python')      #Print statement concatenating at the end the statement " of Python"

#Statments in Python

#Assignment statements
number1=18
number2=21

#Multi-line Python Statement (Explicit Line)
sum=3+6+7+\
    9+1+3+11+4+8
print(sum)

sum=(3+6+7+
    9+1+3+
     11+4+8)
print(sum)


total = 2+9+6+8\
    +2+5+1+14+5+21+26+4+7+13+31+24

print(total)

count=(13+1+56+3+7+9+5+
       12+54+4+7+45+71+4+8+5)

print(count)

employee1 = 25; employee2 = 45; employee3 = 32;
employee4 = 43

print(employee1+employee2+employee3+employee4)

#Indentation in Python


#Comments Examples

number1 = 45
number2 = 12

print(number1+number2)


employee1 = 'Daisy'
employee2 = 'Richard'

print(employee1)
print(employee2)

yvonee = 235
ian = 782
james = 1235
juliet = 568

print(yvonee)
print(ian)
print(james)
print(juliet)


student1_age=23  #This is the age of the first student
student2_age=19  #This is the age of the student

sotal_age = student1_age + student2_age

print(sotal_age)


#Arithmetic Operators

#Difference
number1 = 35
number2 = 12
difference = number2 - number1
print(difference)

#Multiplication
number1 = 2
number2 = 15

product = number1 * number2

print(product)

#Division
number1 = 10
number2 = 50

division = number2/number1

print(division)

#Modulus
number1 = 2
number2 = 15

remainder = number2%number1

print(remainder)


#Squaring and Cubing in Python
#Squaring a number - number**2
#Cubing a number - number**3

number=3
square=number**2
print(square)

number=5
cube=number**3
print(cube)

number = 7
print(number**7)

number=15
print(number**2)

number=6
print(number**3)

number=11
print(number**2)

number = 8
print(number**3)

number=13
print(number**2)

#Operators with string in Python
status = "I am happy I know" + "how to write programs in Python"
print(status)

#Python Multiplication of a string to create a sequence
many_words='Great Programmer' * 5
print(many_words)

str1 = 'I have realized '
str2 = 'that programming is a passion '
str3 = 'dedication and frequent practice'
print(str1+str2+str3)

str1 = 'Happy'
print(str1*10)

#Data Types in Python

#type() is used to determine the variable class
#instance() is invoked to a make a determination of which class function originates from

number=6
print(type(number))                       #should output class int
print(type(6.0))                          #should output class float
complex_num=7+5j
print(complex_num+5)                      #should out 12+5j
print(isinstance(complex_num, int))       #should output False
print(isinstance(complex_num, complex))   #should output true

#Number Conversion
#Programmers often need to convert decimal numbers in octal, hexadecimal and binary forms.

#Number System                 Prefix
#Octal                         'oO' or 'oo'
#Binary                        'oB' or 'ob'
#Hexadecimal                   'oX' or 'ox'

print(0b1010101)                        #Output:85
print(0x7B+0b0101)                      #Output:128 (123+5)
print(0o1306)                           #Output:710
print(0x7f841c81602)

print(0b1010101)

#Type Conversion
print(int(5.3))                         #Output: 5
print(int(5.9))                         #Output: 5

print(float(6))                         #Output: 6
print(complex('4+2j'))                  #Output: 4+2j

print(int(4.1))
print(int(4.7))
print(int(13.3))
print(int(13.9))

print(float(7))
print(float(16))
print(float(19))


(1.2+2.1) == 3.3                       #Will return True because 1.2+2.1 = 3.3
print((1.2+2.1) == 3.3)

import random

import math

print(math.pi)                          #output:3.14159
print(math.cos(math.pi))                #output: will be -1.0
print(math.exp(10))                     #output: will be 22026.4
print(math.sqrt(34))                    #output: 5.830951894845301
print(math.log(1010000))                #output: 13.825460888817442
print(math.cos(45)*math.sin(90))        #output: 0.4696361053190599
print(math.exp(20))                     #output: 485165195.4097903


list = [20, 16, 10, 5];
random.shuffle(list)


y=['f','g','h','m']
random.shuffle(y)
print(random.choice,y)
random.choice(y)
# print(y)


#print(random.shuffle(11,21))

#print(random.)

#Lists in Python
list_mine=[]                           #empty list
list_mine=[2,5.8]                      #list of integers
list_mine=[5,'Happy',5.2]              #list having mixed data



list_mine=['Best',26,89,3.9]

print(list_mine[0])
print(list_mine[1])
print(list_mine[2])
print(list_mine[3])


#Nested List
list_mine = ['carrot',[9,3,6],['g']]

list_mine = [[36,2,1],'Writer','t',[3.0,2.5]]

print(list_mine)            #Output: [[36,2,1],'Writer','t',[3.0,2.5]]
print(list_mine[0])         #Output: [36,2,1]
print(list_mine[0][1])      #Output: 2
print(list_mine[1])         #Output: Writer
print(list_mine[2])         #Output: t
print(list_mine[3])         #Output: [3.0, 2.5]

list_mine=['b','e','s','t']

print(list_mine[0])
print(list_mine[1])
print(list_mine[2])
print(list_mine[3])


your_collection = ['t','k','v','w','z','n','f']

print(your_collection[1])


print(your_collection[5])
print(your_collection[6])

your_collection[6]=your_collection[5]
print(your_collection[6])

nested_list=['Best',[4,7,2,9]]
print(nested_list[0][1])

list_mine=['c','h','a','n','g','e','s']

print(list_mine[-1])     #Output is s

print(list_mine[-4])     #Output is n

#Slicing Operator (Full Colon) is used to access a range of elements in a list

list_mine=['c','h','a','n','g','e','s']
print(list_mine[3:5])         #Picking elements from the 4 to the 6th

print(list_mine[:7])          #Output ['c', 'h', 'a', 'n', 'g', 'e', 's']
print(list_mine[:1])          #Output ['c']
print(list_mine[:2])          #Output ['c', 'h']
print(list_mine[:-6])         #Output ['c']
print(list_mine[2:])          #Output ['a', 'n', 'g', 'e', 's']
print(list_mine[3:])          #Output ['n', 'g', 'e', 's']
print(list_mine[:-1])         #Output ['c', 'h', 'a', 'n', 'g', 'e']
print(list_mine[:-2])         #Output ['c', 'h', 'a', 'n', 'g']


class_names = ['John','Kelly','Yvonne','Una','Lovy','Pius','Tracy']
print(class_names[2:])        #Displays 2nd student and the rest
print(class_names[:-4])       #Display 1st student to the 3rd
print(class_names[3:-2])      #Display 4th and 5th student only

#Manipulating Elements in a list using the assignment operator
list_yours=[4,8,5,2,1]

list_yours[1]=6
print(list_yours)             #Output: [4, 6, 5, 2, 1]

#Changing a range of items in a list

print(list_yours[0:3])           #Output: [4, 6, 5]
list_yours[0:3]=[12,11,10]       #Will change first item to fourth item in the list [12, 11, 10, 2, 1]
print(list_yours)                #Output: [12, 11, 10, 2, 1]

#Appending/Extending items in the list
list_yours=[4,6,5]
list_yours.append(3)
print(list_yours)                #The output will be [4, 6, 5, 3]

list_yours = [4,6,5]

list_yours.extend([13,7,9])
print(list_yours)               #Output will be [4, 6, 5, 13, 7, 9]

#The plus operator(+) can also be used to combine two lists.  The * operator can be used to perform iteration of a list given severally

list_yours=[4,6,5]
print(list_yours+[13,7,9])      #Output:[4,6,5,13,7,9]

print(['Happy']*4)              #Output: ['Happy', 'Happy', 'Happy', 'Happy']

#Removing or Deleting Items from a list

list_mine=['t','r','o','g','r','a','m']

print(list_mine)               #Output: ['t','r','o','g','r','a','m']
del list_mine[1]
print(list_mine)               #Output: ['t','o','g','r','a','m']

#Deleting Multiple Elements

del list_mine[0:3]             #Removes ['t','o','g']
print(list_mine)               #Output ['r', 'a', 'm']

# delete list_mine
# print(list_mine)

list_mine=['t','k','b','d','w','q','v']
list_mine.remove('t')
print(list_mine)               #Output: ['k', 'b', 'd', 'w', 'q', 'v']

list_mine=['t','k','b','d','w','q','v']
print(list_mine.pop(1))        #Output: k

print(list_mine.pop())         #Output: v (Last location)

list_yours=['K','N','O','C','K','E','D']
list1=(list_yours.pop(3))       #Output: C
print(list_yours)

list_yours=['K','N','O','C','K','E','D']
list_yours.remove('C')       #Output: C
print(list_yours)

list_yours=['K','N','O','C','K','E','D']
list3=(list_yours.pop(2))       #Output: O
print(list_yours)
print(list3)

list_yours=['K','N','O','C','K','E','D']
list4=(list_yours.pop())       #Output: D
print(list_yours)
print(list4)


list_mine=['t','k','b','d','w','q','v']

print(list_mine[1:4])          #Output: ['k', 'b', 'd']
print(list_mine[2:4])          #Output: ['b', 'd']
print(list_mine[3:4])          #Output: ['d']
print(list_mine[4:4])          #Output: []
print(list_mine[1:2])          #Output: ['k']
#list_mine=[1:2]=[]
print(list_mine)


#Reverse Order

x =[4,9,2,1,6,7]
print(x)

for i in reversed(x):
      print(i)   #Output: 7,6,1,2,9,4

c =[4,9,2,1,6,7]
x = len(c)
#print(x)
#print(len(c))
c.reverse()
print(c)

cars=['bmw','audi','toyota','subaru']
print(len(cars))

# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
#
# x = len(points)
# print(x)

c =[4,9,2,1,6,7]
c.sort()         #1st option to sort
x = sorted(c)    #2nd option to sort
print(c)
print(x)
print(sorted(c))                 #3rd option to sort

#Sort function
cities = ['chicago','paris','new york','tokyo','baghdad','orlando','houston','hong kong']

x = sorted(cities)
print(x)                              #Output: ['baghdad', 'chicago', 'hong kong', 'houston', 'new york', 'orlando', 'paris', 'tokyo']
print(cities)                         #Output: ['chicago', 'paris', 'new york', 'tokyo', 'baghdad', 'orlando', 'houston', 'hong kong']

#Reverse alphabetical order

x = sorted(cities, reverse=True)
print(x)                              #Output: ['tokyo', 'paris', 'orlando', 'new york', 'houston', 'hong kong', 'chicago', 'baghdad']
print(sorted(cities, reverse=True))   #Output: ['tokyo', 'paris', 'orlando', 'new york', 'houston', 'hong kong', 'chicago', 'baghdad']
print(cities)                         #Output: ['chicago', 'paris', 'new york', 'tokyo', 'baghdad', 'orlando', 'houston', 'hong kong']

cities.reverse()
print(cities)                         #Output: ['hong kong', 'houston', 'orlando', 'baghdad', 'tokyo', 'new york', 'paris', 'chicago']

cities.sort()
print(cities)                         #Output: ['baghdad', 'chicago', 'hong kong', 'houston', 'new york', 'orlando', 'paris', 'tokyo']

cities.sort(reverse=True)
print(cities)                         #Output: ['tokyo', 'paris', 'orlando', 'new york', 'houston', 'hong kong', 'chicago', 'baghdad']

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)                                           #Output: ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)                                           #Output: ['honda', 'yamaha', 'suzuki']

print("\nA " + too_expensive + " is too expensive for me")   #Output: A ducati is too expensive for me

#POP

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(len(motorcycles))


#Tuple in Python
#Tuple is like a list but cannot change elements in a tuple

tuple_mine=(21,12,31)
print(tuple_mine)

tuple_mine=(31,'Green',4.7)
print(tuple_mine)

tuple_mine=['t','r','o','g','r','a','m']
print(tuple_mine[1])         #Output: r

print(tuple_mine[3])         #Output: g

print(tuple_mine[-2])        #Output: a

#Slicing tuple
#            0   1   2   3   4   5   6
tuple_mine=['t','r','o','g','r','a','m']
print(tuple_mine[2:5])       #Output: ['o', 'g', 'r']
print(tuple_mine[:4])        #Output: ['t', 'r', 'o', 'g']
print(tuple_mine[:-4])       #Output: ['t', 'r', 'o']
print(tuple_mine[:-1])       #Output: ['t', 'r', 'o', 'g', 'r', 'a']
print(tuple_mine[:-5])       #Output: ['t', 'r']
print(tuple_mine[3:5])       #Output: ['g', 'r']
print(tuple_mine[1:5])       #Output: ['r', 'o', 'g', 'r']


magicians = ['Alice','David','Carolina']
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

pizzas = ['sausage pizza','pepperoni pizza','deep dish pizza','mushroom pizza','vegetable pizza','cheese pizza']
for pizza in pizzas:
    print("I like " + pizza.title())
print("I really love pizza!")

animals = ['horse','dog','cat','buffalo','lion','tiger','deer','pig','cow']
for animal in animals:
    print("\n A " + animal.title() + " would make a great pet")
print("\nAny of these animals would make a great pet")

