#!/usr/bin/env python3
# OCR for multiple images passed via command-line

import os, sys
from PIL import Image
import pytesseract

# Define the OCR function
def ocr_image(file_path):
    image = Image.open(file_path)
    # Specify languages English and Thai for Tesseract
    return pytesseract.image_to_string(image, lang='eng+tha')

# Get the list of file paths from the command-line arguments
if len(sys.argv) < 2:
    print("Error: Please provide at least one image file as an argument.")
    sys.exit(1)
fps = [arg for arg in sys.argv[1:] if os.path.isfile(arg)]

# Apply OCR to each image and collect the results
ocr_results = [ocr_image(fp) for fp in fps]

# Print the file name and OCR result to the console, with a separator line after each result
for fp, text in zip(fps, ocr_results):
    print(f"File: {os.path.basename(fp)}")
    print(text)
    print("-" * 80)
