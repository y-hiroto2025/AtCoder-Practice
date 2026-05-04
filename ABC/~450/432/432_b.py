"""
問題URL: https://atcoder.jp/contests/abc432/tasks/abc432_b
----------------------------------------------------
結果
・自力（8min）
----------------------------------------------------
"""
def main():
    X = int(input())
    X_list = sorted([int(x) for x in str(X)])
    ans = []

    for i in range(len(X_list)):
        if X_list[i] != 0:
            ans.append(X_list[i])
            X_list.remove(X_list[i])
            break
    
    for x in X_list:
        ans.append(x)
    
    print(*ans, sep="")


if __name__ == "__main__":
    main()