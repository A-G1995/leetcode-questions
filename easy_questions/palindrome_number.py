def isPalindrome(x: int) -> bool:
    new_int = str(x)[::-1]
    if str(x) == new_int:
        return True
    else:
        return False