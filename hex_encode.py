#!/usr/bin/python3

string = 'hidd3n_flag_cft'
encode_hex_a  = []

for i in string:
    encode_hex = i.encode().hex()
    a = "\\x{}".format(encode_hex)

    encode_hex_a.append(a)

shellcode_split = ','.join(encode_hex_a)
shellcode       = ' '.join(encode_hex_a)

print(shellcode_split)
print()

import codecs

for i in shellcode.split():
    d = i[2:]
    c = codecs.decode(d, 'hex').decode()

    print(c, end='')

