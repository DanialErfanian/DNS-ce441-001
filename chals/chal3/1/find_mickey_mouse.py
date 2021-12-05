

def find_d(phi, e):
    for i in range(100000000):
        if (i * phi + 1) % e == 0:
            return (i * phi + 1) // e


def quick_power(c, d, N):
    if c >= N:
        print("Vaaaaay")
    if d == 0:
        return 1
    if d == 1:
        return c % N
    else:
        ans = (quick_power(c, d // 100, N) ** 100) % N
        if d % 100 > 0:
            ans = (ans * (c ** (d % 100))) % N
        return ans


def RSA_decryption():
    c = 73640634968105837622206742993587129728129727871068520455061424132152241827225519039076042626317947435901917812699908249402464264512617388216707329358735966972269561895146895588563819756113881700497517671812329896466873041460693992710034119425904476026210160945512008493784159582708972370047179534125866273801
    p = 12306659173157958582444989292124162444364120282519051734386183182498363004933072801438005054837711412414913412857743812799621880509228799225768094412919013
    q = 11047354728099105297995458117358033395095373828593480589129781261816097613044636973071724083097267939728103869210843827600697829385840691669850613320538209
    # e = 220
    e = 55  # * 4 == 220
    d = find_d((p - 1) * (q - 1), e)
    print(f"d = {d}")
    message = quick_power(c, d, p * q)
    # This is m^4 but m is enough small than m^4 < N so we could find m easily
    # https://www.alpertron.com.ar/ECM.HTM
    factors = [
        417346105717146062627678998641546336691756483,
        3613,
        23,
        3
    ]
    print(message)
    print("should be zero:", message - (factors[0] ** 4 * factors[1] ** 4 * factors[2] ** 4 * factors[3] ** 4))
    # decryption of c with the following parameters using RSA:
    msg_int = factors[0] * factors[1] * factors[2] * factors[3]
    result = int.to_bytes(msg_int, length=21, byteorder='big').decode('utf-8')
    print(result)
    return result
RSA_decryption()