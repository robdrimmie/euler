# project euler project 5
# http://projecteuler.net/index.php?section=problems&id=5

factors = range( 20, 0, -1 )

# remove factors that are even divisors of larger ones.
for factor in factors:
    for divisor in range( 1, factor ):
        if divisor in factors:
            if factor % divisor == 0:
                factors.remove( divisor )

print factors

