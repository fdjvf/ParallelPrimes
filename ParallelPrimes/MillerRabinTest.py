from math  import ceil, log
class MillerRabinTest():
    def isPrime2(self, start, end, prims, Pri):
        if end == 2: return 1  
        n = start
        m = end - (end + 1) % 2       
        if m < 2: return 0

        primes = 0
        v, d, e = int(ceil(log(m, 2))) + 2, m, 1 

        if n <= 100 or m <= 100:
            for i in Pri:
                if i < n: continue
                if i > m: break
                primes = primes + 1

        if n <= 1: n = 2

        n = n - 1
        if n % 2 == 0: n = n - 1

        for s in xrange(2, v):
            d >>= 1
            e <<= 1
            f, p = e << 1, -e
            
            h = int(ceil((n - e) / f)) + 1 
            p = p + h * f + 1

            rng = xrange(1, s)
            
            for r in xrange((h * 2) + 1, d + 1, 2):
                p = p + f
                z = p % 6
                if z != 1 and z != 5: continue
                for prime in Pri:
                    if p % prime == 0:
                        break
                else:                    
                    o = p - 1             
                    for i in prims:
                        y = pow(i, r, p)            
                        if y == 1: continue                    
                        for j in rng:
                            if y == o: break
                            y = pow(y, 2, p)
                        else:
                            break
                    else:
                        primes = primes + 1
        return primes
