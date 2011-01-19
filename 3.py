bignum = 600851475143
#bignum = 13195
working = bignum
primefactors = []
factor = 1
largest = 1
while factor < working: 
    if bignum % factor == 0:
        largest = factor
        print 'Found factor: %s' % (largest)
        
        if factor not in primefactors:
            primefactors.append( factor )

        
        #working = bignum / factor
        #print 'working now: %s' % (working)
    factor += 1

print primefactors 
