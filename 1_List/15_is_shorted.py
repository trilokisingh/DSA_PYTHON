
L = [1, 22, 3, 4, 8, 12, 48, 222, 384]
L2 = [1, 2, 3, 4, 8]

def CheckShorting(list):
    i=1
    while i<len(list):
        if list[i]<=list[i-1]:
            return False
        i=i+1

    return True



if CheckShorting(L):
    print("Yes shorted")
else:
    print("Not shorted")

if CheckShorting(L2):
    print("Yes shorted")
else:
    print("Not shorted")


