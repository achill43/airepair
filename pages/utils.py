import os

from PIL import Image, ImageOps, ImageDraw, ImageFont


class ImageThumbnail():
    def add_watermart_text(input_image_path, output_image_path, text):
        photo = Image.open(input_image_path)
        width, height = photo.size
        drawing = ImageDraw.Draw(photo)
        black = (3, 8, 12)
        font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 240)
        w, h = drawing.textsize(text, font=font)
        pos_x = (width - w) / 2
        pos_y = (height - h) / 2
        drawing.text(
            (pos_x, pos_y), text, fill=black, font=font
        )
        try:
            photo.save(output_image_path)
        except FileNotFoundError:
            create_path = "".join(output_image_path.split("/")[:-1])
            create_path = create_path + "/"
            os.mkdir(f"{create_path}")
            photo.save(output_image_path)
        return output_image_path

    def my_thumbnail(inputImgPath, outputImgPath, size):
        try:
            baseImg = Image.open(inputImgPath)
            newImg = ImageOps.fit(baseImg, size, Image.ANTIALIAS)
            newImg.save(outputImgPath)

        except IOError:
            print
            "cannot create thumbnail for", inputImgPath
            return inputImgPath
