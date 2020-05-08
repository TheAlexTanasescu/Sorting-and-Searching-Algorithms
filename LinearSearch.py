def linearSearch(array, size, valueToFind):
    for i in range(0, size):
        if (valueToFind == array[i]):
            return i
    return -1

array = [5,3,9,21,13,67,8,11,42]
valueToFind = 67
size = len(array)
result = linearSearch(array, size, valueToFind)
if (result == -1):
    print("number not found")
else:
    print("number found at index ",result)
