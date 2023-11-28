def main():
    a = input()
    b = input()

    check = True
    diff = 0
    sza = len(a)
    szb = len(b)

    if sza != szb:
        print("NO")
        return
    else:
        index = []
        for i in range(sza):
            if a[i] != b[i]:
                diff += 1
                index.append(i)

        if diff == 2:
            if a[index[0]] != b[index[1]] or a[index[1]] != b[index[0]]:
                check = False
        else:
            check = False

    if check:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
