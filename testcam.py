import cv2

cap = cv2.VideoCapture(0)  # Use the correct index

if not cap.isOpened():
    print("Error: Camera not accessible.")
else:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Test Frame", frame)
        cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()