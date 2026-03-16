"""
問題URL: https://atcoder.jp/contests/abc195/tasks/abc195_c
----------------------------------------------------
結果
・自力（21min）
----------------------------------------------------
"""
def main():
    N = input().strip()

    comma = ((len(N) - 1) // 3)

    ans = 0
    current_n = int(N)

    for i in range(comma):
        ans += (current_n - int("9" * (comma-i)*3)) * (comma-i)
        current_n = int("9" * (comma-i)*3)
    
    print(ans)


if __name__ == "__main__":
    main()