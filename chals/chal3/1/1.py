import binascii

from Crypto.Cipher import AES


def encrypt1(var, key):
    return bytes(a ^ b for a, b in zip(var, key))


def reverse_aes(plain, key, cipher):  # -> iv
    amo = AES.new(key, AES.MODE_CBC, "\x00" * 16)
    # print("1", binascii.unhexlify(cipher))
    # print("2", plain.encode())
    # print("3", amo.decrypt(binascii.unhexlify(cipher)))
    res = encrypt1(amo.decrypt(binascii.unhexlify(cipher)), plain.encode())
    return res


def AES_encytpion(plaintext):
    # key_part2 = RSA_decryption()
    key_part2 = "G0ofyaNdMiiickeyM0us3"
    # aes_key = "----" + key_part2[9:]
    aes_key = "v0pc" + key_part2[9:]
    # iv = "--JDy9kNZcGjux0Q"
    iv = "75JDy9kNZcGjux0Q"
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    return binascii.hexlify(cipher.encrypt(plaintext))


print(AES_encytpion(
    "CR--------------never gave up and worked HAaRrDd"))  # parcham is the first 16 character of this string
print(AES_encytpion(
    "CR1stiAnoR0Na1dOnever gave up and worked HAaRrDd"))  # parcham is the first 16 character of this string

# output: --------------------------------------------------------e238c365 6cf0073c9a0bede05e39517aff83ed94
key_part2 = "G0ofyaNdMiiickeyM0us3"
# aes_key = "----" + key_part2[9:]
aes_key = "v0pc" + key_part2[9:]
msg = "CR--------------never gave up and worked HAaRrDd"
expected = "6cf0073c9a0bede05e39517aff83ed94"
print(binascii.hexlify(reverse_aes(msg[-16:], aes_key, '6cf0073c9a0bede05e39517aff83ed94')))
print(binascii.hexlify(reverse_aes(msg[-32:-16], aes_key, '1b5c647496543590362c14a2e238c365')))
print(binascii.hexlify(reverse_aes("\x00"*16, aes_key, '925c3292f3b72ff924e3e88468de5366')))
print(encrypt1(binascii.unhexlify("74677b370d502a20353177241449541e"), b'--JDy9kNZcGjux0Q').decode())
