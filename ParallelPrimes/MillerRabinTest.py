import sys
class MillerRabinTest():
    def isPrime(self,n,primes,Max):
     if n <= Max:
         if n in primes: return True
         return False
     for prime in primes:
         if n % prime == 0: return False

     s, r = n - 1, 1  
     while not s & 1:
         s >>= 1
         r  += 1
     for i in primes:    
         y = pow(i,s,n)
         if y == 1:
             continue         
         for j in xrange(1,r):   
             if y == n - 1:
                 break            
             y = pow(y,2,n)
         else: return False
     return True

    def isPrime2(self,start, end, prims):
        if end == 2: return 2
  
        n = start
        m = end - (end + 1) % 2       
        if m < 2: return 1

        primes = 0
      

        v, d, e = int(ceil(log(m,2))) + 2, m, 1
        
        cent_primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

        if n <= 100 or m <= 100:
            for i in cent_primes:
                if i < n: continue
                if i > m: break
                primes = primes + 1

        if n <= 1: n = 2

        n = n - 1

        if n % 2 == 0: n = n - 1

        for s in xrange(2,v):
            d >>= 1
            e <<= 1
            f, p = e << 1, -e
            
            h = int(ceil((n - e) / f)) + 1 
            p += h * f + 1

            rng = xrange(1,s)
            
            for r in xrange((h * 2) + 1, d + 1,2):
                p += f
                z = p % 6
                if z != 1 and z != 5: continue
                for prime in cent_primes:
                    if p % prime == 0:
                        break
                else:
                    
                    o = p - 1
             
                    for i in prims:
                        y = pow(i,r,p)
            
                        if y == 1: continue
                    
                        for j in rng:
                            if y == o: break
                            y = pow(y,2,p)
                        else:
                            break
                    else:
                        primes = primes + 1
        if (start) <= 2: primes = 1
     
        return primes
 

