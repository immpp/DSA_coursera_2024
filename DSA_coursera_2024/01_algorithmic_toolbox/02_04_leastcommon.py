def lcm(num1, num2):
    num3 = num1 * num2
    while num2 > 0:
        ans = num1 % num2
        num1 = num2
        num2 = ans
        # print(num1, num2)
        if num2 == 0: return int(num3/num1)


if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    print(lcm(num1, num2))
