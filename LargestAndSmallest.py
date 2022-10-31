#Create function to calculate the largest and smallest element present on an array. Elements and
#number of elements present on the array is taken from the keyboard.
def LargestAndSmallest(arr):
    ma = arr[0]
    mi = arr[0]
    for i in arr:
        if i > ma :
            ma = i
        if i < mi :
            mi = i
    return [mi , ma]
temp = input("enter space sperated integer\n").split(" ")
arr = [int(i) for i in temp]
maxmin = LargestAndSmallest(arr)
print("Smallest No is : ", maxmin[0])
print("Largest No is : ", maxmin[1])

