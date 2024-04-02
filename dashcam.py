import cv2

def main():
    # Initialize the USB camera
    cap = cv2.VideoCapture(0)  # Change the parameter if you have multiple cameras (e.g., 1 for the second camera)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        # Capture video frame by frame
        while True:
            ret, frame = cap.read()  # Read a frame from the camera

            if not ret:
                print("Error: Failed to grab frame.")
                break

            # Display the frame
            cv2.imshow('USB Camera', frame)

            # Check for key press and exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Release the camera and close OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
