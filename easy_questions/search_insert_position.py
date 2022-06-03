def searchInsert(nums: list, target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if nums[i] > target:
                    return i
                else:
                    return len(nums)
            elif target > nums[i]:
                continue
            else:
                return i
