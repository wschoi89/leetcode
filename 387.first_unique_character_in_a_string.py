s = 'leetcode'



def first_uniq_char(s: str)->int:

    from collections import Counter
    counter = Counter(s)

    for i in range(len(s)):
        if counter.get(s[i]) ==1:
            return i

    return -1

print(first_uniq_char(s))