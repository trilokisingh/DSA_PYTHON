strng = input("Enter string  ")


def checkPalin(s):
    start = 0
    end = len(s)-1
    while (start < end):
        if s[start] != s[end]:
            print("No")
            break
        start = start+1
        end = end-1
    else:
        print("Yes ")


checkPalin(strng)




#####################   another approch ######################################


if (strng==strng[::-1]):
    print("Yes")
else:
    print("no")    
