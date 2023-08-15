from PIL import Image, ImageFilter


def main():
    print(im.format, im.size, im.mode)


im = Image.open("picture.jpg")


picture = im.convert("L")
picture.save('pictureconvert.jpg')
im.close()


if __name__ == '__main__':
    main()