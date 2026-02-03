"""
問題URL: https://atcoder.jp/contests/discovery2016-qual/tasks/discovery_2016_qual_a
----------------------------------------------------
結果
・自力（6min）
----------------------------------------------------
"""
def main():
    W = int(input())
    s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
    for i in range(len(s)):
        print(s[i], end="")
        if (i + 1) % W == 0:
            print()
        elif i + 1 == len(s):
            print()

if __name__ == "__main__":
    main()