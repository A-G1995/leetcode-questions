def answerQueries(nums: list, queries):
    nums.sort()
    temp = []
    result = []
    for query in queries:
        for number in nums:
            if query >= number:
                temp.append(number)
                query -= number
            else:
                break
        result.append(len(temp))
        temp.clear()
    return result




#answerQueries([469781,45635,628818,324948,343772,713803,452081], [816646,929491])
answerQueries([4,5,2,1], [3,10,21])               

