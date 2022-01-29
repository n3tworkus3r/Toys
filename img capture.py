import cv2

"""capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
result,img = capture.read()
#cv2.imshow("_", img)
cv2.imwrite("D:\\img.jpg", img)
"""

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
codec = cv2.VideoWriter_fourcc(*'XVID')
# VideoWriter(filename, fourcc, fps, frameSize)
out = cv2.VideoWriter('captured.avi',codec, 25.0, (640,480))


while capture.isOpened():
    result, frame = capture.read()
    out.write(frame)
    if result == False:
        break

out.release()
capture.release()