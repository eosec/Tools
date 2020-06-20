#################################################
#
# Script to encode and decode BIG-IP persistence cookie
# https://support.f5.com/csp/article/K6917
#
# usage:
#  to encode python3 f5cookie.py e <ip:port>")
#  to decode python3 f5cookie.py d <cookie>")
#
#################################################
# Author: Elvis OSMAN
# Email: elosman@protonmail.com
#################################################

import sys

def decode(inp):
    a = int(inp.split('.')[0])
    b = int(inp.split('.')[1])
    c = a.to_bytes(4,'little')
    ip = str(c[0]) + '.' + \
         str(c[1]) + '.' + \
         str(c[2]) + '.' + \
         str(c[3])
    port = str(int.from_bytes(b.to_bytes(2,'little'),'big'))
    return ip + ":" + port


def encode(inp):
    a = inp.split(':')[0]
    b = inp.split(':')[1] 
    octs = a.split('.')
    c = int(octs[0]).to_bytes(1, 'little') + \
        int(octs[1]).to_bytes(1, 'little') + \
        int(octs[2]).to_bytes(1, 'little') + \
        int(octs[3]).to_bytes(1, 'little')
    d = str(int.from_bytes(c,'little'))
    b = str(int.from_bytes(int(b).to_bytes(2,'little'),'big'))
    return d + '.' + b + '.0000'


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'e':
        print(encode(sys.argv[2]))
    elif len(sys.argv) == 3 and sys.argv[1] == 'd':
        print(decode(sys.argv[2]))
    else:
        print("usage:")
        print(" to encode python3 " + sys.argv[0] + " e <ip:port>")
        print(" to decode python3 " +  sys.argv[0] + " d <cookie>")
