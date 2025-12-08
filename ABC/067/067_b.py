# 問題URL: https://atcoder.jp/contests/abc067/tasks/abc067_b

def main():
    bar_amount, k = map(int, input().split())
    bar_lengths = list(map(int, input().split()))

    bar_lengths.sort()

    ans = 0
    for i in range(1, k+1):
        ans += bar_lengths[-i]
    print(ans)

"""
Reviewed By AI
By arranging the sort ascending order, I can take elements easily.
In addition, I can use the slice in stead of for-loop.

bar_lengths.sort(reverses=True)
ans = barlengths[:3]
print(ans)
"""


if __name__ == "__main__":
    main()