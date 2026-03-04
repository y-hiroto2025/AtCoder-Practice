def main():
    N, Q = map(int, input().split())
    S = input().strip()


    prefix = [0] * N
    for i in range(1, N):
        if S[i] == S[i-1]:
            prefix[i] = prefix[i-1] + 1
        else:
            prefix[i] = prefix[i-1]

    for _ in range(Q):
        l, r = map(int, input().split())
        print(prefix[r-1] - prefix[l-1])


if __name__ == "__main__":
    main()