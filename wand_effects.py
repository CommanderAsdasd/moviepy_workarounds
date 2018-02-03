# -*- coding: utf-8 -*-
# C:/Python27/python.exe
import moviepy.editor as MpEditor
import wand as wnd
import wand.image as WndImage
import StringIO
import png
import scipy.misc
from PIL import Image
import io
from random import choice
import numpy as np
import time
from moviepy.editor import *
# from moviepy.video.fx.all import *

# from __future__ import print_function

# def make_frame(t):
# 	'''returns an imge of the frame at t'''
# 	return frameFortimeT # Numpy array

write_data = time.strftime("%I%M%S")

def wand_opener(img):
    blob = io.BytesIO()
    with WndImage.Image(blob=img) as img:
        img.format = 'jpeg'
        print('width =', img.width)
        print('height =', img.height) 
        size = img.size
        coef_x = choice((2,3,4,5))
        coef_y = choice((2,3,4,5))
        if choice((0, 1)) == 0:
           ch = ('div', 'mul')
           x_size = size[0]//coef_x
           y_size = size[1]//coef_x
        else:
            ch = ('mul', 'div')
            x_size = size[0]//coef_x
            y_size = size[1]//coef_x
        img.liquid_rescale(x_size, y_size)
        # img.save(filename="D:\\Videos\\moviepy\\outimages\\img{}.jpeg".format(write_data))
        img.sample(size[0], size[1])
        # img.save(filename="D:\\Videos\\moviepy\\outimages\\img{}.jpeg".format(write_data))
        print(size[0], size[1])
        img_bin = img.make_blob('jpeg')
        blob = io.BytesIO(b'{}'.format(img_bin))
        # img.save(blob=blob)
        # print(img.size)
    return blob

# Надо заставить его сожрать изображение из 

def show_me_type(imarray):
    blob = io.BytesIO()
    inpImage = Image.fromarray(imarray, 'RGB')
    print(inpImage.size)
    inpImage.save(blob, format='JPEG')
# png.from_array(img)
    print(blob)
# print("LOL", bytemage)
    blob2 = wand_opener(blob.getvalue())
    # print(blob, blob2)
    blob2.seek(0)
    img = Image.open(blob2)
    # img = Image.frombuffer('RGB', (150,100), blob2.open(), "raw")
    # print(img)
    img.save("D:\\Videos\\moviepy\\outimages\\img{}_PIL.jpeg".format(write_data))
    imarray = np.fromstring(img.tobytes(), dtype=np.uint8)
    imarray = imarray.reshape((img.size[1], img.size[0], 3))
    return imarray

# animation = MpEditor.VideoClip(make_frame, duration=3)

def main():
    x = MpEditor.VideoFileClip("D:\\Videos\\5Upak.mp4")
    x = x.fl_image(show_me_type)
    # x = x.resize( (1920, 1080) )
    x = x.subclip(1, 10)
    # x = concatenate_videoclips(x, method='compose')
    x.write_videofile("D:\\Videos\\moviepy\\outimages\\CAS_COOL{}.mp4".format(write_data),  fps=60)

if __name__ == "__main__":
    main()