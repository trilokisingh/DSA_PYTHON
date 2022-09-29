from os import remove


L=[12,14,9,45,16,32,2,12]
print(f"original list is {L}")
L.append(55)
print(L)
L.insert(2,12)  #2 is index 
print(L)




print(96 in L)

print(L.count(12))

print(L.index(32))
# print(L.index(32,0,3))

L.remove(2)
print(L)