from operator import xor
from messages import *
from xor_example import string2Int, string2Hex, hex2String, int2String, XORStrings, XORStringsByLine
from Crypto.Util.number import *

string1 = bytes_to_long(bytes.fromhex (mess1))
string2 = bytes_to_long(bytes.fromhex (mess2))

byte2 = xor(string1, string2)
key = long_to_bytes(byte2)
decodeKey =


print(key)