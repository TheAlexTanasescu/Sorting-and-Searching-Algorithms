import matplotlib.pyplot as plt


numItems = int(raw_input("Enter how many items you want to sort: "))
count = 0
numList = []


#plt.ion()

#def display(list):
#	plt.clf()
#	plt.bar(range(len(list)), list)
#	plt.draw()
#
#	plt.show(block = "True")


	

while (count < numItems):
	number = int(raw_input("Enter a number: "))
	numList.append(number)
	count += 1
	print (numList)
	print("count is: " + str(count))




def insertionSort(list):
	for i in range(1, len(list)):
		value  = list[i]

		j = i - 1
		while (j >= 0 and value < list[j]):
			list[j+1] = list[j]
			j -= 1
			#print("length of list is: " + (len(list)))
			#print list

		list[j + 1] = value
		return list


print insertionSort(numList)








#for i in range(len(numList)):
#	print("% d" % numList[i])



	


#x = range(len(numList))
#plt.bar(x, numList)