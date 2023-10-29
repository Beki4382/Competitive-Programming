class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0
        for i in range(len(s) - k + 1):
            divisor = self.getNumber(k, s, i)
            if divisor != 0 and num % divisor == 0:
                count += 1
        return count

    def getNumber(self, k: int, s: str, start: int) -> int:
        num = 0
        while k > 0:
            num = num * 10
            num = int(s[start]) - int('0') + num
            start += 1
            k -= 1
        return num

        