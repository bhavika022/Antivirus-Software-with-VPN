import socket
import os
import subprocess
import glob
s = socket.socket()
#host=raw_input("enter the host address")
host = '167.172.235.115'
#host='192.168.0.7'
#host="192.168.43.244"
port = 9899

s.connect((host, port))
print("connected")

def filer():
        os.chdir("/home/pratik/Desktop/test")
        filename=raw_input("please enter the filename")
        with open(filename, 'wb') as f:
            print ('file opened')
            while True:
                print('receiving data...')
                data = s.recv(1024)
        #        print('data=%s', (data))
                if not data:
                    break
                # write data to a file
                f.write(data)

        for root, dirs, files in os.walk("/home/pratik/Desktop/test"):
            for file in files:
                if file.endswith(".py"):
                    
                    a="true"
                    print(os.path.join(root, file))
        if(a=="true"):
            print("deleted")

            directory='test' #JIS FOLDER MAI VIRUS H US FOLDER KA NAAM LIKH test ke badle, yeh code us folder ke bhar save kr yaah fir directory ki address daalo
           # os.chdir(directory)
            file=glob.glob('*.py')
            for filename in file:
              os.unlink(filename)

        f.close()
        print('Successfully got the file')
        s.close()
        print('connection closed')
        
filer()


