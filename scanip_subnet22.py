#scan ip in subnetmask /22
#range ip: 103.221.220.1 - 103.221.223.254

import sh, os

ip = str(raw_input("nhap lop mang ip thuoc subnet 22 theo dinh dang x.y.z.w: "))
list_ip = ip.split(".")

for i in list_ip:
    n = list_ip[2]

print "Dang Ping Scan ... Doi Xiu Nha..."

def ping_n():
    f = open("/home/tritran/Desktop/python_learn/scanip.csv", "a")
    for i in range(1, 256):
        address = list_ip[0] + "." + list_ip[1] + "." + n + "." + str(i)
        print address
        try:
            sh.ping(address, "-c 1", _out="/dev/null")
            f.write(address + "\t" "Live" + "\n")
        except sh.ErrorReturnCode_1:
            f.write(address + "\t" "None" + "\n")
    f.close()
    print " 1/4 completed ..."

def ping_n1():
    a = int(n) + 1
    a = str(a)

    f = open("/home/tritran/Desktop/python_learn/scanip.csv", "a")
    for i in range(0, 256):
        address = list_ip[0] + "." + list_ip[1] + "." + a + "." + str(i)
        print address
        try:
            sh.ping(address, "-c 1", _out="/dev/null")
            f.write(address + "\t" "Live" + "\n")
        except sh.ErrorReturnCode_1:
            f.write(address + "\t" "None" + "\n")
    f.close()
    print " 2/4 completed ..."

def ping_n2():
    b = int(n) + 2
    b = str(b)

    f = open("/home/tritran/Desktop/python_learn/scanip.csv", "a")
    for i in range(0, 256):
        address = list_ip[0] + "." + list_ip[1] + "." + b + "." + str(i)
        print address
        try:
            sh.ping(address, "-c 1", _out="/dev/null")
            f.write(address + "\t" "Live" + "\n")
        except sh.ErrorReturnCode_1:
            f.write(address + "\t" "None" + "\n")
    f.close()
    print " 3/4 completed ..."

def ping_n3():
    c = int(n) + 3
    c = str(c)

    f = open("/home/tritran/Desktop/python_learn/scanip.csv", "a")
    for i in range(0, 255):
        address = list_ip[0] + "." + list_ip[1] + "." + c + "." + str(i)
        print address
        try:
            sh.ping(address, "-c 1", _out="/dev/null")
            f.write(address + "\t" "Live" + "\n")
        except sh.ErrorReturnCode_1:
            f.write(address + "\t" "None" + "\n")
    f.close()
    print "4/4 completed ..."

if __name__ == '__main__':
    ping_n()
    ping_n1()
    ping_n2()
    ping_n3()



