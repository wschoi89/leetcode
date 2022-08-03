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

def group_anagrams(input: List[str]):

        dict_ = defaultdict(int)
        for word in input:
            # print(word)
            # print(list(word))
            dict_[''.join(sorted(list(word)))] +=1

        # print(dict_)

        num_groups = len(list(dict_.keys()))
        # print(num_groups)

        result = defaultdict(list)
        # print('result: ', result)

        for word in input:
            sorted_word = ''.join(sorted(list(word)))
            if sorted_word in dict_.keys():
                result[sorted_word].append(word)

        # print(result)
        # print(list(result.values()))

        return list(result.values())


input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input)
print(output)