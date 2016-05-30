from mpi4py import MPI
from MillerRabinTest import MillerRabinTest
from sys import  argv
from time import time
from itertools import tee, ifilter



comm = MPI.COMM_WORLD
IdProcess = comm.Get_rank() #Id Del Proceso
M = comm.Get_size()#Numero de Procesos
N = int(argv[1]) #Numero de digitos
start = time()
if IdProcess == 0:     
    Pri = xrange(2, 104, 1)
    Pri = filter(lambda x: (x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3) and (x % 5 != 0 or x == 5) and (x % 7 != 0 or x == 7), Pri)   
    if N <= 3:
        Primes = [2] #2
    elif N <= 6: 
        Primes = range(2, 4, 1) #2 y 3
    elif N <= 7:
        Primes = range(2, 6, 1) #2 y 3 y 5
        Primes = filter(lambda x:(x % 2 != 0 or x == 2), Primes)
    elif N <= 9:
        Primes = range(2, 8, 1) #2 y 3 y 5 y 7
        Primes = filter(lambda x:(x % 2 != 0 or x == 2), Primes)  
    elif N <= 12:
       Primes = range(2, 14, 1) #2 y 3 y 5 y 7 y 11 y 13
       Primes = filter(lambda x:(x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3), Primes)
    elif N <= 14:
        Primes = range(2, 18, 1) #2 y 3 y 5 y 7 y 11 y 17
        Primes = filter(lambda x:(x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3), Primes)
    elif N <= 17:
        Primes = range(2, 24, 1) #2 y 3 y 5 y 7 y 11 y 17 y 19 y 23
        Primes = filter(lambda x:(x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3), Primes)   
    elif N <= 23:
        Primes = range(2, 38, 1) #2 y 3 y 5 y 7 y 11 y 17 y 19 y 23 y 29 y 31 y 37
        Primes = filter(lambda x:(x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3) and (x % 5 != 0 or x == 5), Primes)   
    else:    
        Primes = range(2, 42, 1)
        Primes = filter(lambda x: (x % 2 != 0 or x == 2) and (x % 3 != 0 or x == 3) and (x % 5 != 0 or x == 5), Primes)
else:
 Primes = None
    Pri = None

Primes = comm.bcast(Primes, root=0) 
Pri = comm.bcast(Pri, root=0)

Y = MillerRabinTest()
if IdProcess == 0:    
    if(N != 1):
        R = xrange((10 ** (N - 1)) + 1, 10 ** N, 2)    
    else:
        R = xrange(1, 9)        
else: R = None

R = comm.bcast(R, root=0)   
Size = len(R)
H = Size / M
Lower = R[H * IdProcess]
if IdProcess == M - 1:
    Upper = R[-1]
else:   
    Upper = R[H * (IdProcess + 1) - 1] 

Result = Y.isPrime2(Lower, Upper, Primes, Pri)
Total = comm.reduce(Result, op=MPI.SUM)
if IdProcess == 0:     
    print 'El numero de primos de ', N, ' digitos es ' , Total, '\nTiempo: ', time() - start