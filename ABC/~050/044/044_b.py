"""
問題URL: https://atcoder.jp/contests/abc044/tasks/abc044_b
----------------------------------------------------
結果
・2min
----------------------------------------------------
"""
from collections import Counter
def main():
    w = input().strip()

    cnt = Counter(w)

    for value in cnt.values():
        if value % 2 != 0:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()