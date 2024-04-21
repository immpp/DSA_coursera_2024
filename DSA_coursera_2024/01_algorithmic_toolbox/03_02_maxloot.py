from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0
    vw = []
    dic = {}
    # write your code here
    print(capacity)

    for i in range(n):
        vw.append(values[i]/weights[i])

    for d in vw:
        dic[weights[d]] = vw[d]

    print(dic)

    for k in range(n):
        if capacity == 0:
            return value
        else:
            a = max(vw)
            if weights[k] >= capacity:
                value = vw[k]*capacity
                capacity = 0
                return value


if __name__ == "__main__":
    #data = input()
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    print(data)
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
    #print(opt_value)

