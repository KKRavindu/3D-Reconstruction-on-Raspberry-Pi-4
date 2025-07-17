from picamera2 import Picamera2
import time, os, cv2

save_dir = "/home/pi/Desktop/2D_to_3D/images"
os.makedirs(save_dir, exist_ok=True)

picam2 = Picamera2()
config = picam2.create_still_configuration(main={"format": 'RGB888', "size": (640, 480)})
picam2.configure(config)
picam2.start()

print("Camera ready. Move camera slightly before each capture.")

for i in range(20):  # Adjust number of images here
    input(f"[{i+1}/20] Press Enter to capture...")
    frame = picam2.capture_array()
    filename = os.path.join(save_dir, f"img_{i:03d}.jpg")
    cv2.imwrite(filename, frame)
    print(f"Saved {filename}")
    time.sleep(1)

print("Image capture complete.")
