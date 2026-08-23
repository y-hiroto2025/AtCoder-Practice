"""
問題URL: https://atcoder.jp/contests/abc123/tasks/abc123_b
----------------------------------------------------
----------------------------------------------------
"""
from itertools import permutations
def main():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())

    cooking_times_comb = list(permutations([a,b,c,d,e]))
    ans = float('inf')

    for cooking_times in cooking_times_comb:
        time = 0

        for i in range(5):
            time += cooking_times[i]

            while time % 10 != 0 and i != 4:
                time += 1

        ans = min(ans, time)

    print(ans)


if __name__ == "__main__":
    main()