import re
from collections import defaultdict

ip_regex = '(\\d+\\.\\d+\\.\\d+\\.\\d+)\\.(\\d+)'
regex = ip_regex + " > " + ip_regex + "\\: Flags \\[S\\]"

db = defaultdict(set)
with open("./trace.txt", "r")as f:
    lines = f.readlines()
    for line in lines:
        m = re.search(regex, line)
        if m:
            src_ip = m.group(1)
            src_port = m.group(2)
            dst_ip = m.group(3)
            dst_port = m.group(4)
            db[src_ip].add(dst_ip + ":" + dst_port)
for ip, attempts in db.items():
    if len(attempts) > 100:
        print(ip, len(attempts), list(attempts)[:10])
