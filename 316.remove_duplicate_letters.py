class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        from collections import Counter

        # pairs = {"a":1, "b":2, "c":2}
        pairs = Counter(s)
        print('pairs: ', pairs)

        stack = []

        for ch in s:

            pairs[ch] -= 1

            if not ch in stack:

                while stack and stack[-1] > ch and pairs[stack[-1]] != 0:
                    stack.pop()

            if ch in stack:
                continue
            stack.append(ch)

        return ''.join(stack)


s = "cbacdcbc"
result = Solution().removeDuplicateLetters(s)
print(result)  #
