#Binary Search
def binarySearch(array, target):

    if(len(array) == 0):
        return False

    size = len(array)
    minIndex = 0
    maxIndex = size - 1
    midIndex = maxIndex // 2
    midValue = array[midIndex]


    if (target < array[minIndex] or target > array[maxIndex]):
        return False

    elif (target > midValue):
        upper = array[midIndex+1:]
        print(midValue)
        print(upper)
        return binarySearch(upper,target)

    elif (target < midValue):
        lower = array[:midIndex]
        print(midValue)
        print(lower)
        return binarySearch(lower,target)

    elif (target == midValue):
        return True

#Driver Code
array = []
counter = 0

numItems = int(input("Enter how many items you want to have in the array: "))

while (counter < numItems):
    number = int(input("Add a value to add to the array: "))
    array.append(number)
    counter += 1
    print("Array is: ", array)

target = int(input("Enter the value you're trying to find: "))



result = binarySearch(array,target)
if (result == True):
    print("Target is in the array")
else:
    print("Couldn't find target")
