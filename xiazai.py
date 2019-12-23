
import urllib
import re
import urllib.request as ur

def readtxt(): #读取文件

    with open("D:\\ll\\mak.txt",'r') as f:
        a = f.readlines()
        list3 = []
        for j in a:
           lines = j.split()
           list3.append(lines[0])
        return list3

def noarch(mas,kubelet): #下载nparch下的文件
    r = ur.urlopen(kubelet)
    a = r.read().decode('utf-8')
    c = re.compile(r'title="' + mas + '.*?</a>')
    b = c.findall(a)
    lists = []
    list1 = []

    for i in b:  #判断是否在linux里面
        w = i.split(">")
        s = w[0].strip("title=").strip(("\"\""))
        lists.append(s)

    for j in range(0, len(lists)):
        list1.append(lists[j])

    for k in list1:
        ur.urlretrieve(kubelet+ k, 'E:\\noarch\\%s' % k)

def linux(mecury,proxy): #下载linux下的文件

    r = ur.urlopen(mecury)
    a = r.read().decode('utf-8')

    for k in readtxt():
        c = re.compile(r'title="'+k+'.*?</a>')
        b= c.findall(a)
        lists=[]
        list1=[]

        if b:
            for i in b:
                w=i.split(">")
                s=w[0].strip("title=").strip(("\"\""))
                #list1 = []
                lists.append(s)
            for j in range(0,len(lists)):
                list1.append(lists[j])

            for k in list1:

                ur.urlretrieve(mecury+k,'E:\\linux\\%s'%k)

        else:
             noarch(k,proxy)

def main():
  bb='https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/linux-64/'
  cc='https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/noarch/'
  linux(bb,cc)

if  __name__  ==   '__main__':
    main()
