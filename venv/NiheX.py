from colorama import Fore, init
import json
import socket
import os
import requests
import platform
init()


def ipinfo():
    ip = input("IP: ")
    try:
        geo = requests.get('http://ipwho.is/' + ip).text
        d = json.loads(geo)
        parse = {'IP':d["ip"], 'IP_type':d["type"], 'Country_INF':d['country'], 'Region':d['region'],
                 'City':d['city'], 'Success':d['success']}
        print(Fore.LIGHTYELLOW_EX + "IP INFORMATION:",
              Fore.LIGHTYELLOW_EX + "\n [IP]: " + Fore.LIGHTGREEN_EX + str(parse['IP']),
              Fore.LIGHTYELLOW_EX + "\n [Success]: " + Fore.LIGHTGREEN_EX + str(parse['Success']),
              Fore.LIGHTYELLOW_EX + "\n [IP type]: " + Fore.LIGHTGREEN_EX + str(parse['IP_type']),
              Fore.LIGHTYELLOW_EX + "\n [Country]: " + Fore.LIGHTGREEN_EX + str(parse['Country_INF']),
              Fore.LIGHTYELLOW_EX + "\n [Region]: " + Fore.LIGHTGREEN_EX + str(parse['Region']),
              Fore.LIGHTYELLOW_EX + "\n [City]: " + Fore.LIGHTGREEN_EX + str(parse['City'],))
    except:
        parse = {'IP': ip,'Success':Fore.LIGHTRED_EX + "False"}
        print(Fore.LIGHTYELLOW_EX + "IP INFORMATION:",
              Fore.LIGHTYELLOW_EX + "\n [IP]: " + Fore.LIGHTGREEN_EX + str(parse['IP']),
              Fore.LIGHTYELLOW_EX + "\n [Success]: " + Fore.LIGHTGREEN_EX + str(parse['Success']))
    input()
    start()


def auth():
    print(Fore.LIGHTGREEN_EX + "Sign in your account:")
    username = input("Username: ")
    passwd = input("Passwd: ")
    if username == "Kepheer":
        if passwd == "14031548":
            start()
        else:
            print(Fore.LIGHTRED_EX + "Incorrect password to this username!")
            auth()
    elif username == "dev":
        if passwd == "":
            start()
        else:
            print(Fore.LIGHTRED_EX + "Incorrect password to this username!")
            auth()
    else:
        print(Fore.LIGHTRED_EX + "Incorrect username!")
        auth()


def start():
    mach = platform.system()
    if mach == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    try:
        check = requests.get("https://google.com")
        conn = Fore.LIGHTGREEN_EX + "Avaliable"
    except:
        conn = Fore.LIGHTRED_EX + "Not avaliable"

    try:
        ip = requests.get('https://api.ipify.org').text
    except:
        ip = Fore.LIGHTRED_EX + "Not avaliable"

    try:
        js_geo = requests.get('http://ipwho.is/' + ip).text
        pars = json.loads(js_geo)
        geoloc = {pars["region"]}
    except:
        geoloc = Fore.LIGHTRED_EX + "Not avaliable"

    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except:
        local_ip = Fore.LIGHTRED_EX + "Not avaliable"

    check_res = {'internet':conn, 'ip':ip, "geo":geoloc, 'local_ip':local_ip}


    def console():
        print(Fore.LIGHTGREEN_EX + "                Welcome!",
            Fore.LIGHTYELLOW_EX + "\n [Internet]: " + Fore.LIGHTGREEN_EX + check_res['internet'],
            Fore.LIGHTYELLOW_EX + "\n [Public IP]: " + Fore.LIGHTGREEN_EX + check_res['ip'],
            Fore.LIGHTYELLOW_EX + "\n [System]: " + Fore.LIGHTGREEN_EX + mach,
            Fore.LIGHTYELLOW_EX + "\n [GEO]: " + Fore.LIGHTGREEN_EX + str(check_res['geo']),
            Fore.LIGHTYELLOW_EX + "\n [Local IP]: " + Fore.LIGHTGREEN_EX + check_res['local_ip'])
        command = input(">>> ")
        if command == "ipinfo":
            ipinfo()
        elif command == "exit":
            os.system("exit")
        else:
            start()

    console()


auth()