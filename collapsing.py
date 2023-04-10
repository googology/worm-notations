x = lambda a,b: (a[0]<b[0]) or (a[0]==b[0] and x(a[1:],b[1:])) if len(a)>0 and len(b)>0 else ((a==[] or b==[]) and len(a)<len(b))

def BR(a):
    br = None
    for i in range(len(a)):
        if a[len(a)-1-i] < a[-1]:
            br=len(a)-i
            break
    return br

def BR2(a):
    br = None
    for i in range(BR(a)):
        p0 = a[len(a)-1-i:len(a)]
        p1 = a[BR(a):len(a)]
        if x(p0,p1):
            br=len(a)-i
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