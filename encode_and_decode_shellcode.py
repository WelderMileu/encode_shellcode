#!/usr/bin/env python3
'''
Simple script the encrypt and decrypt shellcode
created in: [17-11-2022]
'''

flag = 'flag{3nc0d3d_flag_h3xd3c1mal}'
hexdump = []

# encoded
for x in flag:
	encoded = "0x{}".format(x.encode().hex())
	hexdump.append(encoded)
print(hexdump)

# decoded
for x in hexdump:
	b = bytes.fromhex(x.replace('0x', '')).decode('utf-8')
	print(b, end='')
print('\n')