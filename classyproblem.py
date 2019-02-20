'''

problem can be found at https://open.kattis.com/problems/classy

'''

import sys
class Person:
    def __init__(self, name, clas):
        self.clas=clas
        self.name=name

    def __lt__(self, other):
        if getbest(self,other) == self:
            return True
        else:
            return False

def lengthen(p1,p2): # adds 2 until the class is 10 long as that is the maximum length of class
    p1c =p1.clas
    p2c =p2.clas
    while len(p1c)<10:
        p1c.append('2')
    while len(p2c)<10:
        p2c.append('2')
    p1c = int(''.join(p1c))
    p2c = int(''.join(p2c))
    return p1c,p2c

def getbest(p1,p2): # gets the best of the two people beeing compared
    p1c,p2c=lengthen(p1,p2) #first they get lengthened
    if p1c==p2c: # if the class is the same the best (compared alphabetical, a>b)name gets selected
        if p1.name<p2.name:
            return p1
        else:
            return p2
    else:
        if p1c>p2c:
            return p1
        else:
            return p2



def read():
    cases=0
    list=[]
    counter=0
    for line in sys.stdin:
        line = line.strip('\n')
        if cases==0: #to get how many casese there will be in the input
            cases=int(line)
        else:
            try: # if it's not an integer it a person
                counter=int(line) # if it is an integer its he counter
            except ValueError:
                counter=counter-1 #decreases counter
                list.append(line)
            if counter<1: #if counter <1 every person has been read.
                sort(list) # function sort is calld upon
                list=[]
                cases=cases-1
            if cases==0:
                return



def sort(list):
    ppl=[]
    for i in list:
        i=i.split(':')
        i[1]=i[1][1:-6]
        person=Person(i[0],i[1].split('-'))
        ppl.append(person)
        ppl2 = []
    for i in ppl:
        numclass=[]
        for j in reversed(i.clas): # replaces the classes upper middle and lower with numbers as strings
            if j[0]=='u':
                numclass.append('3')
            if j[0]=='m':
                numclass.append('2')
            elif j[0]=='l':
                numclass.append('1')
        ppl2.append(Person(i.name,numclass))
    ppl2.sort() #sorts the ppl2 list, can be done as __lt__ has been defined for the class person
    for i in ppl2: # prints
        print(i.name)
    print('==============================')
read()



