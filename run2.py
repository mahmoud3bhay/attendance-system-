import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import tkinter.ttk as ttk
import tkinter.font as font
import numpy as np
from PIL import Image, ImageTk
import csv
import json
import pandas as pd
import pandasgui
import re
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView

import pandas as pd

window=tk.Tk()  # window creation 
window.title("Student Attendence system")
window.geometry('1366x768')


####Login Credentials


#####Loading Data from txt file
def loading_data():
    file=open('data.txt','r',encoding='utf-8')
    data=json.load(file)
    file.close()
    return data
##Saving Data to .txt file
def saving_data(data):
    file=open('data.txt','w',encoding='utf-8')
    json.dump(data,file,ensure_ascii=False)
    file.close()

##saving data in a variable
#data=dict()
data=loading_data()
print(data)



#HEADINGS




login_label= tk.Label(window, text="Login Here" ,bg="gray"  ,fg="white"  ,width=20 ,height=1,font=('times', 30, 'bold')) 
login_label.place(x=40, y=150)

reg_label= tk.Label(window, text="Register Here" ,bg="gray"  ,fg="white"  ,width=20 ,height=1,font=('times', 30, 'bold')) 
reg_label.place(x=700, y=150)

msg_label=tk.Label(window,text="Notification: ",bg='grey' ,fg='white',width=10,height=1,font=('times',15,'bold'))
msg_label.place(x=350,y=500)
message = tk.Label(window,text="",bg="Grey" ,fg="white", width=30, height=1, font=('times',15,'bold'))
message.place(x=500,y=500)

#get_info=tk.Label(window,text="get info: ",bg='#0467D6' ,fg='white',width=10,height=2,font=('times',15,'bold'))
#get_info.place(x=350,y=600)



#Login FIEDLS
lbl = tk.Label(window, text="Enter ID :",width=10,height=1  ,fg="black"  ,bg='#0467D6' ,font=('times', 15, ' bold ') ) 
lbl.place(x=40, y=210)

txt = tk.Entry(window,width=25  ,bg='#0467D6' ,fg="black",font=('times', 15, ' bold '))
txt.place(x=250, y=210)

lbl2= tk.Label(window, text="Enter Password :",width=15  ,height=1  ,fg="black"  ,bg='#0467D6' ,font=('times', 15, ' bold ') ) 
lbl2.place(x=40, y=250)

txt2 = tk.Entry(window,width=25  ,bg='#0467D6' ,show='*',fg="black",font=('times', 15, ' bold '))
txt2.place(x=250, y=250)

day = tk.Entry(window,width=8  ,bg='#0467D6' ,fg="black",font=('times', 30, ' bold '))
day.place(x=250,y=80)

day_label= tk.Label(window, text="Day : " ,bg='#0467D6'  ,fg="white"  ,width=8 ,height=1,font=('times', 30, 'bold')) 
day_label.place(x=40, y=80)
info = tk.Entry(window,width=10  ,bg='#0467D6' ,fg="black", font=('times', 15, ' bold '))
info.place(x=500,y=600)



#Register Fields

name_label = tk.Label(window, text="Enter Name :",width=10  ,height=1  ,fg="black"  ,bg='#0467D6' ,font=('times', 15, ' bold ') ) 
name_label.place(x=700, y=213)

name_entry = tk.Entry(window,width=25  ,bg='#0467D6' ,fg="black",font=('times', 15, ' bold '))
name_entry.place(x=940, y=213)

lbl3 = tk.Label(window, text="Enter ID :",width=10  ,height=1  ,fg="black"  ,bg='#0467D6' ,font=('times', 15, ' bold ') ) 
lbl3.place(x=700, y=250)

txt3 = tk.Entry(window,width=25  ,bg='#0467D6' ,fg="black",font=('times', 15, ' bold '))
txt3.place(x=940, y=250)

lbl4= tk.Label(window, text="Enter Password",width=15  ,height=1  ,fg="black"  ,bg='#0467D6' ,font=('times', 15, ' bold ') ) 
lbl4.place(x=700, y=300)

txt4 = tk.Entry(window,width=25  ,bg='#0467D6' ,show='*',fg="black",font=('times', 15, ' bold '))
txt4.place(x=940, y=300)






#Main

def login_clear():
    txt.delete(0,'end')
    txt2.delete(0,'end')
    
    #res = ""
    #txt.configure(text= res)
    #txt2.configure(text=res)
