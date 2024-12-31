"# ImgBoost" 
# Image Augmentation with Sequential and Parallel Processing

This project demonstrates image augmentation using sequential, multiprocessing, and threading approaches in Python. The goal is to optimize performance for large datasets and measure the effectiveness of different approaches.

---

## Features
- **Sequential Augmentation**: Processes images one by one.
- **Parallel Augmentation**: Leverages multiprocessing for faster augmentation.
- **Threaded Augmentation**: Utilizes threading for I/O-bound tasks.
- **Performance Comparison**: Evaluates the time taken by each approach.

---

## Project Structure
```
pdc_project/
├── data/               # Input and augmented datasets
├── src/                # Python scripts for augmentation
│   ├── augment.py      # Core augmentation methods
│   ├── parallel.py     # Parallel processing script
│   └── sequential.py   # Sequential processing script
├── README.md           # Documentation
├── requirements.txt    # Python dependencies
├── main.py             # Main entry point
└── .gitignore          # Files/folders to ignore in Git
```

---

## Performance Results

The project compares sequential, parallel, and threaded augmentation:
| Method                     | Time Taken (seconds) |
|----------------------------|----------------------|
| Sequential Augmentation     | ~1008               |
| Threaded Parallel Augmentation | ~480               |

Here’s the output console of the performance comparison:

![Performance Results](output-image.png)


---

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Tahamallick/ImgBoost.git
cd ImgBoost
```

### 2. Install Dependencies
Install the required Python libraries using:
```bash
pip install -r requirements.txt
```

### 3. Run the Project
Run the main script to execute sequential and parallel augmentation:
```bash
python main.py
```

---

## Implementation Details

### Core Augmentation Methods
1. **Rotation**: Rotates the image by 90°, 180°, or 270° randomly.
2. **Flipping**: Horizontally flips the image.
3. **Cropping**: Crops the image to 80% of its original dimensions.

### Processing Approaches
- **Sequential**:
   - Processes each image one at a time.
   - Useful for small datasets but slow for large ones.
- **Parallel**:
   - Uses Python’s `multiprocessing` and `threading`  to process images concurrently.
   - Ideal for CPU-bound tasks.

---








---


