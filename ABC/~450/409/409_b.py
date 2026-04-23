"""
問題URL: https://atcoder.jp/contests/abc409/tasks/abc409_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    for i in range(1, N+1):
        cnt = 0

        for a in A:
            if a >= i:
                cnt += 1
        
        if cnt >= i:
            ans = max(ans, i)
    
    print(ans)
    

if __name__ == "__main__":
    main()