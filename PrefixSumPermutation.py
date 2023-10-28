def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        A = list(map(int, input().split()))

        total_sum = (n * (n + 1)) // 2

        if A[n - 2] > total_sum:
            print("NO")
            continue

        avail = set(range(1, n + 1))
        val = -1

        for i in range(1, n - 1):
            diff = A[i] - A[i - 1]
            if diff not in avail:
                val = diff
            else:
                avail.remove(diff)

        if A[n - 2] == total_sum:
            if len(avail) == 2:
                cur_sum = sum(avail)
                if cur_sum == A[0]:
                    print("YES")
                else:
                    print("NO")
            elif len(avail) > 3:
                print("NO")
            else:
                if A[0] not in avail:
                    print("NO")
                else:
                    avail.remove(A[0])
                    cur_sum = sum(avail)
                    if cur_sum == val:
                        print("YES")
                    else:
                        print("NO")
        else:
            if len(avail) > 2:
                print("NO")
            elif A[0] not in avail:
                print("NO")
            else:
                print("YES")


if __name__ == "__main__":
    main()
