import requests, time, os


def request_to_monitoring_servers(ips: list):
    for ip in ips:
        ip: str = ip.strip()
        for _ in range(30):
            result = requests.get(f"http://{ip}")
            time.sleep(0.3)
            print(result)


def ping_to_server(ips: list):
    for ip in ips:
        os.system(f"ping {ip} &")
