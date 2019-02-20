import sys

'''

problem can be found at https://open.kattis.com/problems/shopaholic
'''


# sorts the list and picks the third element, solves the problem
def main():
    n=0
    for line in sys.stdin:
        line = line.strip('\n')
        if n==0:
            n=int(line)
        else:
            lista=line.split(' ')
            lista = [int(x) for x in lista]
            lista.sort()
            lista.reverse()
            lista=lista[2::3]
            print(sum(lista))

if __name__ == '__main__':
    main()