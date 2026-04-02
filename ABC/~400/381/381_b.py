"""
問題URL: https://atcoder.jp/contests/abc381/tasks/abc381_b
----------------------------------------------------
結果
・自力（6min）
----------------------------------------------------
"""
def main():
    S = input().strip()

    if len(S) % 2 != 0 or len(set(S)) != len(S)//2:
        print("No")
        return

    for i in range(0, len(S), 2):
        if S[i] != S[i+1]:
            print("No")
            return
    
    print("Yes")


if __name__ == "__main__":
    main()