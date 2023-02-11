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

def elias_delta_encoding(val):
    """
    Params:
    val: An Integer on which elias delta encoding has to be performed
    
    Example:
    val: 12
    elias_gamma_encoding(val): '00100100'
    """
    n = 1; temp = 2
    while temp < val:
        temp *= 2
        n += 1
    n -= 1
    
    bin_format = '{0:0'+f'{n}'+'b}'
    return elias_gamma_encoding(n + 1) + bin_format.format(val - pow(2, n))

def elias_delta_decoding(bin_string):
    L = 0; index = 0
    for i in range(len(bin_string)):
        if bin_string[i] == '1':
            index = i
            break
        else:
            L += 1
            
    bin_decode = '0b1' + bin_string[index + L + 1:]
    return int(bin_decode, 2)

def get_vb_encode(val, rems = []):
    """
    Purpose:
    Helper function to get the VBencode of a value
    
    Params:
    val: An integer which has to be encoded
    rems: Initially empty, stores the individual remainders
    
    Example:
    val: 99
    rems: []
    get_vb_encode(val, rems): [99]
    """
    if val < pow(2, 7):
        return [val] + rems
    else:
        return get_vb_encode(val // pow(2, 7), rems = [val % pow(2, 7)] + rems)

def variable_byte_encoding(postings):
    gaps = [postings[0]]; byte_stream = []
    gaps = gaps + [postings[i] - postings[i-1] for i in range(1, len(postings))]
    for n in gaps:
        vb_encode = get_vb_encode(n)
        byte_encode = []
        for i in range(len(vb_encode)):
            if i == len(vb_encode) - 1:
                byte_encode.append('1' + str('{0:08b}'.format(vb_encode[i]))[1:])
            else:
                byte_encode.append(str('{0:08b}'.format(vb_encode[i])))
        byte_stream.append(byte_encode)
        
    for b in byte_stream:
        for bb in b:
            print(bb, end=" ")
        print("  ", end="")

