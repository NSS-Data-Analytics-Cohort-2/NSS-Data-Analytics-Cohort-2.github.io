import os
from PIL import Image


def resize_image(fp, hw_ratio=0.67):
    im = Image.open(fp)
    
    width, height = im.size
    
    # want to base the cropped size off the smallest edge
    smallest = min([width, height])
    center = width/2, height/2
    
    # always based off the center
    offset = smallest/2

    left = int(center[0] - (offset*hw_ratio))
    top = int(center[1] - offset)
    right = int(center[0] + (offset*hw_ratio))
    bottom = int(center[1] + offset)
    
    # Cropped ratio is based on the hw_ratio ratio
    return im.crop((
        left, top, right, bottom
    ))


def save_image(img, fp):
    try:
        img.save(fp, "JPEG")

    except OSError:
        # Handling PNG
        img = img.convert("RGB")
        img.save(fp, "JPEG")


def resize_images(fp):
    for image_name in os.listdir(fp):
        if not os.path.isdir(f"{fp}/{image_name}"):
            print(f"Resizing {image_name}")

            resized = resize_image(f"{fp}/{image_name}")

            if not os.path.exists(f"{fp}/resized"):
                os.mkdir(f"{fp}/resized")

            new_name = '.'.join(image_name.split(".")[:-1]) + ".jpeg"
            save_image(resized, f"{fp}/resized/{new_name}")
