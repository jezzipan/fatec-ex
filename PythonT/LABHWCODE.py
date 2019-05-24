from util import *
def particiona(v,p,u):
    x = v[p]
    i = p-1
    j = u+1
    while True:
        j -= 1
        i += 1
        while v[j]>x: j -= 1
        while v[i]<x: i += 1
        if i<j: troca(v,i,j)
        else: return j
def troca(v,i,j):
    x = v[i]
    v[i] = v[j]
    v[j] = x
def qs(v,p,u):
    if p==u: return
    m = particiona(v,p,u)
    qs(v,p,m)
    qs(v,m+1,u)
    
def qsort(v):
    qs(v,0,len(v)-1)

def particionap(v,p,u):
    troca(v,p,randrange(p,u+1)) 
    x = v[p]
    i = p-1
    j = u+1
    while True:
        j -= 1
        i += 1
        while v[j]>x: j -= 1
        while v[i]<x: i += 1
        if i<j: troca(v,i,j)
        else: return j
def qsp(v,p,u):
    if p==u: return
    m = particionap(v,p,u)
    qsp(v,p,m)
    qsp(v,m+1,u)
def qsortp(v):
    qsp(v,0,len(v)-1)
    
I = (10**4,10**5,10**4)
F = [qsortp,qsort] 
cpu(*F,N=I)

