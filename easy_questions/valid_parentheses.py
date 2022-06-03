def isValid(s: str) -> bool:
    flag = False
    dict = {
    '{':'}',
    '[':']',
    '(': ')'
    }
    if len(s) % 2 == 0:
        stack = []
        for i in s:
            if i in dict.keys():
                stack.append(i)
            elif len(stack) > 0:
                if i == dict.get(stack[-1]):
                    stack.pop()
                    flag = True
                else:
                    return False
            else:
                flag = False
        if len(stack) != 0:
            return False
            
    return flag