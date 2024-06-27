#list.sort()

list1 = [1,4,3,77,55,33,22,10,11]
list1.sort()#prints the list in ascending order
print(list1)
list1.sort(reverse=True)#prints the list in descending order
print(list1)

#list.reverse()

list1.reverse()#prints the original list in reverse order
print(list1)
#list.index()

print(list1.index(77))#returns the index where the value is present

#list.count()

print(list1.count(22))#counts the number of occurences of item present in the list

#list.copy()

new_list = list1.copy()#returns the copy of the list this can be done to 
#perform operations on the list without modifying the original list.
print(new_list)

#list.append()

list1.append(100) #appends items to the end of existing list.
print(list1)

#list.insert()
list1.insert(1,10)# inserts an item at index 1
print(list1)

#extend()
list2 = [78,79]
list1.extend(list2)
#this method adds an entire list or any other collection datatype 
#to the existing list
print(list1)

#concatenating two lists

print(list1+list2)