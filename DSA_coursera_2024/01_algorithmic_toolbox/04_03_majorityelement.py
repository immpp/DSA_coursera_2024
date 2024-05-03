def majority_element(elements):
    dict = {}
    for e in elements:
        if e not in dict:
            dict[e] = 1
        else:
            dict[e] = dict[e] + 1

    #sdict = sorted(dict, reverse=True)
    km = max(dict.values())

    #print(dict, max(dict), len(elements), km)

    if km > len(elements)/2:
        return 1
    else: return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))