"""
問題URL: https://atcoder.jp/contests/abc377/tasks/abc377_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    Q, R = [], []
    for _ in range(N):
        q, r = map(int, input().split())
        Q.append(q)
        R.append(r)
    
    Ques = int(input())
    for _ in range(Ques):
        t, d = map(int, input().split())

        t -= 1
        b, c = d // Q[t], d % Q[t]
        if c <= R[t]:
            a = b
        else:
            a = b + 1
        
        ans = a * Q[t] + R[t]

        print(ans)


if __name__ == "__main__":
    main()