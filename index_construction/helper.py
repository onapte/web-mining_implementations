def run_length_encoding(code_string):
    """
    Params:
    code_string: The string on which run length encoding has to be performed
    
    Example:
    code_string: 'aaabbcdaa'
    run_length_encoding(code_string): 'a3b2c1d1a2'
    """
    
    encoded_string = ''
    curr_c = code_string[0]
    counts = 0
    for c in code_string:
        if curr_c == '':
            curr_c = c
        if c != curr_c:
            encoded_string += f'{curr_c}{counts}'
            curr_c = c
            counts = 1
        else:
            counts += 1
    
    encoded_string += f'{curr_c}{counts}'
    return encoded_string

def unary_coding(val):
    """
    Params:
    val: An Integer which has to be converted to unary code
    
    Example:
    val: 5
    unary_coding(val): '000001'
    """
    
    unary_string = ''
    for i in range(val):
        unary_string += '0'
    unary_string += '1'
    return unary_string

def elias_gamma_encoding(val):
    """
    Params:
    val: An Integer on which elias gamma encoding has to be performed
    
    Example:
    val: 12
    elias_gamma_encoding(val): '0001100'
    """
    offset = str(bin(val))[3:]
    selector = unary_coding(len(offset))
    return selector + offset
