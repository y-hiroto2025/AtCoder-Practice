# 問題URL: https://atcoder.jp/contests/arc048/tasks/arc048_a

def main():
    start, last = map(int, input().split())
    if (start < 0) and (last > 0):
        ans = abs(last - start) - 1
    else:
        ans = abs(last - start)
    print(ans)

if __name__ == "__main__":
    main()