def is_prime( bignum ):
  print bignum
  factor = 2
  while factor * factor < bignum:
      if bignum % factor == 0:
          return False
      factor += 1
  return True

bignum = 600851475143
#bignum = 13195d
print is_prime(59569) 
primefactors = []
factor = 2
working = bignum
while factor < working: 
    if bignum % factor == 0:
      if is_prime( factor ):
        primefactors.append( factor )
        working = bignum / factor
        print "Working %s", (working)
    factor += 1

print primefactors 
