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

     word = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
     # 위 표현을 아래로 풀어서 작성할 수 있음
     # para = re.sub('[^\w]', ' ', paragraph) # string
     # para = para.lower().split() # list
     # word = [word for word in para if word not in banned]

     counter = collections.Counter(word)

     return counter.most_common(1)[0][0]
    # counter.most_common(1) ('ball', 2)


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

most_common_word(paragraph, banned)
