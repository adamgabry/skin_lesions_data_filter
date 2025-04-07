import os
import cv2
from concurrent.futures import ThreadPoolExecutor, as_completed

##OPTIONS
ROTATE_90 = 90
ROTATE_180 = 180
ROTATE_270 = 270
FLIP = True

IMAGE_DIR = 'small'
OUTPUT_PATH = 'small_flipped'
os.makedirs(OUTPUT_PATH, exist_ok=True)

def flip_image(filename):
    input_path = os.path.join(IMAGE_DIR, filename)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}_flipped{ext}"
    output_path = os.path.join(OUTPUT_PATH, output_filename)

    try:
        img = cv2.imread(input_path)
        if img is None:
            print(f"Warning: Couldn't read {filename}")
            return
        flipped = cv2.flip(img, 1)  # Horizontal flip (Y-axis)
        cv2.imwrite(output_path, flipped)
    except Exception as e:
        print(f"Error processing {filename}: {e}")

def main():
    files = [
        f for f in os.listdir(IMAGE_DIR)
        if f.lower().endswith(('.jpg', '.jpeg', '.png')) and '_flipped' not in f
    ]
    with ThreadPoolExecutor() as executor:
        executor.map(flip_image, files)

if __name__ == "__main__":
    main()
