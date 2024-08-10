import os
import cv2
people = [name for name in os.listdir('../Resources/Faces') if os.path.isdir(os.path.join('../Resources/Faces', name))]
# count1 = 0


# def capture_image(camera_index):
def capture_image(camera_index,text1):
    cap = cv2.VideoCapture(camera_index)
    count = 0
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video', 600, 600)
    while count < 15:
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return

        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            cap.release()
            return

        cv2.putText(frame, "Press S for Capture & Q for Exit ", (100,  400), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), thickness=2)
        cv2.imshow('Video', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('s'):
            # cv2.imwrite(f'Faces/{people[count1]}/{count}.jpg', frame)
            try:
                os.mkdir(f'../Resources/Faces/{text1}')
            except FileExistsError:
                print(f"Folder already exists")

            cv2.imwrite(f'../Resources/Faces/{text1}/{count}.jpg', frame)
            print(f"Image captured and saved to {count}")
            count += 1

    cap.release()
    cv2.destroyAllWindows()


# while count1<len(people):
# capture_image(f'Faces/{people[count1]}.mp4')
# capture_image(0)
# capture_image(0,"900")
# count1+=1
