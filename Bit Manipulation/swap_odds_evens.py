def swapBits(n):
        even_mask = 0xAAAAAAAA
        odd_mask = 0x55555555
        even_bits = n&even_mask
        odd_bits = n&odd_mask
        even_bits = even_bits >> 1
        odd_bits = odd_bits << 1
        return even_bits | odd_bits