'''
for kattis problem see https://kth.kattis.com/problems/a1paper
'''

import sys
class Paper:
    def __init__(self,size,x,y):
        self.size=size
        self.x=x
        self.y=y
    def area(self):
        return(self.x*self.y)
class Tape:
    def __init__(self):
        self.needed=0

def gety(num):
    a2=Paper(2, float(2 ** (-5 / 4)), float(2 ** (-3 / 4)))

def getxy(num): # för att få dimensionerna för ett papper av storleken A'num'
    stop=Paper(2, float(2 ** (-5 / 4)), float(2 ** (-3 / 4)))
    while stop.size<num:
        stop=Paper(stop.size+1,float((stop.area()/2)/stop.x),float(stop.x))

    return stop

def read():
    #dist är en lista som innehåller alla papper
    max=0
    for line in sys.stdin:
        line=line.strip('\n')
        #sätter första värdet till max
        if max ==0: # sätter första värdet man läser in till max
            max=line
        else: # lägger alla följande värden i en lista som heter dist
            dist=line
            dist=dist.split(' ')
            dist = [int(i) for i in dist]
            possible(dist,max) #kollar om det är möjligt
            return
            max=0
            dist=[]
def addup(dist,tape,max):
    req=2
    for i in range(0,max-1): # går igenom listan av alla papper man har
        if dist[i]>=req:  # om så många papper man behöver finns på positionen man är på
            dist[i - 1] = int(dist[i - 1] + req/2) # man 'skapar' papper av en storlekstörre
            tape.needed = tape.needed + (getxy(i + 2).y*req/2) # i+2 för att man har börjar med a2 papper och för att komma förbi noll indexeringen
            # till tape needed så lägger man till längden av y axeln på de papper man nyss skapade
            dist[i]= dist[i]-req# minskar antalet papper på plats i
            return
        else:
            req=(req-dist[i])*2 # ifall man inte hade tillräckligt papper på platsen så ökar man hur många man behöver
    return False # ifall det inte gick att sätta ihop papper så får man false

def possible(dist,max):
    works=True
    tape=Tape()# här under loopar mana igenom dist tills man är färdig
    while int(dist[0])<2 and works==True: # om dist[0] ==2 så är man färdig
        if addup(dist,tape,int(max)) ==False:
            works=False
            break
    if works==True:
        tape.needed=float(tape.needed+getxy(2).y)
        print(tape.needed)
    else:
        print('impossible')



def main():
    read()

if __name__ == '__main__':
    main()

