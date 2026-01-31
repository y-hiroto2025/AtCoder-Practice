"""
問題URL: https://atcoder.jp/contests/arc046/tasks/arc046_a
----------------------------------------------------
結果
・自力（10min）
----------------------------------------------------
"""
def main():
    N = int(input())
    i = 0
    ans = 0

    while i != N:
        ans += 1
        if len(set(str(ans))) == 1:
            i += 1
    
    print(ans)
    
if __name__ == "__main__":
    main()