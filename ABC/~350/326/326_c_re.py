import sys
import bisect
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans = max(ans, bisect.bisect_left(A, A[i]+M) - i)
    
    print(ans)


if __name__ == "__main__":
    main()