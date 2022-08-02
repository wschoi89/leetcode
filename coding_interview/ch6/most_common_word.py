"""
04. 가장 흔한 단어
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력
대소문자 구분하지 않으며, 구두점 무시

입력 : paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

출력 : "ball"
"""
import collections
from typing import List
import re


def most_common_word(paragraph: str, banned: List[str]):

    print(re.sub('[^\w]', ' ', paragraph), type(re.sub('[^\w]', '', paragraph))) # paragraph에서 word가 아닌것들 제거
    words = [word for word in (re.sub('[^\w]', ' ', paragraph).lower().split()) if word not in banned]
    # print(words)

    counts = collections.defaultdict(int)
    for word in words:
        counts[word] +=1
        # print(counts)

    # print(max(counts, key= lambda k: counts[k]))



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

most_common_word(paragraph, banned)

from collections import defaultdict

from collections import Counter

counter = Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(counter.most_common()) # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
print(counter.most_common(1)) # [('l', 3)]
print(counter.most_common(1)[0]) # ('l', 3)
print(counter.most_common(1)[0][0]) # l