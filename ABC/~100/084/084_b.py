"""
問題URL: https://atcoder.jp/contests/abc084/tasks/abc084_b
----------------------------------------------------
結果
・7min
----------------------------------------------------
"""
def main():
    A, B = map(int, input().split())
    S = input().strip()

    h_cnt = sum([1 for i in range(len(S)) if S[i]=="-"])

    if len(S) != A+B+1 or S[A] != "-" or h_cnt != 1:
        print("No")
        return
    else:
        print("Yes")


if __name__ == "__main__":
    main()