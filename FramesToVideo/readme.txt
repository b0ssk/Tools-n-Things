Frames to Video Converter
Jon Parkins, May 13th, 2024
Python 3.12
Version 1.0

Converts a sequence of rendered frames into a mp4 file using FFMPEG
Run from directory with your frames, will create your video and tidy up after itself moving frames into 
a named directory based on the file name.

Dependancies: ffmpeg linked into your system path so the script can find it easily.
Filename should be 4 digit padded, but can alter in the script, and should have the name and padding deliminated by an _ as an example 
animTest_0001.jpg
