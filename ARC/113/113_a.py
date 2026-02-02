"""
問題URL: https://atcoder.jp/contests/arc113/tasks/arc113_a
----------------------------------------------------
----------------------------------------------------
"""
def main():
    K = int(input())
    ans = 0
    for a in range(1, K + 1):
        for b in range(1, (K//a) + 1):
            c = K // (a * b)
            ans += c
    print(ans)


if __name__ == "__main__":
    main()