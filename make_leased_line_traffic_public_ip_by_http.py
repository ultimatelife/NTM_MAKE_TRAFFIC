import requests
from ProtocolToMonitoringServer import http_to_server

internal_traffic_public_ip_list = requests.get(
    "https://raw.githubusercontent.com/ultimatelife/NTM_MAKE_TRAFFIC/master/public_ip_list").text.split("\n")
http_to_server(internal_traffic_public_ip_list)