import cv2
import face_recognition
import os
from datetime import datetime
from datetime import date

path="Assets//Faces"
imageList = [ ]
imageName = [ ]

#---------Storing the images names
myList = os.listdir(path)
print(myList)

#START OF READING IMAGES FROM FILE
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    imageList.append(curImg)
    imageName.append(os.path.splitext(cl)[0])
print(imageName)
#END OF READING IMAGES FROM FILE


#-------------------START OF FINDING ENCODINGS OF THE KNOWN FACES
def findEncodings(images):
    encodList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodList.append(encode)
    return encodList

knownEncodings=findEncodings(imageList)
#-------------------END OF FINDING ENCODINGS OF THE KNOWN FACES

#START OF ADDING WEBCAM FACES TO excel Sheet
def markAttendance(name):
    now = datetime.now()
    today = date.today()
    st_date = today.strftime("%d/%m/%Y")
    st_time = now.strftime("%H:%M:%S")
    with open('Attendence.csv','r+') as f:
        myDataList = f.readlines()
        nameList = [ ]
        DateList = [ ]

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            DateList.append(name+entry[2])
        if name not in nameList:
            f.writelines(f'\n{name},{st_time},{st_date}')
        elif name+st_date not in DateList:
            f.writelines(f'\n{name},{st_time},{st_date}')
#END OF ADDING WEBCAM FACES TO excel Sheet............


#-------------------START OF RECOGNISING FACES FROM WEBCAM
cap = cv2.VideoCapture(0)
while(True):
    RecognizedName = [ ]
    ret, frame = cap.read()
    gray = frame[:, :, ::-1]    #TO CONVERT COLOR TO GRAY
    loc = face_recognition.face_locations(gray)
    enc = face_recognition.face_encodings(gray,loc)


    for i,j in zip(enc,loc):
        matches = face_recognition.compare_faces(knownEncodings,i)
        dis = face_recognition.face_distance(knownEncodings,i)
        if True in matches:
            index = matches.index(True)
            RecognizedName.append(imageName[index])
            markAttendance(imageName[index])
        else:
            RecognizedName.append("Unknown")
        for(x,y,w,h),j in zip(loc,RecognizedName):
            cv2.rectangle(frame , (h,w-35) , (y,w) , (100,100,100) , cv2.FILLED)
            cv2.putText(frame, j, (h + 6, w - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
