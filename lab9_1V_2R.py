import math

def max_wire_length(w, heights):
    N = len(heights)
    dp = [{} for _ in range(N)]

    for h in range(1, heights[0] + 1):
        dp[0][h] = 0.0

    for i in range(1, N):
        for h_cur in range(1, heights[i] + 1):
            max_len = 0.0
            for h_prev in dp[i - 1]:
                length = dp[i - 1][h_prev] + math.sqrt(w**2 + (h_prev - h_cur)**2)
                if h_cur not in dp[i] or length > dp[i][h_cur]:
                    dp[i][h_cur] = length

    return round(max(dp[N - 1].values()), 2)
