def is_prime( bignum ):
  factor = 2
  while factor * factor < bignum:
      if bignum % factor == 0:
          return False


bignum = 600851475143
#bignum = 13195d
primefactors = []
factor = 2
while factor * factor < bignum: 
    if is_prime(factor):
      if bignum % factor == 0:
        primefactors.append( factor )
        
    factor += 1

print primefactors 
