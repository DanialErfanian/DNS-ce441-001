import re
from collections import defaultdict

ip_regex = '(\\d+\\.\\d+\\.\\d+\\.\\d+)\\.(\\d+)'
regex = ip_regex + " > " + ip_regex + "\\: Flags \\[S\\]"

db = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))

with open("./trace.txt", "r")as f:
    lines = f.readlines()
    for line in lines:
        m = re.search(regex, line)
        if m:
            src_ip = m.group(1)
            src_port = m.group(2)
            dst_ip = m.group(3)
            dst_port = m.group(4)
            db[src_ip][dst_ip][dst_port] += 1
for src_ip in db.keys():
    for dst_ip in db[src_ip].keys():
        for port, count in db[src_ip][dst_ip].items():
            if count > 100:
                print(src_ip + " -> " + dst_ip + ":" + str(port), count)
