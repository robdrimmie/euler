# project euler project 5
# http://projecteuler.net/index.php?section=problems&id=5

upper = 1
for factor in range(1, 20):
    upper *= factor

print "%s" % (upper )
