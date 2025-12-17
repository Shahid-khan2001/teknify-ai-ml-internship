# class student():
#     institute="jinnah"
#     def __init__(self,name,city,program,university):
#         self.name=name
#         self.city=city
#         self.program=program
#         self.university=university
#     def intro(self):
#         print("intoduce yourself")

# s1=student("hamza hanif","abbottabad","computer science","CUI atd.")
# s1.intro()
# print(f"My name is {s1.name}.\nI am from {s1.city} and doing {s1.program} from {s1.university} ")
# print(s1.institute)

#.........................
#create student class that take names and marks of 3 subjects as argument in 
#constructor. than create a method to print the average.
# class student():
#     def __init__ (self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=int(marks1)
#         self.marks2=int(marks2)
#         self.marks3=int(marks3)
#     def calc_average(self):
#         average =((self.marks1+self.marks2+self.marks3)/3)
#         print(f"{s1.name} :",average)
# s1 = student("hamza hanif",93,91,95)
# s1.calc_average()


#............................
#Create an account class with attributes balace and acc number.
#create method for credit, debit and print the balance
# class account():
#     def __init__ (self, balance, acc_number):
#         self.balance=balance
#         self.acc_number=acc_number

#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs", amount, " debited to your accout")
#         print("your total balance is", self.balance)

#     def debit(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#             print("Rs", amount, " debited from your account")
#             print("your remaining balance is ",self.balance)

#         else:
#             print("you dont have that much amout.\nyou you can only withdraw Rs",self.balance)



# shahidkhan=account(10000,123)
# print(shahidkhan.balance)
# # print(shahidkhan.acc_number)
# shahidkhan.credit(2500)
# shahidkhan.debit(13000)

#.................................
#del in python
# class student():
#     def __init__ (self,name):
#         self.name=name
# std1=student("shahid khan")
# print(std1)
# del std1
# print(std1)


#................................
#inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car is starting")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class Toyota(Car):
#     def __init__ (self,name):
#         self.name=name

# car1=Toyota("grandy")
# print(car1.name)
# car1.start()


#............................
#make a class to add imaginary numbers
# class Complex:
#     def __init__ (self,real,imag):
#         self.real=real
#         self.imag=imag
#     def shownumber(self):
#         print(self.real,"i","+", self.imag,"j")

#     def __add__(self,number):
#         self.rnumber=num1.real + num2.real
#         self.inumber=num1.imag + num2.imag
#         print(self.rnumber,"i",  "+" ,self.inumber,"j")

#     def __sub__(self,number):
#         self.rnumber=num1.real - num2.real
#         self.inumber=num1.imag - num2.imag
#         print(self.rnumber,"i",  "-" ,self.inumber,"j")
    
# num1=Complex(2,3)
# num1.shownumber()
# num2=Complex(4,5)
# num2.shownumber()
# num3=num1+num2
# print(num3)

#...............................
#creat a circle class to create a circle with radius r using constructor.
#Define an area() method of the class which calculates the area of the circle
#Define a pertimeter() method of the class which allows you to calculate the perimeter of the circle
# class circle:
#     def __init__ (self,radius):
#         self.radius=radius

#     def calc_area(self):
#         #area=3.14*r^2
#         # r^2 = self.radius *self.radius
#         pi=3.14
#         area=pi * self.radius ** 2
#         print(area)

#     def calc_perimeter(self):
#         pi=3.14
#         perimeter=2*pi*self.radius
#         print(perimeter)


# circle1=circle(5)
# circle1.calc_area()
# circle1.calc_perimeter()

#............................
#define an employee class with attributes role, department and salary. It also have showdetails method.
#create an engineer class that inherits properties from employee and have new attributes name and age.

# class Employee():
#     def __init__ (self, role, department, salary):
#         self.role=role
#         self.department=department
#         self.salary=salary

#     def showdetails(self):
#         print("role =", self.role)
#         print("department =", self.department)
#         print("salary =", self.salary)

# class Engineer(Employee):
#         def _init__ (self, name, age):
#               self.name=name
#               self.age=age

# e1=Employee("ai engineer", "technical department",'50,00000')
# e1.showdetails()

#.............................
#create a class order which store item and its price
#use dunder function __gt__ to convey that:
#order1>order2 if price of order1 > price of order2
class Order():
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__ (self,o1):
        self.o1=o1
        return self.price > o2.price

o1=Order("meat",1200)
print(o1.item,o1.price)
o2=Order("eggs", 400)
print(o2.item,o2.price)
print(o1>o2)



    







        
        

