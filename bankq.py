import sys

'''
problem can be found at https://open.kattis.com/problems/bank
'''


class Person:
    def __init__(self, money, time):
        self.money=money
        self.time=time

    def __lt__(self, other):
        if self.money>other.money:
            return True
        else:
            return False

def maximize(queue,minutes): #this function sorts the list and places the person with the most money as long back as they can be
    queue.sort()
    totmoney=0
    newqueue=[0]*minutes
    for i in queue:
        j=i.time
        if i.time<minutes:
            if newqueue[i.time]==0:
                newqueue[i.time]=i.money
            else:
                while j>-1:
                    if newqueue[j]==0:
                        newqueue[j]=i.money
                        break
                    j-=1
    for k in newqueue:
        totmoney+=k
    return totmoney

def read(): ## reads the input and calls for maximize which is the main function
    minutes = 0
    people = 0
    queue = []
    for line in sys.stdin:
        line = line.strip('\n')
        line = line.split(' ')
        if minutes==0 and people==0:
            minutes=int(line[1])
            people=int(line[0])
        elif people>0:
            person=Person(int(line[0]),int(line[1]))
            queue.append(person)
            people-=1
        if people==0:
            maximum=maximize(queue,minutes)
            print(maximum)
            return

read()