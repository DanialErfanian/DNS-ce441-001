import binascii
import random

from Crypto.Cipher import AES


def get_key(inp="abcd"):
    key_part2 = "G0ofyaNdMiiickeyM0us3"
    aes_key = inp + key_part2[9:]
    cipher = AES.new(aes_key, AES.MODE_CBC, "------------RrDd")
    return cipher.decrypt(binascii.unhexlify("6cf0073c9a0bede05e39517aff83ed94"))


while True:
    amo = [random.choice("abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper() + "1234567890") for i in
           range(4)]
    dastan = get_key("".join(amo))
    # e238c365
    if True \
            and dastan[-1] == 0x65 \
            and dastan[-2] == 0xc3 \
            and dastan[-3] == 0x38 \
            and dastan[-4] == 0xe2:
        print(amo)
        break
        # amo = ['v', '0', 'p', 'c']
