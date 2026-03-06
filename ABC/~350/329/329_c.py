"""
問題URL: https://atcoder.jp/contests/abc329/tasks/abc329_c
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N = int(input())
    S = input().strip()

    max_len = {S[0]: 1}

    idx = 0
    s_len = 1
    for i in range(1, N):

        s = S[i]

        if S[idx] == s:
            s_len += 1
        else:
            s_len = 1
            idx = i
        
        max_len[S[idx]] = max(max_len.get(s, 0), s_len)

    print(sum(max_len.values()))


if __name__ == "__main__":
    main()