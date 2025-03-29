'''2. Loops: 
a. Easy Questions: 

i. Print all numbers from 1 to 100 using a for loop.'''

# for i in range(1,101):
  # print(i)


''' ii. Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)'''

# sum=0
# for i in range(1,20):
#   sum +=i

# print(sum)


'''iii. Print all even numbers between 1 and 50 using a while loop.'''

# for i in range(2, 50, 2):
#   print(i)


'''iv. Write a program to display the multiplication table of a given number. First 20'''

# num=int(input('enter any number '))
# for i in range(1,21):
#    print(num, '*',i,'=',num*i )
#    i+=1
   

# num=int(input('enter any number '))
# for i in range(1,num+1):
#   for j in range(1,11):
#     print(i, '*',j,'=',i*j )
    


# for i in range(1,21):
#   for j in range(1,11):
#     # print(i,'*',j,'=',i*j)
  

'''v. Reverse a number using a while loop. 1. Also can we get the sum of all the digits.'''

# num=123456

# while num > 0:
#   rem = num % 10 
#   print(rem)      # 6 5 4 3 2 1
#   num = num // 10

num=123456
rev_num=0

while num > 0:
  rem = num % 10 
  # print(rem)     
  rev_num = rev_num * 10 + rem
  num = num // 10

print(rev_num) 

'''vi. Write a program to count the number of digits in a given number using a while loop.'''



'''vii. Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.'''




                            #  '''b. Medium Questions:'''

'''ii. Check if a given number is a prime number using a for loop.'''
# num=97
# is_prime=True
# for i in range(2,num):
#   if num%i==0 :
#     is_prime=False
#     break
# if is_prime and num>1:
#     print(num,' is prime')
# else:    
#     print(num,' is not prime')

'''iii. Write a program to calculate the factorial of a number using a while loop.'''

# num=5
# fact=1
# i=1
# while i<=num :
#   fact *= i
#   i=i+1
  
# print(fact)

'''iv. Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.'''

# for i in range(1,101):
#   if i%3==0 and i%5==0 :
#     print(i)

