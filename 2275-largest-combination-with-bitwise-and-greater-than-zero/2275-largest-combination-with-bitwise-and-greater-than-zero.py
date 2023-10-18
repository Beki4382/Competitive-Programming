class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_counts = [0] * 24
        for n in candidates:
            for i, digit in enumerate(bin(n)[2:][::-1]):
                if digit == "1":
                    bit_counts[i] += 1
        return max(bit_counts)