from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0

    sfs = sorted(first_sequence, reverse=True)
    sss = sorted(second_sequence, reverse=True)

    for i in range(n):
        #print(i)
        max_product = max_product + sfs[i]*sss[i]

    #print(sfs,sss)

    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))