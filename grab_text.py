#!/usr/bin/env python3
# OCR for multiple images passed via command-line

import os, sys
from PIL import Image
import pytesseract

# Define the OCR function
def ocr_image(file_path):
    try:
        image = Image.open(file_path)
        # Specify languages English and Thai for Tesseract
        return pytesseract.image_to_string(image, lang='eng+tha')
    except IOError:
        # Return None if the file is not an image or cannot be opened
        return None

# Get the list of file paths from the command-line arguments
if len(sys.argv) < 2:
    print("Error: Please provide at least one file or folder as an argument.")
    sys.exit(1)

# Collect any files including files in folders and subfolders
files_to_process = []
for arg in sys.argv[1:]:
    if os.path.isfile(arg):
        files_to_process.append(arg)
    elif os.path.isdir(arg):
        for root, _, files in os.walk(arg):
            for file in files:
                files_to_process.append(os.path.join(root, file))

# Apply OCR to each image and collect the results
ocr_results = []
for fp in files_to_process:
    text = ocr_image(fp)
    if text is not None:
        ocr_results.append((fp, text))

# Print the file name and OCR result to the console, with a separator line after each result
for fp, text in ocr_results:
    print(f"File: {os.path.basename(fp)}")
    print(text)
    print("-" * 80)
