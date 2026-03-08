import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ball = sorted([(A[i], i+1) for i in range(N)])

    for _ in range(Q):
        K = int(input())
        B = set(map(int, input().split()))

        for a in ball:

            if a[1] not in B:
                print(a[0])

                break

if __name__ == "__main__":
    main()