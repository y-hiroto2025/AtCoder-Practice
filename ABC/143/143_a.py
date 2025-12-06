# 問題URL: https://atcoder.jp/contests/abc143/tasks/abc143_a

def main():
    a, b = map(int, input().split())
    if a < 2 * b:
        return 0
    else:
        return a - 2 * b

if __name__ == "__main__":
    print(main())