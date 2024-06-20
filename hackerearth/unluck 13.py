# https://www.hackerearth.com/practice/codemonk/

#    _ _ _
#    10 * 10 * 10 - (10 + 10) = 980
#
#
#    n = 6:
#    _ _ _ | _ _ _
#
#    Let total no of valid 3 digit strings = x
#    _ _ 1_ | 3_ _ _
#
#    Let total no of valid 2 digit strings = y
#
#    Thus total no of valid 6 digit strings = (x * x) - (y * y)   # x = 980 ; y = 99
#
#
#    n = 5:
#
#    _ _ | _ _ _
#
#    Let total no of valid 2(stupid) digit strings = x
#
#    Let total no of valid 3(stupid) digit strings = y
#
#    _ 1 | 3 _ _
#
#    Let total no of valid 1 digit string = z
#
#    No of valid 2 digit string is already x.
#
#    # x = 99; y = 980; z = 10 ;
#    Thus total valid strings - (x * y) - (z * x) = x * (y - z)
#
#
#    _ _ _ _ | _ _ _ _ _


# why mod is done on values in cache

# why question ahs 100000009 number?


cache = {}
cache2 = {}
mod = 1000000009


def ans(n):
    if (
        n < 25000
    ):  # by trial and eror to tackle memory exceed problem we are splitting cache at 25k
        if n in cache:
            return cache[n]

        if n == 0:
            cache[n] = 1
            return cache[n]
        if n == 1:
            cache[n] = 10
            return cache[n]

        temp1 = ans(n // 2)  # Split in half.
        # Split in half to find the number of times 13 appears in the middle.
        temp2 = ans(n // 2 - 1)

        if (n % 2) == 0:
            cache[n] = (temp1 * temp1 - temp2 * temp2) % mod
        else:
            temp3 = ans(n // 2 + 1)
            cache[n] = (temp1 * (temp3 - temp2)) % mod

        return cache[n]
    else:
        if n in cache2:
            return cache2[n]

        # why is n == 0 and n ==1 required here when here we are only dealing with n > 25k
        if n == 0:
            cache2[n] = 1
            return cache2[n]
        if n == 1:
            cache2[n] = 10
            return cache2[n]

        temp1 = ans(n // 2)
        temp2 = ans(n // 2 - 1)

        if (n % 2) == 0:
            cache2[n] = (temp1 * temp1 - temp2 * temp2) % mod
        else:
            temp3 = ans(n // 2 + 1)
            cache2[n] = (temp1 * (temp3 - temp2)) % mod

        return cache2[n]


inp_len = int(input())

for i in range(inp_len):
    cache2 = {}
    n = int(input())
    print(ans(n))
