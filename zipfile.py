import  zipfile36
import os
import itertools
import threading
import sys
from datetime import datetime
from time import time
#############这是一个破解压缩包密码的程序############

def zip():
     mas=zipfile36.ZipFile('test.zip','a')
     for i in os.listdir('C:\\Users\\Administrator\\Desktop\\OpsManage-beta\\OpsManage\\views\\test'):
          mas.write(i)
     mas.close()

def unzip(pwd_1,mas):
    try:
         mas.extractall(path='.',pwd=pwd_1.encode('utf-8')) #解压
         print(pwd_1)
         global  flag
         flag=False
    except RuntimeError:
        pass

if __name__=='__main__':
    mas_1 = zipfile36.ZipFile('test1.zip', 'r')
    iter_1 = itertools.permutations(range(3), 2)
    flag = True
    for i in iter_1:
        a = str(i).split(',')
        iter_2 = ''.join(a)
        iter_3 = iter_2.strip('(').strip(')')
        passwd = iter_3.replace(' ', '')
        th1 = threading.Thread(target=unzip,args=(passwd,mas_1))
        th2 = threading.Thread(target=unzip,args=(passwd,mas_1))
        th1.start()
        th2.start()
        th1.join()
        th1.join()



