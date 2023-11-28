def reversWord(L):
    # Lstring = ''.join(L)
    # LWordList = Lstring.split()
    # LWordList = LWordList[::-1]
    # LWordList = (' '.join(LWordList)).strip()
    # LWordList = list(LWordList)
    n = len(L)
    LWordList = []
    j = 0
    for i in range(n):
        if L[i] == " ":
            word = [" "] + L[j:i]
            LWordList = word + LWordList
            j = i+1
    word = L[j:]
    LWordList = word + LWordList

    print(LWordList)


reversWord(["t", "h", "e", " ", "s", "k", "y",
           " ", "i", "s", " ", "b", "l", "u", "e"])
