import requests
import Firelink

from pprint import pprint

ip = requests.get("https://api.ipify.org/?format=json")
ip = ip.json()['ip']

url = requests.get(f"https://ipinfo.io/{ip}/geo")

pprint(ip)
pprint(url.json())
Firelink.FireFox(f"https://ipinfo.io/{ip}/geo")
