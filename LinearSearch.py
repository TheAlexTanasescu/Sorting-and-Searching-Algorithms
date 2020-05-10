def linearSearch(array, target):
    size = len(array)
    for i in range(0, size):
        if (target == array[i]):
            return i
    return -1

#Driver code
array = []
counter = 0

numItems = int(input("Enter how many items you want to have in the array: "))


while(counter < numItems):
    number = int(input("Enter a number to add to the array: "))
    array.append(number)
    counter += 1
    print("Array is: ",array)
target = int(input("Enter the value you're trying to find: "))
#print(array)    
result = linearSearch(array, target)
if (result == -1):
    print("number not found")
else:
    print("number found at index ",result)
