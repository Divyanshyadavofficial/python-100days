#update
info = {'name':'karan','age':19,'eligible':True}
print(info)
info.update({'age':21})
info.update({'Dob':2001})
print(info)

#clear()

info1 = {'name':'divyansh','age':21,'eligible':True}
info1.clear()
print(info1)

#pop
info2 = {'name':'jitesh','age':20,'eligible':True}
info2.pop('eligible')
print(info2)

#pop item
info2.popitem()
print(info2)

#del
del info['age']
print(info)

del info
#print(info) it raises error cause now info is deleted.