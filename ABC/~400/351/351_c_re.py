import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ball = []

    for i in range(N):
        ball.append(A[i])
        while len(ball) > 1 and ball[-1] == ball[-2]:
            ball.pop(-1)
            ball[-1] += 1
            
    print(len(ball))


if __name__ == "__main__":
    main()