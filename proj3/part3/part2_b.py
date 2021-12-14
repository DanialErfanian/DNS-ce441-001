import re
from collections import defaultdict

ip_regex = '(\\d+\\.\\d+\\.\\d+\\.\\d+)\\.(\\d+)'
regex = ip_regex + " > " + ip_regex + "\\: Flags \\[S\\]"

db = defaultdict(lambda: defaultdict(set))

with open("./trace.txt", "r")as f:
    lines = f.readlines()
    for line in lines:
        m = re.search(regex, line)
        if m:
            src_ip = m.group(1)
            src_port = m.group(2)
            dst_ip = m.group(3)
            dst_port = m.group(4)
            db[src_ip][dst_ip].add(dst_port)
for src_ip in db.keys():
    for ip, ports in db[src_ip].items():
        if len(ports) > 100:
            print(src_ip + " -> " + ip, len(ports))
