def longest_palindromic_substring(s):
    n = len(s)
    if n < 2:
        return s

    # Initialize the DP table
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for substrings of length greater than 2
    for length in range(3, n + 1):
        # i starts from 0 and can go  up to n - length included
        for i in range(n - length + 1):
            # -1 becuase the ith element is also included
            j = i + length - 1
            # Check if the current substring is a palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length

    # Return the longest palindromic substring
    return s[start : start + max_length]


# Example usage
input_string = "babad"
print(
    longest_palindromic_substring(input_string)
)  # Output can be "bab" or "aba"
