#  Write a Python program to sum all the items in a list

list = [1,5,8,0,95,1]

def sum(list):
    grand_sume= 0
    for i in list:
        grand_sume+=i
    return grand_sume

print(sum(list))        