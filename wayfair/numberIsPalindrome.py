def isPalindrome(x: int):
    original = x
    reverse = 0

    while x:
        reverse = reverse * 10 + x % 10
        x = x // 10
    
    return reverse == original

# Time complexity: O(log(n))

# Space complexity: O(1)

assert isPalindrome(1) == True# True