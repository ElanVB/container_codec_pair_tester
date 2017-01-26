# container_codec_pair_tester
This program tests your system and lets you know what containers and codecs can
be used to create or alter videos.

I created this program with the OpenCV library in mind. I found it difficult to
find video file extensions (containers) and codec pairs that would allow me to
successfully write video files using the OpenCV library. Thus I made this
program to do all the work for you. You simply run the "start.py" file, it
will do all the processing for you and will write to the "info/results.txt"
file, you can then check this file to see which container codec pairs your
system use.

If you wish you could create your own "extensions.txt" and "fourcc.txt" files,
this allows you to choose which containers and condec you test for instead of
the default ones (which admittedly take very long, but are quite thorough).
