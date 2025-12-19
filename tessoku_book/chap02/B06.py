def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    prefix_sum = [0]

    for i in range(N):
        prefix_sum.append(prefix_sum[i] + A[i])
        
    for i in range(Q):
        L_i, R_i = map(int, input().split())
        one_amount = prefix_sum[R_i] - prefix_sum[L_i - 1]
        if one_amount > (R_i - L_i + 1) - one_amount:
            print("win")
        elif one_amount < (R_i - L_i + 1) - one_amount:
            print("lose")
        else:
            print("draw")

if __name__ == "__main__":
    main()