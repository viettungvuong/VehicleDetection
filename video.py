from os.path import isfile, join
import re
import cv2
import os

def videoGenerate():
    pathFrames = "frames/"
    pathVideo = 'carDetection.mp4'

    fps = 15.0

    frames = []
    files = [f for f in os.listdir(pathFrames) if isfile(join(pathFrames, f))]

    # sort file theo so thu tu
    files.sort(key=lambda f: int(re.sub('\D', '', f)))

    for i in range(len(files)):
        filename = pathFrames + files[i]

        # read frames
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)

        # inserting the frames into an image array
        frames.append(img)

    out = cv2.VideoWriter(pathVideo, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frames)):
        # writing to a image array
        out.write(frames[i])

    out.release()
