#1 Create a 2-D array and slice out the second number in the second column
#2D Array
_2DArray = [[1,2], [3,4]]
_2DArray[1].pop(1)
print(_2DArray)



#2 Write a python program to sort array element in the ascending/descending order
fruits = ["a","f","z","s"]
fruits.sort()
# print(fruits)
print("ascending order is {}".format(fruits))
fruits.sort(reverse = True)
print("descending order is {}".format(fruits))


# #3 Write a python program to find the maximum and minimum value in a given 2-D array
my2DArray = [[1,3,5], [4,8,12]]
minimum = min(my2DArray)
SamMinValue = min(minimum)
print("The minumum of {} is {}".format(my2DArray,SamMinValue))

maximum = max(my2DArray)
EstherMax = max(maximum)
print("The maximum of {} is {}".format(my2DArray,EstherMax))

#4 Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on 
# following criteria
# # percentage less than 50 (Grade C)
# # percentage equal to 50 and less than 80 (Grade B)
# # percentage equal to 80 and more than 80 (Grade A)


# print(my_list)

def total(my_list):
    return sum(my_list)/5

def grade(avg):
    if avg < 50:
        print("Grade C")
    elif avg == 50 and avg < 80:
        print("grade B")

    elif avg >= 80:
        print("grade A")
    else:
            return ("invalid input")
    

def main():
    marks = input("Please input the 5 subjets separated by a comma ")
    my_list = []
    my_list = marks.split(",")
    my_list = list(map(int,my_list))

    avg = total(my_list)
    grade(avg)

if __name__ == '__main__':
    main()

# 5 Write a python program to fetch only Email ID from text file which include following fields -:
#         Name
#         Mobile Number
#         Roll Number
#         Email ID


import re
fileToRead = 'readText.txt'
fileToWrite = 'emailExtracted.txt'
delimiterInFile = [',', ';']
def validateEmail(strEmail):
    # .* Zero or more characters of any type. 
    if re.match("(.*)@(.*).(.*)", strEmail):
        return True
    return False
def writeFile(listData):
    file = open(fileToWrite, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)
listEmail = []
file = open(fileToRead, 'r') 
listLine = file.readlines()
for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()
    for word in wordList:
        if(validateEmail(word)):
            listEmail.append(word)
if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail),"emails collected!")
    writeFile(uniqEmail)
else:
    print("No email found.")

#6. Write a function for checking the speed of drivers. This function should have one parameter: speed.
#         If speed is less than 70, it should print “Ok”.
#         Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
#         If the driver gets more than 12 points, the function should print: “License suspended”

def check_speed(speed):
    if speed <= 70:
        return 'Ok'
    elif speed >= 70:
        points = (speed - 70) // 5
        print('points = {}'.format(points))
        if points >= 12:
            return 'License suspended'
check_speed(80)
points = 2

# 7. Write a function called show_stars(rows). If rows is 5, it should print the following:

# *
# **
# ***
# ****
# *****


from ast import Break


rows = int(input('Enter the number of rows: '))
for i in range(rows):
    for j in range(i):
        print('*', end=' ')
    print('')
    print('\r')


#8. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers =[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        numbers.append(str(x))
print (','.join(numbers))

#9. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)

#10. Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

#11. Write a function to compute 5/0 and use try/except to catch the exceptions.

def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')

# 12. Create a nesting list that prints out the color and the car brand?
class car:
    def __init__(self, prize, color):
        self.prize = prize
        self.color = color

class cars:
    def __init__(self, list_of_cars):
        for one_car in list_of_cars:
            assert isinstance(one_car, car) # ensure you are only given cars
        self.my_cars = list_of_cars

    @property
    def prize(self):
        return [one_car.prize for one_car in self.my_cars]

    @property
    def color(self):
        return [one_car.color for one_car in self.my_cars]


a = car('prize1', 'red')
b = car('prize2', 'green')
c = car('prize3', 'azure')
cars = cars([a,b,c])
cars.prize
['prize1', 'prize2', 'prize3']
cars.color
['red', 'green', 'azure']

# 13. Create Bonus Question: Algorithm challenge: Create your own sorting algorithm?  
l = [[1,2],[2,3],[2,1]]
l.sort(key=lambda x: (x[1], -x[0]), reverse=True)
print(l)










