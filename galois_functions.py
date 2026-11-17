def add_GF(p,q):
    return format(int(p, 2) ^ int(q, 2), 'b')

def multiply(p,q):
    pr = p[::-1]
    qr = q[::-1]
    result = [0] * (len(p) * len(q))
    for i, a in enumerate(pr):
        for j, b in enumerate(qr):
            if a == '1' and b == '1':
                result[i + j] ^= 1

    result_str = ''
    for r in result:
        result_str += str(r)

    return result_str[::-1].lstrip('0')

def divide(p: str, q: str) -> tuple[str, str]:
    q = q.lstrip('0')
    if not q:
        raise ZeroDivisionError("division by zero polynomial")
    
    pl = list(p)
    diff = len(p) - len(q)
    if diff < 0:                     # deg p < deg q
        return '0', p.lstrip('0') or '0'

    quotient = ['0'] * (diff + 1)

    for i in range(diff + 1):
        if pl[i] == '1':
            quotient[i] = '1'
            for j, b in enumerate(q):
                if b == '1':
                    pl[i + j] = '0' if pl[i + j] == '1' else '1'

    quotient_str = ''.join(quotient).lstrip('0') or '0'
    remainder_str = ''.join(pl[diff + 1:]).lstrip('0') or '0'
    return quotient_str, remainder_str


def multiply_GF(p,q):
    poly = "100011011"
    mult = multiply(p, q)
    return divide(mult, poly)[1] # wynikiem mnożenia w grupie jest reszta