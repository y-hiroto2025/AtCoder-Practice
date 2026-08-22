"""
問題URL: https://atcoder.jp/contests/abc063/tasks/abc063_b
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
def main():
    S = input().strip()

    if len(set(S)) == len(S):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()