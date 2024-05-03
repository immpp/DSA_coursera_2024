def binary_search(keys, query):
    # write your code here

    left = 0
    right = len(keys) - 1
    #print(keys, query)

    while right >= left:
        middle = round((left + right)/2)
        #print(middle)
        #print(keys[middle])
        #print(left)
        if keys[middle] == query:
            if keys[middle] == keys[middle - 1] and middle > 0:
                right = middle
                #print('try')
            else:
                return middle
        elif keys[middle] < query:
            left = middle + 1
        else: right = middle - 1
    return - 1



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        #print(q)
        print(binary_search(input_keys, q), end=' ')