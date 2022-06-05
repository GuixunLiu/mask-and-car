import cv2
import os,sys
cap = cv2.VideoCapture(r"opencv\result1.mp4")
isOpened = cap.isOpened
print(isOpened)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(fps,width,height)

os.chdir(r"opencv\savePic\1")

print(os.getcwd())

i = 0
while(isOpened):
    if i == 100:
        break
    else:
        i = i+1
    (flag,frame) = cap.read()   #读取每一帧，flag表示是否读取成功，frame为图片内容。
    fileName = "image" +str(i) +".jpg"
    print(fileName)
    if flag == True:
        cv2.imwrite(fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])

os.chdir(r"opencv\savePic")
print(os.getcwd())
print("end!")
