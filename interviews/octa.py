# Input: s = "babad"
# Output: "bab"


def longest_palindrome(input):
    for i in range(len(input)):
        for j in range(len(input), i, -1):
            # check using utility if palindrome:
            if utility(input, i, j):  # it returns if it is palindrome
                return input[i : j + 1]


def utility(s, l, r):
    while l >= 0 and r <= len(s) and s[l] == s[r]:
        l -= 1
        r += 1

    if True:
        pass
    return True


# babad
# i  = 0, j = 5 utility(s,0,5)
# i = 0, j = 4, utility(s,0,4)
# i = 0, j =3, utility(s,0,3)


# s = s, l =0, r =3
#
