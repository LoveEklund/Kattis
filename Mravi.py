import sys

class pipe:
    def __init__(self,i,out,p,s,data):
        self.i=int(i)
        self.out=int(out)
        self.p=int(p)/100
        self.s=int(s)
        self.data=data

def main():
    pipes={}
    N=0
    i=1
    max=0
    for line in sys.stdin:
        if N==0:
            N=int(line)
        elif i<N:
            line=line.strip("\n")
            data=line.split(" ")
            #print(data)
            pipes[int(data[1])]=pipe(data[0],data[1],data[2],data[3],i)
            i+=1
        else:
            line = line.strip("\n")
            vals=line.split(" ")
            #print(vals)
            for i in range(1,len(vals)+1):
                val=int(vals[i-1])
                if val!= -1:
                    #print(str(i) +"index")
                    p=pipes[i]
                    #print(str(p.data) +"pipe index")
                    needed=val
                    while p.i!=1:
                        if (p.s == 1):
                            #print(needed)
                            needed = needed ** (1 / 2)
                        needed = needed / p.p
                        p = pipes[p.i]
                    if (p.s == 1):
                        #print(needed)
                        needed = needed ** (1 / 2)
                    needed = needed / p.p
                    if needed>max:
                        max=needed
            print(max)

if __name__ == '__main__':
    main()