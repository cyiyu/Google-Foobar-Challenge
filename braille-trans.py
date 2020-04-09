def make_dict(string, braille):
    brailledict = {}
    n = 6
    aiyaarray = [braille[i:i + n] for i in range(6, len(braille), n)]
    n_string = string.lower()
    print(len(n_string))
    print(len(aiyaarray))
    for i in range(len(n_string)):
        brailledict[n_string[i]] = aiyaarray[i]

    return brailledict


def solution(s):
    braille_dict = {'t': '011110', 'h': '110010', 'e': '100010', ' ': '000000', 'q': '111110', 'u': '101001',
                    'i': '010100', 'c': '100100', 'k': '101000', 'b': '110000', 'r': '111010', 'o': '101010',
                    'w': '010111', 'n': '101110', 'f': '110100', 'x': '101101', 'j': '010110', 'm': '101100',
                    'p': '111100', 's': '011100', 'v': '111001', 'l': '111000', 'a': '100000', 'z': '101011',
                    'y': '101111', 'd': '100110', 'g': '110110'}
    in_string = s.lower()
    out_string = ""
    i = 0
    for char in in_string:
        if s[i].isupper():
            out_string += "000001"
        out_string += braille_dict[char]
        i += 1
    return out_string
