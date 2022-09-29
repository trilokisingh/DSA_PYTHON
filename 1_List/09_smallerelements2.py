List=[1, 4, 548, 45, 4, 85, 875, 8, -4, 867, -7, 54, 4875, ]

def checkSmaller(list,value):
    smallList=[]
    for i in list:
        if i<value:
            smallList.append(i)

    return smallList

value=8
print(f"Value smaller than {value} is {checkSmaller(List,value)}")        
