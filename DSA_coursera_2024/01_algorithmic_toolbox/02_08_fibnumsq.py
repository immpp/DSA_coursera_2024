def fibnumsqr(num):
    if num > 60:
        num = num % 60

    if num <= 1:
        return num
    prev = 1
    curr = 1
    for i in range(num-2):
        prev, curr = curr , prev % 10 + curr % 10
        #print(prev, curr)
    return (curr * (curr + prev)) % 10


if __name__ == '__main__':
    print(fibnumsqr(int(input())))