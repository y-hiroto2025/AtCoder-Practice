"""
問題URL: https://atcoder.jp/contests/abc352/tasks/abc352_b
----------------------------------------------------
結果
・自力（8min）
----------------------------------------------------
"""
def main():
    S = input()
    T = input()
    ans = []
    j = 0

    for i in range(len(T)):
        if S[j] == T[i]:
            ans.append(i + 1)
            j += 1
            if j == len(T):
                break
    
    print(*ans)

if __name__ == "__main__":
    main()