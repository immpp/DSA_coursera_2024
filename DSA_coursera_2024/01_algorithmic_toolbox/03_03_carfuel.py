from sys import stdin


def min_refills(distance, tank, stops):
    #write your code here
    #distance between cities: 950
    #distance travel on full tank: 400
    #num of gas stations: 4
    #gas station distances: 200 375 550 750
    count = 0
    dist = tank
    full = [0] + stops + [distance]
    print(full)

    #while distance > 0:



    for i in full:
        if i > 0:
            if full[i-1] + full[i] > dist:
                dist = dist + tank
                count = count + 1
        elif


    for i in range(len(stops)):
        if tank >= distance:
            count = 0
            break
        elif full[i] > tank:



            except: dist = dist + stops[i]
        else:
            print(count)



    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))