import cv2
import imageio
import os

# Opens the Video file
cap = cv2.VideoCapture('video.mp4')

# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS) 

# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Calculate the duration of the video in seconds
# duration = frame_count / fps

# Set estimated last frame time in [hr, min, sec]
end = [1, 40, 10]

# Set estimated start frame time in [hr, min, sec]
start = [1, 39, 51]

second = start[0]*3600 + start[1]*60 + start[2]
duration = 3600*end[0] + end[1]*60 + end[2]

cap.set(cv2.CAP_PROP_POS_MSEC, second*1000) 
success, image = cap.read()
count = 0
while success and second <= duration:
    # do stuff
    cv2.imwrite(os.path.join("ConvoFrames/", "frame"+str(count)+".jpg"), image)     # save frame as JPEG file
    second += 1/fps
    cap.set(cv2.CAP_PROP_POS_MSEC, second * 1000)
    success, image = cap.read()
    #print('Read a new frame: ', success)
    count += 1

with imageio.get_writer('ConvoFrames/loop.gif', mode='I') as writer:
    for i in range(82, 238):
        image = imageio.imread(os.path.join("ConvoFrames/", "frame"+str(i)+".jpg"))
        writer.append_data(image)
        
    for i in range(236, 81, -1):
        image = imageio.imread(os.path.join("ConvoFrames/", "frame"+str(i)+".jpg"))
        writer.append_data(image)