__all__ = ['resize_image']


from PIL import Image


def resize_image(image_path, width, height):
    image = Image.open(image_path)
    if image.width > 700 or image.height > 700:
        image.thumbnail((500, 500))
        image.save(image_path)
