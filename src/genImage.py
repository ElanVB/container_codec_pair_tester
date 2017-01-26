from PIL import Image
import numpy as np

def genImage(RGB=[255, 0, 0]):
    size = 1
    w, h = size, size
    data = np.zeros((h, w, 3), dtype=np.uint8)
    data[0, 0] = RGB
    img = Image.fromarray(data, 'RGB')
    # img.save('%s.png' % name)
    return img, data

# genImage([0, 255, 0])[0].save('1.png')
