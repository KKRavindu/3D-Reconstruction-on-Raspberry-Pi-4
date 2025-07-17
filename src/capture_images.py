from picamera2 import Picamera2
import time, os, cv2

save_dir = "/home/pi/Desktop/2D_to_3D/images"  # save images on //home/pi/Desktop/2D_to_3D/images
os.makedirs(save_dir, exist_ok=True)

# Initialize camera
picam2 = Picamera2()
config = picam2.create_still_configuration(main={"format": 'RGB888', "size": (640, 480)})
picam2.configure(config)
picam2.start()

print("Camera is warming up...")

time.sleep(2)  # Let camera adjust

for i in range(20):
    print(f"[{i+1}/20] Previewing... Press 'c' to capture or 'q' to quit.")
    
    while True:
        frame = picam2.capture_array()
        cv2.imshow("Live Camera Preview", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):  # Press 'c' to capture
            filename = os.path.join(save_dir, f"img_{i:03d}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Captured and saved {filename}")
            break

        elif key == ord('q'):  # Optional exit
            print("Capture aborted.")
            picam2.stop()
            cv2.destroyAllWindows()
            exit()

    time.sleep(0.5)

picam2.stop()
cv2.destroyAllWindows()
print("✅ All images captured.")
