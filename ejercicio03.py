t = int(input())
while not t == 0:
    def funcion(subs, online, conexiones):
        if subs == online:
            return 'YES'
        else:
            online_conexiones = 0
            online_desconexiones = 0
            for i in conexiones:
                if i == '+':
                    online_conexiones +=1
                elif i == '-':
                    online_desconexiones -=1
                elif subs == online + online_conexiones + online_desconexiones:
                    return 'YES'
            if subs == online + online_conexiones + online_desconexiones:
                return 'YES'
            elif online_conexiones >= subs - online:
                return 'MAYBE'
            else:
                return 'NO'


    n,a,q = map(int, input().split())
    conexiones = list(map(str, input()))
    while not len(conexiones) == q:
        print('Error, ingrese nuevamente las conexiones')
        conexiones = list(map(str, input()))
    t=t-1

    print(funcion(n,a,conexiones))


