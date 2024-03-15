#!python -m pip install rotpy
from rotpy.system import SpinSystem
from rotpy.camera import CameraList

import numpy as np
import cv2
import time

system = SpinSystem()
cameras = CameraList.create_from_system(system, update_cams=True, update_interfaces=True)
# print(cameras.get_size())

camera = cameras.create_camera_by_index(0)

camera.init_cam()
print(camera.get_max_packet_size())
camera.begin_acquisition()

font = cv2.FONT_HERSHEY_SIMPLEX
start_time = time.time()
frames = 0 
fps=0

while True:
    frames += 1
    elapsed_time = time.time() - start_time
    if elapsed_time >= 1.0:  # Calculate FPS every second
        fps = frames / elapsed_time
        start_time = time.time()
        frames = 0
    try:
        image_cam = camera.get_next_image(timeout=5)
        image_byarr = image_cam.get_image_data()
        np_array = np.array(image_byarr, dtype=np.uint8)
            
            
        image_cam.release()  # Release resources immediately
        image = np_array.reshape(1200, 1600)
        cvimage = cv2.cvtColor(image, cv2.COLOR_BayerBGGR2RGB)

        cv2.putText(cvimage, f"FPS: {int(fps)}", (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Image', cvimage)
    except:
        print('WARNING: Missing image packages!')

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Short delay for smoother display
        cv2.destroyAllWindows() 
        break  # Exit the loop


# print(type(image))
image_cam.release()
camera.end_acquisition()
camera.deinit_cam()
camera.release()
