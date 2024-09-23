# print("Hello, World!")
# print(23)
# print("23+8")


# a, b = 1, 2.0
# sum = a + b
# print(sum)


# a, b = 1, "5"
# c = int(b)
# sum = a + c
# sub = a - c
# print("sum is =",sum, "and subtraction is =", sub)


# # Write a Program to input 2 numbers & print their sum.
# print("enter first number")
# a=input()
# print("enter second number")
# b=input()
# sum = a + b
# print("sum is =",sum)


# # WAP to input side of a square & print its area.
# a=int(input("enter the side of the square = "))
# area = a**2
# area1 = pow(a,2)
# print("Area of the square =",area,area1)

# # WAP to input 2 floating point numbers & print their average.
# input1=float(input("Enter 1st floating point number = "))
# input2=float(input("Enter 2nd floating point number = "))
# average = (input1+input2)/2
# print("Average = ",average)

# # WAP to input 2 int numbers, a and b.
# # Print True if a is greater than or equal to b. If not print False.
# a = int(input("Enter 1st integer number, a = "))
# b = int(input("Enter 2nd integer number, b = "))
# if a>b:
#     print("True: a is greater than b")
# elif a<b: #why a=b is giving error
#     print("False: a is neither greater nor equal to b")
# else:
#     print("True: a is equal than b")


# for i in range(11):
#     print(i)

# # looping through a list
# numbers = [1,2,3,4,5]

# for number in numbers:
#   print(number)

# my_string = "Hello Future Data Scientist!"

# for letter in my_string:
#     print(letter)

# # Python Nested Loops
# lists = [[1,2,3], [4,5,6], [7,8,9]]

# for lst in lists:
#     for item in lst:
#         print(item)


# str_var = "Data scientists don't just build models; they build solutions"
# list_var=['Harry potter','Hermione','Ron']
# tupple_var=('Harry potter','Hermione','Ron')
# print(type(str_var))
# print(type(list_var))
# print(type(tupple_var))


# my_dict = {'name':'John', 'age':25}
# my_dict2 = {1:'a', 2:'b', 3:'c'}
# my_dict3 = {'fruits':['apple', 'banana', 'mango'], 'vegetables':['carrot', 'potato', 'cucumber']}
# print(type(my_dict3))


# # boolean
# x = True
# y = False
# if x:
#     print("x is True!")
# else:
#     print("x is False!")


# sort the list
list1 = [5,7,9,4,2,1]
sorting = list1.sort()
print(sorting)
print(list1)

# Change Dictionary Items
country_capitals = {
  "Germany": "Berlin", 
  "Italy": "Naples", 
  "England": "Londonn"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)

# Changes after setup remote repo
def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')