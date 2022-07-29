# https://www.hackerearth.com/practice/codemonk/

T = int(input())

for _ in range(T):
    result = -1
    _ = int(input())
    array = []
    for i in input().split(' '):
        array.append(int(i))
    # print(array)

    for i, _ in range(len(array)):
        for j in range(i, len(array)+1):
            temp = (array[i] and array[j]) ^ (array[i] or array[j])
            if temp < result:
                result = temp


(2 & 3) ^ (2 | 3)
