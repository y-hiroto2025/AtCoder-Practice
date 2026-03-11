"""
問題URL: https://atcoder.jp/contests/abc380/tasks/abc380_c
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N, K = map(int, input().split())
    S = input().strip()

    S_list = []
    s = [S[0]]
    for i in range(1, N):
        if s[-1] == S[i]:
            s.append(S[i])
        else:
            S_list.append("".join(s))
            s = [S[i]]
        
        if i == N-1:
            S_list.append("".join(s))

    count = 0
    for idx, s in enumerate(S_list):
        if s[0] == "1":
            count += 1
            
        if count == K:
            S_list[idx], S_list[idx-1] = S_list[idx-1], S_list[idx]
            print("".join(S_list))
            return


if __name__ == "__main__":
    main()