"""
問題URL: https://atcoder.jp/contests/abc413/tasks/abc413_c
----------------------------------------------------
----------------------------------------------------
"""
import sys
input = sys.stdin.readline
from collections import deque

def main():
    Q = int(input())

    A = deque()

    for _ in range(Q):
        q = list(map(int, input().split()))

        if q[0] == 1:
            A.append([q[2], q[1]])
        
        else:
            k = q[1]
            ans = 0

            while k > 0:
                x = A[0][0]
                c = A[0][1]
                
                if c <= k:
                    ans += x * c
                    k -= c
                    A.popleft()
                
                else:
                    ans += x * k
                    A[0][1] -= k
                    k = 0
            
            print(ans)
            

if __name__ == "__main__":
    main()