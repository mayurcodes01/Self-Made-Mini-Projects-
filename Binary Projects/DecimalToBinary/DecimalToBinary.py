def DecimaltoBinary(decimal_number: int) -> str:
    """
    Convert a decimal integer to its binary string equivalent.

    >>> DecimaltoBinary(5)
    '101'
    >>> DecimaltoBinary(10)
    '1010'
    >>> DecimaltoBinary(-29)
    '-11101'
    >>> DecimaltoBinary(0)
    '0'
    """
    if decimal_number == 0:
        return "0"
    
    is_negative = decimal_number < 0
    decimal_number = abs(decimal_number)
    
    binary_string = ""
    while decimal_number > 0:
        binary_string = str(decimal_number % 2) + binary_string
        decimal_number //= 2
    
    return "-" + binary_string if is_negative else binary_string


DtoB = int(input("Enter a Decimal number,\nto convert into Binary: "))
print(DecimaltoBinary(DtoB))
