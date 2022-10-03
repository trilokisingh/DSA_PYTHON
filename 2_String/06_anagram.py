s1="triloki"
s2="ilrotik"

def check(s1,s2):
    if(len(s1)!=len(s2)):
        return False
    else:
        s1=list[s1]  
        s2=list[s2]
        s1.sort(s1)
        s2.sort(s2)
        return s1==s2

check(s1,s2)        