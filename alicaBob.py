def main():
    while True:
        try:
            n = int(input())
            a = list(map(int, input().split()))

            i = 0
            j = n - 1
            A = a[i]
            B = a[j]
            ca = 0
            cb = 0

            while True:
                if A > B:
                    j -= 1
                    B += a[j]
                    cb += 1
                elif B >= A:
                    i += 1
                    A += a[i]
                    ca += 1
                if i > j:
                    break

            print(ca, cb)

        except EOFError:
            break


if __name__ == "__main__":
    main()
