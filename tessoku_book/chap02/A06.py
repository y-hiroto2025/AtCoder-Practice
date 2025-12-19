def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    prefix_sum = [0] # 累積和

    for i in range(N):
        prefix_sum.append(prefix_sum[i] + A[i])
    for i in range(Q):
        L_i, R_i = map(int, input().split())
        print(prefix_sum[R_i] - prefix_sum[L_i - 1])

if __name__ == "__main__":
    main()