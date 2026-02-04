"""
問題URL: https://atcoder.jp/contests/abc411/tasks/abc411_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    mass = [True]* N # True: 白い状態
    current_ans = 0
    ans_list = []

    for i in range(Q):
        if A[i] == 1:
            if mass[A[i] - 1] and mass[A[i]]:
                current_ans += 1
            elif not mass[A[i] - 1] and mass[A[i]]:
                current_ans -= 1
        
        elif A[i] == N:
            if mass[A[i] - 1] and mass[A[i] - 2]:
                current_ans += 1
            elif not mass[A[i] - 1] and mass[A[i] - 2]:
                current_ans -= 1
        
        else:
            if mass[A[i] - 1] and mass[A[i]] and mass[A[i] - 2]:
                current_ans += 1
            elif mass[A[i] - 1] != mass[A[i] - 2] and mass[A[i] - 1] != mass[A[i]]:
                current_ans -= 1
        
        mass[A[i] - 1] = not mass[A[i] - 1]

        ans_list.append(current_ans)
    print(*ans_list, sep="\n")


if __name__ == "__main__":
    main()