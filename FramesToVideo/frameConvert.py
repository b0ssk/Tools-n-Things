# Frames to Video Converter
# Jon Parkins, May 13th, 2024
# Python 3.12
# Version 1.0

# Converts a sequence of rendered frames into a mp4 file using FFMPEG
# Run from directory with your frames, will create your video and tidy up after itself moving frames into 
# a named completed directory.

# ffmpeg command I generally run
# -y auto overwrite if output exists
# -r rate set frame rate (Hz value, fraction or abbreviation)
# -f fmt force format
# -s size set frame size (WxH or abbreviation)
# -start_number .D…… set first number in the sequence (from 0 to INT_MAX) (default 0)
# -i animTest_%04d.jpg Input with 4 padding %04d, animTest_0001.jpg
# -vcodec codec force video codec (‘copy’ to copy stream)
# -crf E..V…. Select the quality for constant quality mode (from 0 to 63) (default 0) 0 lossless 63 worst
# -pix_fmts show available pixel formats
# Currently not using -s 1920x1080
# ffmpeg -y -r 30 -f image2 -s 1920x1080 -start_number 0001 -i animTest_%04d.jpg -vcodec libx264 -crf 15 -pix_fmt yuvj420p test.mp4

import subprocess
import os
import re
import shutil

def make_video():
    # creates list of all files and directories in current location
    file_list = os.listdir('.')

    # create list of all the frames to get frame length
    image_list = []

    #create dictionary for building FFMPEG Vars
    image_elements = {}

    # separate out image files from files and directories and print list
    for images in file_list:
        if '.jpg' in images:
            image_list.append(images)
        elif '.tif' in images:
            image_list.append(images)
        elif '.tga' in images:
            image_list.append(images)

    # sort the list, as it comes in willy nilly, that's technical term I'm sure.        
    image_list.sort()

    # add elements to the image info dictionary for passing vars to FFMPEG
    # add amount of frames to dictionary
    image_elements['frame_count'] = len(image_list)
    
    # getting file name elements
    first_frame = image_list[0]

    # splitting the file name into name, frame count start and extension
    frame_elements = re.split(r'[_.]', first_frame)

    # add frame start to dictionary
    image_elements['first_frame_#'] = frame_elements[1]

    # add filename of frame to dictionary to be used for video name
    image_elements['vid_name'] = frame_elements[0]

    # add file extention of frame to dictionary
    image_elements['file_ext'] = frame_elements[2]

    # vars to pass into ffmpeg command from filename dictionary
    first_frame_num = image_elements['first_frame_#']
    vid_name = image_elements['vid_name']
    ext = image_elements['file_ext']

    # create command to pass to subprocess
    ffmpeg_command = str (f'ffmpeg -y -r 30 -f image2 -start_number {first_frame_num} -i {vid_name}_%04d.{ext} -vcodec libx264 -crf 15 {vid_name}.mp4')
    print(ffmpeg_command)
    
    # create video from frames
    subprocess.run(ffmpeg_command, shell=True)

    # create a dir on render completion to move files to
    os.mkdir(vid_name)

    # move the files
    for files in image_list:
        shutil.move(files, vid_name)

make_video()