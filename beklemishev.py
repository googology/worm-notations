def BMW(a,n):
    if a[-1]==0:return a[:-1]
    if a[-1]-1 in a:
        k=-1
        while a[k]>=a[-1]:k-=1
        b=a[k:-1]
    else:
        b=a[:-1]+[a[-1]-1]
        k=0
    return a[:k]+b*(n+1)