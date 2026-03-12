"""
問題URL: https://atcoder.jp/contests/abc381/tasks/abc381_c
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N = int(input())
    S = input().strip()

    ans = 0
    for i in range(N):
    
        if S[i] == "/":
            d = 1

            while (i-d >= 0 and i+d < N) and (S[i-d] == "1" and S[i+d] == "2"):
                d += 1
            
            ans = max(ans, d*2 - 1)
    
    print(ans)


if __name__ == "__main__":
    main()