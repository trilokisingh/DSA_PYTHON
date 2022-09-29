L = [1, 2, 1, 5, 0, -1, 45, 15, 45]
L2=["A",'B','C','D','E','F','G','H','I']

l2={x:x*3  for x in L  }
print(type(l2))
print(l2)

l3={x:f"ID {x}" for x in L}
print(l3)

l4={L[x]:L2[x] for x in range(len(L2))}   #IMPORTANT**********
print(l4)


