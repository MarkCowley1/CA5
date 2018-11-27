# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:17:31 2018

@author: markcowley
"""
import functools, math # Will need these for map, reduce and math functions.
class Calculator(object): #Create class with instance variables
    def __init__(self):
        self.myList = []
        self.myInput = ''
        self.first = 0
        self.second = 0
        self.operator = ''
    def mainMenu(self): # MAin menu for user to create a list of numbers or use normal calculator.
        self.myInput = input("Type L to create a list of numbers or any other key for a normal calculator: ")
        if self.myInput.lower() == 'l':
            myNumber = input("Please enter the numbers you wish to add to your list. Add numbers one at a time, then press enter. Press 'F' when finished: ")
            while myNumber.lower() != 'f':#Breaks the loop when user is finished.
                try:
                    self.myList.append(float(myNumber))
                except ValueError:
                    print("Not Valid")
                myNumber = input("Please enter another number or press 'F' to quit:")
        elif self.myInput.lower() != 'l': #Breaks to here if user wants a normal calculator
            while True:
                try:
                    self.first = float(input("Please enter your first number: "))
                    break
                except ValueError: #Any non numbers will prompt the user to input their value again
                    print("Not a valid number")
        while True:
            self.operator = input("Please enter your operator: +/-/*/**/sin/cos/tan/cubed/sqrt: ") #choose your operator
            operatorList = ['tan', 'sin', 'cos', 'squared', 'cubed', 'sqrt', '+', '-', '/','*', '**' ]
            if self.operator.lower() in operatorList:
                break
            else:
                print("Sorry, this calculator doesn't support that operation.")
        secondNumOperator = ['+', '-', '/', '*'] #These are the operations that require a second number 
        if self.operator in secondNumOperator:
            while self.myInput.lower() != 'l':
                    try:
                        self.second = float(input("please enter your second number: "))
                        break
                    except ValueError: #Same error handling as before. Only except numbers.
                        print('Not a valid number')
        #print(self.myList)
    def add(self): #Here we define in the function is using a list of not.
        if self.myInput.lower() == 'l':
            return functools.reduce(lambda x, y: x+y, self.myList)
        else:
            return self.first + self.second
    def subtract(self):
        if self.myInput.lower() == '1':
            return functools.reduce(lambda x, y: x-y, self.myList)
        else:
            return self.first - self.second
    def multiply(self):
        if self.myInput.lower() == 'l':
            return functools.reduce(lambda x, y: x*y, self.myList)
        else:
            return self.first*self.second
    def division(self):
        if self.myInput.lower() == 'l':
            return functools.reduce(lambda x, y: x/y, self.myList)
        elif self.myInput.lower() != 'l' and self.second == 0:
            return 'Division by Zero Not Allowed'
    def power(self):
        if self.myInput.lower() == 'l':
            return list(map(lambda x: x**2, self.myList))
        else:
            return self.first**2
    def cube(self):
        if self.myInput.lower() == 'l':
            return list(map(lambda x: x**3, self.myList))
        else:
            return self.first**3
    def sqrt(self):
        if self.myInput.lower() =='l':
            return list(map(lambda x: x**0.5, self.myList))
        else:
            return self.first**0.5
    def sin(self):
        if self.myInput.lower() == 'l':
            return list(map(lambda x: math.sin(math.radians(x)), self.myList))
        else:
            return math.sin(math.radians(self.first))
    def cos(self):
        if self.myInput.lower() == 'l':
            return list(map(lambda x: math.cos(math.radians(x)), self.myList))
        else:
            return math.cos(math.radians(self.first))
    def tan(self):
        if self.myInput.lower() == 'l':
            return list(map(lambda x: math.tan(math.radians(x)), self.myList))
        else:
            return math.tan(math.radians(self.first))
    
    
    
    def output(self): #Operation defined by the user determines the output
        if self.operator == '+':
            print(self.add())
        elif self.operator == '-':
            print(self.subtract())
        elif self.operator == '/':
            print(self.division())
        elif self.operator == '*':
            print(self.multiply())
        elif self.operator == '**':
            print(self.power())
        elif self.operator.lower() == 'cube':
            print(self.cube())
        elif self.operator == 'sqrt':
            print(self.sqrt())
        elif self.operator == 'sin':
            print(self.sin())
        elif self.operator == 'cos':
            print(self.cos())
        elif self.operator == 'tan':
            print(self.tan())
if __name__ == '__main__':
    c = Calculator()
    c.mainMenu()
    c.output()
    
