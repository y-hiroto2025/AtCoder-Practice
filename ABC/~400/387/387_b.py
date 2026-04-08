"""
問題URL: https://atcoder.jp/contests/abc387/tasks/abc387_b
----------------------------------------------------
結果
・自力（2min）
----------------------------------------------------
"""
def main():
    x = int(input())

    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i*j != x:
                ans += i*j
    
    print(ans)


if __name__ == "__main__":
    main()