# 座標圧縮
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    T = sorted(set(A))

    ans = []

    for a in A:
        # bisect.bisect_left: aを挿入するインデックスを返す
        rank = bisect.bisect_left(T, a)
        ans.append(rank + 1)
    
    print(*ans)

if __name__ == "__main__":
    main()