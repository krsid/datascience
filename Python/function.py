def name(str):
    rev = ""
    for i in range(len(str)-1, -1, -1):
        rev = rev + str[i]

    if rev == str:
        return "Your name is a pallindrome"
    else:
        return "Your name is not a pallindrome"

print(name("NAMAN"))
print(name("ARRAY"))