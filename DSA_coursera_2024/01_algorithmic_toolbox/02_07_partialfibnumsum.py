## i have not solved this one yet..

def fibnumsum(num1, num):
    #every 60 f(n) last digit repeats
    if num > 60:
        num = (num) % 60

    fsum = 0
    prev, curr = 0, 1

    if num1 <= 1:
        fsum = fsum + num1
        if num <= 1:
            fsum = fsum + num


    for i in range(num+1):
        prev, curr = curr, prev % 10 + curr % 10

        if i >= num1: # and i > num-3:
            fsum = fsum + curr % 10
            print(i, curr % 10, fsum)
    return fsum % 10


def fibnumlast(num):
    if num <= 1:
        return num
    prev = 1
    curr = 1
    for i in range(num-2):
        prev, curr = curr % 10, prev % 10 + curr % 10
    return curr % 10


if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    if num1 == num2:
        print(fibnumlast(num1))
    else: print((fibnumsum(num1, num2)))
