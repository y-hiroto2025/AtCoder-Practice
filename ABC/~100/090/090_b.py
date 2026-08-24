"""
問題URL: https://atcoder.jp/contests/abc090/tasks/abc090_b
----------------------------------------------------
結果
・2min
----------------------------------------------------
"""
def main():
    A, B = map(int, input().split())

    ans = 0

    for i in range(A, B+1):
        num_str = str(i)

        if num_str == num_str[::-1]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()