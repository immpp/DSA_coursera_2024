#0, 1, 1,[ 2, 3, 5, 8]

def fibnum(num):
    fibbi = [0,1,1]
    if num <= 1:
        return num
    else:
        for i in range(num-2):
            #print(i, num)
            fibbi.append(fibbi[-1] +fibbi[-2])
    return fibbi[-1]

if __name__ == '__main__':
    print(fibnum(int(input())))