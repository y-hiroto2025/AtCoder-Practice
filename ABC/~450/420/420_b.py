"""
問題URL: https://atcoder.jp/contests/abc420/tasks/abc420_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline
from collections import Counter

def main():
    N, M = map(int, input().split())

    s = list(zip(*[input().strip() for _ in range(N)]))
    scores = [0] * N

    for i in range(M):
        count = Counter(s[i])
        
        if count["0"] < count["1"]:
            minority = "0"
        else:
            minority = "1"

        for j in range(N):
            if s[i][j] == minority:
                scores[j] += 1
    
    ans = [x+1 for x in range(N) if scores[x] == max(scores)]

    print(*ans)



if __name__ == "__main__":
    main()