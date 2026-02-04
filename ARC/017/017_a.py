"""
問題URL: https://atcoder.jp/contests/arc017/tasks/arc017_1
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N = int(input())
    ans = "YES"
    if N == 1:
        ans = "NO"
    else:
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                ans = "NO"
                break
    
    print(ans)

if __name__ == "__main__":
    main()