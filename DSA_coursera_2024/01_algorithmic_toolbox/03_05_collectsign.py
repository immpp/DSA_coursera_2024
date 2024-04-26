from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    n = len(segments)
    #print('n', n)

    while n > 0:
        dict = {}

        for s in sorted(segments, reverse=True):
            for i in range(s.start, s.end+1):
                if i not in dict:
                    dict[i] = 1
                else:
                    dict[i] = dict[i] + 1

        maxd = max(dict, key=lambda x: dict[x])
        if maxd not in points: points.append(maxd)
        #print(dict)
        for s in sorted(segments, reverse=True):
            #print(s)
            if maxd in range(s.start, s.end+1):
                #print(maxd, range(s.start, s.end+1))
                n = n - 1
                segments.remove(s)
            elif s == segments[-1]:
                dict[maxd] = 0

    return sorted(points)


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
