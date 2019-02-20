'''
problem can be found at https://open.kattis.com/problems/bard

'''

import sys



class Person:

    def __init__(self):
        self.songs=[]

def Write(village):
    printlist=[]
    j=1
    for i in village: # goes through the village list
        i.songs.sort() # sorts the songs
        if i.songs==village[0].songs: # if the songs are equal to the bards songs then the villager knows all songs
            printlist.append(j)
        j+=1
    for k in printlist:
        print(k) # prints all the villagers that knows every song


def read():
    N=0
    E=0
    nr=1 # nr is songnnr
    for line in sys.stdin:
        line = line.strip('\n')
        line = line.split(' ')
        if N==0: # to read N
            N=int(line[0])
            village=[]
            for i in range(0,N):
                village.append(Person()) # Creates tha village as an array with person objects
        elif E==0: # Too read E
             E=int(line[0])
        else:
            line=line[1:]
            if '1' in line: # if 1 is in the line then the bard is singing that night and every villager learns the new song
                for i in line:
                    village[int(i) - 1].songs.append(nr)
                nr = nr + 1 # when the next song is sung it's the next one
            else:# if the bard is not present they exchange songs
                exchange=[]
                for i in line: # checks the input or the people there that evening
                    for j in village[int(i)-1].songs: # for every song in that persons songsregister add it to the exchange list
                        exchange.append(j)
                for k in line:
                    for p in exchange: # after all the songs been put in the exchange list all the villagers gets the sons added to their .songs
                        if p not in village[int(k)-1].songs:
                            village[int(k) - 1].songs.append(p)

            if E==1: #if it's the last evening
                Write(village)
                return
            else: # decrease evenings left by 1
                E-=1



read()