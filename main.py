import cv2 

ref = cv2.CascadeClassifier('ref/ref.xml')
cam = cv2.VideoCapture(0)


def settingCamera(kamera):
    wajah = ref.detectMultiScale(kamera,scaleFactor=1.1, minSize=(40, 40))
    return wajah


def box(kamera):
    for x ,y,w,h in settingCamera(kamera):
        cv2.rectangle(kamera ,(x,y),(x+w , y+h),(255,255,255),5)
        
def main():
    while True:
        _, kamera = cam.read()
        box(kamera)
        gray = cv2.cvtColor(kamera, cv2.COLOR_BGR2GRAY)
        cv2.imshow("box camera", kamera)
        key = cv2.waitKey(1) & 0xFF
        if key == 27 :
            break
result = main()


cam.release()
cv2.destroyAllWindows()