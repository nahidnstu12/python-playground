# C:\Windows\WinSxS\amd64_microsoft-windows-w..ucture-other-minwin_31bf3856ad364e35_10.0.17134.1_none_1ac029cdce3c581c/hosts

import time
from datetime import datetime as dt

hosts_tmp = "hosts"
hosts_path = r"C:\Windows\WinSxS\amd64_microsoft-windows-w..ucture-other-minwin_31bf3856ad364e35_10.0.17134.1_none_1ac029cdce3c581c/hosts"
redirect = "127.0.0.1"
website_list = ["https://www.w3schools.com/","www.w3schools.com/","www.prothomalo.com/","https://www.prothomalo.com/"]

start = dt(dt.now().year,dt.now().month,dt.now().day,16)
end = dt(dt.now().year,dt.now().month,dt.now().day,23)

# print(end)

while True:
    if(start < dt.now() <= end):
        print("working hours...")
        with open(hosts_tmp,'r+') as file:
            content = file.read()

            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect + " " + site + "\n")
    else:
        print("fun hours...")
        with open(hosts_tmp,'r+') as file:
            content = file.readlines()
            # print(content)
            file.seek(0)
            for line in content:
                if not any (site in line for site in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)