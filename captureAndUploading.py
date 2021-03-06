import cv2
import dropbox
import time
import random
start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = 'img'+ str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print('snapshottaken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = '_2F3kkpTl_oAAAAAAAAAAd1ik1lU48_dfX50CDzlt3Q_nU12TN-uiDyle5rwir1G'
    file = img_counter
    file_from = file
    file_to = '/newFolder1/'+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print('fileuploaded')

def main(): 
    while(True): 
        if ((time.time() - start_time) >= 5): 
            name = take_snapshot() 
            upload_file(name) 
            
main()

    