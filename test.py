import  time

def  read():
    with open('/Users/mac/opt/2.txt','r') as f:
          f.seek(0,2)
          b=f.tell()
          return b

def readtxt():
    with open('/Users/mac/opt/3.txt','w+') as f2:
        f2.write(str(read()))
def read3():
    with open('/Users/mac/opt/3.txt','r') as f4:
        mercury = int(f4.readline().strip())
        return mercury

def key():
    with open('/Users/mac/opt/2.txt','r') as f3:
        #mas=f3.seek(0,2)
        #sum = mas-read3()
        #print(f3.read(sum))
        f3.seek(read3(),0)
        read()
        readtxt()
        xx=f3.read()
        print()

        
def  writetxt():#生成数据
            while True:
                with open('/Users/mac/opt/2.txt','a') as f1:
                    b=time.localtime()
                    a=time.strftime('%Y-%m-%d %H:%M:%S',b)
                    f1.write('hello'+a+'\n')
                    time.sleep(60)
def main():
    #writetxt()
    key()
    #readtxt()
    
    
if __name__=='__main__':
    main()
