import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    B = sorted(map(int, input().split()), reverse=True)
    W = sorted(map(int, input().split()), reverse=True)

    ans = 0
    current = 0
    for i in range(N):

        current += B[i]

        if i < M and W[i] > 0:
            current += W[i]
        
        ans = max(ans, current)

    print(ans)


if __name__ == "__main__":
    main()