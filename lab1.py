#Que1:-Print a welcome message on the output screen.
print ("Welcome to IoT Lab-1_CS/IT316")


#Que2:-Perform arithmetic operation (+, -,*,/) on two floating point numbers.
a = float(input("enter first number: "))
b = float(input("enter second number: "))

sum = a + b
sub = a-b
mul=a*b
div=a/b
print("sum:", sum)
print("sub:", sub)
print("mul:", mul)
print("div:", div)


#Que3:-Calculate maximum of two numbers using built in, if statement and arithmetic operators.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Maximum Number Using Built In Library : ", (max(a,b)))
print("Maximum Number Using If Statement: ", a if a>b else b)
print("Maximum Number Using Airthmetic Operators : ", (a + b) / 2 + abs(a - b) / 2)


#Que4:-Check a given number is odd or not.
num = int(input("Enter a number: "))  
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))  
   
  
 #Que5:-Find list of prime numbers from 1 to 1000. 
primes=[]
flag=True 
for num in range(1, 1001):
      if num > 1:
          flag=True 
          for i in range(2, num):
              if (num % i) == 0: 
                  flag=False 
          if flag==True: 
              primes.append(num) 
print("List Of Prime Numbers from 1 to 1000 :- ",primes)


#Que6:-A program to Make a Simple Calculator which performs only +, -, *, / and % using function concept.


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function Reminder two numbers
def Reminder(x, y):
    return x % y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Reminder")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the five options
    if choice in ('1', '2', '3', '4' ,'5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
            print(num1, "%", num2, "=", Reminder(num1, num2))    
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


#Que8:-A Program to Display Fibonacci Sequence Using Recursion.

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 15

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       
       
#Que9:-Python Program to Find Armstrong Number in an Interval

lower = 50
upper = 5000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print("Armstrong Number in an Interval" ,num)
       

#Que10:-A program to print all pronic numbers between 1 and 100.
#The pronic number is a product of two consecutive integers of the form: n(n+1).
#For example:
#6 = 2(2+1)= n(n+1),
#72 =8(8+1) = n(n+1)
#Some pronic numbers are: 0, 2, 6, 12, 20, 30, 42, 56 etc.       
       
       


#isPronicNumber() will determine whether a given number is a pronic number or not    
def isPronicNumber(num):    
    flag = False;    
        
    for j in range(1, num+1):    
         
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
     
#Displays pronic numbers between 1 and 100    
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i),    
        print(" "),   






