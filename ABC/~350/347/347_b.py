"""
問題URL: https://atcoder.jp/contests/abc347/tasks/abc347_b
----------------------------------------------------
結果
・自力（6min）
----------------------------------------------------
"""
def main():
    S = input()
    ans_set = set()

    for i in range(len(S)):
        for j in range (i, len(S)):
            ans_set.add(S[i: j + 1])
    
    print(len(ans_set))

if __name__ == "__main__":
    main()