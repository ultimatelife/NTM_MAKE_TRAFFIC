import requests
from ProtocolToMonitoringServer import request_to_monitoring_servers, ping_to_server

internal_traffic_public_ip_list = requests.get(
    "https://raw.githubusercontent.com/ultimatelife/NTM_MAKE_TRAFFIC/private_ip_list").text.split("\n")
ping_to_server(internal_traffic_public_ip_list)
