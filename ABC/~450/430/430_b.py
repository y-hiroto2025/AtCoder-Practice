"""
問題URL: https://atcoder.jp/contests/abc430/tasks/abc430_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    pattern = set()

    for i in range(N - M + 1):

        for j in range(N - M + 1):
            line = ""

            for k in range(i, i+M):
                line += S[k][j:j+M]
        
            pattern.add(line)
    
    print(len(pattern))



if __name__ == "__main__":
    main()