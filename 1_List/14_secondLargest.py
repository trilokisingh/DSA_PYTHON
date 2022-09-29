list = [3, 5, 74, 2, 541, 25, 12, 15, 1]


# APPROCH 1  # we will short list in assending and second last will largest
list.sort()
print(list)

print(f"Second Largest is {list[len(list)-2]}")
print(f"Second Largest number is {list[-2]}")

# approch 2  ?? we will remove the largest element then largest will second largest

List2 = [3, 5, 74, 2, 541, 25, 12, 15, 1, 524, 424, 999, 1000]
newList = set(List2)
newList.remove(max(newList))
print(newList)
print(f"second largest is {max(newList)}")