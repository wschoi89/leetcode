'''
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

def intersect(nums1, nums2):
    dict1 = dict()
    result = []

    for v in nums1:
        dict1[v] = dict1.get(v, 0) + 1

    for v in nums2:
        if v in dict1 and dict1[v] >0:
            result.append(v)
            dict1[v] -=1

    print(result)
    return result

# print(int(5 / 2))
intersect(nums1, nums2)



