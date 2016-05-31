from MillerRabinTest import MillerRabinTest
Y = MillerRabinTest()
N=3
M=1
Pri = xrange(2,104,1)
Pri = filter(lambda x: (x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3) and (x % 5 != 0 or x == 5) and (x % 7 != 0 or x == 7) ,Pri)
if N <= 3:
    Primes = [2] #2
elif N <= 6:
    Primes = range(2,4,1) #2 y 3
elif N <= 7:
    Primes = range(2,6,1) #2 y 3 y 5
    Primes = filter(lambda x:(x % 2 != 0 or x == 2),Primes)
elif N <= 9:
    Primes = range(2,8,1) #2 y 3 y 5 y 7
    Primes = filter(lambda x:(x % 2 != 0 or x == 2),Primes)
elif N <= 12:
    Primes = range(2,14,1) #2 y 3 y 5 y 7 y 11 y 13
    Primes = filter(lambda x:(x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3),Primes)
elif N <= 14:
    Primes = range(2,18,1) #2 y 3 y 5 y 7 y 11 y 17
    Primes = filter(lambda x:(x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3),Primes)
elif N <= 17:
    Primes = range(2,24,1) #2 y 3 y 5 y 7 y 11 y 17 y 19 y 23
    Primes = filter(lambda x:(x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3),Primes)
elif N <= 23:
    Primes = range(2,38,1) #2 y 3 y 5 y 7 y 11 y 17 y 19 y 23 y 29 y 31 y 37
    Primes = filter(lambda x:(x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3) and (x % 5 != 0 or x == 5),Primes)
else:
    Primes = range(2,42,1)
    Primes = filter(lambda x: (x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3) and (x % 5 != 0 or x == 5),Primes)
R = xrange((10 ** (N - 1)) + 1, 10 ** N, 2)
Size = len(R)
H = Size / M
start = pow(10 ,(N - 1)) + 1
end = pow(10 ,N)
s=1 + (end - 1 - start) // 2
h=s/M
rc = fc = 0
for i in xrange(0,M):
     print i
     rlow = R[H*i]
     flow = start+2*i*h
     print "rlow",rlow,"flow",flow
     if i == M-1:
         rup = R[-1]
         fup = end - 1
     else:
         rup = R[H*(i+1)-1]
         fup = flow+2*h-2
     print "rup",rup,"fup",fup
     rres = Y.isPrime2(rlow,rup,Primes,Pri)
     fres = Y.isPrime2(flow,fup,Primes,Pri)
     rc = rc + rres
     fc = fc + fres
     print "rres",rres,"fres",fres
     print "--"
print "rc",rc,"fc",fc