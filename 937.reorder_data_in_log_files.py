from typing import List

# 로그 재정렬
'''

1. 로그의 가장 앞 부분은 식별자
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 함.
4. 숫자 로그는 입력 순서대로 함. (문자는 알파벳순)

입력 : ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
출력 : ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 81 1 5 1", "dig2 3 6"]

'''


def reorder_data_in_log_files(logs: List[str]):
    pass
    # 식별자 이후 숫자, 문자 나눔

    # 숫자는 입력 순서대로

    # 문자는 alphabet 비교, alphabet 모두 동일하면 식별자 순

    list_alpha = []
    list_numeric = []

    for log in logs:
        splitted = log.split()
        # print(splitted)

        if splitted[1].isalpha():
            list_alpha.append(log)
        elif splitted[1].isnumeric():
            list_numeric.append(log)

    # print(list_alpha)
    list_alpha = sorted(list_alpha, key=lambda x: (x.split(' ')[1:], x.split(' ')[0])) # 중요
    return list_alpha + list_numeric


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# print(reorder_data_in_log_files(logs))


# lambda 표현식 이용한 예. 아래 결과값 예측 해보기
s = ['2 A', '1 B', '4 C', '1 A']
print(sorted(s))
print(sorted(s, key=lambda x:x.split()[1]))
print(sorted(s, key=lambda x:(x.split()[1], x.split()[0])))
