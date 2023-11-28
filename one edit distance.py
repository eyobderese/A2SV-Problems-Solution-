def edit(t, s):

    n1 = len(t)
    n2 = len(s)
    count = 0
    if abs(n1-n2) > 1 or (n1 == 0 and n2 == 0):
        return False

    if n1 < n2:
        return edit(s, t)
    i = 0
    j = 0

    while i < n1 and j < n2:

        if t[i] != s[j] and n1 == n2:
            count += 1
            if count > 1:
                return False
            i += 1
            j += 1
        elif t[i] != s[j]:
            count += 1
            if count > 1:
                return False
            i += 1
        else:
            i += 1
            j += 1
    return True


print(edit('', 'a'))
