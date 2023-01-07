def summaryRanges(nums: list) -> list:
    start, current, end = nums[0], nums[0], None 
    output = []
    for num in nums[1:]:
        current += 1
        if num == current:
            end = num
        else:
            if not end:
                output.append(str(start))
            else:
                output.append(str(start) + "->" + str(end))
            start = num
            current = num
            end = None
    if not end:
        output.append(str(start))
    else:
        output.append(str(start) + "->" + str(end))

        
summaryRanges([0,1,2,4,5,7])
