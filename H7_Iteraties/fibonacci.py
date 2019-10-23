fibo1 = 0
fibo2 = 1
fibo = 0
lijst = []
for y in range(10):
    lijst.append(fibo)
    # print(fibo)
    if fibo == 0:
        fibo += 1
    else:
        fibo = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo

print(lijst)
