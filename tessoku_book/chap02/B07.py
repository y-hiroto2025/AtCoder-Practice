def main():
    T = int(input())
    N = int(input())
    time = [0] * (T + 1)

    for _ in range(N):
        L_i, R_i = map(int, input().split())
        time[L_i] += 1
        time[R_i] -= 1

    ans = 0
    for i in range(T):
        ans = ans + time[i]
        print(ans)

if __name__ == "__main__":
    main()