"""
問題URL: https://atcoder.jp/contests/abc071/tasks/abc071_b
----------------------------------------------------
結果
・6min
----------------------------------------------------
"""
import string

def main():
    S = input().strip()

    alp_set = set(string.ascii_lowercase)

    for i in range(len(S)):

        if S[i] in alp_set:
            alp_set.remove(S[i])

    if alp_set == set():
        print(None)
    else:
        print(sorted(alp_set)[0])


if __name__ == "__main__":
    main()