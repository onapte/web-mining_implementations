def unary_coding(val):
    unary_string = ''
    for i in range(val):
        unary_string += '0'
    unary_string += '1'
    return unary_string

def elias_gamma_encoding(val):
    offset = str(bin(val))[3:]
    selector = unary_coding(len(offset))
    return selector + offset
