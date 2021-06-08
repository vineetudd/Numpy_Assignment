# Vandermonde function
import numpy as np
def vanderm(x,N=None,increasing=False):
    l=len(x)
    if N==None:
        y=[[] for i in range(l)]
        if increasing ==True:
            for j in range(l):
                for i in range(l):
                    y[i].append(x[i]**j)
        else:
            for j in range(l):
                for i in range(l):
                    y[i].append(x[i]**(l-j-1))
    elif N!=None:
        y=[[]for i in range(l)]
        if increasing ==True:
            for j in range(N):
                for i in range(l):
                    y[i].append(x[i]**j)
        else:
            for j in range(N):
                for i in range(l):
                    y[i].append(x[i]**(N-j-1))
        
    return np.array(y)


# Moving average
import numpy as np
def moving_avg(x,k):
    n=len(x)
    global s
    o=[]
    i=0
    while i < n-k+1:
        l=x[i:i+k]
        s=0
        for j in l:
            s=s+j
        o.append(s/k)
        i=i+1
    return np.array(o)
