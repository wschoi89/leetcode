s = "abacb"

from collections import Counter

# pairs = {"a":1, "b":2, "c":2}
pairs = Counter(s)
print('pairs: ', pairs)

# print([k>'b' for k, v in pairs.items() if pairs[k]==1])
# print(all([k>'b' for k, v in pairs.items() if pairs[k]==1]))

stack = []

for ch in s:

    pairs[ch] -= 1

    if not ch in stack:

        while stack and stack[-1] > ch and pairs[stack[-1]] != 0:
            stack.pop()

    if ch in stack:
        continue
    stack.append(ch)

print(stack)
