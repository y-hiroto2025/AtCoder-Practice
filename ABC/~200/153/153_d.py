"""
問題URL: https://atcoder.jp/contests/abc153/tasks/abc153_d
----------------------------------------------------
結果
・9min
----------------------------------------------------
"""
def main():
    H = int(input())

    num = 1
    ans = 0
    while num < H:
        num *= 2
        ans += num

    if num != H:
        ans = ans // 2
    else:
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()