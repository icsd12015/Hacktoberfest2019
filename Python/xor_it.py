#!/usr/bin/python3

from itertools import cycle
from string import hexdigits

def xor_it(data, key):
    ishex = False
    if all(d in hexdigits for d in data):
        data = bytes.fromhex(data).decode('utf-8')
        ishex = True
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
    return xored if ishex else xored.encode("utf-8").hex()


print('=' * 25)
key = 'password'
print('Key: ' + key)
msg = 'secret!'
print('Message: ' + msg)
print('-'*25)
encrypted = xor_it(msg,key)
print('Encrypted: ' + encrypted)
decrypted = xor_it(encrypted,key)
print('Decrypted: ' + decrypted)
print('='*25)



'''
Ouput:

=========================
Key: password
Message: secret!
-------------------------
Encrypted: 03041001121b53
Decrypted: secret!
=========================

'''
