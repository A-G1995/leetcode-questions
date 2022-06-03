def removeElement(nums: list, val: int) -> int:
    j = len(nums) -1
    k = 0
    i = 0
    while i <= j:
        if nums[i] == val:
            temp = nums[i]
            nums.remove(nums[i])
            nums.append(temp)
            k += 1
            j -= 1
        else:
            i += 1
    result = len(nums) -k        
    nums = nums[0:i]
    return result