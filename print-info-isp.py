import requests
import json


def resolveIP(ip):
    url = "https://ipinfo.io/" + ip
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data


def main():
    with open("listIP.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(" ")[1]
            print("ISP: {} | City: {} | Region: {} | Country: {} | IP: {}".format(resolveIP(line)['org'], resolveIP(line)['city'], resolveIP(line)['region'], resolveIP(line)['country'], line))


if __name__ == '__main__':
    main()
