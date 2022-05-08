#Pearl Assistant
import json

from colorama import Fore, init
import json
init()

def Network():
    import socket
    # Local IP
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    #Local IP
    print(ips)


def console():
    import socket
    import os
    import requests
    import platform
    import time
    mach = platform.system()
    if mach == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    try:
        check = requests.get("https://google.com")
        conn = Fore.LIGHTGREEN_EX + "avaliable"
    except:
        conn = Fore.LIGHTRED_EX + "not avaliable"

    ip = requests.get('https://api.ipify.org').text
    js_geo = requests.get('http://ipwho.is/'+ip).text
    pars = json.loads(js_geo)
    geoloc = {pars["region"]}
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "                Welcome Kepheer!",
        "\n Internet: " + conn,
        "\n Public IP: " + ip,
        "\n System: " + mach,
        "\n GEO: "+ str(geoloc),
        "\n Local IP: " + local_ip)
    input()



console()
