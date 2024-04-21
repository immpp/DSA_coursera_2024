def maxpair(l2):
    x = sorted(l2, reverse=True)
    return (x[0]*x[1])

if __name__ == '__main__':
    l1 = int(input())
    l2 = list(map(int, input().split()))
    print(maxpair(l2))

