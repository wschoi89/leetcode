from collections import defaultdict

def firstUniqChar(s: str) -> int:
    characters = defaultdict(int)

    for char in s:
        characters[char] +=1

    # for key in characters.keys():
    #     if characters[key] ==1:
    #         charac = key
    #         return list(s).index(charac)

    for i in range(len(s)):
        if characters[s[i]] ==1:
            return 1

    else:
        return -1