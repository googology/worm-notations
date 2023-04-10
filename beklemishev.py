def BR(a):
    ret = False
    br = None
    for i in range(len(a)+1):
        if a[len(a)-i] < a[-1]:
            br=len(a)-i
            break
    return br

def BMW(a,n):
    if a[-1]==0:return a[:-1]
    if BR(a)!=None: # If the bad root exists, search for it
        b=a[BR(a):-1]
    else:
        b=a[:-1]+[a[-1]-1]
        k=0
    return a[:k]+b*(n+1)