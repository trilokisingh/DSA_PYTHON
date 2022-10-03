# write a program to right rotate one index of list 

L = [10, 20, 30, 40, 50]

# direct Methods

L = L[1:]+L[0:1]

print(L)


L.append(L.pop(0))
print(L)

# Another Approch


def Rotation(List):
    S = List[0]
    E = len(List)
    for i in range(1, E-1):
        List[i-1] = List[i]

    List[E-1] = S

Rotation(L)
print(L)