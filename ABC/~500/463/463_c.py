"""
問題URL: https://atcoder.jp/contests/abc463/tasks/abc463_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    h_l = []
    for _ in range(N):
        h, l = map(int, input().split())
        h_l.append((h, l))
    
    h_l.sort(reverse=True)

    Q = int(input())
    T = list(map(int, input().split()))
    T_sorted = sorted(T)

    idx = 0
    ans = {}

    for i in range(Q):

        while (idx < N) and (h_l[idx][1] <= T_sorted[i] + 0.5):
            idx += 1
        
        if (idx < N) and (h_l[idx][1] >= T_sorted[i] + 0.5):
            ans[T_sorted[i]] = h_l[idx][0]
    
    
    for i in range(Q):
        print(ans[T[i]])



if __name__ == "__main__":
    main()