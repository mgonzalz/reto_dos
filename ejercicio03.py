t = int(input())

def funcion(subs, online, conexiones):
    if subs == online:
        print('YES')
    else:
        for i in conexiones:
            if i == '+':
                subs -=1
                online +=1
            elif i == '-':
                online -=1
        if subs == online:
            print('MAYBE')
        elif subs > online:
            print('NO')
        else:
            print('YES')


n,a,q = map(int, input().split())
conexiones = list(map(str, input()))
while not len(conexiones) == q:
    print('Error, ingrese nuevamente las conexiones')
    conexiones = list(map(str, input()))

funcion(n,a,conexiones)


