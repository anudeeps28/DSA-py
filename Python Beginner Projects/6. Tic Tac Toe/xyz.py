import cv2

# Open a connection to the webcam (usually the first camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    if not ret:
        break
    cv2.imshow('Webcam', frame)  # Display the frame

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()