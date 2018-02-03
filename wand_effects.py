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
# from __future__ import print_function

# def make_frame(t):
# 	'''returns an imge of the frame at t'''
# 	return frameFortimeT # Numpy array

def wand_opener(img):
	with WndImage.Image(blob=img) as img:
	    print('width =', img.width)
	    print('height =', img.height) 

# Надо заставить его сожрать изображение из 

def show_me_type(imarray):
	blob = io.BytesIO()
	inpImage = Image.fromarray(imarray, 'RGB')
	print(inpImage)
	inpImage.save(blob, format='JPEG')
	# png.from_array(img)
	print(blob)
	# print("LOL", bytemage)
	wand_opener(blob.getvalue())
	return imarray

# animation = MpEditor.VideoClip(make_frame, duration=3)
x = MpEditor.VideoFileClip("D:\\Videos\\Bandicam\\bandicam 2018-01-21 21-30-59-894.mp4")
x.fl_image(show_me_type)