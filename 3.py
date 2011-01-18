bignum = 600851475143
working = bignum
factor = 1
largest = 1
while factor < working: 
    if bignum % factor == 0:
            largest = factor
            print 'Found factor: %s' % (largest)
            working = bignum / factor
            print 'working now: %s' % (bignum)
    factor += 1

print largest
