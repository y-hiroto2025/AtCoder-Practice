"""
問題URL: https://atcoder.jp/contests/abc396/tasks/abc396_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    Q = int(input())
    card = [[0, 100]]

    for _ in range(Q):
        q = list(map(int, input().split()))

        if q[0] == 1:
            x = q[1]
            if card[-1][0] == x:
                card[-1][1] += 1
            else:
                card.append([x, 1])
        
        else:
            if card[-1][1] == 1:
                print(card[-1][0])
                card.pop(-1)
            else:
                print(card[-1][0])
                card[-1][1] -= 1


if __name__ == "__main__":
    main()