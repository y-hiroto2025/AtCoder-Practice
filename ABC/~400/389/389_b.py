"""
問題URL: https://atcoder.jp/contests/abc389/tasks/abc389_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
def main():
    x = int(input())
    
    num = 1
    ans = 1
    while num != x:
        num *= ans
        ans += 1
    
    print(ans-1)


if __name__ == "__main__":
    main()