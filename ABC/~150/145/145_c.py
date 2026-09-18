"""
問題URL: https://atcoder.jp/contests/abc145/tasks/abc145_c
----------------------------------------------------
結果
・12min
----------------------------------------------------
"""
import sys
from itertools import permutations

input = sys.stdin.readline

def main():
    N = int(input())    
    cities = []

    for _ in range(N):
        x, y = map(int, input().split())
        cities.append((x,y))

    comb = list(permutations(cities))

    ans = 0

    for c in comb:

        for i in range(N-1):
            city1 = c[i]
            city2 = c[i+1]

            length = ((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2) ** 0.5

            ans += length
    
    num = 2
    while num <= N:
        ans /= num
        num += 1

    print(ans)


if __name__ == "__main__":
    main()