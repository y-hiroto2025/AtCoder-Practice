"""
問題URL: https://atcoder.jp/contests/abc323/tasks/abc323_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    scores = [0] * N
    max_score = 0
    unsolves = []

    for i in range(N):
        s = input().strip()
        unsolve = []

        for j in range(M):

            if s[j] == "o":
                scores[i] += A[j]
            else:
                unsolve.append(j)
        
        scores[i] += i+1
        max_score = max(max_score, scores[i])
        unsolves.append(unsolve)
    

    for i in range(N):
        if scores[i] == max_score:
            print(0)
            continue

        unsolve_score = sorted([A[x] for x in unsolves[i]], reverse=True)

        curr_score = scores[i]

        for j in range(len(unsolve_score)):
            curr_score += unsolve_score[j]
            if curr_score >= max_score:
                print(j + 1)
                break


if __name__ == "__main__":
    main()