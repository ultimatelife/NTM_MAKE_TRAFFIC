import os


def ping_to_server(ips: list):
    for ip in ips:
        os.system(f"ping {ip} &")
