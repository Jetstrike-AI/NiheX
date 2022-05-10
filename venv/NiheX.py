from colorama import Fore, init
init()


def net_scan():
    import os
    import platform
    import threading
    import socket
    mach = platform.system()
    if mach == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    def getMyIp():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.connect(('<broadcast>', 0))
        return s.getsockname()[0]

    def scan_Ip(ip):
        addr = net + str(ip)
        comm = ping_com + addr
        response = os.popen(comm)
        data = response.readlines()
        for line in data:
            if 'TTL' in line:
                print(Fore.LIGHTYELLOW_EX + " [SCANER]:" + Fore.LIGHTGREEN_EX + addr + "--> avaliable")
                break

    net = getMyIp()
    net_split = net.split('.')
    a = '.'
    net = net_split[0] + a + net_split[1] + a + net_split[2] + a

    oc = platform.system()
    if oc == "Windows":
        ping_com = "ping -n 1 "
    else:
        ping_com = "ping -c 1 "

    print(Fore.LIGHTYELLOW_EX + "                Scanning local network:")

    for ip in range(1, 100):
        if ip == int(net_split[3]):
            continue
        potoc = threading.Thread(target=scan_Ip, args=[ip])
        potoc.start()
    potoc.join()
    print(Fore.LIGHTYELLOW_EX + " [OS]:" + Fore.LIGHTGREEN_EX + " Succesful finished!")
    input()
    console()



def help():
    print(Fore.LIGHTYELLOW_EX + "                    HELP PAGE:",
          Fore.LIGHTGREEN_EX + "\n [netinfo] - showing information of your local network;",
          "\n [ipinfo] - showing info of inputed IP {IF INPUT '0', SHOW INFORAMION OF YOUR IP};",
          "\n [netscan] - scaning local network on avaliable devices;"
          "\n [cl] - clearing terminal;",
          "\n [reload] - reloading NiheX;",
          "\n [exit] - exit to terminal.")
    input()
    console()


def net_info():
    import socket
    import netifaces
    import speedtest
    hostname = socket.gethostname()
    gws = netifaces.gateways()
    print(Fore.LIGHTYELLOW_EX + " [OS]: " + Fore.LIGHTGREEN_EX + "CONNECTING TO SPEEDTEST.COM!")
    print(Fore.LIGHTYELLOW_EX + " [OS]: " + Fore.LIGHTGREEN_EX + "PLEASE WAIT!")
    s = speedtest.Speedtest()
    w = s.download()
    u = s.upload()
    res = {"ping": s.results.dict()["ping"]}
    import os
    import platform
    mach = platform.system()
    if mach == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    def humansize(nbytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while nbytes >= 1024 and i < len(suffixes) - 1:
            nbytes /= 1024.
            i += 1
        f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])

    info = {'Local_IP':socket.gethostbyname(hostname), 'Gateway_IP':gws['default'][netifaces.AF_INET][0],
            'Download': humansize(w), 'Upload': humansize(u), 'Ping':res['ping']}
    print(Fore.LIGHTYELLOW_EX + "                LOCAL NET INFO:",
          "\n" + Fore.LIGHTYELLOW_EX + " [LOCAL IP]: " + Fore.LIGHTGREEN_EX + info['Local_IP'],
          "\n" + Fore.LIGHTYELLOW_EX + " [GATEWAY IP]: " + Fore.LIGHTGREEN_EX + info['Gateway_IP'],
          "\n" + Fore.LIGHTYELLOW_EX + " [DOWNLOAD SPEED]: " + Fore.LIGHTGREEN_EX + info['Download'],
          "\n" + Fore.LIGHTYELLOW_EX + " [UPLOAD SPEED]: " + Fore.LIGHTGREEN_EX + info['Upload'],
          "\n" + Fore.LIGHTYELLOW_EX + " [AVERAGE PING]: " + Fore.LIGHTGREEN_EX + str(info['Ping']) + " ms")
    input()
    console()


