from PIL import Image


def qr():
    res = []
    image1 = Image.open("1.png")
    image2 = Image.open("2.png")
    pixels1 = image1.load()
    pixels2 = image2.load()
    count = 0
    for j in range(0, image1.size[1]):
        for i in range(0, image1.size[0]):
            amo1 = pixels1[i, j]
            amo2 = pixels2[i, j]
            if sum(map(abs, [amo1[i] - amo2[i] for i in range(3)])) > 3:
                count += 1
                print(i, j, abs(amo1[0] - amo2[0]), amo1, amo2)
            if 144 <= i <= 169 and j == 533:
                res.append(abs(amo1[0] - amo2[0]))
            if sum(map(abs, [amo1[i] - amo2[i] for i in range(3)])) > 3:
                pixels1[i, j] = (255, 255, 255)
            else:
                pixels1[i, j] = (0, 0, 0)
    print(count)
    image1.save("diff.png")
    return res


dastan1 = qr()
# dastan2 = '\x63\x68\x66\x63\x7e\x71\x73\x34\x76\x57\x72\x3c\x74\x73\x5c\x31\x75\x5d\x6b\x32\x34\x77\x59\x38\x4c\x7f'
dastan2 = list(map(lambda s: int(s, 16),
                   ['63', '68', '66', '63', '7e', '71', '73', '34', '76',
                    '57', '72', '3c', '74', '73', '5c', '31', '75', '5d',
                    '6b', '32', '34', '77', '59', '38', '4c', '7f']))
for i in range(len(dastan1)):
    print(chr(dastan1[i] ^ dastan2[i]), end='')
print()
# result:
