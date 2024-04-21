def twosum(d1, d2):
    dsum = d1 + d2
    return dsum

if __name__ == '__main__':
    d1, d2 = map(int, input().split())
    print(twosum(d1, d2))
