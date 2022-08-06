'''
그룹 애너그램
input = ["eat", "tea", "tan", "ate", "nat", "bat"]

output=
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat]

]
'''

'''
몇개의 그룹인지 찾고, 각 단어가 어떤 그룹에 속하는지 정보를 알아야 함 
몇개의 그룹인지는 알았음
각 단어가 어떤 그룹에 속하는지 알기 위해서는? 
'''

from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]):

    groups = defaultdict(list)

    for word in strs:
        groups[''.join(sorted(word))].append(word)

    return list(groups.values())


input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input)
print(output)