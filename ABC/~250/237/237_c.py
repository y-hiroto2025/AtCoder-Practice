"""
問題URL: https://atcoder.jp/contests/abc237/tasks/abc237_c
----------------------------------------------------
----------------------------------------------------
"""
def main():
    S = input().strip()

    l = len(S) - len(S.lstrip("a"))
    r = len(S) - len(S.rstrip("a"))

    if l > r:
        print("No")
    else:
        core = S.strip("a")

        if core == core[::-1]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()