def ipinfo():
    import platform
    import os
    import requests
    import json
    ip = input("IP: ")
    mach = platform.system()
    if mach == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    try:
        geo = requests.get('http://ipwho.is/' + ip).text
        parse = {'IP':json.loads(geo)["ip"], 'IP_type':json.loads(geo)["type"],
                 'Country_INF':json.loads(geo)['country'], 'Region':json.loads(geo)['region'],
                 'City':json.loads(geo)['city'], 'Success':json.loads(geo)['success']}
        print(Fore.LIGHTYELLOW_EX + "                IP INFORMATION:",
              Fore.LIGHTYELLOW_EX + "\n [IP]: " + Fore.LIGHTGREEN_EX + str(parse['IP']),
              Fore.LIGHTYELLOW_EX + "\n [Success]: " + Fore.LIGHTGREEN_EX + str(parse['Success']),
              Fore.LIGHTYELLOW_EX + "\n [IP type]: " + Fore.LIGHTGREEN_EX + str(parse['IP_type']),
              Fore.LIGHTYELLOW_EX + "\n [Country]: " + Fore.LIGHTGREEN_EX + str(parse['Country_INF']),
              Fore.LIGHTYELLOW_EX + "\n [Region]: " + Fore.LIGHTGREEN_EX + str(parse['Region']),
               Fore.LIGHTYELLOW_EX + "\n [City]: " + Fore.LIGHTGREEN_EX + str(parse['City']))
    except:
        parse = {'IP': ip,'Success':Fore.LIGHTRED_EX + "False"}
        print(Fore.LIGHTYELLOW_EX + "                IP INFORMATION:",
            Fore.LIGHTYELLOW_EX + "\n [IP]: " + Fore.LIGHTGREEN_EX + str(parse['IP']),
            Fore.LIGHTYELLOW_EX + "\n [Success]: " + Fore.LIGHTGREEN_EX + str(parse['Success']))
    input()
    console()


def start():
    import requests
    import os
    import platform
    import json
    import socket
    mach = platform.system()
    if mach == "Windows":
        os.system("cls")
    else:
        print(Fore.LIGHTRED_EX + "                WARNING!"
                         "\n NiheX isn't supporting Termux or Linux!")
        input()
        os.system("clear")

    try:
        requests.get("https://google.com")
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
    except:
        geoloc = Fore.LIGHTRED_EX + "Not avaliable"

    try:
        hostname = socket.gethostname()
    except:
        local_ip = Fore.LIGHTRED_EX + "Not avaliable"

    if mach == "Windows":
        mach1 = "Windows"
    else:
        mach1 = Fore.LIGHTRED_EX + mach

    check_res = {'internet': conn, 'ip': ip, "geo": pars['region'], 'local_ip': socket.gethostbyname(hostname)}
    print(Fore.LIGHTGREEN_EX + "                Welcome!",
          Fore.LIGHTYELLOW_EX + "\n [Internet]: " + Fore.LIGHTGREEN_EX + check_res['internet'],
          Fore.LIGHTYELLOW_EX + "\n [Public IP]: " + Fore.LIGHTGREEN_EX + check_res['ip'],
          Fore.LIGHTYELLOW_EX + "\n [System]: " + Fore.LIGHTGREEN_EX + mach1,
          Fore.LIGHTYELLOW_EX + "\n [GEO]: " + Fore.LIGHTGREEN_EX + str(check_res['geo']),
          Fore.LIGHTYELLOW_EX + "\n [Local IP]: " + Fore.LIGHTGREEN_EX + check_res['local_ip'])
    console()


def console():
    command = input(">>> ")
    if command == "ipinfo":
        ipinfo()
    elif command == "netinfo":
        net_info()
    elif command == "exit":
        import os
        os.system("exit")
    elif command == "cl":
        import platform
        import os
        mach = platform.system()
        if mach == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        console()
    elif command == "help":
        help()
    elif command == "reload":
        start()
    elif command == "netscan":
        net_scan()
    else:
        console()

start()