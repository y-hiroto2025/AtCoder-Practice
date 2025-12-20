"""
問題URL: https://atcoder.jp/contests/abc014/tasks/abc014_1
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
def main():
    a = int(input())
    b = int(input())
    ans = b - a % b
    if a == b:
        ans = 0
    print(ans)

if __name__ == "__main__":
    main()