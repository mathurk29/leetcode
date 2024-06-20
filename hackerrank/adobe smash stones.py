# adobe-1 (1).png
# adobe-1 (2).png


# following attempt is incorrect :(


from functools import reduce

lst = [6, 27, 17, 17, 27, 67, 88, 82, 65, 41, 87, 22, 63, 22, 65, 10, 16, 3, 74, 25]

lst.sort(reverse=True)

reduce(lambda x, y: y - x, lst)

for _ in range(len(lst) - 1):
    x = lst.pop()
    y = lst.pop()

    temp = x - y
    lst.append(temp)
    lst.sort()

print(lst)


#
