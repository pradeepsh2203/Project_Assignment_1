from re import A
from key import Key
from tables import IP, IIP, E, S_Box, P


def preprocessing(plaintext):
    txt = []
    for ind in IP:
        txt.append(plaintext[ind-1])

    return txt[:32], txt[32:]


def xor(key1, key2):
    key = []
    for i in range(len(key1)):
        key.append((key1[i]+key2[i]) % 2)
    return key


def substitusion(txt):
    res = []
    for ind in range(8):
        block = txt[6*ind:6*(ind+1)]
        row = block[0]*2+block[5]
        col = block[1]*8 + block[2]*4 + block[3]*2 + block[4]

        val = S_Box[ind][row][col]
        # Now you have to convert this val to binary number of 4 bits
        tmp = 8
        while(tmp > 0):
            if (val//tmp):
                val -= tmp
                res.append(1)
            else:
                res.append(0)
            tmp = tmp//2

    return res


def perform_round(Li, Ri, key_gen):
    # expansion of RI
    mod_ri = []
    for ind in E:
        mod_ri.append(Ri[ind-1])

    ki = key_gen.roundKey()
    # Take xor of the current Ri with Ki
    mod_ri = xor(mod_ri, ki)

    # apply substitution
    mod_ri = substitusion(mod_ri)

    # Permute the modified RI
    mod_ri = [mod_ri[ind-1] for ind in P]

    # take xor with Li
    mod_ri = xor(Li, mod_ri)

    return Ri, mod_ri


def encrypt(_plaintext, _key):
    plaintext = _plaintext
    key = _key
    key_gen = Key(key)

    res = []
    Li, Ri = preprocessing(plaintext)
    res.append(Li+Ri)
    for i in range(16):
        Li, Ri = perform_round(Li, Ri, key_gen)
        res.append(Li+Ri)

    # At the end of the last round apply Final permutation
    cipher_text = Ri+Li
    cipher_text = [cipher_text[ind-1] for ind in IIP]
    return cipher_text, res


# Performing test
if __name__ == '__main__':
    # print(plaintext)
    # print(key)

    # a, b = perform_round(Li, Ri, key_gen)
    # print(a)
    # print(b)
    # res = []
    # Li, Ri = preprocessing(plaintext)
    # for i in range(16):
    #     Li, Ri = perform_round(Li, Ri, key_gen)
    #     res.append([Li, Ri])

    # # At the end of the last round apply Final permutation

    # cipher_text = res[-1][1]+res[-1][0]
    # cipher_text = [cipher_text[ind-1] for ind in IIP]

    # print(cipher_text)

    pt = [
        0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0
    ]
    ky = [
        0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0,
        1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0
    ]

    ciphertext, res = encrypt(pt, ky)

    print(ciphertext)
