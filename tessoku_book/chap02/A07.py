# １次元の累積和
def main():
    D = int(input())
    N = int(input())
    pfx = [0] * (D + 2)

    for _ in range(N):
        L_i, R_i = map(int, input().split())
        pfx[L_i] += 1
        pfx[R_i + 1] -= 1
    
    ans = [0] * (D + 2)

    for i in range(1, D + 1):
        ans[i] = pfx[i] + ans[i - 1]
    
    for i in range(1, D + 1):
        print(ans[i])

if __name__ == "__main__":
    main()