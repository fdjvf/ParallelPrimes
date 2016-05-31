#from MillerRabinTest import MillerRabinTest
#Y = MillerRabinTest()
N=2
M=7
R = xrange((10 ** (N - 1)) + 1, 10 ** N, 2)
Size = len(R)
H = Size / M
start = pow(10 ,(N - 1)) + 1
end = pow(10 ,N)
s=1 + (end - 1 - start) // 2
h=s/M
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
     #rres = Y.isPrime2(rlow,rup,Primes,Pri)
     #fres = Y.isPrime2(flow,fup,Primes,Pri)
     #rc = rc + rres
     #fc = fc + fres
     #print "rres",rres,"fres",fres
     print "--"