import psutil
import os

def bytes2human(n): #ham chuyen doi byte sang GB
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


templ = "%-17s %8s %8s %8s %8s %8s  %s"
print(templ % ("Device", "Total", "Used", "Free", "Percent", "Type", "Mount"))

for part in psutil.disk_partitions():
    #print(part)
    usage = part.mountpoint
    disk_usage = psutil.disk_usage(usage)
    #print(disk_usage)

    print(templ % (
        part.device,
        bytes2human(disk_usage.total),
        bytes2human(disk_usage.used),
        bytes2human(disk_usage.free),
        str(disk_usage.percent) + "%",
        part.fstype,
        part.mountpoint
    )
          )
