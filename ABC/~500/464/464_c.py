"""
問題URL: https://atcoder.jp/contests/abc464/tasks/abc464_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    records = []
    color_dict = {i: 0 for i in range(1, N+1)}
    ans = 0

    for i in range(N):
        a, d, b = map(int, input().split())
        records.append((d,a,b))
        color_dict[a] += 1

        if color_dict[a] == 1:
            ans += 1
    
    records.sort()
    idx = 0

    for i in range(M):

        while idx < N and records[idx][0] == i+1:
            a = records[idx][1]
            b = records[idx][2]

            if a != b:
                color_dict[a] -= 1

                if b not in color_dict:
                    color_dict[b] = 1
                else:
                    color_dict[b] += 1

                if color_dict[a] == 0:
                    ans -= 1
                if color_dict[b] == 1:
                    ans += 1

            idx += 1

        print(ans)


if __name__ == "__main__":
    main()