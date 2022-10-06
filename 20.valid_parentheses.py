from collections import defaultdict
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "{[]}"
s5 = '('
s6 = ']'
s7 = "(){}}{"


def is_valid(s: str) -> bool:
    bracket_pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []
    for ch in s:
        if ch in bracket_pairs.values():
            stack.append(ch)

        elif len(stack) == 0 or bracket_pairs[ch] != stack.pop():
            return False

    return len(stack) == 0


result = is_valid(s7)
print(result)





