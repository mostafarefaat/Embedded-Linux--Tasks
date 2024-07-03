import cv2

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("ERROR: Unable to access the Camera.")

window_name = "Camera Preview"

while True:
    ret, frame = capture.read()
    if not ret:
        print("ERROR: Unable to capture frame.")
    
    cv2.imshow(window_name, frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('c'):
        cv2.imwrite("captured_image.png", frame)
        print("Image Captured successfully")

capture.release()
cv2.destroyAllWindows()

