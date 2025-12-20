"""
問題URL: https://atcoder.jp/contests/abc425/tasks/abc425_b
----------------------------------------------------
結果
・ギブアップ
----------------------------------------------------
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 使われた数字をまとめる
    used_num = set()
    for x in A:
        if x != -1:
            if x in used_num:
                print("No")
                return
            used_num.add(x)
    
    # まだ使われていない数字をまとめる
    missing_num = []
    for x in range(1, N + 1):
        if x in used_num:
            missing_num.append(x)
    
    P = []
    missing_idx = 0

    for i in range(N):
        if A[i] != -1:
            P.append(A[i])
        else:
            P.append(missing_num[missing_idx])
            missing_idx += 1
    print("Yes")
    print(*P) # リストを空白区切りで出力する簡単な書き方



if __name__ == "__main__":
    main()