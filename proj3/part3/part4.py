import re
from collections import defaultdict

ip_regex = '(\\d+\\.\\d+\\.\\d+\\.\\d+)\\.(\\d+)'
regex = ip_regex + " > " + ip_regex + "(?:.* seq )?(\\d+)?:?(\\d+)?"
tcp_stream = defaultdict(list)
tcp_stream_raw = defaultdict(list)
with open("./trace.txt", "r")as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        line = str(idx) + ": " + line
        m = re.search(regex, line)
        if m:
            src_ip = m.group(1)
            src_port = m.group(2)
            dst_ip = m.group(3)
            dst_port = m.group(4)
            seq_start = int(m.group(5) or 0)
            seq_end = int(m.group(6) or 0)
            connection = src_ip + src_port + dst_ip + dst_port

            if src_ip == '10.30.22.101' and seq_start and seq_end:
                if len(tcp_stream[connection]) and seq_start <= tcp_stream[connection][-1][0] <= seq_end:
                    print("-" * 100)
                    print(*tcp_stream_raw[connection][-4:], sep='\n')
                    print(">", line, end='')
                    print(tcp_stream[connection])
                    print()
                    print()
                    print(*tcp_stream_raw[dst_ip + dst_port + src_ip + src_port][-4:], sep='\n')
                    print("-" * 100)
                tcp_stream[connection].append((seq_start, seq_end))

            tcp_stream_raw[connection].append(line.strip())
