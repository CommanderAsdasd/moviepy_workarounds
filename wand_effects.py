import moviepy.editor as MpEditor
import wand
from wand.image import Image


# def make_frame(t):
# 	'''returns an imge of the frame at t'''
# 	return frameFortimeT # Numpy array

with Image(filename='D:\\Pictures\\Textures\\glitch.jpg') as img:
    print('width =', img.width)
    print('height =', img.height)

def show_me_type(img):
	print(type(img))
	return img

# animation = MpEditor.VideoClip(make_frame, duration=3)
x = MpEditor.VideoFileClip("D:\\Videos\\grossbeat\\AErender\\bunnies2.avi")
x.fl_image(show_me_type)