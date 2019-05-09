for multiplicand in range(1, 10):
    for multiplier in range(1, multiplicand + 1):
        print('%d x %d=%d' % (multiplicand, multiplier, multiplicand*multiplier), end='\t')
    print()
    
