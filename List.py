numList = [10,20,30,40,50]
nameList = ["Jahid","Alamin","Osman","Shariful"]

print(nameList[0])
print(numList[4])

numList[3]= 80
print(numList)

del numList[2]
print(numList)
print(len(numList))
print(min(numList))
print(max(numList))

numList.append(90)
print(numList)
print(numList.count(10))
print(numList.count(90))


list1, list2 = [20,30,40], [200,300,400]

list1.extend(list2)
print(list1)

list1.reverse()
print(list1)

print(list1.index(40))

index = list1.index(40)

print("Index of 40 is ",index)