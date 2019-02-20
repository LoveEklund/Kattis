import sys
'''
problem can be found at https://open.kattis.com/problems/phonelist
'''
 # sorts the list and then checks if the next value in the list starts with the same numbers as the i:th
def ifcool(lista):
    lista.sort(key=lambda s: s)
    for i in range(0,len(lista)-1):
        if len(lista[i])< len(lista[i+1]):
            if lista[i] in lista[i+1][:len(lista[i])]:
                print('NO')
                return
    else:
        print('YES')
        return

def read(): #reads the input
    casedone=0
    line=sys.stdin.readline()
    cases=int(line)
    while casedone<cases:
        line=sys.stdin.readline()
        numbers=int(line)
        numblist = []
        while numbers>len(numblist): # adds all the numbers in a list
            numblist.append(sys.stdin.readline().strip('\n'))
        ifcool(numblist)
        casedone=casedone+1
    return

read()
