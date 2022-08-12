def isIsomorphic(s: str, t: str) -> bool:
    first_map = {

    }
    second_map = {

    }
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        first_map[s[i]] = t[i]
    for i in range(len(t)):
        second_map[t[i]] = s[i]
    if list(first_map.values()) == list(second_map.keys()):
        return True
    else:
        return False
print(isIsomorphic("add", "egg"))
        