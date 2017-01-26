import numpy as np
import cv2
import sys

# def image_equals(image1, image2):
#     return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())

# def video_equals(video_stream1, video_stream2):
#     fps1 = video_stream1.get(cv2.CAP_PROP_FPS)
#     fps2 = video_stream2.get(cv2.CAP_PROP_FPS)
#
#     if fps1 != fps2:
#         print 'fps'
#         return False
#
#     width1 = video_stream1.get(cv2.CAP_PROP_FRAME_WIDTH)
#     width2 = video_stream2.get(cv2.CAP_PROP_FRAME_WIDTH)
#
#     if width1 != width2:
#         print 'width'
#         return False
#
#     height1 = video_stream1.get(cv2.CAP_PROP_FRAME_HEIGHT)
#     height2 = video_stream2.get(cv2.CAP_PROP_FRAME_HEIGHT)
#
#     if height1 != height2:
#         print 'height'
#         return False
#
#     frame_count1 = int(video_stream1.get(cv2.CAP_PROP_FRAME_COUNT))
#     frame_count2 = int(video_stream2.get(cv2.CAP_PROP_FRAME_COUNT))
#
#     if frame_count1 != frame_count2:
#         print 'frame count'
#         return False
#
#     ret1, frame1 = video_stream1.read()
#     ret2, frame2 = video_stream2.read()
#
#     for frame_index in range(frame_count1):
#         if not (ret1 and ret2):
#             return True
#         elif ret1 and not ret2:
#             print 'stream 2 end'
#             return False
#         elif not ret1 and ret2:
#             print 'stream 1 end'
#             return False
#         elif not image_equals(frame1, frame2):
#             print 'frames dont match'
#             print frame1, frame2
#             return False
#
#     return True

# def is_video_corrupt(vid_stream):
#     ret, frame = vid_stream.read()
#     return not ret

def test_fourcc_file_extension(file_ext, codec):
    # copy it with a fourcc and file extension combo
    # extensions_file = open('extensions.txt', 'r')
    # extensions = extensions_file.readlines()
    #
    # codecs_file = open('fourcc.txt', 'r')
    # codecs = codecs_file.readlines()

    # for file_ext in extensions:
    #     for codec in codecs:
    fourcc = cv2.VideoWriter_fourcc(*codec)

    vid_in = cv2.VideoCapture('../video/input.mp4')

    fps = vid_in.get(cv2.CAP_PROP_FPS)
    width = vid_in.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vid_in.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_count = vid_in.get(cv2.CAP_PROP_FRAME_COUNT)

    vid_out = cv2.VideoWriter('../video/output.' + file_ext, fourcc, int(fps), (int(width), int(height)), True)

    ret, frame = vid_in.read()

    vid_out.write(frame)

    vid_out.release()
    vid_in.release()

    # test to see if it is valid
    ret = False
    vid_in2 = cv2.VideoCapture('../video/output.' + file_ext)
    # get ret for first frame and print it
    ret, frame = vid_in2.read()
    print ret

    vid_in2.release()
    cv2.destroyAllWindows()

# print 'Arguments:', sys.argv
test_fourcc_file_extension(sys.argv[1], sys.argv[2])

# check if vid has been generated
 # if not then gen (loop here)
# check if fails_ext?_codec?.txt exists
 # if so then try those
 # else try normal files

 # maybe check if files have been done correctly from std output
  # file_ext codec : True/False/Error