def reg_clear():
    txt3.delete(0,'end')
    txt4.delete(0,'end')
    name_entry.delete(0,'end')
    #res = ""
    #txt3.configure(text= res)
    #txt4.configure(text=res)
    
    
    
    
    ################## Login_Functions   ######################

    #When Submit button is clicked We have to Track the Person from our data through web cam
        
def TrackImages() :#(UserId,pasword):
    d= day.get()
    if len(d) == 0:
        message.configure(text="please enter day first ")
        return
        
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    
    
    df=pd.read_csv("Details\Details.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX          
    run_count=0;run=True
    
    while run:
        
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5) 
        
        for(x,y,w,h) in faces:
            
            #cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            
            print(Id, conf)
            
            if(conf < 50):
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                
                #aa=df.loc[df['Id'] == Id][data[Id]].values
                #aa = pasword
                pasword = data[str(Id)]
                tt = str(Id)+"-"+ str(pasword)#str(aa[0])
                
                #if (str(Id)==str(Id)): #***
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)
                message.configure(text="Face Recognised Successfully")
                attendence = pd.read_csv('Data.csv')
                row =attendence.loc[attendence['Id']==int(Id)]
                row_index = row.index[0]
                #print(row_index)
                attendence.iloc[row_index , int(d)+1] = "yes"
                attendence.to_csv('D:\\Computer vision\\login system with face id\\Data.csv',index=False)
                    #run=False
            else:
                cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
                #Id='Unknown'                
                #tt=str(Id)  
                cv2.putText(im,"unknown",(x,y+h), font, 1,(255,255,255),2)
                    
        #run_count += 1    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q') ):#or run_count==150):
            #message.configure(text="Unable to Recognise Face")
            break
    
    cam.release()
    cv2.destroyAllWindows()
        


def login_submit():
    a=txt.get()
    b=txt2.get()
    d = day.get()
    #c= int(a)
    #print(type(d))
    #print(type(c))
    
    if len(d) !=0 :
        if (str(a) in data):
            if(data[a] == str(b)):
                #TrackImages(a,b)
                message.configure(text="successfully logged in ")
                attendence = pd.read_csv('Data.csv')
                row = attendence.loc[attendence['Id']==int(a)]
                row_index = row.index[0]
                #print(row_index)
                attendence.iloc[row_index , int(d)+1] = "yes"
                attendence.to_csv('D:\\Computer vision\\login system with face id\\Data.csv',index=False)
            else:
                message.configure(text="Id and Password does not Match")
        else:
            message.configure(text="Entered Id does not Exist")
    else :
        message.configure(text="please, enter Day first")
    

    login_clear()
    
    
    
    
################## Register_Functions   ######################




