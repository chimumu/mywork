import requests
import urllib
import re
import os
r = urllib.request.urlopen('https://mirrors.aliyun.com/ceph/rpm-nautilus/el7/x86_64/')
a = r.read().decode('utf-8')
c = re.compile('>.*14\.2\.4-0.*<')
b= c.findall(a)

lists = []
list1 = []
for i in b:
    w = i.strip('<').strip('>')
    lists.append(w)

for j in range(0,len(lists)):
    list1.append(lists[j])

for k in list1:
    urllib.request.urlretrieve('https://mirrors.aliyun.com/ceph/rpm-nautilus/el7/x86_64/'+k,'E:\\ll\\%s'%k)

