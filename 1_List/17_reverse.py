L=[10,20,30,40,50]




def Reversed(L):

    s=0
    e=len(L)-1
    
    while(s<e):
        L[s], L[e]=L[e],L[s]
        s=s+1
        e=e-1
        
    
#print(Reversed(L))    // will not work 

Reversed(L)

print(L)