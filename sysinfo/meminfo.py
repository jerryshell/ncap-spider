def meminfo():
    meminfo = {}

    with open('/proc/meminfo') as f:
        for line in f:
            line_split = line.split(':')
            key = line_split[0].strip()
            value = line_split[1].strip()
            meminfo[key] = value

    return meminfo


if __name__ == '__main__':
    meminfo = meminfo()
    print(meminfo)
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))
