n = int(input())
a = list(map(int, input().split()))

while not len(a) == n:
    print("Error en la entrada de datos")
    a = list(map(int, input().split()))

m = abs(a[0])

for i in a[1:]:
    if abs(i) < m:
        m = abs(i)

print(m)
