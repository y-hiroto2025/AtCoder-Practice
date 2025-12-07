# 問題URL: https://atcoder.jp/contests/abc207/tasks/abc207_b


def main():
    a, b, c, d = map(int, input().split())
    if b >= c*d:
        ans = -1
    else:
        num = 1
        while True:
            if (a + num * b) <= (d * num * c):
                ans = num
                break
            num += 1
    print(ans) 

if __name__ == "__main__":
    main()