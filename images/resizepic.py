from PIL import Image

from resizeimage import resizeimage


with open('split.jpg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [16, 16])
        cover.save('favicon.jpg', image.format)
