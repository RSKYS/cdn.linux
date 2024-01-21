#!/bin/bash

mirrors = (
  'https://mirror.datacenter.by/pub/slackware/slackware64-current/'
  'https://mirrors.ustc.edu.cn/slackware/slackware64-current/'
  'https://ftp.tu-chemnitz.de/pub/linux/slackware/slackware64-current/'
  'https://ftp.heanet.ie/mirrors/ftp.slackware.com/pub/slackware/slackware64-current/'
  'https://ftp.linux.org.tr/slackware/slackware64-current/'

)

for mirror in "${mirrors[@]}"; do
    if curl --output /dev/null --silent --head --fail "$mirror"; then
        echo "$mirror" > /etc/slackpkg/mirrors
        break
    fi
done
