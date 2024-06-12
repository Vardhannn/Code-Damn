class Solution:
    def countPrimes(self, n: int) -> int:

        primes = [True for i in range(n)]
        count = 0
        p = 2
        while(p * p < n):


            if primes[p]:
                for i in range(p*p, n, p):
                    primes[i] = False
            p += 1

        for i in range(2, n):
            if primes[i]:
                count += 1
        return count
