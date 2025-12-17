#general representation
#def function_name(parameter1, parameter2):
#rest of the code

#write a function to add two numbers
# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
# cal_sum(2,3)
# cal_sum(5,5)

#calculate the average of three numbers
# def calc_average(a,b,c):
#     average = ((a+b+c)/3)
#     print(average)
# calc_average(98,97,95)

#define a function calculate the number of items in a list
# numbers = [1,2,3,4,5]
# fruits = ["mango", "apple", "grapes", "banana"]
# def calc_length(list):
#     print(len(list))
# calc_length(numbers)
# calc_length(fruits)

#wap to print all of the elements in a single line
# seasons = ["winters", "summers", "autumn", "spring"]
# def print_list(list):
#     for items in list:
#         print(items, end=" ")

# print_list(seasons)

#wap to find the factorial of n numbers using function
# def calc_factorial(n):
#     fact=1
#     i=1
#     while i<=n:
#         fact*=i
#         i+=1
#     print(fact)
# calc_factorial(5)

#write a program to convert usd to pkr using functions
# def currency_converter(usd_val):
#     usd = float(input("how much dollars do you want to convert: "))
#     pkr1 = usd*282.57
#     print(f"{usd}usd = {pkr1:.2f}pkr")
# currency_converter(30)

#wap using function to identify wether the number is even or odd
# def even_odd(n):
#     if n%2==0:
#         print(f"{n} is an even number")
#     else:
#         print(f"{n} is an odd number")

# even_odd(34)


##################### RECURSION #######################


#write a recursive function to calculate the sum of first n natural numbers
# def sum(n):
#     if n==0:
#         return 0    
#     return sum(n-1) + n

# print(sum(4))


#write a recursive function to print all elements in a list
def print_list(list, index=0):
    if(index==len(list)):
        return
    print(list[index])
    print_list(list, index+1)
fruits=["mango", "apple", "banana", "orange"]
print_list(fruits)







