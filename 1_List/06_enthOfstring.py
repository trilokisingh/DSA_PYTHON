# Write a Python program to count the number of strings where the string length is 2 or more and 
# total hown many elements are graeter than 2

List = ["HI", 15, 164, "LOVE", "HAte", "SuCsEs", "A", 2, "LOCKER",9,"656"]


def checkLenth(list):
    greter_then_two = 0
    for element in List:
        if len(str(element)) >= 2:
            greter_then_two += 1

    return greter_then_two


print(checkLenth(List))
