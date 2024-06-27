#union and update
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.union(cities2)
print(cities3)

cities.update(cities2)
print(cities)
''' prints all the items present in the set the union() method returns a new set where as update() method adds
item into the existing set from another set'''


#intersection and intersection_update()

cities3 = cities.intersection(cities2)
print(cities3)

cities.intersection_update(cities2)
print(cities)
'''the intersection() and intersection_update method prints only items
that are similar to both the sets the intersection() method returns a 
new set whereas intersection_update method updates into the existing 
set from another set.'''

#symmetric_difference and symmetric_difference_update

cities3 = cities.symmetric_difference(cities2)
print(cities3)
cities.symmetric_difference_update(cities2)
print(cities)
'''the symmetric_difference and symmetric_difference_update methods
prints only items that are not similar to both the sets.
the symmetric_difference() method returns a new set whereas
symmetric_difference_update() method updates into the existing
set from another set.'''

#difference() and difference_update()
cities3 = cities.difference(cities2)
print(cities3)
cities.difference_update(cities2)
print(cities)
'''the difference and difference_update() methods prints only items 
that are only present in the original set and not in both the sets
the difference method returns a new set whereas difference_update()
method updates into the existing set from another set'''

#built_in methods of the set

#disjoint_method
print(cities.isdisjoint(cities2))

#issuperset()
print(cities.issuperset(cities3))

#issubset()
print(cities2.issubset(cities))

#add 

cities.add("Helsinki")
print(cities)

#update
cities2 = {"helsinki","warsaw","seoul"}
cities.update(cities2)
print(cities)
#remove

#cities.remove('Tokyo')
print(cities)
cities.discard("gurugram")
'''The main difference between remove and discard is that, 
if we try to delete an item which is not present in set, then remove()
 raises an error, whereas discard() does not raise any error.
'''
#pop

item = cities.pop()
print(cities)
print(item)

#del
#it deletes the entire set 
#del cities

#clear
#this method deletes the items in a set
#cities.clear()