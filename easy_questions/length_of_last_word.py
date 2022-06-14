def lengthOfLastWord(s: str):
    if len(s) == 1:
        return len(s)
    result = s.split(" ")
    for i in result:
        if i == "":
            result.remove(i)
        else:    
            i = i.strip()
    return result[-1]    

print(lengthOfLastWord("   fly me   to   the moon  "))