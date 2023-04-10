x = lambda a,b: (a[0]<b[0]) or (a[0]==b[0] and x(a[1:],b[1:])) if len(a)>0 and len(b)>0 else ((a==[] or b==[]) and len(a)<len(b))

def BR(a):
    if len(a)<2:return None
    for i in a[:-1]:
        if i<a[-1]:
            k=-1
            while a[k]>=a[-1]:k-=1
            return len(a)+k
    return None

def BR2(a):
    if BR(a)<1:return None
    for i in range(len(a)-1,-1,-1):
        ai = a[i:]
        bi = a[BR(a):]
        if x(ai,bi):
            return i
    return None

def CW(a,n):
    if a[-1]==0:return a[:-1]
    if HBR(a):
        k=BR(a)
        b=a[k:-1]
    else:
        k=0
        b=a[:-1]+[a[-1]-1]
    return a[:k]+b*(n+1)