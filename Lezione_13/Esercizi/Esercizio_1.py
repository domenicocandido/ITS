def recursivePower(base:int, exponent:int) -> int:
    
    if exponent == 0:
        return 1
    
    elif base == 0:
        return 0
    else:
        return int(base * recursivePower(base, exponent - 1))
    
print(recursivePower(8,2))