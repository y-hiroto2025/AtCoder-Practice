"""
問題URL: https://atcoder.jp/contests/abc338/tasks/abc338_b
----------------------------------------------------
----------------------------------------------------
"""
import collections
def main():
    """S = collections.Counter(input())
    ans = sorted(S.items(), key=lambda x: (-x[1], x[0]))
    print(ans[0][0])"""
    S = collections.Counter(sorted(input()))
    print(S.most_common(1)[0][0])

if __name__ == "__main__":
    main()