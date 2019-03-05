import sys

def getnumbers(n):
    a=[]
    for i in range(21):
        a.append(i)
        a.append(i*2)
        a.append(i*3)
    pos=list(set(a))
    for i in pos:
        for j in pos:
            for k in pos:
                if(i+j+k==n):
                    return i,j,k
    return 0
def stringify(ijk):
    res=[]
    for n in ijk:
        if n==0:
            pass
        elif n % 3 ==0:
            res.append("triple "+str(n//3))
        elif n%2 ==0:
            res.append("double "+ str(n//2))
        else:
            res.append("single " + str(n))
    return res

for n in sys.stdin:
    n=int(n)
    nummer= getnumbers(n)
    if nummer==0:
        print("impossible")
    else:    
        for i in stringify(nummer):
            print(i)
        