def TakeImages():        
    Id=(txt3.get())
    password=(txt4.get())
    name = (name_entry.get())
    ret=0
    if (Id not in data):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+password +'.'+Id+'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>30:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" password : "+ password
        
        
        folder = 'D:/Computer vision/login system with face id/TrainingImage'
        img = folder +'/' +' '+password +'.'+Id+'.'+'2'+'.jpg'
        row = [Id ,password, name,img]
        with open('Details\Details.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        
        with open('Data.csv','a+') as File:
            writer1 = csv.writer(File)
            writer1.writerow([Id,name])
        File.close()
        #print(type(Id))

        message.configure(text= res)
        ret=1
    else:
        res = "User name Already Exists...Try another one!!!"
        message.configure(text= res)
    return ret

# Training Images

def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    #print(faces,np.array(Id))
    #res = "Image Trained"#+",".join(str(f) for f in Id)
    res="Registration Successful"
    message.configure(text= res)
    return True
    

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image path  s and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids


def reg_submit():
    name_value = name_entry.get()
    if name_value.isdigit() == False:
        Userid=txt3.get()
        if Userid.isdigit():# and type(name_value)!=str:
            if TakeImages()==1:
                if TrainImages():
                    data[txt3.get()] = txt4.get()
                    #data[id] = password 
                    saving_data(data)
                else:
                    pass
        
        else:
            message.configure(text="User Id Should contain number only!!!")
    else :
        message.configure(text="Name Should contain string only!!!")
    reg_clear()
    print(data)










#-----------------------info
def get_info():
    user = info.get()
    if len(user) ==0 :
        message.configure(text="please enter ID  ")
        
    else :
        if str(user) not in data:
            message.configure(text="ID does not exist")
        else :
           ######
            userid = int(user)
            df = pd.read_csv('Data.csv')
            df =df.loc[df['Id']== userid]
            
            
            #row_index = row.index[0]
            #root = tk.Tk()
        
            # Set the window title
            #root.title('DataFrame Viewer')
        
            # Create a frame for the DataFrame viewer
            #frame = ttk.Frame(root, padding=10)
            #frame.pack(fill='both', expand=True)
            
            folder_path = 'D:/Computer vision/login system with face id/TrainingImage/'
            #image_ext = ('.jpg', '.jpeg', '.png', '.gif')
            #pattern = r'.'+str(id)
            #regex = re.compile(pattern)
            #for file in os.listdir(folder_path):
                #match = regex.search(file)
                #if match :
                    #img = folder_path + '/'+str(id)
                    
                    #print(img)
                    #break
        
            image =folder_path+' '+data[str(user)]+'.'+str(user)+'.2'+'.jpg'
            
            #testImage = img.imread(image)
          
        # displaying the image
            #plt.imshow(testImage)
            # Create a PandasGui DataFrame viewer in the frame
            #viewer = pandasgui.show(df, app_name='Data Viewer')
            
            #cv2.imshow("student photo" , image)
            #cv2.waitKey(0)
          
            # closing all open windows
            #cv2.destroyAllWindows()
            # Run the Tkinter event loop
            #root.mainloop() #####
            #import sys
            #from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
            #from PyQt5.QtWebEngineWidgets import QWebEngineView
            #from PyQt5.QtGui import QPixmap
            
            #import pandas as pd
            
            
            #df = pd.DataFrame(data)
            
            app = QApplication(sys.argv)
            window = QWidget()
            
            # Create a QWebEngineView widget to display the DataFrame as an HTML table
            table_view = QWebEngineView()
            table_html = df.to_html()
            table_view.setHtml(table_html)
            
            # Create a QLabel widget to display the image
            image_label = QLabel()
            pixmap = QPixmap(image)
            pixmap = pixmap.scaled(500, 500)  # Resize the QPixmap to 500x500 pixels
            image_label.setPixmap(pixmap)
            
            # Create a QShortcut object to listen for the "q" key press event
            q_shortcut = QShortcut((QKeySequence("q")), window)
            q_shortcut.activated.connect(app.quit)
            
            # Create a QVBoxLayout and add the table_view and image_label widgets to it
            layout = QVBoxLayout()
            layout.addWidget(table_view)
            layout.addWidget(image_label)
            
            # Set the main window's layout to the QVBoxLayout
            window.setLayout(layout)
            
            # Show the main window
            window.show()
            
            # Start the application event loop
            app.exec_()
            #sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    #----------------------------------
    #Login Actions
    
submit = tk.Button(window, text="Submit",fg="black",command= login_submit, bg='#0467D6'  ,width=25  ,height=1 ,activebackground = "white" ,font=('times', 10, ' bold '))
submit.place(x=40, y=300)



clearButton = tk.Button(window, text="Clear",fg="black", command=login_clear,bg='#0467D6'  ,width=25  ,height=1, activebackground = "white" ,font=('times', 10, ' bold '))
clearButton.place(x=300, y=300)

#Register Actions
submit2 = tk.Button(window, text="Submit",fg="black", command=reg_submit, bg='#0467D6'  ,width=25  ,height=1 ,activebackground = "white" ,font=('times', 10, ' bold '))
submit2.place(x=700, y=350)

clearButton2 = tk.Button(window, text="Clear",command=reg_clear, fg="black"  ,bg='#0467D6'  ,width=25  ,height=1, activebackground = "white" ,font=('times', 10, ' bold '))
clearButton2.place(x=940, y=350)

infoButton2 = tk.Button(window, text="get info",command=get_info , fg="black"  ,bg='#0467D6'  ,width=20  ,height=2, activebackground = "white" ,font=('times', 10, ' bold '))
infoButton2.place(x=340, y=600)

startcamera = tk.Button(window, text="start camera",command= TrackImages  , fg="black"  ,bg='#0467D6'  ,width=20  ,height=2, activebackground = "white" ,font=('times', 10, ' bold '))
startcamera.place(x=40, y=350)


#final Actions
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg='#08155F'   ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=1000, y=550)
window.mainloop()
    