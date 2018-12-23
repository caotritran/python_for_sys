# script read by line file and print info:
# 1. resolve IP - timeout 5s
# 2. check status code http
# 3. remark
import os, subprocess
import requests

def reslve_ip(domains):
    #return socket.gethostbyname(domains.strip())
    #ip = os.system('dig +short @resolver1.opendns.com ' + domains)
    ip = os.popen("dig +short @resolver1.opendns.com " + domains).read().strip()

    return ip

def get_http_code(domains):
    domains = "http://" + domains
    try:
        r = requests.head(domains, timeout=4)
        location = r.headers['Location']

        status_code = r.status_code
        print(status_code)

        if status_code == 200:
            print("OK!")
        elif status_code == 404:
            print("Not Found!")
        elif status_code == 503:
            print("Service Unavailable!")
        elif status_code == 301:
            print("Redirect to: " + location)

    except requests.ConnectionError:
        print("failed to connect")

def main():
    with open("list_domain.txt", "r") as f:
        domain = [i.strip() for i in f.readlines()]
        for x in domain:
            print(x)
            print(reslve_ip(x))
            print(get_http_code(x))
            print("=============================================")


if __name__ == '__main__':
    main()
