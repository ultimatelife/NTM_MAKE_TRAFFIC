import requests
from ProtocolToMonitoringServer import request_to_monitoring_servers

internal_traffic_public_ip_list = requests.get(
    "https://raw.githubusercontent.com/ultimatelife/NTM_MAKE_TRAFFIC/public_ip_list").text.split("\n")
request_to_monitoring_servers(internal_traffic_public_ip_list)
