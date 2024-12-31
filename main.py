from src.sequential import sequential_augmentation
from src.parallel import parallel_augmentation

if __name__ == "__main__":
    print("Starting Sequential Augmentation...")
    sequential_augmentation(r"C:\\Users\\Taha\\Desktop\\pdc project\\data", r"C:\\Users\\Taha\\Desktop\\pdc project\\data\\augmented\\sequential")

    print("Starting Parallel Augmentation...")
    parallel_augmentation(r"C:\\Users\\Taha\\Desktop\\pdc project\\data", r"C:\\Users\\Taha\\Desktop\\pdc project\\data\\augmented\\parallel")

