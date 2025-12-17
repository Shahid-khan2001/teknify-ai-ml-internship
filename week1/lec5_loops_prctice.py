#while loop practice questions

#print numbers from 1 to 100
# i=1
# while i<=100:
#     print (i)
#     i+=1

#print numbers from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1


#print the multiplication table of number n
# n=int(input("enter a number: "))
# i=1
# while i <=10:
#     print(f"{n} * {i} = ",i*n)
#     i+=1

#print the elements of the following list using a loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# numbers=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# indx=0
# while indx<len(numbers):
#     print(numbers[indx])
#     indx+=1

#search for a number x in this tuple using loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# numbers=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x=81
# i=0
# while i<len(numbers):
#     if(numbers[i]==x):
#         print("number found at index",i)
#     i+=1

#print the elements of the following list using loop and than search the number x
# x=81
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,81]
# for numbers in list:
#     print(numbers)
# indx=0
# for numbers in list:
#     if x==numbers:
#         print("number found at index", indx)
#     indx+=1

#Range funtions:
#they returns a sequence of numbers, starting from 0 by default and incrementing by 1,
#and they excludes the last number
#range(start, stop, step)
# numbers=range(10)
# for i in numbers:
#     print(i)

#print all of the od numbers between 1 and 10 using range function
# for i in range(1,10,2):
#     print(i)

#find the factorial of n numbers using for loop
#fact of 5= 1*2*3*4*5
# n=4
# fact=1
# i=1
# while i<=n:
#     fact *= i
#     i += 1
# print(fact)




