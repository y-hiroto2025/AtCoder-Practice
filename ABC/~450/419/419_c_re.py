import sys
input = sys.stdin.readline

def main():
    N = int(input())
    
    max_r, min_r = 1, 1000000000
    max_c, min_c = 1, 1000000000

    for _ in range(N):
        R, C = map(int, input().split())

        max_r = max(max_r, R)
        min_r = min(min_r, R)
        max_c = max(max_c, C)
        min_c = min(min_c, C)
    
    print(max(max_r - min_r + 1, max_c - min_c + 1) // 2)


if __name__ == "__main__":
    main()