import cv2

capture = cv2.VideoCapture(0)

test = cv2.VideoWriter_fourcc(*'XVID')
sortie = cv2.VideoWriter('vidéo.avi',test, 25.0, (640,480))

while( capture.isOpened() ):
    ret, frame = capture.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        sortie.write(frame)
        cv2.imshow('frame' , frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
sortie.release()
cv2.destroyAllWindows()