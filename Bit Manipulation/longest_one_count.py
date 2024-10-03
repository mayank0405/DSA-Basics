def maxConsecutiveOnes(self, N):
        max_len = 0
        curr_len = 0
        while N:
            if N & 1:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 0
            N = N >> 1
        # Check for the case where the last bits were consecutive 1s
        max_len = max(max_len, curr_len)
        return max_len