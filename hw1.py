import data
from data import Price, Rectangle, Point, Book, Circle, Employee
from math import sqrt
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
temp_lists = [[16, 12], [4], [72, 90, 98], [14, 155]]
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
print("Part 3")
#creates a function ascending_pairs that takes a list of a list as
def ascending_pairs(input_list:list[list[int]]):
    #creates a temp output variable list
    output = []
    # iterates through the list of lists
    for n in input_list:
        # if the length of each sub-list is 2, then continues
        if len(n) == 2:
            #if the sublist is in order, append it
            if n[0] < n[1]:
                output.append(n)
            #if it isn't in order, fix it
            else:
                #fix the swapper
                t = n[0]
                n[0] = n[1]
                n[1] = t
                output.append(n)
        else:
            output.append(n)
    return output

print(ascending_pairs(temp_lists))

# Part 4
print("Part 4")

#defines the prices to add
newprice1 = Price(12, 80)
newprice2 = Price(8, 45)
#creates a function with 2 Price inputs that outputs a price
def add_prices(price1:Price, price2:Price) -> Price:
    #initializes an output price
    outputPrice = Price(0, 0)
    #adds the cents together and find the remainder from 100
    outputPrice.cents += (price1.cents + price2.cents) % 100
    #adds anything above 100 to dollars
    outputPrice.dollars += (price1.cents + price2.cents) // 100
    #adds dollars
    outputPrice.dollars += price1.dollars + price2.dollars
    return outputPrice

print(add_prices(newprice1, newprice2))

# Part 5
print("Part 5")
#creates a function that takes the input rectangle and returns its length
def length(inputRectangle:Rectangle) -> float:
    return inputRectangle.bottom_right.x - inputRectangle.top_left.x
#creates a function that takes the input rectangle and returns its height
def height(inputRectangle:Rectangle) -> float:
    return inputRectangle.top_left.y - inputRectangle.bottom_right.y
#creates a function that takes the input rectangle and multiplies its height and length
def rectangle_area(inputRectangle:Rectangle) -> float:
    return height(inputRectangle) * length(inputRectangle)

print(rectangle_area(Rectangle(Point(0,4),Point(4,0))))


# Part 6
print("Part 6")
#initializes a test list of books
inputBooks = [Book(["Charles Dickens"],"A Tale of Two Cities"),
              Book(["Mark Twain"], "Huckleberry Finn"),
              Book(["C.S. Lewis"],"The Chronicles of Narnia"),
              Book(["Mark Twain", "Charles Dickens"],"A Tale of Finn"),
              Book(["Mark Twain", "C.S. Lewis"], "Huckleberry Narnia"),
              Book(["Charles Dickens", "C.S. Lewis"], "The Chronicles of City")]

#creates a function that takes an author and list of books and returns all the books they are
# an author in
def books_by_author(inputAuthor:str, inputList:list[Book]) -> list[Book]:
    outputList = []
    for n in inputList:
        for x in n.authors:
            if x == inputAuthor:
                outputList.append(n)
    return outputList

print(books_by_author("Mark Twain", inputBooks))
print(books_by_author("Tom Sawyer", inputBooks))


# Part 7
print("Part 7")
#creates a function that takes an input rectangle and finds the length of the hypotenuse
def hypotenuse(inputRectangle:Rectangle) -> float:
    return sqrt(
        inputRectangle.bottom_right.x - inputRectangle.top_left.x +
        inputRectangle.top_left.y - inputRectangle.bottom_right.y
    )
#creates a function that takes an input rectangle and returns a resulting bounding circle
def circle_bound(inputRectangle:Rectangle) -> Circle:
    outputCircle = Circle(Point(0,0),0)
    #creates the output circle's center
    outputCircle.center.x = (inputRectangle.top_left.x + (length(inputRectangle) / 2))
    outputCircle.center.y = (inputRectangle.bottom_right.y + (height(inputRectangle) / 2))
    #finds the circle's radius using the hypotenuse
    outputCircle.radius = hypotenuse(inputRectangle) / 2
    return outputCircle

print(circle_bound(Rectangle(Point(0,4), Point(4, 0))))

# Part 8
print("Part 8!!!")
#initializes a test employee List with wages
employeeList = [Employee("Tom", 12),
                Employee("Jeff", 13),
                Employee("Timothy", 12),
                Employee("Wanda", 4)]
#creates a function that takes an input of a list of employees and returns a
# list of the underpaid workers
def below_pay_average(inputEmployeeList:list[Employee]) -> list[str]:
    #initializes the list of underpaid workers
    underpaidWorkers = []
    #calculates the wage average
    avgWage = 0
    for n in inputEmployeeList:
        avgWage += n.pay_rate
    avgWage = avgWage / len(inputEmployeeList)
    #compares each person to the wage average, and adds them to the underpaid list if they are
    for n in inputEmployeeList:
        if n.pay_rate < avgWage:
            underpaidWorkers.append(n.name)
    return underpaidWorkers

print(below_pay_average(employeeList))
