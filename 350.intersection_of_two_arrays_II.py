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
result = []
key_map = dict()


for i, v in enumerate(nums1):
    key_map[v] = key_map.get(v, 0) + 1

print(key_map)

for i in nums2:
    if i in key_map.keys() and key_map[i]>0:
        result.append(i)
        key_map[i] -=1






