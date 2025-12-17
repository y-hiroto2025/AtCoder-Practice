def main():
    N, K = map(int, input().split())
    ans = 0

    """
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if i + j + k == K:
                    ans += 1
    """
    # ３枚目には K-i-j が書かれる
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            k = K - i - j
            if 1 <= k <= N:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()