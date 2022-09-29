

List = [12, 1, 3, 5, 1, 541, 5, 1, 3, 4212, 8, 0, 54, 81, 5, 5]


def Filter(list):
    Lodd = []
    Leven = []
    for i in list:
        if i % 2 == 0:
            Leven.append(i)
        else:
            Lodd.append(i)
    return Lodd, Leven


Lodd, Leven = Filter(List)
print(Lodd)
print(Leven)
