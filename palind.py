def palind(s):
    rev = ""
    for i in s:
        rev = i + rev
    if rev ==s:
        return True
    return False
print(palind("madammimmaam"))
print(palind("madamimadam"))
print(palind("ratsliveonnoevilstar"))
print(palind("amanaplanacanalpanama"))