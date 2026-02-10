# 配列の二分探索
def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    right = N - 1
    left = 0
    mid = (N - 1) // 2

    while left <= right:
        mid = (left + right) // 2

        if A[mid] < X:
            left = mid + 1
        elif A[mid] > X:
            right = mid - 1
        else:
            print(mid + 1)
            return

if __name__ == "__main__":
    main()