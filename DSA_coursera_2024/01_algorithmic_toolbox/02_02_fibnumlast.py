def fibnumlast(num):
    if num <= 1:
        return num
    prev = 1
    curr = 1
    for i in range(num-2):
        prev, curr = curr % 10, prev % 10 + curr % 10
    return curr % 10


if __name__ == '__main__':
    print(fibnumlast(int(input())))
