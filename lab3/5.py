def Perm(text):
    for i in range(len(text)):
        if len(text) == 1:
            return text
    result = []
    for i in range(len(text)):
        current = text[i]
        remaining = text[:i] + text[i+1:]
        perms = Perm(remaining)
        for j in range (len(perms)):
            result.append(current + perms[j])
    return result
text="abc"
print(Perm(text))
