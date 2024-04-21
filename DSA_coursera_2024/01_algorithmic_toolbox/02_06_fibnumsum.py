def fibnumsum(num):
    #every 60 f(n) last digit repeats
    if num > 60:
        num = (num) % 60

    if num <= 1:
        return num
    prev, curr = 1, 1
    fsum = 2
    for i in range(num-2):
        prev, curr = curr, prev % 10 + curr % 10
        fsum = fsum + curr % 10
    return fsum % 10


if __name__ == '__main__':
    print(fibnumsum(int(input())))