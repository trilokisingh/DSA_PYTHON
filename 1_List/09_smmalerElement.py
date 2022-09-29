 

list = [1, 4, 548, 45, 4, 85, 875, 8, -4, 867, -7, 54, 4875, ]


def checkSmaller(list):
    small = list[0]
    for element in list:
        if element < small:
            small = element

    return small


print(f"The samllest number in List is {checkSmaller(list)}")
