import urllib2

fourcc = urllib2.urlopen('http://www.fourcc.org/codecs.php')
source = fourcc.read()
start_search = source.index('content_list')
source = source[start_search:]

corners = ['/', 'THROUGH', '-']
prev_token = '<strong>'
post_token = '</strong>'
pre_token_length = len(prev_token)
post_token_length = len(post_token)

codecs = []

while(prev_token in source):
    start_search = source.index(prev_token)
    end_search = source.index(post_token)

    codec = source[start_search + pre_token_length : end_search]
    source = source[end_search + post_token_length:]

    for corner in corners:
        if corner in codec:
            temp_codec = map(str.strip, codec.split(corner))
            codec = temp_codec
            
    if type(codec) is list:
        # codecs += codec
        print 'ignoring', codec
    else:
        codecs.append(codec)

return '\n'.join(codecs)
