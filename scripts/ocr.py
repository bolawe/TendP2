import pytesseract
from pdf2image import convert_from_path
import os

print("Starting OCR processing...")

# Process all files in inputs/
for filename in os.listdir("inputs"):
    if filename.endswith((".pdf", ".png", ".jpg")):
        print(f"Processing {filename}...")
        
        # PDF → Images → Text
        if filename.endswith(".pdf"):
            images = convert_from_path(f"inputs/{filename}")
            text = "\n".join([pytesseract.image_to_string(img) for img in images])
        else:
            text = pytesseract.image_to_string(f"inputs/{filename}")
        
        # Save extracted text
        os.makedirs("outputs", exist_ok=True)
        with open(f"outputs/{filename}.txt", "w") as f:
            f.write(text)

print("OCR complete! Text saved to /outputs")
