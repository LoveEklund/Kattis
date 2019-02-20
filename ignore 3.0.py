'''
problem can be found at https://open.kattis.com/problems/ignore
'''


import sys
#Alla tal som inte innehåller 3,4 och 7 blir tal när man vänder dem upp och ner
#Uppgiften löstes genom att ta in ett nummer och sedan omvandla det till bas 7.
#Men Eftersom man då får med 3 och 4 så fick jag göra om det så att 3 blev 5, eftersom 5 är mitt tredje tal osv, se funktionen flip.
#
def base7(number): # gör om inputen till bas 7
    ans=''
    while number >= 1:
        ans = str(number%7) + ans
        number = number//7
    return int(ans)

def flip(num): # vänder på numret och ser även till att 3->5 osv
    num=str(num)[::-1]
    numlist=[]
    for i in num:
        numlist.append(i)
    for i in range(0,len(numlist)):
        if numlist[i]=='3':
            numlist[i]='5'
        elif numlist[i]=='4':
            numlist[i]='9'
        elif numlist[i]=='5':
            numlist[i]='8'
    numlist="".join(numlist)
    return numlist

def getk(num):#funktion som kallar på bas 6 omvandlaren och även flip funktionen och sedan skriver ut num
    num=base7(num)
    num=flip(num)
    print(num)


def main():
    for line in sys.stdin:
        line = line.strip('\n')
        getk(int(line))
if __name__ == '__main__':
    main()