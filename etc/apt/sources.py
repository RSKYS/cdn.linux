import os
import re
import random

curls = ['artfiles.org',
 'ftp.agdsn.de',
 'ftp.byfly.by',
 'ftp.fau.de',
 'ftp.halifax.rwth-aachen.de',
 'ftp.linux.org.tr',
 'ftp.sh.cvut.cz',
 'ftp.uni-hannover.de',
 'mirror.23m.com',
 'mirror.datacenter.by',
 'mirror.netcologne.de',
 'mirror.one.com',
 'mirror.telepoint.bg',
 'mirrors.dotsrc.org',
 'mirrors.netix.net',
 'mirrors.ustc.edu.cn',
 'mirrors.xtom.de',
 'mirrors.xtom.ee']

def Goddamn():
    with open('/etc/os-release') as f:
        os_info = f.read()
    if 'debian' in os_info.lower():
        return 'debian'
    elif 'ubuntu' in os_info.lower():
        return 'ubuntu'
    else:
        return None

def Overwrite(os_type):
    with open('/etc/apt/sources.list', 'r') as file:
        lines = file.readlines()

    newlines = []
    for line in lines:
        if os_type == 'debian' and ('http://*/debian' in line or 'https://*/debian' in line):
            newlines.append(re.sub(r'https?://.*/debian', random.choice([url for url in curls if 'debian' in url]), line))
            
        else:
            newlines.append(re.sub(r'https?://.*/ubuntu', random.choice([url for url in curls if 'ubuntu' in url]), line))
            

    with open('/etc/apt/sources.list', 'w') as file:
        file.writelines(newlines)

os_type = Goddamn()
if os_type:
    Overwrite(os_type)
