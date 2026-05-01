"""
問題URL: https://atcoder.jp/contests/abc418/tasks/abc418_b
----------------------------------------------------
----------------------------------------------------
"""
from collections import Counter
def main():
    S = input().strip()

    ans = 0

    for i in range(len(S)-1):
        for j in range(i+1, len(S)):
            count_t = 0

            if S[i] == "t" and S[j] == "t" and j-i+1 >= 3:
                s = S[i:j+1]
                count_t = Counter(s)["t"]

                ans = max(ans, (count_t - 2) / (j-i+1 - 2))
                
            else:
                continue
    
    print(ans)


if __name__ == "__main__":
    main()