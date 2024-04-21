from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0
    vw = []
    l = len(values)
    #num of items:3 capacity: 50
    #val weight
    # 60    20
    # 100   50
    # 120   30

    for i in range(n):
        vw.append((weights[i], values[i]))

    svw = sorted(vw, key=lambda x: (x[1]/x[0]), reverse=True)

    while capacity > 0 and l > 0:
        for w, v in svw:
            #print(w, v)
            if w >= capacity:
                value = value + (v/w)*capacity
                capacity = 0
            elif w < capacity:
                value = value + v
                capacity = capacity - w
                l = l - 1

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
