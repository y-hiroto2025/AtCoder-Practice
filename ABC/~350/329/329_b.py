"""
問題URL: https://atcoder.jp/contests/abc329/tasks/abc329_b
----------------------------------------------------
結果
・自力（5min）

解法ポイント、学び
・set()ではソートされない。
----------------------------------------------------
"""
def main():
    N = int(input())
    A = list(map(int, input().split()))
    """A = list(set(A))
    A.sort()
    print(A[-2])"""
    print(sorted(set(A))[-2])
    

if __name__ == "__main__":
    main()