"""
問題URL: https://atcoder.jp/contests/abc032/tasks/abc032_a
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
def main():
    a = int(input())
    b = int(input())
    n = int(input())

    ans = n
    while ans % a != 0 or ans % b != 0:
        ans += 1

    print(ans)

if __name__ == "__main__":
    main()