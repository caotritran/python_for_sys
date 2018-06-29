import psutil

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

temp = "%-17s %8s %8s %8s %8s %8s %8s %10s %8s"
print(temp % ("", "Total", "Used", "Free", "Shared", "Buffer", "Cache", "Available", "Percent"))
ram = psutil.virtual_memory()
swap = psutil.swap_memory()

print(temp % (
    "Ram:",
    bytes2human(ram.total),
    bytes2human(ram.used),
    bytes2human(ram.free),
    bytes2human(ram.shared),
    bytes2human(ram.buffers),
    bytes2human(ram.cached),
    bytes2human(ram.available),
    str(ram.percent) + "%"
)
      )
print(temp % (
    "Swap:",
    bytes2human(swap.total),
    bytes2human(swap.used),
    bytes2human(swap.free),
    "",
    "",
    "",
    "",
    str(swap.percent) + "%"
)
      )
