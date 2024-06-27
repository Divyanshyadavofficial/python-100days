list1 = [1,2,3,4,5]
list2 = ["Red","Green","Blue"]
print(list1)
print(list2)


Details = ["Divyansh",21,"Aiml",24226.0]
print(Details)
Names = ["Divyansh","Digisha","Mridul","Jitesh","Sakshi","gourav","Kunal","Mickey"]
#positive indexing
print(Names[0])
print(Names[1])
print(Names[2])
print(Names[3])
print(Names[4])
print(Names[5])
print(Names[6])
print(Names[7])
#negative indexing
print(Names[-1])
print(Names[-2])
print(Names[-3])
print(Names[-4])
print(len(Names)-5)
print(Names[2])

#to check whether an item is present in list
if "Divyansh" in Names:
    print("Divyansh is present.")
else:
    print("Divyansh is not present")
#range of index
print(Names[0:8:1])

#printing elements with in a given range.
print(Names[3:7])
#printing all element from a given index till the end 
print(Names[4:])
print(Names[-4:])
#print all elements from start to a given index
print(Names[:5])
#print alternate values
print(Names[::2])
#printing every 3rd consecutive value within a given range
print(Names[1:8:3])

''' List comprehension.
 list comprehension are used for crearing new lists from other 
 iterables like lists,tuples,dictionaries,sets and even in arrays and 
 strings.
 List = [Expression(item)for item in iterable if condition]
 Iterable: It can be list,tuples,dictionaries,sets and even in arrays 
 and strings
 Condition: condition checks if the item should be added to the new 
 list or not. 
   '''

namesWith_d = [item for item in Names if "D" in item]
print(namesWith_d)
