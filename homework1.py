##create two list.The firs list should of odd numbers. The second list is also of even numbers.
##Merge these two lists. Multiply all values in the new list by 2.
##Use a loop a print the data type of the all values in the new list.


doubleList= [2,4,6,8,10]
singleList= [1,3,5,7,9]
singleList.extend(doubleList)
print("Merged List =",singleList)
print("listnumber x 2 :")
for single in singleList:
    print(single*2)