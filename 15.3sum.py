
nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 1, 1]
# nums = [0, 0, 0]


results = []
nums.sort()

print(nums)

result = []

for i in range(0, len(nums)-2):


    if i>0 and nums[i] == nums[i-1]:
        continue
    idx_l, idx_r = i+1, len(nums)-1

    while idx_l < idx_r:
        sum = nums[i] + nums[idx_l] + nums[idx_r]


        if sum < 0:
            idx_l += 1
        elif sum > 0:
            idx_r -= 1
        else:
            result.append([nums[i], nums[idx_l], nums[idx_r]])

            while nums[idx_l] == nums[idx_l+1]:
                idx_l +=1

            while nums[idx_r] == nums[idx_r-1]:
                idx_r -=1

            idx_l += 1
            idx_r -= 1

print(result)









