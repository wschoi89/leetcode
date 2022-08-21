

#
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numDuplicates' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY name
#  2. INTEGER_ARRAY price
#  3. INTEGER_ARRAY weight
#

def numDuplicates(name, price, weight):
    num_dupl = 0
    products = zip(name, price, weight)

    unique = dict()

    for product in products:
        unique[product] = unique.get(product, 0) + 1

    for k, v in unique.items():
        if v >= 2:
            num_dupl += v - 1

    return num_dupl

#
def getMin(s):
    only_right_paren = 0
    stack = 0


    while s[only_right_paren] == ')':
        only_right_paren +=1

    for paren in s[only_right_paren:]:
        if paren=='(':
            stack += 1
        elif stack >0 and paren == ')':
            stack -=1

        else:
            only_right_paren += 1

    return only_right_paren + abs(stack)


# 3
#
# Complete the 'countPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER k
#

def countPairs(numbers, k):
    # Write your code here

    numbers.sort()
    set_ = set(numbers)

    num_pairs = 0

    for i in set_:
        remain = i + k

        if remain in set_:
            num_pairs += 1
    return num_pairs


# 4
def slotWheels(history):
    total_stops = 0

    for j in range(len(history[0])):
        highest_value = 0
        for i in range(len(history)):
            # print(f'{i}th spin')
            history[i] = [int(x) for x in history[i]]
            # print('max : ', max(history[i]))
            highest_value = max(highest_value, max(history[i]))
            # print('hightest_value: ', highest_value)

        for i in range(len(history)):
            history[i].remove(max(history[i]))
        total_stops += highest_value
        # print('total_stop:' ,total_stops)
    return total_stops

## 5
def getUsernames(threshold):
    import requests
    import json

    list_users = []

    url = 'https://jsonmock.hackerrank.com/api/article_users/search?page=1'

    response = requests.get(url)
    result = json.loads(response.content)

    total_pages = int(result['total_pages'])
    data = result['data']
    for user in data:
        user_name = user['username']
        submission_count = int(user['submission_count'])
        if submission_count > threshold:
            list_users.append(user_name)

    if total_pages == 1:
        return list_users

    for page in range(2, total_pages + 1):
        url = 'https://jsonmock.hackerrank.com/api/article_users/search?page=' + str(page)

        response = requests.get(url)
        result = json.loads(response.content)
        data = result['data']
        for user in data:
            user_name = user['username']
            submission_count = int(user['submission_count'])
            if submission_count > threshold:
                list_users.append(user_name)