s = "cbacdcbc"

from collections import Counter

counter = Counter(s)
seen = set()
stack = []

for ch in s:
    counter[ch] -=1

    if ch in seen:
        continue

    # 뒤에 붙일 문자가 남아있다면 스택에서 제거
    while stack and ch < stack[-1] and counter[stack[-1]] > 0:
        seen.remove(stack.pop())

    stack.append(ch)
    seen.add(ch)

print(''.join(stack))



