def maxAND(self, arr,N):
        #Your code here
        max_AND = 0

    # Iterate over each bit from the 31st bit (assuming 32-bit integers)
        for bit in range(31, -1, -1):
            # Create a mask by setting the current bit of max_AND
            mask = max_AND | (1 << bit)
    
            # Count the number of elements having the current bit set
            count = 0
            for num in arr:
                if (num & mask) == mask:
                    count += 1
    
            # If at least two numbers have this bit set, update max_AND
            if count >= 2:
                max_AND = mask
    
        return max_AND