def lengthOfLastWord(s: str):
    if len(s) == 1:
            return len(s)
    result = s.split(" ")
    result.reverse()
    for i in result:
        if i == "":
            continue
        else:
            return len(i)