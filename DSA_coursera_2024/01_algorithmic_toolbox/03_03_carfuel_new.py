from sys import stdin


def min_refills(distance, tank, stops):
    #write your code here
    #distance between cities: 950
    #distance travel on full tank: 400
    #num of gas stations: 4
    #gas station distances: 200 375 550 750
    count = 0
    full = [0] + stops + [distance]
    prev, curr, next = 0, 0, 0

    for i in range(len(full)):
        #print(full[i])
        #print(full[-2])
        try:
            next = full[i+1]
            curr = full[i]
            if curr - prev > tank or next - curr > tank:
                count = -1
                break
            elif next - prev > tank:
                #print(curr, prev, count)
                prev = full[i]
                count = count + 1
            else:
                continue
        except: break

    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
