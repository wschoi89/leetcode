s = "012123454321000"


def helper(s, l, r):
    while l >=0 and r<len(s) and s[l]==s[r]:
        l -=1
        r +=1
    return s[l+1:r]

def longest_palindrome(s: str):
    if len(s) < 2 or s == s[::-1]:
        return s

    result=""
    for i in range(len(s)):
        temp_1 = helper(s, i, i+1)
        temp_2 = helper(s, i, i+2)
        result = max(result, temp_1, temp_2, key=len)

    return result

a = "ccd"
print(longest_palindrome(a))