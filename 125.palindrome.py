from coding_interview.utils import my_timer
str1 = "A man, a plan, a canal: Panama"*10000

# 1. list로 변환
@my_timer
def is_palindrome_1(s: str) -> bool:
    str = []
    for char in s:
        if char.isalnum():
            str.append(char.lower())

    while len(str) > 1:
        if str.pop(0) != str.pop():
            return False

    return True

# 2. deque 자료형 사용
'''
deque은 내부적으로 doubly linked list
접근 : O(n) (list는 O(1))
처음 삽입/삭제 : O(1) (list는 O(n), 나머지 노드들 옮겨야 함 )
'''
@my_timer
def is_palindrome_2(s:str) -> bool:
    from collections import deque
    str = deque()
    for char in s:
        if char.isalnum():
            str.append(char.lower())

    while len(str) > 1:
        if str.popleft() != str.pop():  # popleft(): O(1)
            return False

    return True


# 3. 정규식 및 slicing 사용
'''
정규식
- [] : 문자 클래스로 [] 사이의 문자들과 매치
- [a-z] : 소문자 알파벳과 매치
- [a-zA-Z] : 알파벳 모두
- [0-9] : 숫자 모두 
- [^a-z] : 소문자 알파벳을 제외한 문자와 매치 
'''
@my_timer
def is_palindrome_3(s:str) -> bool:
    import re
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s) # 숫자 문자가 아닌 문자열을 공백으로 변환
    return s==s[::-1]


is_palindrome_1(str1)
is_palindrome_2(str1)
is_palindrome_3(str1)