def BR(a):
    br = None
    for i in range(len(a)):
        if a[len(a)-i-1] < a[-1]:
            br=len(a)-i-1
            break
    return br

def BMW(a,n):
    g=b=[]
    if a[-1]==0:return a[:-1]
    if BR(a) != None:
        i0 = BR(a)
    else:
        b=a[:-1]+[a[-1]-1]
    return a[:k]+b*(n+1)