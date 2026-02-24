"""
問題URL: https://atcoder.jp/contests/abc013/tasks/abc013_b
----------------------------------------------------
結果
・自力（5min）
----------------------------------------------------
"""
def main():
    a = int(input())
    b = int(input())

    ans = min(abs(a - b), 10 - abs(a - b))
    
    print(ans)


if __name__ == "__main__":
    main()