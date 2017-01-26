import genImage
import cv2

filename = '../video/input.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 1
width, height = 1, 1

vid_out = cv2.VideoWriter(filename, fourcc, fps, (int(width), int(height)), True)

image, data = genImage.genImage()
# print data

vid_out.write(data)
# print filename, 'generated'

vid_out.release()
