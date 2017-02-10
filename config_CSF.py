import os, sh
 
if not os.path.isfile("/etc/csf/csf.conf"):
    print "chua cai csf, vui long cai dat!!!"
else:
    os.system("rm -rf " + "/etc/csf/csf.conf")
    sh.wget("--no-check-certificate", "https://cocghe.com/csf.conf", "-O", "/etc/csf/csf.conf")
    os.system("chmod 600 " + "/etc/csf/csf.conf")
    os.system("chown root:root " + "/etc/csf/csf.conf")
    os.system("csf -r " +  "> " + "/root/csf.log")
    print "da tai file config chuan cua csf ve"