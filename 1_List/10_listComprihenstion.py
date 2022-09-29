L = [1, 2, 1, 5, 0, -1, 45, 15, 45]

L1 = [x for x in L if x < 5]
print(L1)

L2 = [x for x in L if x > 5]
print(L2)

L3 = [x for x in range(21) if x % 2 == 0 and x != 0]
print(L3)


def findOddeven(list):
    return [x for x in list if (x % 2 == 0)], [y for y in list if y % 2 != 0]


evenlist, oddlist = findOddeven(L)
print(f"Odd containing list is {oddlist}")
print(f"Even containig list is {evenlist}")

s="Triloki Singh"
l1=[x for x in s if x in "love you i"]
print(l1)

LL=[x for x in s if x.startswith("T")]
LLL=[x for x in s if x.startswith("r")]
print(LL)
print(LLL)

