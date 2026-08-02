"""
問題URL: https://atcoder.jp/contests/abc466/tasks/abc466_c
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N = int(input())

    ans = 0
    right = 1

    for left in range(1, N):
        if right < left:
            right = left

        while right < N:
            print("?", left, right+1, flush=True)
            response = input().strip()

            if response == "Yes":
                right += 1
            else:
                break

        ans += (right - left)

    print("!", ans, flush=True)


if __name__ == "__main__":
    main()