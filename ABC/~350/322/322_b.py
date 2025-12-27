"""
問題URL: https://atcoder.jp/contests/abc322/tasks/abc322_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N, M = map(int, input().split())
    S = input() # len(S) = N <= M
    T = input() # len(T) = M

    # 便利なメソッドがある
    is_prefix = T.startswith(S)
    is_suffix = T.endswith(S)

    if is_prefix and is_suffix:
        print(0)
    elif is_prefix:
        print(1)
    elif is_suffix:
        print(2)
    else:
        print(3)

    """prefix = T[:N]
    suffix = T[M - N:]

    if prefix == S and suffix == S:
        print(0)
        return
    elif prefix == S:
        print(1)
        return
    elif suffix == S:
        print(2)
        return
    else:
        print(3)
        return"""

if __name__ == "__main__":
    main()