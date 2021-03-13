import json
import csv
import requests
import os.path

def download_json_file():
    zabbix_url = 'http://1.2.3.4/zabbix/api_jsonrpc.php'

    r = requests.get(zabbix_url,
                     json={
                        "jsonrpc": "2.0",
                        "method": "item.get",
                        "params": {
                            "output": "extend",
                            "hostids": "10084",
                            "search": {
                                "key_": "domain"
                            },
                            "sortfield": "name"
                        },
                        "auth": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        "id": 1
                    })
    if os.path.isfile('myfile.csv'):
        os.remove("myfile.csv")

    data = json.dumps(r.json(), indent=4, sort_keys=True)
    csv_file = open("myfile.csv", "w")
    csv_file.writelines(data)
    csv_file.close()

def json_handle():
    with open('myfile.csv') as json_file:
        data = json.load(json_file)
        with open('listDomainsExpire.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Domains", "Days Left"])
            for p in data['result']:
                domain = str(p['name']).split(" ")[0]
                exprire_date = p['lastvalue']
                writer.writerow([domain, exprire_date])

if __name__ == '__main__':
    download_json_file()
    json_handle()
