#Create function to calculate the list of Armstrong Numbers present between 2 to 2000.

def ArmstrongNumber():
    armNum =[]
    for num in range(2,2001):
        temp = num
        n=0
        while temp!=0 :
            temp = temp//10
            n=n+1
        sum = 0 
        temp = num
        while temp !=0 :
            i = temp%10
            sum = sum + (i**n)
            temp = temp // 10
        if(sum == num):
            armNum.append(num)
    return armNum
arm = ArmstrongNumber()
print("List of armstrong no in range 2 to 2000 is ")
for i in arm:
    print(i , end = " ")
print("")