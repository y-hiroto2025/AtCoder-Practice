import sys
input = sys.stdin.readline

def main():
    N = int(input())
    C = sorted(map(int, input().split()))

    ans = C[0]
    for i in range(1, N):
        ans *= C[i] - i
        ans %= 10**9 + 7
    
    print(ans)


if __name__ == "__main__":
    main()