import subprocess
import os.path
import urllib2
import time
import sys

def myrun(cmd):
    subproc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = subproc.stdout.readline()
        stdout.append(line)
        if line == '' and subproc.poll() != None:
            break
    return ''.join(stdout).strip()

def scrapeFourcc():
    fourcc = urllib2.urlopen('http://www.fourcc.org/codecs.php')
    source = fourcc.read()
    start_search = source.index('content_list')
    source = source[start_search:]

    corners = ['/', 'through', '-']
    prev_token = '<strong>'
    post_token = '</strong>'
    pre_token_length = len(prev_token)
    post_token_length = len(post_token)

    codecs = []

    while(prev_token in source):
        start_search = source.index(prev_token)
        end_search = source.index(post_token)

        codec = source[start_search + pre_token_length : end_search].lower()
        source = source[end_search + post_token_length:]

        for corner in corners:
            if corner in codec:
                temp_codec = map(str.strip, codec.split(corner))
                codec = temp_codec

                if corner is '/':
                    codecs += codec
                elif corner is 'through' or corner is '-':
                    # read the numbers from the end of each element (there will only be 2)
                    # then get the string "rest"
                    # count from the one number to the other and append the "rest" string

                    # get number at end of the last element
                    index = len(codec[1]) - 1
                    while index >= 0 and codec[1][index].isdigit():
                        index -= 1;
                    end_number = int(codec[1][index+1 :])

                    # get number at end of the first element
                    index = len(codec[0]) - 1
                    while index >= 0 and codec[0][index].isdigit():
                        index -= 1;
                    start_number = int(codec[0][index+1 :])
                    string_part = codec[0][0:index+1]

                    codec = []
                    for i in range(start_number, end_number+1):
                        codec.append(string_part + str(i))

        if type(codec) is list:
            codecs += codec
        else:
            codecs.append(codec)

    return '\n'.join(codecs)


if not os.path.exists('../video'):
    os.mkdir('../video')

if not os.path.exists('../video/input.mp4'):
    print 'Input video does not exist, generating it now...'
    output = myrun(['python genVideo.py'])

    while 'Didn\'t successfully update movie file.' in output:
        output = myrun(['python genVideo.py'])

    print 'input.mp4 generated'

if not os.path.exists('../info'):
    os.mkdir('../info')

try:
    extensions_file = open('../info/extensions.txt', 'r')
    extensions = extensions_file.readlines()
except IOError:
    extensions_file = open('../info/extensions.txt', 'w')
    extensions_file.write('avi\nmov\nqt\navchd\nflv\nswf\nmpg\nmp4\nwmv')
    extensions_file.close()

    extensions_file = open('../info/extensions.txt', 'r')
    extensions = extensions_file.readlines()

try:
    codecs_file = open('../info/fourcc.txt', 'r')
    codecs = codecs_file.readlines()
except IOError:
    codecs_file = open('../info/fourcc.txt', 'w')
    # go fetch list from internet
    codecs_file.write(scrapeFourcc())
    codecs_file.close()

    codecs_file = open('../info/fourcc.txt', 'r')
    codecs = codecs_file.readlines()

extensions_file.close()
codecs_file.close()

checks = len(extensions) * len(codecs)
check = 0

results = []

start_time = time.time()

for file_ext in extensions:
    file_ext = file_ext.strip()
    results.append(file_ext + ':')

    for codec in codecs:
        codec = codec.strip()

        check += 1

        output = myrun(['python fourcc_file_extension_test.py' + ' ' + file_ext + ' ' + codec])
        while 'Didn\'t successfully update movie file.' in output or\
            'WARNING: Couldn\'t read movie file output.mp4' in output:
            output = myrun(['python fourcc_file_extension_test.py' + ' ' + file_ext + ' ' + codec])

        total_time = time.time() - start_time
        average_time = total_time/check
        estimated_time = int(average_time * (checks - check))

        info_output = '%10s' % file_ext
        info_output += '%10s' % codec
        info_output += '%20s' % ('%.2f' % (float(100 * check)/checks) + '% complete')
        info_output += '\tETC:' + ('%10d' % estimated_time) + ' seconds'

        if 'True' in output:
            info_output = 'Success:' + info_output

            results.append(' ' + codec)
        else:
            # info_output = (
            #     'Failure:'
            #     '%010s' % file_ext
            #     '%010s' % codec
            #     '%020s' % ('%.2f' % float(100 * check)/checks + '% complete')
            #     'ETC:' + ('%010d' % estimated_time) + ' seconds'
            # )
            info_output = 'Failure:' + info_output

        sys.stdout.write('%s\r' % info_output)
        sys.stdout.flush()

    results.append('\n')

results_file = open('../info/results.txt', 'w')
results_file.write(''.join(results))
results_file.close()
