L=[2,2,3,4,4,5,5,5]

def N_appreance(list):
    count=None
    for i in list:
        count=list.count(i)
        if count%2!=0:
            count=i
        return count

    return None

print(N_appreance(L))             

        