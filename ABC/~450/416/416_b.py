"""
問題URL: https://atcoder.jp/contests/abc416/tasks/abc416_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    S = input().strip().replace(".", "o")
    T = []

    for i in range(len(S)-1):
        if S[i] == "o" and S[i+1] == "o":
            T.append(".")
        else:
            T.append(S[i])
    
    T.append(S[-1])
    
    print(*T, sep="")


if __name__ == "__main__":
    main()