def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

import random, math
def is_prime(n, k = 3):
   if n < 6:
      return [False, False, True, True, False, True][n]
   elif n % 2 == 0:
      return False
   else:
      s, d = 0, n - 1
      while d % 2 == 0:
         s, d = s + 1, d >> 1
      for a in random.sample(range(2, n-2), k):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False
               elif x == n - 1:
                  a = 0
                  break
            if a:
               return False
      return True
def comb(a, b):
    len_a = math.floor(math.log10(a))+1
    len_b = math.floor(math.log10(b))+1
    if is_prime(int(a*(10**len_b)+b)) and is_prime(int(b*(10**len_a)+a)):
        return True
    return False

primes = sieve(10000)

def prime_pairs():
    for a in primes:
        for b in primes:
            if b < a:
                continue
            if comb(a, b):
                for c in primes:
                    if c < b:
                        continue
                    if comb(a, c) and comb(b, c):
                        for d in primes:
                            if d < c:
                                continue
                            if comb(a, d) and comb(b, d) and comb(c, d):
                                for e in primes:
                                    if e < d:
                                        continue
                                    if comb(a, e) and comb(b, e) and comb(c, e) and comb(d, e):
                                        return a+b+c+d+e

print (prime_pairs())