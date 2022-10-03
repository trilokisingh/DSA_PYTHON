#find the number which occurence in list is odd times 

L=[10,20,20,30,30,10,10]

def N_appreance(list):
    count=None
    for i in list:
        count=list.count(i)
        if count%2!=0:
            count=i
            
            break 

    return count

print(N_appreance(L))             

        