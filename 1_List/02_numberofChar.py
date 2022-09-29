#  Write a Python program to count the number of characters (character frequency) in a string

strng = "google.com "


def Countchar(string):
    count=0
    for i in string:
        count+=1
    return count
    
print(Countchar(strng))
