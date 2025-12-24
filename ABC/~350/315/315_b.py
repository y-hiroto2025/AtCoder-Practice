"""
問題URL: https://atcoder.jp/contests/abc315/tasks/abc315_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    m = int(input())
    D = list(map(int, input().split()))

    day = (sum(D) + 1) // 2
    day_count = 0

    for i in range(0, m):
        day_count += D[i]
        if day <= day_count:
            month = i + 1
            break

    day -= (day_count - D[i])

    print(month, day)

if __name__ == "__main__":
    main()