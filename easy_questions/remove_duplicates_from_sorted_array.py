def removeDuplicates(nums: list) -> int:
    i = 0
    k = 0
    j = len(nums) - 1
    while i < j:
        if len(nums) != 1:
            if nums[i] == nums[i+1]:
                k += 1
                nums.remove(nums[i])
                nums.append(nums[i])
                j -= 1
            else:
                i += 1
        else:
            break
    result = len(nums) - k
    nums = nums[0:k]
    return result  