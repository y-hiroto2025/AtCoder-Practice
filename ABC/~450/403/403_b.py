"""
問題URL: https://atcoder.jp/contests/abc403/tasks/abc403_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
def main():
    T = input().strip()
    U = input().strip()

    for i in range(len(T)-len(U)+1):
        t = T[i:i+len(U)]

        same = True

        for j in range(len(U)):
            if t[j] != U[j] and t[j] != "?":
                same = False

        if same:
            print("Yes")
            return
    
    print("No")
    
    


if __name__ == "__main__":
    main()