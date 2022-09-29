# Write a Python program to get the largest number from a list

list = [0,12, 515, 1, 81, 11,8787987, 68, 302, 7, 888]


def findgraeter(list):
    greter = list[0]
    for i in list:
        if (i > greter):
            greter = i

    return greter


           


print(findgraeter(list))



# def max_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# print(max_num_in_list([1, 2, -8, 0]))
