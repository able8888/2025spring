def f(n):
    if n == 1:
        return [' /\\ ', '/__\\']
    t = f(n - 1)
    x = 2 ** (n - 1)
    res = [' ' * x + u + ' ' * x for u in t]
    res.extend([u + u for u in t])
    return res


al = [f(i) for i in range(1, 11)]
while True:
    n = int(input())
    if n == 0:
        break
    for u in al[n - 1]:
        print(u)
    print()