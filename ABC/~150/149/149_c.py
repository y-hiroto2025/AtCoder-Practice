"""
問題URL: https://atcoder.jp/contests/abc149/tasks/abc149_c
----------------------------------------------------
----------------------------------------------------
"""
def is_prime(num):

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False

    return True

def main():
    X = int(input())

    x = X
    while not is_prime(x):
        x += 1
    print(x)


if __name__ == "__main__":
    main()