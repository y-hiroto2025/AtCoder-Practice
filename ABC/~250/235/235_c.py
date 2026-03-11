"""
問題URL: https://atcoder.jp/contests/abc235/tasks/abc235_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    a = list(map(int, input().split()))

    num_dict = {}
    for i in range(N):
        a_i = a[i]
        if a_i not in num_dict:
            num_dict[a_i] = [i+1]
        else:
            num_dict[a_i].append(i+1)

    for _ in range(Q):
        x, k = map(int, input().split())
        
        if x in num_dict and len(num_dict[x]) >= k:
            print(num_dict[x][k-1])
        else:
            print(-1)


if __name__ == "__main__":
    main()