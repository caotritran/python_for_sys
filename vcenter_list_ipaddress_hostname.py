from unittest import result
import requests, urllib3, json, re, csv

urllib3.disable_warnings()

AUTH_VDC = "ahihi:dongok"
user = AUTH_VDC.split(':')[0]
password = AUTH_VDC.split(':')[1]

global data_resp_network
list_vms = []

def create_session():
    response = requests.post('https://127.0.0.1/api/session', auth=(user, password), verify=False)
    sessionid = json.loads(response.text)
    return sessionid

def get_list_vms():
    sessionid = create_session()
    header = {
            'vmware-api-session-id': '%s' % (sessionid)
    }

    resp = requests.get('https://127.0.0.1/rest/vcenter/vm/', auth=(user, password), headers=header, verify=False)
    if resp.status_code == 200:
        data_response = json.loads(resp.text)['value']

    for i in range(0, len(data_response)):
        target_name = data_response[i].get('vm')
        list_vms.append(target_name)
    return list_vms

        
def get_ipaddress():
    sessionid = create_session()
    vms = get_list_vms()
    header = {
        'vmware-api-session-id': '%s' % (sessionid)
    }

    for i in list_vms:
        resp_network = requests.get('https://127.0.0.1/api/vcenter/vm/{}/guest/networking/interfaces'.format(i), auth=(user, password), headers=header, verify=False)
        resp_hostname = requests.get('https://127.0.0.1/api/vcenter/vm/{}/guest/networking/'.format(i), auth=(user, password), headers=header, verify=False)

        if resp_network.status_code == 200:
            data_resp_network = json.loads(resp_network.text)

        if resp_hostname.status_code == 200:
            data_resp_hostname = json.loads(resp_hostname.text)

        for x in range(0, len(data_resp_network[0].get('ip')['ip_addresses'])):
            ipaddress = data_resp_network[0].get('ip')['ip_addresses'][x].get('ip_address')
            hostname = data_resp_hostname['dns_values'].get('host_name')

            
            if re.search(r'1.2.40.', ipaddress) or re.search(r'1.2.5.', ipaddress):
                with open('listIPs.csv', 'a') as csv_file:
                    csv_file.write("{0},{1},{2}\n".format(ipaddress, hostname, i))
                
    
if __name__ == "__main__":
    with open('listIPs.csv', 'a') as csv_file:
        csv_file.write("IPADDRESS,HOSTNAME,VMID\n")
    get_ipaddress()
