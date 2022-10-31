#A Program to Find LCM of five numbers using functions.

def findLCM(arr):
    t1 = arr[0]
    t2 = arr[1]
    num = 0
    den = 0 
    if(t1>t2):
        num = t1
        den = t2
    else:
        num = t2
        den = t1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = (t1 * t2)/gcd
    for i in range(2,5):
        t1 = lcm
        t2 = arr[i]
        num = 0
        den = 0
        if(t1>t2):
            num = t1
            den = t2
        else:
            num = t2
            den = t1
        rem = num % den
        while(rem != 0):
            num = den
            den = rem
            rem = num % den
        gcd = den
        lcm = (t1 * t2)/gcd
    return lcm    
temp = input("enter space sperated 5 integer\n").split(" ")
arr = [int(i) for i in temp]
lcm = findLCM(arr)
print("LCM of above no is : ", lcm)
