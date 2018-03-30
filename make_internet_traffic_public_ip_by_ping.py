import random, time
from PingToServer import ping_to_server

ips: list = ["8.8.8.8", "8.8.4.4"]
ips.extend([".".join(map(str, (random.randint(0, 255) for _ in range(4)))) for _ in range(1000)])
ping_to_server(ips=ips)
time.sleep(29)
