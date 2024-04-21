def moneychange(num):
    count = 0
    while num > 0:
        if num >= 10:
            num = num - 10
            count += 1
        elif num >= 5:
            num = num - 5
            count += 1
        else:
            count = count + num
            num = 0
    return count


if __name__ == '__main__':
    print(moneychange(int(input())))
