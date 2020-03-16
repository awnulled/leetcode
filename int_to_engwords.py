class Solution:

    def numberToWords(self, num: int) -> str:

        d = { 0 : 'Zero', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five',
          6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
          11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
          15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen',
          19 : 'Nineteen', 20 : 'Twenty',
          30 : 'Thirty', 40 : 'Forty', 50 : 'Fifty', 60 : 'Sixty',
          70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety' }

        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000

        if (num < 20):
            return d[num]

        if (num < 100):
            if num % 10 == 0: return d[num]
            else: return f'{d[num // 10 * 10]} {d[num % 10]}'

        if (num < k):
            if num % 100 == 0: return f'{d[num // 100]} Hundred'
            else: return f'{d[num // 100]} Hundred {self.numberToWords(num % 100)}'

        if (num < m):
            if num % k == 0: return f'{self.numberToWords(num // k)} Thousand'
            else: return f'{self.numberToWords(num // k)} Thousand {self.numberToWords(num % k)}'

        if (num < b):
            if (num % m) == 0: return f'{self.numberToWords(num // m)} Million'
            else: return f'{self.numberToWords(num // m)} Million {self.numberToWords(num % m)}'

        if (num < t):
            if (num % b) == 0: return f'{self.numberToWords(num // b)} Billion'
            else: return f'{self.numberToWords(num // b)} Billion {self.numberToWords(num % b)}'

        if (num % t == 0): return f'{self.numberToWords(num // t)} Trillion'
        else: return f'{self.numberToWords(num // t)} Trillion {self.numberToWords(num % t)}'

obj = Solution()
s1 = 1234567891
print(obj.numberToWords(s1))