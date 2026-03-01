nums = [3,2,2,3]
val = 3

counter = 0
for x in nums:
    if x!=val:
        nums[counter] = x
        counter += 1
    print('done')