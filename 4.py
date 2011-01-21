# project euler problem 4
# http://projecteuler.net/index.php?section=problems&id=4

def paltest(product, left, right):
    if left < len( product ) / 2:
        return false

    if product[left] != product[right]:
        return false



largest = 0
for x in range( 999, 900, -1 ):
    for y in range( 999, 900, -1 ):
        iproduct = x * y
        product = str(iproduct)
        if product[-1] == '8' or product[-1] == '9':
            left = 0
            right = -1
            mid = len(product) / 2
            while ( left < mid ) and (product[left] == product[right]):
                left += 1
                right -= 1
            if mid == left and left + 1 == abs(right):
                if iproduct > largest:
                    largest = iproduct

print largest
