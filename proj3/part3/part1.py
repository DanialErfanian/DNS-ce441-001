import re

regex = '10.30.22.101\\.(?:\\d)+ > ((\\d)+\\.(\\d)+\\.(\\d)+\\.(\\d)+)\\.443'

result = set()
with open("./trace.txt", "r")as f:
    lines = f.readlines()
    for line in lines:
        m = re.search(regex, line)
        if m:
            ip = m.group(1)
            result.add(ip)
print(*list(result)[:5], sep=', ')
