def antecede(a, b):
    if a % 10 == 0:
        if b % 10 == 0:
            return a < b
        return True
    else:
        if b % 10 == 0:
            return False
        return a > b


# Programa Principal
n = int(input())

x = []
for _ in range(n):
    x.append(int(input()))

for i in range(len(x) - 1):
    k = i
    for j in range(i + 1, len(x)):
        if antecede(x[j], x[k]):
            k = j
    x[i], x[k] = x[k], x[i]

for i in range(n):
    print(x[i])