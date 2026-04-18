"""
問題URL: https://atcoder.jp/contests/abc398/tasks/abc398_b
----------------------------------------------------
結果
・
---------------
"""
from collections import Counter
def main():
    A = list(map(int, input().split()))

    cnt = Counter(A)

    values = sorted(cnt.values(), reverse=True)
    
    if len(values) >= 2:
        if values[0] >= 3 and values[1] >= 2:
            print("Yes")
            return
    
    print("No")

if __name__ == "__main__":
    main()