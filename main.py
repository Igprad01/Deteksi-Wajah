import cv2 
import os

ref = cv2.CascadeClassifier('ref/ref.xml')
cam = cv2.VideoCapture(0)

if not os.path.exists('record'):
    os.makedirs('record')

def settingCamera(kamera):
    wajah = ref.detectMultiScale(kamera, scaleFactor=1.1, minSize=(40, 40))
    return wajah

def box(kamera, frame_number):
    wajah = settingCamera(kamera)
    for x, y, w, h in wajah:
        kotakdeteksi = cv2.rectangle(kamera, (x, y), (x+w, y+h), (0, 255, 0), 2)
        namapicture = f'wajah.{frame_number}.jpg'
        # namaFile = f'wajah.{frame_number}.{x}.{y}.jpg' (fungsi untuk menangkap gambar secara otomatis)
        cv2.imwrite(f"record/{namapicture}", kotakdeteksi)

def main():
    frame_number = 0
    while True:
        _, kamera = cam.read()
        gray = cv2.cvtColor(kamera, cv2.COLOR_BGR2GRAY)
        box(kamera, frame_number)  
        cv2.imshow("box camera", kamera)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  
            break
        elif key == ord('c'):  
            frame_number += 1

    cam.release()
    cv2.destroyAllWindows()

result = main()
