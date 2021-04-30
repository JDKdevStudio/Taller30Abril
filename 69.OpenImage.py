from cv2imageload import ImageLoad, ImageLoadError

file = 'th-108.jpg'
url = 'http://*.com/test.png'
base64_str = '图片的base64编码字符串'


try:
    image = ImageLoad.loadImage(file)
except ImageLoadError as e:
    print(e.reason)


try:
    image = ImageLoad.loadImage(url)
except ImageLoadError as e:
    print(e.reason)


try:
    image = ImageLoad.loadImage(base64_str)
except ImageLoadError as e:
    print(e.reason)


try:
    base64_str = ImageLoad.base64EncodeImage(image, with_base64_header=True, file_ext='jpg')
except ImageLoadError as error:
    print(error.reason)
print(base64_str[:30])
