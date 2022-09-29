# Write a Python program to get the smallest number from a list

L=[1,2,1,5,0,-1,45]

def checkSmall(list):
    small = list[0]
    for element in list:
        if (element<small):
            small=element
    return small

print(checkSmall(L))            