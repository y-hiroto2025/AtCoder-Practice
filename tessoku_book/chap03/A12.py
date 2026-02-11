# 答えで二分探索
import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def check(x):
        """
        x秒でK枚以上のチラシを刷れるか判定する
        """
        sum_print = 0
        for t in A:
            sum_print += x // t

        return sum_print >= K

    left = 0
    right = 10 ** 9         # 絶対に可能な時間
    while left < right:
        mid = (left + right) // 2

        if check(mid):
            right = mid     # sum_print >= K
        else:
            left = mid + 1  # sum_print < K

    print(left)             # whileを抜けるとleft == right

if __name__ == "__main__":
    main()