from typing import List
from coding_interview.utils import my_timer
string = ['a', 'b', 'c'] * 100000


@my_timer
def reverse_string_1(s: List[str]) -> None:
    first = 0
    last = len(s)-1

    while first < last:
        s[last], s[first] = s[first], s[last]
        first += 1
        last -= 1


@my_timer # 가장 빠름
def reverse_string_2(s: List[str]) -> None:
    s.reverse()


@my_timer
def reverse_string_3(s: List[str]) -> None:
    s[:] = s[::-1]


str_1 = string.copy()
reverse_string_1(str_1)

str_2 = string.copy()
reverse_string_2(str_2)

str_3 = string.copy()
reverse_string_3(str_3)



