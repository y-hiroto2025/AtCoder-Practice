"""
問題URL: https://atcoder.jp/contests/abc210/tasks/abc210_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))

    candy_dict = {}
    

    for k in range(K):
        get = c[k]
        if get not in candy_dict:
            candy_dict[c[k]] = 0
        candy_dict[c[k]] += 1
    ans = len(candy_dict)

    for i in range(K, N):
        get = c[i]
        dump = c[i-K]

        if get not in candy_dict:
            candy_dict[get] = 0
        candy_dict[get] += 1
        
        candy_dict[dump] -= 1
        if candy_dict[dump] == 0:
            del candy_dict[dump]
        

        ans = max(ans, len(candy_dict))
    
    print(ans)


if __name__ == "__main__":
    main()