from PIL import Image
import random
import os


def rotate(image):
    angle = random.choice([90, 180, 270])
    return image.rotate(angle)

def flip(image):
    if random.choice([True, False]):
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    return image

def crop(image):
    width, height = image.size
    crop_size = int(min(width, height) * 0.8)
    left = (width - crop_size) // 2
    top = (height - crop_size) // 2
    right = left + crop_size
    bottom = top + crop_size
    return image.crop((left, top, right, bottom))


def augment_image(image_path, output_dir):
    with Image.open(image_path) as img:
        augmented_images = []
        augmented_images.append(rotate(img))
        augmented_images.append(flip(img))
        augmented_images.append(crop(img))

        for i, aug_img in enumerate(augmented_images):
            # Convert RGBA to RGB if necessary
            if aug_img.mode == 'RGBA':
                aug_img = aug_img.convert('RGB')
            output_path = os.path.join(output_dir, f"{os.path.basename(image_path)}_{i}.jpg")
            aug_img.save(output_path)


