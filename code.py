from PIL import Image, ImageFilter


def main():
    print(im.format, im.size, im.mode)


im = Image.open("picture.jpg")

filtered_picture = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
filtered_picture.save('pictureedgeenhance.jpg')
im.close()


if __name__ == '__main__':
    main()