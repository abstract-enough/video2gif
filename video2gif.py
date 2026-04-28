import cv2
import imageio


cap = cv2.VideoCapture("/content/drive/MyDrive/Nick_G_3_6_D.mp4")


gif_frames = []


while True:


    ret, frame = cap.read()
    if ret:
      color_frame = cv2.cvtColor(frame,
cv2.COLOR_BGR2RGB)
      gif_frames.append(color_frame)


    if not ret:
        break


imageio.mimsave("/content/drive/MyDrive/Nick_G_3_6_D.gif", gif_frames, fps=10)