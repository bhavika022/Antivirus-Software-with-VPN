from Tkinter import *
import os
import socket
import subprocess
import time
import glob 
creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'

def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
 
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Signup') # This renames the title of said window to 'signup'
    roots.geometry('1000x1500')
    roots.configure(background='gray')
    
    intruction = Label(roots, text='Please Enter new Credidentials\n',font=('arial',25)) # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=NE) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
    intruction.configure(background='gray')
 
    nameL = Label(roots, text='New Username: ',font=('arial',20),bd=15) # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ',font=('arial',20),bd=15) # ^^
    nameL.grid(row=1, column=0, sticky=NE) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=NE) # ^^
    nameL.configure(background='gray')
    pwordL.configure(background='gray')
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE.grid(row=2, column=1) # ^^
 
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=NE,padx=10,pady=10)
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
 
 
def FSSignup():
    with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.close() # Closes the file
 
    roots.destroy() # This will destroy the signup window. :)
    Login() # This will move us onto the login definition :D
 
def Login():
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title('Login') # This makes the window title 'login'
    rootA.configure(background='Gray')
    rootA.geometry('1000x1500')
    
 
    intruction = Label(rootA, text='ANTIVIRUS SOFTWARE\n',font=('arial',25),fg='white') # More labels to tell us what they do
    intruction.grid(sticky=NE) 
    intruction.configure(background='Gray')
 
    nameL = Label(rootA, text='Username: ',font=('arial',20),bd=15) # More labels
    pwordL = Label(rootA, text='Password: ',font=('arial',20),bd=15) # ^
    nameL.grid(row=1, sticky=NE)
    pwordL.grid(row=2, sticky=NE)
    nameL.configure(background='Gray')
    pwordL.configure(background='Gray')
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1,padx=8)
    pwordEL.grid(row=2, column=1,padx=8)
 
    loginB = Button(rootA, text='Login',fg='blue',command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=NE,padx=10,pady=10)
 
    rmuser = Button(rootA, text='Sign Up', fg='red', command=DelUser) # This makes the deluser button. blah go to the deluser def.
    rmuser.grid(columnspan=2, sticky=NE,padx=10,pady=10)
    rootA.mainloop()
 
def CheckLogin():
    global rlbl
    
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        r = Tk() # Opens new window
        r.title('Enter IP')
        r.geometry('1000x1500') # Makes the window a certain size
        r.configure(background='gray')

        intructionr = Label(r, text='ANTIVIRUS SOFTWARE\n',font=('arial',25),fg='white') 
        intructionr.grid(sticky=W) 
        intructionr.configure(background='Gray')
        
        rlbl = Label(r, text='Enter IP',font=('arial',20),bd=15) 
        rlbl.grid(row=1,sticky=NE)
        rlbl.configure(background='Gray')
        rlbl = Entry(r)
        rlbl.grid(row=1,column=1)
         # Pack is like .grid(), just different
        #s = socket.socket()
        #host=raw_input("enter the host address")
        #host = '167.172.235.115'
        #host='192.168.0.7 '

        #port = 9999

        
        rgo= Button(r, text='go',fg='blue', command= Home)
        rgo.grid(columnspan=2, sticky=NE)
        
        
        r.mainloop()
    else:
        r = Tk()
        r.title('Enter Site')
        r.geometry('1000x1500')
        r.configure(background='Gray')
        rlbl = Label(r, text='\n[!] Invalid Login',font=('arial',14),bd=15)
        rlbl.configure(background='Gray')
        rlbl.pack()
        r.mainloop()
        
        
        
def Home():
    global s
    s = socket.socket()
    #host=raw_input("enter the host address")
    host = '167.172.235.115'
    #host='192.168.0.7'

    port = 9899

    s.connect((host, port))
    

    global downlF
    global rootf

    rootf=Tk()
    rootf.title('Download File')
    rootf.configure(background='Gray')
    rootf.geometry('1000x1500')

    intructionD = Label(rootf, text='ANTIVIRUS SOFTWARE\n',font=('arial',25),fg='white') 
    intructionD.grid(sticky=W) 
    intructionD.configure(background='Gray')

    downlF = Label(rootf, text='File Name',font=('arial',20),bd=15)
    downlF.grid(row=1,sticky=NE)
    downlF.configure(background='Gray')
    downlF = Entry(rootf)
    downlF.grid(row=1,column=1)
    #filename=StringVar()
    #filename.set(downlF.get())
    
    down =Button(rootf, text='download',fg='blue',command=file2)
    filer()
    down.grid(columnspan=2,sticky=NE)

    down.mainloop()


def filer():
        global downlF
        os.chdir("/home/pratik/Desktop/test")
        filename="s.py"
        with open(filename, 'wb') as f:
         #   print ('file opened')
            while True:
          #      print('receiving data...')
                data = s.recv(1024)
        #        print('data=%s', (data))
                if not data:
                    break
                # write data to a file
                f.write(data)
        fi()
   #     fi2()
        f.close()
        #print('Successfully got the file')
        s.close()
        #print('connection closed')


def fi():
        for root, dirs, files in os.walk("/home/pratik/Desktop/test"):
            for file in files:
                if file.endswith(".py"):             
                    smit="true"
           #        print(os.path.join(root, file))
        if(smit=="true"):
            #print("deleted")
            directory='test' #JIS FOLDER MAI VIRUS H US FOLDER KA NAAM LIKH test ke badle, yeh code us folder ke bhar save kr yaah fir directory ki address daalo
           # os.chdir(directory)
            file=glob.glob('*.py')
            for filename in file:
              os.unlink(filename)
      

"""def fi2():
    for root, dirs, files in os.walk("/home/pratik/Desktop/test"):
            for file in files:
                if file.endswith(".bat"):             
                    s="true"
           #        print(os.path.join(root, file))
        if(s=="true"):
            #print("deleted")
            directory='test' #JIS FOLDER MAI VIRUS H US FOLDER KA NAAM LIKH test ke badle, yeh code us folder ke bhar save kr yaah fir directory ki address daalo
           # os.chdir(directory)
            file=glob.glob('*.bat')
            for filename in file:
              os.unlink(filename)    
"""    
    

def file2():
    global rootn

    rootn=Tk()
    rootn.title('File status')
    rootn.configure(background='Gray')
    rootn.geometry('1000x1500')

    intructionf = Label(rootn, text='ANTIVIRUS SOFTWARE\n',font=('arial',25),fg='white') 
    intructionf.grid(sticky=W) 
    intructionf.configure(background='Gray')

    inst=Label(rootn,text='file is downloaded',font=('arial',15),fg='red')
    inst.grid(sticky=NE)
    inst.configure(background='gray')

    log = Button(rootn, text='Logout',fg='blue',command=Login) 
    log.grid(columnspan=2, sticky=E,padx=10,pady=10)



def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() # Destroys the login window
    Signup() # And goes back to the start!
 
if os.path.isfile(creds):
    Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()
