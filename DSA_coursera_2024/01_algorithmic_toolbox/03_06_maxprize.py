def optimal_summands(n):
    summands = []
    i = 1

    # write your code here
    while sum(summands) <= n:
        #print(n, summands)
        #print('stuck')
        if i + sum(summands) <= n:
            summands.append(i)
            i = i + 1
        elif i + sum(summands) > n:
            #print(summands[-1], n, i)
            summands[-1] = n - sum(summands[:-1])
            break

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
