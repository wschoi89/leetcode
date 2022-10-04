from collections import defaultdict
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "{[]}"
s5 = '('
s6 = ']'
s7 = "(){}}{"

def is_valid(s: str) -> bool:

    pairs = defaultdict(str)

    pairs['('] = ')'
    pairs['['] = ']'
    pairs['{'] = '}'

    stack = list()
    for ch in s:
        if len(stack) == 0 and ch in pairs.values():
            return False

        if ch in ['(', '{', '[']:
            stack.append(ch)

        elif pairs[stack[-1]] == ch:
            stack.pop()
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False


result = is_valid(s7)
print(result)





