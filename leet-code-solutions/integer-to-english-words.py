class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine', ' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        tens = ['', ' Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        thousands = ['', ' Thousand', ' Million', ' Billion']
       
        def calc(n):
            if n < 20 :
                return ones[n]
            elif n < 100:
                return tens[n // 10] + calc(n % 10)
            elif n < 1000:
                return calc(n // 100) + " Hundred" + calc(n % 100)
            else:
                for i in range(3, 0, -1):
                    if n >= (1000 ** i):
                        return calc(n // (1000 ** i)) + thousands[i] + calc(n % (1000 ** i))
            return ""
        return calc(num).lstrip()
        