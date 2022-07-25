def firstUniqChar(s: str) -> int:
    dict_ = dict()

    for char in s:
        dict_[char] = dict_.get(char, 0) + 1

    for i in list(dict_.keys()):
        if dict_[i] == 1:
            return s.index(i)

    return -1