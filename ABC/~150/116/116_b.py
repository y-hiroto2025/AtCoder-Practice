"""
問題URL: https://atcoder.jp/contests/abc116/tasks/abc116_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    s = int(input())

    a_set = {s}

    idx = 0
    a_i = s

    for _ in range(1000001):
        idx += 1

        if a_i % 2 == 0:
            a_i = a_i // 2
        else:
            a_i = 3 * a_i + 1

        if a_i in a_set:
            break

        a_set.add(a_i)

    print(idx+1)


if __name__ == "__main__":
    main()