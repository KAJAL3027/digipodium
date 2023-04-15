import cv2

# create a videocapture object
cam = cv2.VideoCapture(0)  # 0 -> index of camera

while cam.isOpened():
    status,image = cam.read()
    # gyay 
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # scale to 50%
    img_scaled = cv2.resize(image,None,fx=0.5,fy=0.5)
    cv2.imshow('live',image)
    if cv2.waitkey(1) == ord('q'):
        print('You pressed q key')
        break
    cam.release()
    cv2.destroyAllWindows()
