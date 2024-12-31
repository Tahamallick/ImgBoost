import os
import time
from concurrent.futures import ThreadPoolExecutor
from src.augment import augment_image


def process_image(image_path, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    augment_image(image_path, output_folder)


def parallel_augmentation(input_root, output_root):
    start_time = time.time()

    # Collect all image paths and their corresponding output folders
    tasks = []
    for folder_name in os.listdir(input_root):
        input_folder = os.path.join(input_root, folder_name)
        output_folder = os.path.join(output_root, folder_name)
        os.makedirs(output_folder, exist_ok=True)
        for image_file in os.listdir(input_folder):
            image_path = os.path.join(input_folder, image_file)
            if os.path.isfile(image_path) and image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                tasks.append((image_path, output_folder))

    # Process all images using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_image, image_path, output_folder) for image_path, output_folder in tasks]
        # Wait for all threads to complete
        for future in futures:
            future.result()

    end_time = time.time()
    print(f"Parallel Augmentation Time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    parallel_augmentation(
        r"C:\\Users\\Taha\\Desktop\\pdc project\\data",
        r"C:\\Users\\Taha\\Desktop\\pdc project\\data\\augmented\\parallel"
    )
