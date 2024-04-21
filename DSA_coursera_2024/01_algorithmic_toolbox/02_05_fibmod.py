def fibnumlast(num, mod):

    period = fibpis(mod)
    num = num % period

    if num <= 1:
        return num
    prev = 1
    curr = 1
    for i in range(num-2):
        prev, curr = curr, prev % mod + curr % mod
    return curr % mod


def fibpis(mod):
    prev, curr = 0, 1
    period = 1
    while True:
        prev, curr = curr, (prev + curr) % mod
        if prev == 0 and curr == 1:
            break
        period = period + 1
    #print(period)
    return period


if __name__ == '__main__':
    num, mod = map(int, input().split())
    print(fibnumlast(num, mod))
