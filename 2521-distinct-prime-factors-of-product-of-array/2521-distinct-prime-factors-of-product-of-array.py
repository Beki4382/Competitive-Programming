class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def isPrime(num, primes_set): 
            i = 2
            
            while i * i <= num:
                while num % i == 0:
                    primes_set.add(i)
                    num = num //i
                i += 1
            if num > 1:
                primes_set.add(num)
        
        prime_set =set()
        for num in nums:
            isPrime(num, prime_set)
            
        return len(prime_set)
            
            
        