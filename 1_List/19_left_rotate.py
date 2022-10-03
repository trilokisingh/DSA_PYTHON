l=[10,20,30,40,50]
d=2

def Rotation(list,d):
    for i in range(0,d):
        list.append(list.pop(i))
   
Rotation(l,d)
print(l)