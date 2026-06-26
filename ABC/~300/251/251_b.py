"""
問題URL: https://atcoder.jp/contests/abc251/tasks/abc251_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    num_set = set()

    for i in range(N):
        num = A[i]

        if num <= W:
            num_set.add(num)
    
    for i in range(N-1):
        for j in range(i+1, N):
            num = A[i]+A[j]

            if num <= W:
                num_set.add(num)

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                num = A[i]+A[j]+A[k]

                if num <= W:
                    num_set.add(num)
    
    print(len(num_set))


if __name__ == "__main__":
    main()