from PIL import Image


im = Image.open("screenshot2023.05.18.13.18.48.png")

size=(1792,828)

out = im.resize(size)
out.save('resiez-out.png')


# width = im.size[0]
# height = im.size[1]
#
# print('Width of the image is:', width)
# print('Width of the image is:', height)


