
marks = [10,20,30,40,50]
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("awesome")
        index+=1


for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("awesome")



#loop over a list and print the index and value of each element
fruits = ['apple','mango','banana']
for index, fruit in enumerate(fruits):
    print(index,fruit)

#loop over a list and print the index (starting at 1) and value of 
#each element
fruits = ['guvava','banana','mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
    print(f'{index+1}: {fruit}')
#loop over a tuple and print the index and value of each element
colors = ('red','green','blue')
for index, color in enumerate(colors):
    print(index,color)

#loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)