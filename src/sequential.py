import os
import time
from src.augment import augment_image

def sequential_augmentation(input_root, output_root):
    start_time = time.time()
    for folder_name in os.listdir(input_root):
        folder_path = os.path.join(input_root, folder_name)
        output_folder = os.path.join(output_root, folder_name)
        os.makedirs(output_folder, exist_ok=True)
        for image_file in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_file)
            # Ensure the path is a file and has a valid image extension
            if os.path.isfile(image_path) and image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                augment_image(image_path, output_folder)
    end_time = time.time()
    print(f"Sequential Augmentation Time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    sequential_augmentation(r"C:\\Users\\Taha\\Desktop\\pdc project\\data", "data/augmented/sequential")
