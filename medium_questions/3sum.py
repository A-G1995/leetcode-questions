def threeSum(nums):
    result = [[]]
    my_hash = {}
    for i in nums:
        my_hash[i] = -i
    for i in nums:
        if i in my_hash.keys() and my_hash[i] in nums:
            result.append([i,-i])
    print(result)
threeSum([-1,0,1,2,-1,-4])