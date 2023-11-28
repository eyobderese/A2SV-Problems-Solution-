def main():
    with open("input.txt", "r") as f:
        n, k = map(int, f.readline().split())
        lights = list(map(int, f.readline().split()))

    M = lights.copy()
    N = list(range(n))
    S = []

    for i in range(n):
        for j in range(i + 1, n):
            if M[i] < M[j]:
                M[i], M[j] = M[j], M[i]
                N[i], N[j] = N[j], N[i]

    min_light = M[k - 1]

    for i in range(k):
        S.append(N[i] + 1)

    S.sort()

    with open("output.txt", "w") as f:
        f.write(str(min_light) + "\n")
        f.write(" ".join(map(str, S)) + "\n")


if __name__ == "__main__":
    main()
