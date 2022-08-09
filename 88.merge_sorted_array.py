'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

'''
non-decreasing order의 의미: 오름차순이거나 연속된 값이 같을 수 있음 
ex) 1, 1, 2, 3 : non-decreasing order
    1, 2, 3, 4 : increasing order (ascending order)
'''

from typing import List

# re-take
'''
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3
Output: [1, 2, 2, 3, 5, 6]
'''

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# for i in range(m+n-1, -1, -1):
#
#     if m>=1 and n>=1:
#         if nums1[m-1] >= nums2[n-1]:
#             nums1[i] = nums1[m-1]
#             m -=1
#         else:
#             nums1[i] = nums2[n-1]
#             n -=1
#
#     if m>=1:
#        pass
#
#     elif n>=1:
#         nums1[i] = nums2[n-1]
#         n -=1

while m>0 and n>0:
    if nums2[n-1] >= nums1[m-1]:
        nums1[m+n-1] = nums2[n-1]
        n -=1
    else:
        nums1[m+n-1] = nums1[m-1]
        m -=1

nums1[:n] = nums2[:n]





















