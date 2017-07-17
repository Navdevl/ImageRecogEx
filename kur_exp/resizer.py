from resizeimage import resizeimage
#from PIL import Image
import Image
#img = '/home/naveendurai19/image/apple02.jpg'
for i in range(1,10):
    with Image.open('data/apple/00'+str(i)+'.jpg') as image:
        resizeimage.resize_cover(image, [28,28]).save('resized/apple{0}.jpg'.format(i), image.format)

#img = '/home/naveendurai19/image/apple02.jpg'
for i in range(1,10):
    with Image.open('data/orange/00'+str(i)+'.jpg') as image:
        resizeimage.resize_cover(image, [28,28]).save('resized/orange{0}.jpg'.format(i), image.format)
#im = Image.open(img)
