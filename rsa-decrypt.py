from modules.primefactors import prime_factors
from modules.modinv import modinv

e = 13
N = 21079

# factorization
primes = prime_factors(N)
p = primes[0]
q = primes[1]

print("p = {}\nq = {}\n".format(p,q))

x = (p-1)*(q-1)

# calculate modular multiplicative inverse
d = modinv(e, x)
print("d = {}".format(d))


